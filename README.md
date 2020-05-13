# Thai License Plate Recognition

Thai License Plate Recognition with Python

## Getting Started

### Prerequisites

This project is developing with python and it needs the following modules to be installed before run:

  - Pillow
  - Pytesseract

### Installing

Install prerequisites modules

```
pip install pillow
pip install pytesseract
```

Python version 3.4.X or more

```
pip3 install pillow
pip3 install pytesseract
```


## Running the tests

Testing the funciton with an example image.



```
python main.py
```

Python version 3.4.X or more

```
python3 main.py
```

## LicensePlateOCR

### Functions

* **OCR** : Return a class of processed text from the input license plate image.
	* Parameters
	    *  image_path: String of input image file path

```
import LicensePlateOCR as lp

image_path = 'example-license.jpg'
text_result = lp.OCR(image_path)
print(text_result.license_text)
print(text_result.province_text)
```



## Built With

* [Pillow](https://pillow.readthedocs.io/en/stable/) - Image manipulating library
* [Pytesseract](https://github.com/madmaze/pytesseract) - OCR library



## Authors

* **Kanatat Asipong** - *Initial work* - [baht2baht](https://github.com/baht2baht)

## License

**NOTE**: This software depends on other packages that may be licensed under different open source licenses.