# How to construct the data
https://github.com/jovsa/speed-challenge-2017/blob/master/dataset_constructor.ipynb

Read training data csv using pandas

```python
train_y = list(pd.read_csv(os.path.join(DATA_PATH, 'train.txt'), header=None, squeeze=True))

```

Use ```tqdm``` to monitor progress of data preprocessing

```python
for idx, frame in enumerate(tqdm(cap)):    

```

Fill up data in this order
1. Dictionary (easy to use)
2. Dataframe
3. CSV to store


```python
def dataset_constructor(video_loc, img_folder, tot_frames, dataset_type):
    meta_dict = {}

    tqdm.write('reading in video file...')
    tot_frames = train_frames
    cap = skvideo.io.vread(video_loc)
     
    tqdm.write('constructing dataset...')
    for idx, frame in enumerate(tqdm(cap)):    
        img_path = os.path.join(img_folder, str(idx)+'.jpg')
        frame_speed = float('NaN') if dataset_type == 'test' else train_y[idx]
        meta_dict[idx] = [img_path, idx, frame_speed]
        skvideo.io.vwrite(img_path, frame)
    meta_df = pd.DataFrame.from_dict(meta_dict, orient='index')
    meta_df.columns = ['image_path', 'image_index', 'speed']
    
    tqdm.write('writing meta to csv')
    meta_df.to_csv(os.path.join(CLEAN_DATA_PATH, dataset_type+'_meta.csv'), index=False)

```

Then read out images using

```python
import matplotlib.image as mpimg
```

And also use matplotlib to plot speed over time to validate

```python
plt.plot(train_meta['speed'])
```


# Train a model
https://github.com/jovsa/speed-challenge-2017/blob/master/NVIDIA_model.ipynb

Create a run name by concatenating all the hyperparameters

```python
model_name = 'nvidia' #nvidia2
run_name = 'model={}-batch_size={}-num_epoch={}-steps_per_epoch={}'.format(model_name,
                                                                          batch_size,
                                                                          num_epochs,
                                                                          steps_per_epoch)

```

Change brightness of image 

```python

def change_brightness(image, bright_factor):
    """
    Augments the brightness of the image by multiplying the saturation by a uniform random variable
    Input: image (RGB)
    returns: image with brightness augmentation
    """
    
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    # perform brightness augmentation only on the second channel
    hsv_image[:,:,2] = hsv_image[:,:,2] * bright_factor
    
    # change back to RGB
    image_rgb = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)
    return image_rgb
```

Something about optical flow algorithm

Resize image using cv2 library, need to basically remove everything below the dashboard

Use Nvidia model
1. Convolution layers followed by ELU then dropout layers
2. Optimize with ADAM
3. Loss is MSE

Setup Early stopping and model checkpoint config classes

```python
earlyStopping = EarlyStopping(monitor='val_loss', 
                              patience=1, 
                              verbose=1, 
                              min_delta = 0.23,
                              mode='min',)

modelCheckpoint = ModelCheckpoint(weights_loc, 
                                  monitor = 'val_loss', 
                                  save_best_only = True, 
                                  mode = 'min', 
                                  verbose = 1,
                                 save_weights_only = True)

tensorboard = TensorBoard(log_dir=tensorboard_loc, histogram_freq=0,
                            write_graph=True, write_images=True)

callbacks_list = [modelCheckpoint, tensorboard, earlyStopping]

```

Fit model and analyze loss 

Architecture used
* Nvidia
* Look up some more that would work

* DeepVO: uses RNN and CNN but training RNN will result in convergence issues https://github.com/keras-team/keras/issues/9230
* Flownet: differential optical flow https://github.com/sampepose/flownet2-tf

What is optical flow
Two successive images can differe a minimum in pixel intensity from each other due to lighting. Can use this contraint to derive velocity from 2 images