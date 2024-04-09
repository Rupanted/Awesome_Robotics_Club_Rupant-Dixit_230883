def get_user_input():
    angles = list(map(float, input('Enter 4 initial angles separated by spaces ').split(' ')))
      
    
    
    
    target_x = float(input("target X-coordinates: "))
    target_y = float(input("target Y-coordinates: "))
    target_z = float(input("target Z-coordinates: "))
    
    print(f'Value of initial Angle are: {angles[0]}, {angles[1]}, {angles[2]}, {angles[3]}')
    print(f'Target Value is {(target_x, target_y, target_z)}')

    return angles, [target_x, target_y, target_z]



link_length = [23, 15, 3]
  
angles, target_coordinates = get_user_input()
