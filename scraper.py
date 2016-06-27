import os
# os.system("image-scraper  http://www.prettydesigns.com/70-cool-korean-japanese-hairstyles-asian-guys-2015/")

for file in os.listdir("/Users/Gavin/facecheck/web/seed_imgs"):
    if file.endswith(".jpg"):
        print(file)
        file_path = "./images_www.prettydesigns.com/" + str(file)

        os.system("python ./faceswap.py " + file_path + " ira_2.jpg " + file)

form = cgi.FieldStorage()                 # parse form data