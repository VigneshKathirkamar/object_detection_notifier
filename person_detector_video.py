# importing necessary libraries 
import cv2 
import numpy as np 


def detected_object(video):
    detection_folder = '/home/vignesh/virtual_environments/person_notifier/ext_data/detected_objects/'
    
    # reading the class names and making a list out of it 
    with open('/home/vignesh/virtual_environments/person_notifier/ext_data/labels/new_labels.txt','r') as f: 
        class_names = f.read().split('\n') 
    colors = np.random.uniform(0,255,size=(len(class_names),3)) 
        
    # laoding the model
    model = cv2.dnn.readNet(model='/home/vignesh/virtual_environments/person_notifier/ext_data/dl_model/ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.pb',config='/home/vignesh/virtual_environments/person_notifier/ext_data/config_files/ssd_mobilenet.pbtxt.txt',framework="Tensorflow") 
    
    # loading the video
    video = cv2.VideoCapture(video)
    while video.isOpened():
        #img = cv2.imread('/home/vignesh/virtual_environments/person_notifier/ext_data/detected_objects/brad_pitt.jpg') 
        ret, img = video.read()
        img_h, img_w, _  = img.shape 
        blob = cv2.dnn.blobFromImage(image=img, size = (300,300), mean=(104,117,123), swapRB=True) 
        model.setInput(blob) 
        output = model.forward() 
        count = 0
        for detection in output[0,0,:,:]: 
            count+=1
            confidence = detection[2] 
            if confidence > 0.5: 
                class_id = detection[1] 
                class_name = class_names[int(class_id)-1]+' '+str(confidence)[:4] 
                color = colors[int(class_id)] 
                box_x = int(detection[3] * img_w) 
                box_y = int(detection[4] * img_h) 
                box_w = int(detection[5] * img_w) 
                box_h = int(detection[6] * img_h) 
                img = cv2.rectangle(img,((box_x),(box_y)),((box_w),(box_h)),color,thickness =2) 
                crop_img = img[box_y:,box_x:box_w]
                cv2.imwrite(detection_folder+'cropped_img_'+str(count)+'.jpg',crop_img)
    #        img = cv2.putText(img,class_name,(int(box_x),int(box_y-5)),cv2.FONT_HERSHEY_SIMPLEX,1,color,2) 
    # cv2.imshow('image',img) 
    # cv2.imwrite('inference_img.jpg',img) 
    # cv2.waitKey(0) 
    # cv2.destroyAllWindows() 
    return detection_folder