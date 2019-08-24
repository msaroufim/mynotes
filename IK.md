# Inverse Kinematics

## Intro to IK with Jacobian transpose, pseudoinverse nad damped least squares method by Sam Buss

Most common joints are revolute (rotational) and prismatic (translational)

Show 2 pictures. Door hinges are revolute as an example

Let's assume we have bunch of revolute joints then \\(\theta_1 ... \theta_n \\) represents each of the joint angles. We can have \\(k \\) effectors whose position is determined by a vector \\(s = s_1, s_2 ... s_k \\) where \\(s_i \in R^3 \forall i \\)

Given target positions \\(t = (t_1 ... t_k)) for each end effector, the goal of inverse kineamtics is to find the values of \\( \theta \\) s.t \\(t = s(\theta) \\)

The basic equation for forward dynamics is

\\(\vec{s} = J(\theta) \dot \theta \\)

The intuition for the above formula is that the new state is a function of the change in parameters times the sensitivity of each joint state w.r.t to changes in the joint angle.

where \\(J(\theta) = \frac{\partial s_i}{\partial \theta_j})_{i, j} \\)

So we can solve the IK problem by solving the equation

\\( \vec{e} = J \Delta \theta \\) where \\(\vec{e} = \vec{t} - \vec{s} \\)


Each entry of the Jacobian matrix is easy to compute. 

In the case where we're working with a revolute (rotational joint)

\\( \frac{\partial s_i}{\partial \theta_j} = v_j \times (s_i - p_j) \\) where \\(p_j \\) is the position of the joint and \\(v_j \\) is the unit vector pointing along the current axis of rotation of the joint.

In the case of the prismatic (rotational joint) it's even simpler

There are tons of different kinds of joints but the ones we've covered so far are the most popular. Maybe add a table of different kinds of joints

\\( \frac{\partial s_i}{\partial \theta_j} = v_j \\)

At each iteration we can do an iterative and small step \\(\Delta \theta = \alpha J^T \vec{e} \\)

Ideally we'd like to just invert \\(J \\) but that computation can be really slow which is why we can settle for the transpose or the pseudoinverse which work well in practice.

One issue with both of those techniques is they tend to become unstable once they are close to the solution which can cause convergence issues. So we can borrow a trick from the supervised learning litterature to come up with a technique called damped least squares. So we wanna find \\(\Delta \theta \\) that minimizes


\\( || J \Delta \theta - \vec{e} ||^2 + \lambda || \Delta \theta ||^2 \\)

There's also some tricks that involve compressing the size of \\( J \\) by techniques such as Singular Value Decomposition