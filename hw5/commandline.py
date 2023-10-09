def print_dict(dict):
    for k, v in dict.items():
        print(k, v, end=' ')
    print('\n')


def validate_sphere_line(line):
    if len(line) != 11:
        return False
    else:
        for e in line:
            try:
                float(e)
            except ValueError:
                return False
        return True


def validate_commandline(argv):
    if len(argv) < 2:
        return False
    else:
        return True


def parse_commandline(argv, dict):
    new_dict = {
        '-eye': [0.0, 0.0, -14],
        '-view': [-10, 10, -7.5, 7.5, 512, 364],
        '-light': [-100, 100, -100, 1.5, 1.5, 1.5],
        '-ambient': [1, 1, 1]
    }

    for ele in argv:
        idx = argv.index(ele)
        if ele == '-view':
            for i in range(6):
                try:
                    new_dict['-view'][i] = float(argv[idx + i + 1])
                except IndexError:
                    for j in range(6):
                        new_dict['-view'][i] = dict['-view'][j]
                except ValueError:
                    if argv[idx + i + 1] in dict:
                        for j in range(6):
                            new_dict['-view'][j] = dict['-view'][j]
                        else:
                            pass

    for ele in argv:
        idx = argv.index(ele)
        if ele == '-eye':
            for i in range(3):
                try:
                    new_dict['-eye'][i] = float(argv[idx + i + 1])
                except IndexError:
                    for j in range(3):
                        new_dict['-eye'][i] = dict['-eye'][j]
                except ValueError:
                    if argv[idx + i + 1] in dict:
                        for j in range(3):
                            new_dict['-eye'][j] = dict['-eye'][j]
                        else:
                            pass

    for ele in argv:
        idx = argv.index(ele)
        if ele == '-light':
            for i in range(6):
                try:
                    new_dict['-light'][i] = float(argv[idx + i + 1])
                except IndexError:
                    for j in range(6):
                        new_dict['-light'][i] = dict['-light'][j]
                except ValueError:
                    if argv[idx + i + 1] in dict:
                        for j in range(6):
                            new_dict['-light'][j] = dict['-light'][j]
                        else:
                            pass

    for ele in argv:
        idx = argv.index(ele)
        if ele == '-ambient':
            for i in range(3):
                try:
                    new_dict['-ambient'][i] = float(argv[idx + i + 1])
                except IndexError:
                    for j in range(3):
                        new_dict['-ambient'][i] = dict['-ambient'][j]
                except ValueError:
                    if argv[idx + i + 1] in dict:
                        for j in range(3):
                            new_dict['-ambient'][j] = dict['-ambient'][j]
                        else:
                            pass
    return new_dict

# image = open('image.ppm', 'w')

# image.write(f'{color.r}{color.g}{color.b}\n')
# image.close()

# sphere_list = []
# for line in data:
# nums = line.split()
# try:


#   x = nums[0]
#   y = nums[1]
#   z = nums[2]
#   center = point(x,y,z)
#   red = nums[3]
#   green
#   blue
#   sphere = sphere(center, rad, color, finish)
#   sphere_list.append(sphere)
# except IndexError:
#   print('skipping line')


# eye = point(0, 0, -14)
# sys.argv
# i = 2
# while i < len(sys.argv):
#   flag = sys.argv[i]
#   if flag = '_eye':
#       eye = point(float(sys.argv[i+1]), float(sys.argv[i+2]), float(sys.argv[i+3]))
#   i = i+4
#   if flag == '_view':
#   min_x = sys.argv[i+1]
#   max_x =
#   min_y =
#   max_y =
#   width =
#   height =
