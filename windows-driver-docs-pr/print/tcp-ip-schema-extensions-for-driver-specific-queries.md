---
title: TCP/IP Schema Extensions for Driver-Specific Queries
author: windows-driver-content
description: TCP/IP Schema Extensions for Driver-Specific Queries
ms.assetid: c6f85f99-852a-418f-98da-41fe4c36e9ba
keywords:
- TCP/IP schema extensions WDK printer
- schema extensions WDK TCP/IP
- driver-specific queries WDK printer
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# TCP/IP Schema Extensions for Driver-Specific Queries


As noted previously, the standard TCP/IP port monitor supports a subset of the standard print schema so that each driver can send a query and understand the response. However, a particular driver might require additional information that is stored in the printer's MIB.

For queries concerning typical printer properties, you must create queries that contain the properties you define. The following topics describe three constructs that are defined in the Tcpbidi.xsd file and that provide a way to retrieve such information.

[Const](const.md)

[Converter](converter.md)

[Installed](installed2.md)

[Value](value.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20TCP/IP%20Schema%20Extensions%20for%20Driver-Specific%20Queries%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


