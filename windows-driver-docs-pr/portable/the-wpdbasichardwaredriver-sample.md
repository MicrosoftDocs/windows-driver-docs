---
Description: The WpdBasicHardwareDriver Sample
MS-HAID: 'wpddk.the\_wpdbasichardwaredriver\_sample'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: The WpdBasicHardwareDriver Sample
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20The%20WpdBasicHardwareDriver%20Sample%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



