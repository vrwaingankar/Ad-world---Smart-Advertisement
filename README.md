# Ad-world-Smart Advertisement
Improve the consumer marketing designation by counting the number of visitors visited a particular ad published.

The main idea of the project is to develop an embedded system to know how many visitors have looked into a particular Ad for a specified amount of time and keep a counter to determine how many people were interested in it and charge the organisation based on view counts instead of traditional way of charging based on number of days/months the ad was displayed. The ads here are those displayed on electronic displays in and around public places and public transports.
The method helps to analyse the behavior of people in a given region and display ads accordingly for increasing business.
Eg: if a region X has higher view count for product M then for product N, then there is a greater business potential for product M in that region.

Max-Margin (MMOD) CNN face detector algorithm is used for face detection.

Objectives of this project is to design a system with following requirements:
1) To detect visitor standing in front of Ad with non-contact measurement (range 400cm).
2) Turn the camera on when an object is detected in front of Ad.
3) Capture 5 consecutive images with desired intervals of time between successive images.
4) Face detection in those 5 images using MMOD CNN face detector.
5) Increase counter when threshold is met.
6) Periodic updates via email to advertisers on number of views.
7) The view count is stored in text file Individual_Samples.txt.
8) The algorithm considers detection of complete face for updating view count (complete face = True, partial face = False)
NOTE: An improved version for finding the position of head by computing pitch, roll and yaw with nose as centre can be found in my other repository https://github.com/vrwaingankar/head-pose-estimation-and-view-counting

The Result folder contains results of different scenarios
For instance:
1) one person looking away and two looking towards the ad and it has correctly distinguished who was actually looking into the ad and who was looking away.
2) "no_face.jpeg" simulates a scenario where Ultrasonic sensor detects because of some random movements of objects but no person is actually looking into the ad. Hence no faces are detected.
3) The algorithm was tested on maximum of 17 people to find it's maximum capacity for correct face detection
