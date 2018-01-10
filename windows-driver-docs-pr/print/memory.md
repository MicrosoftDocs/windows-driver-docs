---
title: Memory
author: windows-driver-content
description: Memory
ms.assetid: 9e1ad59f-9a97-49d7-b749-14380067cf64
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Memory


Schema Path:\\Printer.Configuration.Memory

Node Type:Property

Description:The value entries for the memory installed in the device

The Memory property contains two child values: **Size** and **PS**.

### <span id="size"></span><span id="SIZE"></span> Size

Schema Path:\\Printer.Configuration.Memory:Size

Node Type:Value

Data Type:BIDI\_INT

Description:The amount of physical memory, in kilobytes (KB), installed in the device.

### <span id="ps"></span><span id="PS"></span> PS

Schema Path:\\Printer.Configuration.Memory:PS

Node Type:Value

Data Type:BIDI\_INT

Description:The amount of memory, in kilobytes (KB), available to the Postscript interpreter in the device. This amount should be less than the amount of physical memory installed.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Memory%20%20RELEASE:%20%2811/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


