---
title: AV/C Streaming INF Example
description: AV/C Streaming INF Example
keywords:
- AV/C WDK , Stream filter driver
- Stream filter driver WDK AV/C
- Avcstrm.sys streaming filter driver WDK , INF example
- INF files WDK AV/C streaming
ms.date: 08/25/2020
---

# AV/C Streaming INF Example

The function driver's INF file (during the subunit device driver installation) installs *Avcstrm.sys* as a lower-filter driver on the driver stack. The INF file includes an ".*hw*" section to perform installation of a device. The following code example demonstrates how to add *Avcstrm.sys* as a lower-filter driver using "Subunit" as the install section name:

```inf
[Subunit.NT.HW]
AddReg=Subunit_AddFilter_NT

[Subunit_AddFilter_NT]
HKR,,"LowerFilters",0x00010000,"AVCSTRM"; NT use this "AVCSTRM" as Service name
```

A function driver also must make the necessary driver dependency in the service install section to preserve the proper driver loading order. 

In the following example, the AVCSTRM service section is loaded before the subunit driver:

```inf
ServiceBinary = %12%\subunit.sys
Dependencies  = AVCSTRM   ; loaded before subunit.sys
```

For more information about device installation files, see [INF File Sections](../install/inf-classinstall32-section.md) and [INF File Directives](../install/inf-addcomponent-directive.md).
