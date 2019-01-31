import numpy as np
import pyglet


class ArmEnvironment():
    #Pyglet specific viewer, we could use others like pygame
    viewer = None

    # refresh rate
    dt = .1    

    #we specify a goal 
    goal = {'x': 100., 'y': 100., 'thickness': 10}
    
    #state is comprised of 9 elements
    state_dim = 9

    #we have two joints which we'll put forces on
    action_dim = 2
    action_bound = [-1, 1]


    def __init__(self):
        self.arm_info = np.zeros(
            2, dtype=[('l', np.float32), ('r', np.float32)])
        
        # arm lengths
        self.arm_info['l'] = 100  

        # arm radiuses      
        self.arm_info['r'] = 0   

        # boolean to check if goal achieved
        self.on_goal = 0

    def step(self, action):
        done = False
        action = np.clip(action, *self.action_bound)
        self.arm_info['r'] += action * self.dt
        self.arm_info['r'] %= np.pi * 2    # normalize, if this was of type angle this wouldnt be needed

        # Arm lengths
        (a1l, a2l) = self.arm_info['l'] 
        
        # Arm radiuses
        (a1r, a2r) = self.arm_info['r']

        # Origin of arm 1
        a1xy = np.array([200., 200.]) 

        # Mid point between arm 1 and arm 2
        a1xy_ = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy

        # Finger, tip of arm 2
        finger = np.array([np.cos(a1r + a2r), np.sin(a1r + a2r)]) * a2l + a1xy_  # a2 end (x2, y2)


        dist1 = [(self.goal['x'] - a1xy_[0]) / 400, (self.goal['y'] - a1xy_[1]) / 400]
        dist2 = [(self.goal['x'] - finger[0]) / 400, (self.goal['y'] - finger[1]) / 400]


        r = -np.sqrt(dist2[0]**2+dist2[1]**2)

        if self.goal['x'] - self.goal['thickness']/2 < finger[0] < self.goal['x'] + self.goal['thickness']/2:
            if self.goal['y'] - self.goal['thickness']/2 < finger[1] < self.goal['y'] + self.goal['thickness']/2:
                r += 1.

                # only reward the agent if it deliberately comes to the goal for over 50 iterations
                self.on_goal += 1
                if self.on_goal > 50:
                    done = True
        else:
            self.on_goal = 0

        s = np.concatenate((a1xy_/200, finger/200, dist1 + dist2, [1. if self.on_goal else 0.]))
        return s, r, done

    def reset(self):
        self.arm_info['r'] = 2 * np.pi * np.random.rand(2)
        self.on_goal = 0
        (a1l, a2l) = self.arm_info['l'] 
        (a1r, a2r) = self.arm_info['r'] 
        a1xy = np.array([200., 200.]) 
        a1xy_ = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy  # a1 end and a2 start (x1, y1)
        finger = np.array([np.cos(a1r + a2r), np.sin(a1r + a2r)]) * a2l + a1xy_  # a2 end (x2, y2)
        # normalize features
        dist1 = [(self.goal['x'] - a1xy_[0])/400, (self.goal['y'] - a1xy_[1])/400]
        dist2 = [(self.goal['x'] - finger[0])/400, (self.goal['y'] - finger[1])/400]
        # state
        s = np.concatenate((a1xy_/200, finger/200, dist1 + dist2, [1. if self.on_goal else 0.]))
        return s

    def render(self):
        if self.viewer is None:
            self.viewer = Viewer(self.arm_info, self.goal)
        self.viewer.render()

    def random_action(self):
        #return 2 random values from -0.5 to 0.5
        return np.random.rand(2)-0.5    # two radians


class Viewer(pyglet.window.Window):
    thickness = 5

    def __init__(self, arm_info, goal):
        # vsync=False to not use the monitor FPS, we can speed up training
        super(Viewer, self).__init__(width=400, height=400, vsync=False)
        pyglet.gl.glClearColor(0, 0, 0, 0)
        self.arm_info = arm_info
        self.center_coord = np.array([200, 200])

        self.batch = pyglet.graphics.Batch()    # display whole batch at once
        self.goal = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,    # 4 corners
            ('v2f', [goal['x'] - goal['thickness'] / 2, goal['y'] - goal['thickness'] / 2,                # location
                     goal['x'] - goal['thickness'] / 2, goal['y'] + goal['thickness'] / 2,
                     goal['x'] + goal['thickness'] / 2, goal['y'] + goal['thickness'] / 2,
                     goal['x'] + goal['thickness'] / 2, goal['y'] - goal['thickness'] / 2]),
            ('c3B', (255, 0, 0) * 4))    # color
        
        #generalize this to multiple arms, each node corresponds to a vertex and together form a rectangle
        #v2f is used for vertices and c3b for colors
        self.arm1 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [250, 250,                # location
                     250, 300,
                     260, 300,
                     260, 250]),
            ('c3B', (255, 255, 255) * 4,))    # color
        self.arm2 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [100, 150,              # location
                     100, 160,
                     200, 160,
                     200, 150]),
                    ('c3B', (255, 255, 255) * 4,))

    def render(self):
        self._update_arm()
        self.switch_to()
        self.dispatch_events()
        self.on_draw()
        #needed if not double buffered, screen won't render without it
        self.flip()

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def _update_arm(self):
        #should make an annotated diagram with the labels so things are dead obvious
        (a1l, a2l) = self.arm_info['l']     # radius, arm length
        (a1r, a2r) = self.arm_info['r']     # radian, angle
        
        #calculate joint positions
        a1xy = self.center_coord            # a1 start (x0, y0)
        a1xy_ = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy   # a1 end and a2 start (x1, y1)
        a2xy_ = np.array([np.cos(a1r+a2r), np.sin(a1r+a2r)]) * a2l + a1xy_  # a2 end (x2, y2)

        #figure out by how much joints need to be rotated
        #what happens if you remove pi over 2 here
        a1tr  = np.pi / 2 - self.arm_info['r'][0] 
        a2tr = np.pi / 2 - self.arm_info['r'].sum()
        #would be better to work with an arm structure as opposed to manually transforming each vertex
        #see by how much joint is transformed to figure out by how much to transform the vertices
        #a picture would make this really obvious for the blog
        #below we are handcoding all these transformations to understand how they work
        #but had we used a robotics simulator like Mujoco we wouldn't face this issue

        xy01 = a1xy + np.array([-np.cos(a1tr), np.sin(a1tr)]) * self.thickness
        xy02 = a1xy + np.array([np.cos(a1tr), -np.sin(a1tr)]) * self.thickness
        
        xy11 = a1xy_ + np.array([np.cos(a1tr), -np.sin(a1tr)]) * self.thickness
        xy12 = a1xy_ + np.array([-np.cos(a1tr), np.sin(a1tr)]) * self.thickness

        #similar to xy11 and xy22
        xy11_ = a1xy_ + np.array([np.cos(a2tr), -np.sin(a2tr)]) * self.thickness
        xy12_ = a1xy_ + np.array([-np.cos(a2tr), np.sin(a2tr)]) * self.thickness
        
        #similar to xy01 and xy02
        xy21 = a2xy_ + np.array([-np.cos(a2tr), np.sin(a2tr)]) * self.thickness
        xy22 = a2xy_ + np.array([np.cos(a2tr), -np.sin(a2tr)]) * self.thickness

        self.arm1.vertices = np.concatenate((xy01, xy02, xy11, xy12))
        self.arm2.vertices = np.concatenate((xy11_, xy12_, xy21, xy22))


if __name__ == '__main__':
    env = ArmEnv()
    while True:
        env.render()
        env.step(env.random_action())