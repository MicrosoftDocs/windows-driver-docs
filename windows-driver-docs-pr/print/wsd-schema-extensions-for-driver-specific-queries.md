---
title: WSD Schema Extensions for Driver-Specific Queries
author: windows-driver-content
description: WSD Schema Extensions for Driver-Specific Queries
ms.assetid: 508a9f87-8fd2-4c95-8efb-5d1d7201981a
keywords:
- WSD schema extensions WDK printer
- schema extensions WDK WSD
- driver-specific queries WDK printer
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WSD Schema Extensions for Driver-Specific Queries


As noted in [Customizing the Printer Port Monitors](customizing-the-printer-port-monitors.md), the Web Services for Devices (WSD) port monitor supports a subset of the standard print schema so that each driver can send a query and understand the response. However, a particular driver might require additional information that is available through the printer's Web service interface.

For queries concerning typical printer properties, you must create queries containing properties that you define. The following topics describe four constructs that are defined in the WsdBidi.xsd file that provide a way to retrieve such information.

[Const](const.md)

[Installed](installed.md)

[List](list.md)

[Value](value.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20WSD%20Schema%20Extensions%20for%20Driver-Specific%20Queries%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


