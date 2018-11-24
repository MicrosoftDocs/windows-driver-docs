---
title: AV/C Streaming INF Example
description: AV/C Streaming INF Example
ms.assetid: c8a2c9cd-c71b-4fd1-80f5-34d13837865e
keywords:
- AV/C WDK , Stream filter driver
- Stream filter driver WDK AV/C
- Avcstrm.sys streaming filter driver WDK , INF example
- INF files WDK AV/C streaming
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AV/C Streaming INF Example





The function driver's INF file (during the subunit device driver installation) installs *Avcstrm.sys* as a lower-filter driver on the driver stack. The INF file includes an ".*hw*" section to perform installation of a device. The following code example demonstrates how to add *Avcstrm.sys* as a lower-filter driver on either Windows 2000 or later operating systems or Windows Millennium Edition, Windows 98, or Windows 95 or later operating systems, using "Subunit" as the install section name:

```INF
[Subunit.HW]
AddReg=Subunit_AddFilter_W9x

[Subunit.NT.HW]
AddReg=Subunit_AddFilter_NT

[SubUnit_AddFilter_W9x]
HKR,,"LowerFilters",0x00010000,"avcstrm.sys"; Win9X use "avcstrm.sys" as driver name

[Subunit_AddFilter_NT]
HKR,,"LowerFilters",0x00010000,"AVCSTRM"; NT use this "AVCSTRM" as Service name
```

For Windows 2000 and later, a function driver also must make the necessary driver dependency in the service install section to preserve the proper driver loading order. In the following example, the AVCSTRM service section is loaded before the subunit driver:

```INF
ServiceBinary = %12%\subunit.sys
Dependencies  = AVCSTRM   ; loaded before subunit.sys
```

For more information about device installation files, see [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433).

 

 




