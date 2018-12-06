---
title: Universal Serial Bus (USB) driver samples
description: The driver samples in this directory provide a starting point for writing a custom USB driver for your device.
ms.assetid: 4A61F62B-9C23-4265-8AB4-D3AB45F512DF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Universal Serial Bus (USB) driver samples


The driver samples in this directory provide a starting point for writing a custom USB driver for your device.

## Universal Serial Bus (USB)


| Sample Name                                                            | Solution                                                              | Description                                                                                                                                                                         |
|------------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| KMDF Bus Driver                                                        | [kmdf\_enumswitches](http://go.microsoft.com/fwlink/p/?LinkId=618000) | Demonstrates how to use KMDF for a bus driver with the OSR USB-FX2 device.                                                                                                          |
| Sample KMDF Function Driver for OSR USB-FX2                            | [kmdf\_fx2](http://go.microsoft.com/fwlink/p/?LinkId=620313)          | Demonstrates how to perform bulk and interrupt data transfers to a USB device. The sample is written for the OSR USB-FX2 Learning Kit.                                              |
| USB Function Client Driver                                             | [ufxclientsample](http://go.microsoft.com/fwlink/p/?LinkId=620315)    | A skeleton sample driver that shows how to create a Windows USB function controller driver using the USB function class extension driver (UFX).                                     |
| Sample UMDF Filter above KMDF Function Driver for OSR USB-FX2 (UMDF 1) | [umdf\_filter\_kmdf](http://go.microsoft.com/fwlink/p/?LinkId=620316) | Demonstrates how to load a UMDF filter driver as an upper filter driver above the kmdf\_fx2 sample driver. The sample is written for the OSR USB-FX2 Learning Kit.                  |
| Sample UMDF Filter above UMDF Function Driver for OSR USB-FX2 (UMDF 1) | [umdf\_filter\_umdf](http://go.microsoft.com/fwlink/p/?LinkId=618001) | demonstrates how to load a UMDF filter driver as an upper filter driver above the umdf\_fx2 sample driver. The sample is written for the OSR USB-FX2 Learning Kit.                  |
| UMDF 1 Function Driver                                                 | [umdf\_fx2](http://go.microsoft.com/fwlink/p/?LinkId=618002)          | A User-Mode Driver Framework (UMDF 1) driver for the OSR USB-FX2 device. It includes a test application and sample device metadata, and supports impersonation and idle power down. |
| UMDF 2 Function Driver                                                 | [umdf2\_fx2](http://go.microsoft.com/fwlink/p/?LinkId=618003)         | A User-Mode Driver Framework (UMDF 2) driver for the OSR USB-FX2 device. It includes a test application and sample device metadata, and supports impersonation and idle power down. |
| Usbsamp Generic USB Driver                                             | [usbsamp](http://go.microsoft.com/fwlink/p/?LinkId=618938)            | Demonstrates how to perform full speed, high speed, and SuperSpeed transfers to and from bulk and isochronous endpoints of a generic USB device.                                    |
| USBView                                                                | [usbview](http://go.microsoft.com/fwlink/p/?LinkId=618004)            | A Windows application that allows you to browse all USB controllers and connected USB devices on your system.                                                                       |

 

 

 




