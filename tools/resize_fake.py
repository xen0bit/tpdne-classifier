from PIL import Image  
from glob import iglob
from tqdm import tqdm

i = 0
for imageFile in tqdm(iglob("./fake/*.jpg")):
    # Opens a image in RGB mode
    try:  
        im1 = Image.open(imageFile)  
        newsize = (128, 128) 
        im1 = im1.resize(newsize)
        im1.save("./fake/resized/" + str(i) + ".png")
    except:
        pass
    i+=1
