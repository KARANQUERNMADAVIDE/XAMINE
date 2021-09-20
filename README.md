# XAMINE

It’s not how much you lift, it’s how well you lift. Doing exercises in the right posture is an important aspect of it. If the posture is incorrect, all the efforts to have a well strengthened physique go in vain. It may even cause injury or have a negative effect on your body. Doing exercises not only makes your body fit but also improves your mental health. Xamine will be a reliable system that will help users to do exercises in the right posture.

Xamine will help the users in home exercises guiding them through the right posture and evaluating their postures if they are correct. It will decrease the need for a physical instructor to instruct the exercise. It will help users to do exercises in the right posture at their convenience. This all will be done using minimum resources and only a camera feed from the user’s device.

With Pose estimation, smart assistance has been built to guide and instruct the users throughout their practice period to attain the correct posture. This helps reduce stress, anxiety, and tension through a series of guided meditative poses. The solution includes human pose estimation using OpenCV framework. Deep Convolutional Neural Network as the architecture, various data collection and processing tasks have been performed.

## Application Link

Use the [link]

## SCOPE 
With the current pandemic situation, most gyms are closed and people are looking for other ways to stay in shape. The most likely solution is to work out at home through the Fitness app. Plus, memberships to good gyms are quite expensive. The main attraction has always been the personal attention given to the members in the current gymnasium. A personal trainer can correct your posture, talk to you, motivate you, and customize exercises to suit your physical condition. With the help of machine learning, these personalized tips can be provided to users. The computer will monitor a person's training to make sure all of their poses and angles are correct. From yoga to lifting weights, the system guides you through every step. It goes beyond your usual training routine and becomes your personal assistant that motivates you to keep practicing.

### Methodology

Implementation: In this phase, implementation of some of the existing state of the art approaches will be carried out like OpenPose or Convolutional Neural Networks or mediapipe etc. Some of these approaches aim to work on the exercise input and generate keypoints that go right into our model for future purposes. Some also generate time series frames free from any impurity or noise. 

Modelling: Now comes the step where the processed keypoints are trained to the model that performs the actual task of classification and correction. Design and development of a suitable platform: After the implementation of some of the existing approaches, a GUI based platform will be designed to operate our business logic. 

Experimental analysis: The experimental analysis will be carried out by testing the developed model in terms of performance evaluation parameters. The analysis and literature survey is a continuous process till the design and implementation phase ; if there is any update related to these approaches, it can be added on.

### Data Collection
In this phase we aim to collect ,prepare and preprocess our dataset which is suitable enough for training the model . From previous analysis made we shall understand the techniques dedicated to give rise to a very appropriate dataset.In our case we may be performing data augmentation – techniques to increase the amount of data by adding slightly modified copies of already existing data.

### Software interface standards
The software package is developed using HTML and CSS, back end is done by Flask and the Deep Learning model is trained using Keras and implemented using TensorFlow. Operating System: Window XP, Windows 7 and higher version Language: HTML, Flask, CSS, HTML, Python Database: SQLite


### Model Training
We have bifurcated our work goals into two streams 
1. Deep Learning Neural Net model 
2. Web Application 
As far as the DNN is concerned we go on continuously processing the images received from the camera feed using OpenCV library and mediapipe Algorithm ( BlazePose Detector and BlazePose GHUM 3D models) that will serve our 2 important agendas of Detection and Estimation respectively. These aim in order to make calculations and predictions to get done all the above requirements. The WebApp is used to display detailed information to a user about a list of exercises. The user can select the desired exercises, practise each pose and finally, check position correctness using the interface which is fed by the DNN models. The solution we came upon was using the technique of generating key-points which further works

###   Novelty of Work 
The proposed solution is quite unique as none of our competitors provide services with the ease that we aim to provide them with. There is no such system at present that can evaluate the real time posture of the person performing some exercise and evaluates it. The alternative present is either the personal trainer or the gym trainer apps that tells users how to perform the exercise but not evaluate it. Our system evaluates the real time posture of the human body and helps them perform exercise to the full potential in the right posture.

### PRODUCT FEATURES
1. Registration : Those who are new to the app are required to register and then login to get benefit of it. 
2. Login in the Web application : For those who have been already registered, can enter their valid e-mail and can benefit from it. 
3. Exercise : The exercise which is desired to be practiced is to be selected. 
4. Practice : This button enables the device camera to detect posture of the human while executing the selected exercise. 5. Profile : This button enables the user to access personal information & exercise history for the user.

### Application Deployment

Flowchart of application process :-

![image](https://user-images.githubusercontent.com/69417609/134057245-395ce94c-86cd-4569-82fa-17988969f00e.png)

Flow of system (Component-Wise) :- 
![image](https://user-images.githubusercontent.com/69417609/134058033-d53ae499-213f-427f-81cf-0c8b0a6fa798.png)

Flow of system (Activity-Wise) :- 
![image](https://user-images.githubusercontent.com/69417609/134058187-24ab6bcd-697e-44b7-9330-ea54421568bd.png)


### Screenshots

![image](https://user-images.githubusercontent.com/69417609/134059580-5b25e6ed-cb52-4dd5-9e98-7e35cc2e014b.png)

User registers for a non existing account.
![image](https://user-images.githubusercontent.com/69417609/134059912-64158ce1-0de4-4c41-a477-0b54dc757a2d.png)

User then logins in to the created account.
![image](https://user-images.githubusercontent.com/69417609/134060274-d5f0516e-b9a2-4bd8-bbed-99de621d7597.png)

User gets a list of exercises that he/she needs to be practised.
![image](https://user-images.githubusercontent.com/69417609/134060341-ba877846-dc7e-4a4d-98cc-4fe54bc11f62.png)

Individual Pages
![image](https://user-images.githubusercontent.com/69417609/134060555-9701a145-9b18-4cc9-9cca-50353a1b2d3e.png)

Key Points generation
![image](https://user-images.githubusercontent.com/69417609/134060704-45e1e1cb-7f15-4415-9716-cfc3282e4301.png)





