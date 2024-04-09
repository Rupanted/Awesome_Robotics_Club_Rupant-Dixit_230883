import math

def forward_kinematics(link_lengths, joint_angles):
  """Calculates the end effector position using forward kinematics."""
  end_effector = [0, 0, 0]
  for i, angle in enumerate(joint_angles):  # Iterate through link lengths and angles
    x = end_effector[0] + link_lengths[i] * math.cos(angle)
    y = end_effector[1] + link_lengths[i] * math.sin(angle)
    end_effector = [x, y, end_effector[2]]  # Update end effector position
  return end_effector

def fabrik(link_lengths, target_position, initial_angles, epsilon=0.01, max_iterations=100):
  """Implements the FABRIK algorithm."""
  joint_angles = [math.radians(angle) for angle in initial_angles]
  for _ in range(max_iterations):
    end_effector = forward_kinematics(link_lengths, joint_angles)
    distance = math.sqrt(
        (target_position[0] - end_effector[0])**2
        + (target_position[1] - end_effector[1])**2
        + (target_position[2] - end_effector[2])**2
    )
    if distance <= epsilon:
      return [math.degrees(angle) for angle in joint_angles]

    # Corrected backward pass using joint angles
    for i in reversed(range(1, len(joint_angles))):
      direction = (end_effector[0] - joint_angles[i - 1][0], end_effector[1] - joint_angles[i - 1][1])
      target_distance = math.sqrt(sum(d**2 for d in direction))

      if target_distance <= link_lengths[i]:
        new_joint_angle = math.atan2(direction[1], direction[0])
      else:
        new_joint_angle
