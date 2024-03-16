def read_file(file_dir):
    with open(file_dir, "r") as file:
        raw_data = file.readlines()
    return raw_data


def make_dic(raw_data):
    temp_dict = {}
    for i in raw_data:
        temp = i.split(" ")
        temp_dict.update(({int(temp[0]): temp[1].strip('\n')}))
    return temp_dict


def org_nums(dictionary):
    nums = list(dictionary.keys())
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
    return pyr_list


def pull_keys(pyrimid):
    keys = []
    for i in pyrimid:
        print(i[-1])
        keys.append(i[-1])
    return keys


def build_sentence(keys, dictionary):
    output = ""
    for i in keys:
       output = f"{output}{dictionary[i]} "
    return output



data = read_file("text.txt")

dictionary = make_dic(data)

pyrimid = org_nums(dictionary)

keys = pull_keys(pyrimid)

output = build_sentence(keys, dictionary)

print(dictionary)
print(pyrimid)
print(keys)
print(output)
