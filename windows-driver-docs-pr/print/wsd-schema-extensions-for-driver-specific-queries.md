---
title: WSD Schema Extensions for Driver-Specific Queries
description: WSD Schema Extensions for Driver-Specific Queries
ms.assetid: 508a9f87-8fd2-4c95-8efb-5d1d7201981a
keywords:
- WSD schema extensions WDK printer
- schema extensions WDK WSD
- driver-specific queries WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WSD Schema Extensions for Driver-Specific Queries


As noted in [Customizing the Printer Port Monitors](customizing-the-printer-port-monitors.md), the Web Services for Devices (WSD) port monitor supports a subset of the standard print schema so that each driver can send a query and understand the response. However, a particular driver might require additional information that is available through the printer's Web service interface.

For queries concerning typical printer properties, you must create queries containing properties that you define. The following topics describe four constructs that are defined in the WsdBidi.xsd file that provide a way to retrieve such information.

[Const](const.md)

[Installed](installed.md)

[List](list.md)

[Value](value.md)

 

 




