# import tesserocr
# from PIL import Image
# image = Image.open('checkCode.jpg')
#
# image = image.convert('L')
# threshold = 127
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# image = image.point(table,'1')
#
# # image.show()
# result = tesserocr.image_to_text(image)
# print(result)


# from PIL import Image,ImageEnhance
# import pytesseract
#
# image = Image.open('checkCode.jpg')
#
# image = image.convert('L')
# # threshold = 127
# # table = []
# # for i in range(256):
# #     if i < threshold:
# #         table.append(0)
# #     else:
# #         table.append(1)
# # image = image.point(table,'1')
# image=ImageEnhance.Contrast(image)
# image=image.enhance(3)
#
# image.show()
# print(pytesseract.image_to_string(image))