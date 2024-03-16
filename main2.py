def decode(file_dir):
    with open(file_dir, "r") as file:
        raw_data = file.readlines()

    temp_dict = {}
    for i in raw_data:
        temp = i.split(" ")
        temp_dict.update(({int(temp[0]): temp[1].strip('\n')}))

    nums = list(temp_dict.keys())
    nums = sorted(nums)
    step = 1
    pyr_list = []
    while len(nums) != 0:
        if step <= len(nums):
            pyr_list.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            print("This is an invalid number of items to decode properly")
            exit()


    keys = []
    for i in pyr_list:
        print(i[-1])
        keys.append(i[-1])


    output = ""
    for i in keys:
        output = f"{output}{temp_dict[i]} "
        output = output.capitalize()
    return output


print(decode("text.txt"))
