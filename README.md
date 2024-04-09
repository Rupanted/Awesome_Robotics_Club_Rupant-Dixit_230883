# Awesome_Robotics_Club_Rupant-Dixit_230883
<br> First we write basic program for taking input and output of initial angles and target coordinates.
<br>Here’s how we can approach Part B:

Input:
Initial joint positions/angles.
Target position coordinates (3D).<br>
Algorithm Overview:
Initialize the joint positions based on the initial angles.
Iteratively adjust the joint positions forward and backward until the end effector reaches the target position or the maximum number of iterations is reached.
If the end effector reaches the target position within the specified tolerance, the point is considered reachable.<br>
Output:
Determine whether the target position is reachable (yes/no).
