# Robot-Plattform-for-the-RMRC-League-of-RoboCup
A Repository for Sharing an easily modifiable and reproducible Robot Plattform including a suspension that was used in the RoboCup German Open 2025 competition

On this Repository a Mechanical Design of a 6 wheeled robot is shared. The robot uses mainly electronic components from EduArt.

![cropped](https://github.com/user-attachments/assets/b1ea88df-4692-45f4-b61a-3d2ad12f5f8c)


## List of 3D Models
### Models for the front, back and sides of the chassis
|*Amount* | *Component* | *Heatset Inserts M3* | *Multi Filament Print* | *Support Material* | 
| ----- | ----- | ----- | ----- | ----- |
| 1 | Plate Front | 4 | X | X |
|2|Frontlight Cover||✔|X|
|1|Plate Back|4|X|X|
|2|Rearlight Cover||✔|X|
|2|Plate Side A||✔|X|
|1|Plate Side B||✔|X|
|1|Plate Side B with IO Hole||✔|X|

### Models for the floor of the chassis
|*Amount* | *Component* | *Heatset Inserts M3* | *Multi Filament Print* | *Support Material* | 
| ----- | ----- | ----- | ----- | ----- |
|1|Raspberry Pi Bracket||X|X|
|1|Battery Case|4|X|✔|
|1|Plate Bottom A|12 + 4 x M2.5|X|X|
|1|Plate Bottom B|8|X|X|

### Models for the roof of the chassis
|*Amount* | *Component* | *Heatset Inserts M3* | *Multi Filament Print* | *Support Material* | 
| ----- | ----- | ----- | ----- | ----- |
|1|Router Case|4|X|✔|
|1|Plate Top A||X|X|
|1|Plate Top B||X|X|
|1|Plate Top Main Input||X|X|
|1|Camera Servo Holder|4|X|X|
|1|Camera Holder||X|X|

### Models for the suspension
|*Amount* | *Component* | *Heatset Inserts M3* | *Multi Filament Print* | *Support Material* | 
| ----- | ----- | ----- | ----- | ----- |
|4|Suspension Support Center|5|X|X|
|2|Suspension Support Outside|1|X|X|
|6|Suspension Partial Axis|2|X|✔|
|6|Suspension Axis Attachment Plate||X|X|
|3|Suspension Axis Cover||X|X|
|2|Suspension Electronics Cover||X|X|
|3|Motorshield Adapter Plate|2|X|X|
|6|Wheel||✔|✔|

## List of additional components you'll have to buy
| *Amount* | *Component* | *Details* | *Link* |
| ---- | ---- | ---- | ---- |
| 6 | DC Motors | PG25M370 Dc Planetary Gear Motor with Encoder Gear Ratio 64:1 | https://www.nbleisonmotor.com/PG222238-Dc-Planetary-Gear-Motor-pd6514204.html |
| 6 | Torsion Spring | Chosen by calculation, Direction: 90°, used here: Febrotec 0T085-090-422 | https://www.febrotec.de/de-DE/torsionsfedern-schenkelfedern/0t085-090-422/ |
| 1 | Makerbeam Starter Kit |  | https://www.makerbeam.com/makerbeam-makerbeam-regular-starter-kit-black.html |
| 12 | Bearing | Ball Bearing DIN 6002 ZZ 2Z 15x32x9 mm | https://www.conrad.de/de/p/reely-kugellager-radial-chromstahl-innen-durchmesser-15-mm-aussen-durchmesser-32-mm-drehzahl-max-24000-u-min-221954.html |
| 50 cm | Nylon String | diameter 5mm | https://www.conrad.de/de/p/nylonfaden-0-5-mm-100-m-800620811.html |
| 4 | Heat Set Inserts | M2.5x4 | https://www.amazon.de/dp/B09J91JWGM?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1 |
| < 100 | eat Set Inserts | M3x3 | https://www.amazon.de/dp/B09FXNX6WF?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1 |
| 24 | Screws for motors | M2x6 | |
| 4 | Screws for Raspberry Pi 5 | M2.5x10 | |
| 1 | Servo motor for the camera | FT90M Digital Servo  270° Drehwinkel | |
| 6 | Tires | 1:10 RC rubber tires  120 mm outer diameter | https://www.pololu.com/product/1557 |

## Suspension Design
The Suspension of this platform is inspired by the now discontinued Dagu Wild Thumper platform. It uses torsion springs attached to rotating motor enclosures to ensure contact with uneven ground.  Two enclosures on each side are connected with a nylon string to prevent the springs from rotating the enclosures too much.

There are some python scripts in this repository that aid in calculating the behavior of the suspension if you want to modify that. The most relevant dimensions of the suspension are shown in the images below. k in the scripts is the spring constant of the torsion spring. If you order your Springs from Febrotec, you can calculate k = (Max. Torque Md)/(Max. Torsion alpha). For a linear behavior of the suspension, the springs should not be used near the 90-degree rest position. The Most important forces of the calculation are the spring force Ff, the weight Fg and the force acting on a wheel FR.


The Script Suspension_one_curve generates a graph of the force that acts on the wheel at each point in the spring travel xR.
The Script suspension_average_forces generates a grid of the average force within the spring travel for different configurations of l0 and dA1.

![CAD2](https://github.com/user-attachments/assets/03fb73bc-9c84-45e7-8580-940ad7cc6551)

![Zeichnung Drehfeder](https://github.com/user-attachments/assets/3a0ef095-6685-4e1b-9a83-0668fa1710ab)

![Drehfeder rechnung6](https://github.com/user-attachments/assets/0971276f-1b84-4c19-88c0-0b428a76e90b)

![grafik](https://github.com/user-attachments/assets/d3e35d55-3ffb-49d6-9122-d38af80c7c0c)

![drehfeder rechnung1](https://github.com/user-attachments/assets/72ec0d4e-0247-4e41-82c7-84d21729771b)

![grafik](https://github.com/user-attachments/assets/14fad3c2-0e1d-402e-a916-67aca63b9fde)

If you don't know the final weight of your modified robot, you can use the excel sheet spring_force_estimation to find out what torsion spring you need. You can set the maximum and minimum weight that your robot will have and change the spring constant to one of a torsion spring you found online. You can use the spring. if the calculated line fits well within the bounds you've set like shown in the graph below.

![dimensionierung drehfeder 1](https://github.com/user-attachments/assets/0acc0c98-3cea-47d9-823c-0f37b4e687f3)

