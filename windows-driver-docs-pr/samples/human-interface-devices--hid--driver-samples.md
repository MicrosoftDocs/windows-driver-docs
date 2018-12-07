---
title: Human interface devices (HID) driver samples
description: The driver samples in this directory provide a starting point for writing a custom HID driver for your device.
ms.assetid: 38C52EAD-9DC6-4575-A9FF-1472FDDC2702
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Human interface devices (HID) driver samples


The driver samples in this directory provide a starting point for writing a custom HID driver for your device.

## Human interface devices (HID)


| Sample Name         | Solution                                                     | Description                                                                                                                                                                                                                                                                                                                                 |
|---------------------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| KMDF HID Filter     | [firefly](http://go.microsoft.com/fwlink/p/?LinkId=620192)   | A filter driver for a HID device. Along with illustrating how to write a filter driver, this sample shows how to use remote I/O target interfaces to open a HID collection in kernel-mode and send IOCTL requests to set and get feature reports, as well as how an application can use WMI interfaces to send commands to a filter driver. |
| HClient Application | [hclient](http://go.microsoft.com/fwlink/p/?LinkId=617730)   | Demonstrates how to write a user-mode client application that communicates with HID devices conforming to the HID device class specification.                                                                                                                                                                                               |
| HIDUSBFX2           | [hidusbfx2](http://go.microsoft.com/fwlink/p/?LinkId=620190) | Demonstrates mapping of a non-HID USB device to a HID device.                                                                                                                                                                                                                                                                               |
| UMDF HID Minidriver | [vhidmini2](http://go.microsoft.com/fwlink/p/?LinkId=617731) | A sample demonstrating how to write a HID minidriver using the User-Mode Driver Framework (UMDF).                                                                                                                                                                                                                                           |

 

 

 




