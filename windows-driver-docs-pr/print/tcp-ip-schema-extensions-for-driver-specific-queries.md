---
title: TCP/IP Schema Extensions for Driver-Specific Queries
description: TCP/IP Schema Extensions for Driver-Specific Queries
ms.assetid: c6f85f99-852a-418f-98da-41fe4c36e9ba
keywords:
- TCP/IP schema extensions WDK printer
- schema extensions WDK TCP/IP
- driver-specific queries WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TCP/IP Schema Extensions for Driver-Specific Queries


As noted previously, the standard TCP/IP port monitor supports a subset of the standard print schema so that each driver can send a query and understand the response. However, a particular driver might require additional information that is stored in the printer's MIB.

For queries concerning typical printer properties, you must create queries that contain the properties you define. The following topics describe three constructs that are defined in the Tcpbidi.xsd file and that provide a way to retrieve such information.

[Const](const.md)

[Converter](converter.md)

[Installed](installed2.md)

[Value](value.md)

 

 




