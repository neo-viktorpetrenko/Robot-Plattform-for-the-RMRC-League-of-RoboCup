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
| 6 | DC Motors | PG25M370 Dc Planetary Gear Motor with Encoder \ Gear Ratio 64:1 | https://www.nbleisonmotor.com/PG222238-Dc-Planetary-Gear-Motor-pd6514204.html |
| 6 | Torsion Spring | Chosen by calculation, Direction: 90°, used here: Febrotec 0T085-090-422 | https://www.febrotec.de/de-DE/torsionsfedern-schenkelfedern/0t085-090-422/ |
| 1 | Makerbeam Starter Kit |  | https://www.makerbeam.com/makerbeam-makerbeam-regular-starter-kit-black.html |
| 12 | Bearing | Ball Bearing DIN 6002 ZZ / 2Z 15x32x9 mm | https://www.conrad.de/de/p/reely-kugellager-radial-chromstahl-innen-durchmesser-15-mm-aussen-durchmesser-32-mm-drehzahl-max-24000-u-min-221954.html |
| 50 cm | Nylon String | diameter 5mm | https://www.conrad.de/de/p/nylonfaden-0-5-mm-100-m-800620811.html |
| 4 | Heat Set Inserts | M2.5x4 | https://www.amazon.de/dp/B09J91JWGM?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1 |
| < 100 | eat Set Inserts | M3x3 | https://www.amazon.de/dp/B09FXNX6WF?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1 |
| 24 | Screws for motors | M2x6 | |
| 4 | Screws for Raspberry Pi 5 | M2.5x10 | |
| 1 | Servo motor for the camera | FT90M Digital Servo \ 270° Drehwinkel | |
| 6 | Tires | 1:10 RC rubber tires \ 120 mm outer diameter | https://www.pololu.com/product/1557 |

## Suspension Design
The Suspension of this platform is inspired by the now discontinued Dagu Wild Thumper platform. It uses torsion springs attached to rotating motor enclosures to ensure contact with uneven ground.  Two enclosures on each side are connected with a nylon string to prevent the springs from rotating the enclosures too much.

