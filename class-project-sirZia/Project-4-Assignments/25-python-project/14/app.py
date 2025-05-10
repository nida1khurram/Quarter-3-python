from PIL import Image, ImageEnhance, ImageFilter


def apply_filter(image_url):
    img = Image.open(image_url) 
    img.show(title="Original Image")

    bright = ImageEnhance.Brightness(img)
    bright_img = bright.enhance(1.5)  
    bright_img.show(title="Brightness Increased")

    contrast = ImageEnhance.Contrast(img)
    contrast_img = contrast.enhance(2.0)  
    contrast_img.show(title="Contrast Increased")

    blur_img = img.filter(ImageFilter.GaussianBlur(5)) 
    blur_img.show(title="Blur Effect")

    bright_img.save("brightened_image.jpg")
    contrast_img.save("contrast_image.jpg")
    blur_img.save("blur_image.jpg")

    print("Filters applied successfully! Images saved.")



def main():
    apply_filter("morskie-oko-tatry.jpg")


if __name__ in "__main__":
    main()