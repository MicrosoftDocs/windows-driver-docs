---
title: HardDisk
author: windows-driver-content
description: HardDisk
ms.assetid: 88eadea0-54cb-4c19-90d2-9941b13b9303
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# HardDisk


Schema Path:\\Printer.Configuration.HardDisk

Node Type:Property

Description:The value entries for a hard disk installed in the device.

The HardDisk property contains three child values: Installed, Capacity, and FreeSpace.

### <span id="installed"></span><span id="INSTALLED"></span> Installed

Schema Path:\\Printer.Configuration.HardDisk:Installed

Node Type:Value

Data Type:BIDI\_BOOL

Description:Indicates whether a hard disk is installed on the device. If **TRUE**, a hard disk is installed; if **FALSE**, a hard disk is not installed.

### <span id="capacity"></span><span id="CAPACITY"></span> Capacity

Schema Path:\\Printer.Configuration.HardDisk:Capacity

Node Type:Value

Data Type:BIDI\_INT

Description:The capacity, in megabytes (MB), of the installed hard disk.

### <span id="freespace"></span><span id="FREESPACE"></span> FreeSpace

Schema Path:\\Printer.Configuration.HardDisk:FreeSpace

Node Type:Value

Data Type:BIDI\_INT

Description:The currently available free space, in megabytes (MB), of the installed hard disk.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20HardDisk%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


