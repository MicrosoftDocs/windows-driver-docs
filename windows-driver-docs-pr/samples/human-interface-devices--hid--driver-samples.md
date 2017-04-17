---
title: Human interface devices (HID) driver samples
author: windows-driver-content
description: The driver samples in this directory provide a starting point for writing a custom driver for your device.
ms.assetid: 38C52EAD-9DC6-4575-A9FF-1472FDDC2702
---

# Human interface devices (HID) driver samples


The driver samples in this directory provide a starting point for writing a custom driver for your device.

## Human interface devices (HID)


| Sample Name         | Solution                                                     | Description                                                                                                                                                                                                                                                                                                                                 |
|---------------------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| KMDF HID Filter     | [firefly](http://go.microsoft.com/fwlink/p/?LinkId=620192)   | A filter driver for a HID device. Along with illustrating how to write a filter driver, this sample shows how to use remote I/O target interfaces to open a HID collection in kernel-mode and send IOCTL requests to set and get feature reports, as well as how an application can use WMI interfaces to send commands to a filter driver. |
| HClient Application | [hclient](http://go.microsoft.com/fwlink/p/?LinkId=617730)   | Demonstrates how to write a user-mode client application that communicates with HID devices conforming to the HID device class specification.                                                                                                                                                                                               |
| HIDUSBFX2           | [hidusbfx2](http://go.microsoft.com/fwlink/p/?LinkId=620190) | Demonstrates mapping of a non-HID USB device to a HID device.                                                                                                                                                                                                                                                                               |
| UMDF HID Minidriver | [vhidmini2](http://go.microsoft.com/fwlink/p/?LinkId=617731) | A sample demonstrating how to write a HID minidriver using the User-Mode Driver Framework (UMDF).                                                                                                                                                                                                                                           |

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdkappendix\wdkappendix%5D:%20Human%20interface%20devices%20%28HID%29%20driver%20samples%20%20RELEASE:%20%289/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


