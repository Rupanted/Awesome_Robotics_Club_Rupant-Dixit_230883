import numpy as np

def fabrik_reachability(initial_angles, target_position, link_lengths, tolerance=1e-6, max_iterations=100):
    
    num_joints = len(initial_angles)
    initial_angles_rad = np.deg2rad(initial_angles)
    
    # Initialize joint positions based on initial angles
    joint_positions = np.zeros((num_joints, 3))
    for i in range(num_joints):
        joint_positions[i, 0] = np.cos(np.sum(initial_angles_rad[:i+1]))
        joint_positions[i, 1] = np.sin(np.sum(initial_angles_rad[:i+1]))
        joint_positions[i, 2] = link_lengths[i]
    
    # Iteratively adjust joint positions
    for _ in range(max_iterations):
        # Forward reaching
        joint_positions[-1] = target_position
        for i in range(num_joints - 2, -1, -1):
            vec_to_next = joint_positions[i+1] - joint_positions[i]
            vec_to_next /= np.linalg.norm(vec_to_next)
            joint_positions[i] = joint_positions[i+1] - link_lengths[i] * vec_to_next
        
        # Backward reaching
        joint_positions[0] = np.array([0, 0, link_lengths[0]])
        for i in range(1, num_joints):
            vec_to_prev = joint_positions[i-1] - joint_positions[i]
            vec_to_prev /= np.linalg.norm(vec_to_prev)
            joint_positions[i] = joint_positions[i-1] + link_lengths[i] * vec_to_prev
        
        # Check convergence
        end_effector_dist = np.linalg.norm(joint_positions[-1] - target_position)
        if end_effector_dist < tolerance:
            return True
    
    return False

# Example usage
initial_joint_angles = [30, 45, 60, 90]  # Initial joint angles in degrees
target_position = np.array([10, 20, 15])  # Target position (3D coordinates)
link_lengths = [23, 15, 3]  # Link lengths

reachable = fabrik_reachability(initial_joint_angles, target_position, link_lengths)
print(f"Is the target position reachable? {'Yes' if reachable else 'No'}")
