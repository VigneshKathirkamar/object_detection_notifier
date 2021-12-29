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
