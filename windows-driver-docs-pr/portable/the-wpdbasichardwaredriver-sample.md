---
Description: The WpdBasicHardwareDriver Sample
title: The WpdBasicHardwareDriver Sample
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The WpdBasicHardwareDriver Sample


The WpdBasicHardwareDriver is a WPD driver that supports nine devices. These devices were selected because of their simplicity. This simplicity allowed the sample to focus on the tasks that are common to portable devices without getting bogged down in hardware complexities.

This sample driver is based on the WpdHelloWorldDriver that is also included in the Windows Driver Kit (WDK). The "Supporting the WPD Infrastructure” sections for this driver show the changes that were made to the WpdHelloWorldDriver source so that it can communicate with basic hardware devices. Before you work through the topics in this section of the documentation, be familiar with the WpdHelloWorldDriver.

If you plan to develop drivers that integrate sensors with Windows 8, use the Sensor API and driver model (rather than WPD). If you develop drivers to integrate sensors with Windows Vista or Windows XP, WPD provides a viable solution.

The sensors that are supported by the WpdBasicHardwareDriver are described in the following table.

| Sensor                                         | Description                                         |
|------------------------------------------------|-----------------------------------------------------|
| Memsic 2125 Accelerometer                      | Senses +/- 2g along the X-axis and Y-axis.          |
| Sensiron Temperature and Humidity Sensor       | Senses temperature and relative humidity.           |
| Flexiforce sensor                              | Senses pressure from 0-25 lbs.                      |
| PING Ultrasonic Sensor                         | Senses distances from 2-300 cm.                     |
| Passive Infrared (PIR) Sensor                  | Senses motion.                                      |
| Hitachi HM55B Compass                          | Senses magnetic bearing (0-360 degrees).            |
| Hitachi H48C Tri-Axis Accelerometer            | Senses +/- 3g along the X-axis, Y-axis, and Z-axis. |
| Piezo Film Vibration Sensor QTI (light) Sensor | Senses vibration.                                   |
| QTI (light) Sensor                             | Senses light intensity.                             |

 

These nine sensors are sold by the [Parallax Corporation](http://go.microsoft.com/fwlink/p/?linkid=154730) in Rocklin, California. They can be purchased separately, or together in a Sensor Sample kit.

To use these sensors with the WpdBasicHardwareDriver, you must purchase the sensors, a programmable microcontroller (Parallax BS2), a test board (like the Parallax BASIC Stamp Homework Board), an RS232 cable, and miscellaneous parts. All of this hardware is available from Parallax and can be ordered through their Web site.

The circuit designs are based on the sample circuits provided by Parallax in their sensor data sheets. These circuits are designed to integrate each sensor with the Parallax BS2 programmable microcontroller .

The microcontroller firmware for each of the nine circuits is included in the src\\wpd\\WpdBasicHardwareDriver\\firmware subdirectory in the Windows Driver Kit (WDK).

 

 




