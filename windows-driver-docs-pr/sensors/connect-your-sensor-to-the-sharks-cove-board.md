---
title: Connect your sensor to the Sharks Cove board
author: windows-driver-content
description: This topic provides guidance on how to connect your sensor test board to the Sharks Cove board.
ms.assetid: B081F4B6-D15E-4F1A-A5C0-E19DA806EAB2
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Connect your sensor to the Sharks Cove board


This topic provides guidance on how to connect your sensor test board to the Sharks Cove board.

In the ADXL345 accelerometer scenario, and after making any necessary modifications, you would end up with the accelerometer test board connected to Sharks Cove as shown in the following diagram.

![connection diagram for sharks cove and the adxl345 accelerometer board.](images/sensor-header.png)

To achieve a stable and reliable connection between the sensor breakout board and the Sharks Cove, you could start by soldering an 8-pin single-row male header to the breakout board, as shown in the following image.

![image of adxl345 accelerometer breakout board, showing 8-pin, single-row male header.](images/adxl-header.png)

Then use a ribbon of eight female-to-female jumper wires (shown below), to connect the sensor breakout board to the Sharks Cove, based on the preceding connection diagram.

![adxl345 sensor brrakout board and an 8-wire female-to-female set of jumper wires.](images/snsr-n-jumpers.png)

Here are some examples of how information from the ADXL345 data sheet, and the Sharks Cove Technical Specifications Rev. 1.0, helped us to arrive at the connection strategy shown in the preceding diagram:

**J1C1 PIN4** connected to **VDD** and **CS** on the accelerometer board.

-   **VDD** is the supply voltage line for the Digital Interface. We decided to use the accelerometer in dual-voltage configuration, and also keep the power consumption low. So out of the four available voltages (**J1C1 PIN1 - PIN4**) we targeted the two lowest ones. These are 2.8V on **J1C1 PIN3** and 1.8V on **J1C1 PIN4**. In dual-voltage configuration, **VDD** must be connected to a lower voltage than **VS**. So we’ve connected **VDD** to **J1C1 PIN4**, the 1.8V line on Sharks Cove.
-   **CS** is the communication mode selection pin for the accelerometer. To enable the I2C communication mode, you must tie **CS** high, in this case to **VDD**, which is taken care of by the modification with the blue wire in [Prepare your sensor test board](prepare-your-sensor-test-board.md). The modification ties both **VDD** and **CS** from the accelerometer board to **J1C1 PIN4**, the 1.8V line.

**J1C1 PIN12** connected to **SDO** on the accelerometer board.

-   When the **SDO** line is high, the 7-bit I2C address for the accelerometer board is 0x1D, followed by the R/W bit. When the **SDO** line is low (i.e. connected to Ground), the I2C address for the accelerometer board is 0x53, followed by the R/W bit. In the Microsoft SPBAccelerometer sample, it was decided that the address of 0x53 would be used. And that’s why the **SDO** line is connected to a Ground pin (**J1C1 PIN12**) on Sharks Cove.

The connection decisions outlined in the preceding bullets were based on information from the *Theory of Operation* section (page 6) and the *Serial Communications* section (page 8) of the ADXL345 data sheet.

For more detailed technical information about the Sharks Cove board, see [Sharks Cove Schematic](http://firmware.intel.com/sites/default/files/Sharks_Cove_Schematic.pdf).

After successfully connecting your sensor test board to Sharks Cove, read the next topic for guidance on how to [write and deploy your universal sensor driver](write-and-deploy-your-universal-sensor-driver.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Connect%20your%20sensor%20to%20the%20Sharks%20Cove%20board%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


