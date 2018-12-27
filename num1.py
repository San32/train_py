try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract


# 영어 인식
print(pytesseract.image_to_string(Image.open('english.png')))

# 한글 
print(pytesseract.image_to_string(Image.open('hangul.png'), lang='Hangul'))

# 출처 : https://webnautes.tistory.com/947