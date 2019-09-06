How to create a  notification when a cell completes

https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/notify

Need to create a YAML file with the description and be explicit about the parameters and tehir input type

```
Type: IPython Notebook Extension
Name: Notify
Description: >
  Show a browser notification when kernel becomes idle again after being busy
  for some time - configurable after 0, 5, 10, or 30 seconds busy.
Link: readme.md
Icon: notification.png
Main: notify.js
Compatibility: 4.x, 5.x
Parameters:
- name: notify.sticky
  description: Require interactions on notifications to dismiss them. (Chrome only)
  input_type: checkbox
  default: false
- name: notify.play_sound
  description: Play notification sound.
  input_type: checkbox
  default: false
```

Jupyter also lets me hook into custom events like

```javascript
$([Jupyter.events]).on('kernel_starting.Kernel',function () {
```


Core logic for notifications looks like

Looks like HTML 5 has its own custom Audio and Notification tags which we can leverage. Javascript has this cool pattern where classes often take a JSON object as an initializer

```javascript
  var notify = function () {
    var elapsed_time = current_time() - start_time;
    if (enabled && !first_start && !busy_kernel && elapsed_time >= min_time) {
      var opts = {
        body: "Kernel is now idle\n(ran for " + Math.round(elapsed_time) + " secs)",
        icon: Jupyter.notebook.base_url + "static/base/images/favicon.ico",
        requireInteraction: params.sticky
      };
      if (params.play_sound) {
        play_notification_sound(opts);
      }
      var n = new Notification(Jupyter.notebook.notebook_name, opts);
      n.onclick = function(event){ window.focus(); }
    }
    if (first_start) {
      first_start = false;
    }
  };

```