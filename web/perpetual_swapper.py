import os, time

while(1):
	for face_img in os.listdir("/Users/Gavin/facecheck/web/files"):
		if face_img.endswith(".jpg"):
			print("Image found: " + face_img)
			face_img_path = "./files/" + face_img
			for file in os.listdir("/Users/Gavin/facecheck/web/seed_imgs"):
			    if file.endswith(".jpg"):
			        print("\tSwapping faces: " + file)
			        file_path = "./seed_imgs/" + str(file)
			        output = file

			        print (face_img_path)
			        print (file_path)
			        os_call = "python ./faceswap.py " + file_path + " " + face_img_path + " " + output
			        print os_call
			        os.system(os_call)

			os.system("rm /Users/Gavin/facecheck/web/files/" + face_img)
	print ("Sleeping...")
	time.sleep(5)