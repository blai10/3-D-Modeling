import sys
import data
import cast
import commandline

USAGE_MESSAGE = 'usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [' \
                '-light x y z r g b] [-ambient r g b] '


def main(argv):
    image_param = {
        '-eye': [0.0, 0.0, -14],
        '-view': [-10, 10, -7.5, 7.5, 512, 364],
        '-light': [-100, 100, -100, 1.5, 1.5, 1.5],
        '-ambient': [1, 1, 1]
    }
    commandline.print_dict(image_param)
    if commandline.validate_commandline(argv) is True:
        try:
            f = open(argv[1], 'r')
        except FileNotFoundError:
            print(USAGE_MESSAGE)
            sys.exit(1)
        image_param = commandline.parse_commandline(argv, image_param)
        commandline.print_dict(image_param)
        sphere_list = []
        line_count = 1
        for line in f.readlines():
            split = line.split()
            if commandline.validate_commandline(split):
                sphere_list.append(data.sphere(data.point(float(split[0]), float(split[1]), float(split[2])),
                                               float(split[3]),
                                               data.color(float(split[4]), float(split[5]), float(split[6])),
                                               data.finish(float(split[7]), float(split[8]), float(split[9]),
                                                           float(split[10]))))
            else:
                print('Malformed Sphere on the Line', line_count, '. . . skipping')
            line_count = line_count + 1
            min_x = image_param['-view'][0]
            max_x = image_param['-view'][1]
            min_y = image_param['-view'][2]
            max_y = image_param['-view'][3]
            width = int(image_param['-view'][4])
            height = int(image_param['-view'][5])
            eye_point = data.point(image_param['-eye'][0], image_param['-eye'][1], image_param['-eye'][2])
            amb_color = data.color(image_param['-ambient'][0], image_param['-ambient'][1], image_param['-ambient'][2])
            light = data.light(data.point(image_param['-light'][0], image_param['-light'][1], image_param['-light'][2]),
                               data.color(image_param['-light'][3], image_param['-light'][4], image_param['-light'][5]))
            cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, amb_color, light)


if __name__ == '__main__':
    main(sys.argv)
