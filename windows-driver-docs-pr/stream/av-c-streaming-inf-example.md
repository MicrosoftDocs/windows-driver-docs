---
title: AV/C Streaming INF Example
author: windows-driver-content
description: AV/C Streaming INF Example
ms.assetid: c8a2c9cd-c71b-4fd1-80f5-34d13837865e
keywords: ["AV/C WDK , Stream filter driver", "Stream filter driver WDK AV/C", "Avcstrm.sys streaming filter driver WDK , INF example", "INF files WDK AV/C streaming"]
---

# AV/C Streaming INF Example


## <a href="" id="ddk-installing-subunit-devices-ksg"></a>


The function driver's INF file (during the subunit device driver installation) installs *Avcstrm.sys* as a lower-filter driver on the driver stack. The INF file includes an ".*hw*" section to perform installation of a device. The following code example demonstrates how to add *Avcstrm.sys* as a lower-filter driver on either Windows 2000 or later operating systems or Windows Millennium Edition, Windows 98, or Windows 95 or later operating systems, using "Subunit" as the install section name:

```
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

```
ServiceBinary = %12%\subunit.sys
Dependencies  = AVCSTRM   ; loaded before subunit.sys
```

For more information about device installation files, see [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20AV/C%20Streaming%20INF%20Example%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


