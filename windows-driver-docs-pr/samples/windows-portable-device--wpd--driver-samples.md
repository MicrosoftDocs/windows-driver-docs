---
title: Windows Portable Device (WPD) driver samples
description: The driver samples in this directory provide a starting point for writing a custom WPD driver for your device.
ms.assetid: 5EB5B820-A29A-4A93-BBB9-6F4CDF101E3B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Portable Device (WPD) driver samples


The driver samples in this directory provide a starting point for writing a custom WPD driver for your device.

## Windows Portable Device (WPD)


| Sample Name                               | Solution                                                                   | Description                                                                                                                                                                                                                                                           |
|-------------------------------------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WPD Basic Hardware Sample Driver (UMDF 1) | [WpdBasicHardwareDriver](http://go.microsoft.com/fwlink/p/?LinkId=620318)  | A WPD sample driver that supports nine sensor devices that integrate with the Parallax BS2 programmable microcontroller.                                                                                                                                              |
| Hello World Example                       | [WpdHelloWorldDriver](http://go.microsoft.com/fwlink/p/?LinkId=618008)     | This sample driver supports four objects: a device object, a storage object, a folder object, and a file object. Each object supports a set of properties.                                                                                                            |
| Multi-transport driver                    | [WpdMultiTransportDriver](http://go.microsoft.com/fwlink/p/?LinkId=618009) | Demonstrates how you could extend the WpdHelloWorldDriver for a device that supports multiple transports. A transport is a protocol over which a portable device communicates with a computer. Example transports include Internet Protocol (IP), Bluetooth, and USB. |
| WPD service sample driver                 | [WpdServiceSampleDriver](http://go.microsoft.com/fwlink/p/?LinkId=618010)  | Demonstrates how to extend the WpdHelloWorldDriver sample so that it supports a simulated device with a Contacts device service.                                                                                                                                      |
| WUDF driver                               | [WpdWudfSampleDriver](http://go.microsoft.com/fwlink/p/?LinkId=618011)     | A comprehensive WPD sample driver demonstrates virtually all aspects of the WPD device driver interface (DDI).                                                                                                                                                        |

 

 

 




