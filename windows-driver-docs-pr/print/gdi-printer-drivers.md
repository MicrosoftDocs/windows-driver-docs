---
title: GDI Printer Drivers
author: windows-driver-content
description: GDI Printer Drivers
ms.assetid: c7ae6c0e-ae43-4b10-9a6f-f2daf578ecd2
keywords:
- GDI printer drivers WDK
- printer drivers WDK , GDI
- GDI printer drivers WDK , about GDI printer drivers
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI Printer Drivers


## <a href="" id="ddk-printer-driver-components-gg"></a>


All Windows 2000 and later printer drivers consist of the following components:

-   A [printer graphics DLL](printer-graphics-dll.md) that assists GDI in rendering a print job, and sends the rendered data stream to the print spooler.

-   A [printer interface DLL](printer-interface-dll.md) that provides both a user interface to the driver's configuration parameters, and an interface the spooler can call to notify the driver of print-related system events.

In addition, Microsoft-supplied printer drivers make use of [printer data files](printer-data-files.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDI%20Printer%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


