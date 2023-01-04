# GYM TRACK
#### Video Demo:  <URL https://www.youtube.com/watch?v=hIXRsczxRL8>
#### Description:
Gym Track is a web application designed to help people keep track of their fitness progress.

Its first feature is "calculators". This section has three different calculators which take in different input depending on what the calculator uses. Firstly, there is a body fat percentage calculator which counts your body fat percentage, it takes as input the gender, weight, height, neck and waist, this calculator uses the following formula to provide the results:
For males =   495 / (1.0324 - 0.19077×log10(waist-neck) + 0.15456×log10(height)) - 450
for females = 495 / (1.29579 - 0.35004×log10(waist+102-neck) + 0.22100×log10(height)) - 450

The second calculator calculates the amount of calories a person needs to take daily. It takes gender, height, weight, age and activity of a person as inputs to provide the results. The calculator provides three different results which a person might use for three different purposes (losing weight, maintaining weight or gaining weight). The following formula is used:
For males = 10 weight + 6.25 height - 5 age + 5
For females = 10 weight + 6.25 height - 5 age - 161
The result is then multiplied by (1.2 to 1.9) depending on the persons activity

Lastly, there is a protein calculator which also calculates the amount of protein a person needs to take categorized into 3 different parts for the same purposes as the calorie calculator. It uses the same inputs however follows a different formula:

for males = (((10*weight + 6.25*height - 5*age + 5)* 1.2) * 0.4)/4
for females=  (((10*weight + 6.25*height - 5*age - 161)* 1.2) *0.4)/4
The results is multiplied in the same way as the calorie calculator depending on person's activity

The other feature of this web application is the ability to plan workouts. You can start by creating a weekly workout routine, by giving the workout a name (EX: push pull legs) and then proceeding to fill what workout you are going to perform on each day of the week. A table is then created which displays your workout on a weekly basis. You can then go into each daily workout and add the exercises that you will perform on that particular day. And you can visit that page back after every workout you finish in order to store your progress of these different exercises in a database (as in amount of weight lifted). This helps fitness people track their progress and gradually increase it to become stronger and fitter. The results can be shown on a chart for an easier understanding and visual data represantion of their progress. The chart represents the weight lifted on a chosen exercise over the time period. If the chart line gradually goes up, this means that the person is becoming better and doing progress.




