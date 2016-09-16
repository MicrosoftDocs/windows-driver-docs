---
title: Windows Portable Device (WPD) driver samples
author: windows-driver-content
description: The driver samples in this directory provide a starting point for writing a custom driver for your device.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5EB5B820-A29A-4A93-BBB9-6F4CDF101E3B
---

# Windows Portable Device (WPD) driver samples


The driver samples in this directory provide a starting point for writing a custom driver for your device.

## Windows Portable Device (WPD)


| Sample Name                               | Solution                                                                   | Description                                                                                                                                                                                                                                                           |
|-------------------------------------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WPD Basic Hardware Sample Driver (UMDF 1) | [WpdBasicHardwareDriver](http://go.microsoft.com/fwlink/p/?LinkId=620318)  | A WPD sample driver that supports nine sensor devices that integrate with the Parallax BS2 programmable microcontroller.                                                                                                                                              |
| Hello World Example                       | [WpdHelloWorldDriver](http://go.microsoft.com/fwlink/p/?LinkId=618008)     | This sample driver supports four objects: a device object, a storage object, a folder object, and a file object. Each object supports a set of properties.                                                                                                            |
| Multi-transport driver                    | [WpdMultiTransportDriver](http://go.microsoft.com/fwlink/p/?LinkId=618009) | Demonstrates how you could extend the WpdHelloWorldDriver for a device that supports multiple transports. A transport is a protocol over which a portable device communicates with a computer. Example transports include Internet Protocol (IP), Bluetooth, and USB. |
| WPD service sample driver                 | [WpdServiceSampleDriver](http://go.microsoft.com/fwlink/p/?LinkId=618010)  | Demonstrates how to extend the WpdHelloWorldDriver sample so that it supports a simulated device with a Contacts device service.                                                                                                                                      |
| WUDF driver                               | [WpdWudfSampleDriver](http://go.microsoft.com/fwlink/p/?LinkId=618011)     | A comprehensive WPD sample driver demonstrates virtually all aspects of the WPD device driver interface (DDI).                                                                                                                                                        |

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdkappendix\wdkappendix%5D:%20Windows%20Portable%20Device%20%28WPD%29%20driver%20samples%20%20RELEASE:%20%289/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


