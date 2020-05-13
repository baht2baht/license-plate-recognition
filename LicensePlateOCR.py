# License Plate Recognition
# Thai license plate recognition with Python
# - Pillow
# - Tesseract
#
# By Kanatat Asipong
#
# Revision
# 12/05/2020 - Kanatat
#   - Initial base code with OCR Function and TextAccuracyCompare Function.

from PIL import Image
import pytesseract

class result:
    license_text = ""
    province_text = ""

# OCR Function
def OCR(image_path):
    # Load image
    load_image = Image.open(image_path)

    # Stored Image width and height
    (image_width, image_height) = load_image.size

    # Convert loaded image to grayscale
    converted_image = Image.Image.convert(load_image , mode="L")

    # Split image to 3 row as aspect ratio
    # Upper 2 rows for license plate characters
    # Lower 1 row for province characters

    # Upper part
    upper_left = 0
    upper_top = 0
    upper_right = image_width
    upper_bottom = (image_height / 3) * 2
    upper_part = converted_image.crop((upper_left, upper_top, upper_right, upper_bottom))

    # Lower part
    lower_left = 0
    lower_top = (image_height / 3) * 2
    lower_right = image_width
    lower_bottom = image_height
    lower_part = converted_image.crop((lower_left, lower_top, lower_right, lower_bottom))

    # Processing OCR
    text_upper = pytesseract.image_to_string(upper_part, lang="tha")
    text_lower = pytesseract.image_to_string(lower_part, lang="tha")

    # result = {
    #     "license_text": text_upper,
    #     "province_text": text_lower,
    # }
    result.license_text = text_upper
    result.province_text = text_lower

    return result

# Text Accuracy Compare Function
def TextAccuracyCompare(label_text, predict_text):

    valid_char = 0
    label_text_length = len(label_text)
    predict_text_length = len(predict_text)
    diff_len = abs(label_text_length - predict_text_length)

    text_length = label_text_length > predict_text_length and label_text_length or predict_text_length

    if(label_text_length > predict_text_length):
        for i in range(0, diff_len):
            predict_text = predict_text + ' '
    elif(predict_text_length > label_text_length):
        for i in range(0, diff_len):
            label_text = label_text + ' '
    else:
        pass

    # print(label_text + 'End')
    # print(predict_text + 'End')

    for index in range(0, text_length):
        # print(index)
        print('Label: ' + label_text[index] + ', Predict: ' + predict_text[index])
        # print(index)
        if(predict_text[index] == label_text[index]):
            # print('Correct')
            valid_char = valid_char + 1
        else:
            # print('Wrong')
            pass

    # print(valid_char)
    # print(label_text_length)
    accuracy = ((valid_char / text_length) * 100 )
    # getcontext().prec = 5
    accuracy = round(accuracy, 5)
    print('Accuracy: ' + str(accuracy) + '%')

    return accuracy