---
title: Stress Testing
author: windows-driver-content
description: Stress Testing
ms.assetid: 14d20ce2-7d98-4fa3-b639-a4e9b7b07a72
keywords:
- stress testing WDK printer
- bus stress testing WDK printer
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Stress Testing


You should run your printer through a stress test by sending large (over 100 MB), long (over 150 pages), and graphically intensive print jobs to it. For graphically intensive jobs, vary the combinations of different sizes and types of graphic images as much as possible.

### Specialized Bus Stress

When you create stress cases, take into consideration stress factors that can occur on a specialized bus. Many devices can share the same bus, so be sure to test that your device coexists gracefully with other devices on the same bus--devices of the same type or model, or common devices that a user could typically have attached to the system. For example, you could plug many devices at the same time into the same USB hub to which your printer is attached.

The following tests are recommended:

1.  Verify that plugging several other devices into the hub or system does not interfere with your device.

2.  Chain multiple hubs and devices together and verify that your device continues to function correctly.

3.  Verify that all devices on the same bus can work simultaneously.

4.  Verify that the your device uninstalls gracefully when the attached hub is unplugged from the system.

For Bluetooth-enabled printers, run stress tests on print jobs as follows:

1.  Move the printer in and out of the maximum range of the Bluetooth radio, typically 30 to 90 feet (10 to 30 meters), depending on the radio.

2.  Send the job to a printer just inside the range of the Bluetooth radio.

3.  Send a job to a printer outside the maximum range of the Bluetooth radio. Wait for an error state to occur, and then move the printer back within range to verify that it recovers gracefully.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Stress%20Testing%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


