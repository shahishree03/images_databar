from simpleimage import SimpleImage

GREEN = 127
BLUE = 127

CANVAS_WIDTH = 1100
CANVAS_HEIGHT = 200
MAX_RED_VALUE = 255

visualization_file = "data-child-mortality.txt"

def main():
    # New image
    canvas = SimpleImage.blank(CANVAS_WIDTH, CANVAS_HEIGHT)
    data_list = create_list()
    canvas = create_image(data_list, canvas)
    canvas.show()

def create_list():
    #Function to read txt file and put all items to the list
    data_list = []
    with open(visualization_file) as f:
        next(f)
        next(f)
        for x in f:
            x = x.strip()
            data_list.append(float(x))
    return data_list


def create_image(data_list, canvas):

    
    #Measure width of each fraction
    frac_width = CANVAS_WIDTH // len(data_list)
    # create new image where the resulted pixels will be stored
    new_image = SimpleImage.blank(frac_width * len(data_list), CANVAS_HEIGHT)
    #Iterate as many times as there will be fractions in whole canvas
    for x in range(len(data_list)):

        #We are rounding, because we are doing float arithmetic to fill whole canvas width
        for y in range(frac_width):
            for z in range(CANVAS_HEIGHT):

                #Get starting point of each fraction
                start_y = frac_width * x + y
                pixel = canvas.get_pixel(start_y, z)
                update_pixel(data_list[x], pixel)
                new_image.set_pixel(start_y, z, pixel)
    return new_image

def update_pixel(list_number, pixel):

    #Function to colour pixel
    pixel.red = list_number * MAX_RED_VALUE
    pixel.green = GREEN
    pixel.blue = BLUE
    return pixel


if __name__ == '__main__':
    main()
