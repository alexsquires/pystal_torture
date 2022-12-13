def shift_index(index_n, shift):
    """
    Shifts the index of a site in the unit cell to the corresponding
    index in the 3x3x3 halo supercell. Used when getting neighbour list for 
    supercell from unit cell neighbour list
    
    Args:
      index_n (int): original index
      shift ([int,int,int]): shift to image for which to obatin index eg. [-1,-1,-1]
     
    Returns:
      new_index (int): index for image site in supercell

    """

    new_x = ((int(index_n / 9) % 3) + shift[0]) % 3
    new_y = ((int(index_n / 3) % 3) + shift[1]) % 3
    new_z = ((int(index_n) % 3) + shift[2]) % 3

    new_index = int(
        27 * int(index_n / (27)) + (new_x % 3) * 9 + (new_y % 3) * 3 + (new_z % 3)
    )
    return new_index
