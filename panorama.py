import cv2
import os

mainFolder = 'Images'
myFolders = os.listdir(mainFolder)
print(myFolders)

for folder in myFolders:
    path = mainFolder+'/'+folder
    images = []
    myList = os.listdir(path)
    print(f'Total no of images detected {len(myList)}')
    for imageName in myList:
        curImg = cv2.imread(f'{path}/{imageName}')
        curImg = cv2.resize(curImg,(0,0),None,0.2,0.2)
        images.append(curImg)

    stitcher = cv2.Stitcher.create()
    (status,result) = stitcher.stitch(images)
    if (status == cv2.STITCHER_OK):
        print("Panorama Generated")
        cv2.imshow(folder,result)

    else:
        print("Panorama Generation Unscucessful")

cv2.waitKey(0)















