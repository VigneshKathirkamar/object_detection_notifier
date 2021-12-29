# Object Detection Notifier
## **Detect objects, capture it and send them to mail with the image attachment**

Follow the below commands step by step to make this project run

```
git clone https://github.com/VigneshKathirkamar/object_detection_notifier.git

cd object_detection_notifier

wget "http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz"
```
Once the tar file gets downloaded, unzip it in the same folder (object_detection_notifier)

```
pip3 install -r requirements.txt
```
## Generation of 16 digit password for you mail id
Follow this link:https://qr.ae/pGepQ7 to generate 16 digit password for your mail id

Run the below command with your user name and password.

```sudo python3 person_detector_video.py --to_mail_id karthik.akash08@gmail.com --pwd qlaxxlvqpknkhhqp --from_mail_id i51vignesh@gmail.com```

## To do
- Scaling the project. Right now, since we are using gmail, the total number of notifications/mails is limited to 2000 per person per day.(i.e 500 mails for 4 person per day)
- Instead of person detection, models like MTCNN can be used to crop the face alone and this data can be used for training a classifier model. This would find use case in retail store analysis
