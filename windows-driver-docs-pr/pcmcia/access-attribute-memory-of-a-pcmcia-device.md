---
title: Access Attribute Memory of a PCMCIA Device
description: Access Attribute Memory of a PCMCIA Device
MS-HAID:
- 'pamch1\_6b66e55f-38b4-478d-b08b-c2b02402ca46.xml'
- 'PCMCIA.access\_attribute\_memory\_of\_a\_pcmcia\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 270b8821-6322-4694-83eb-de319197dd6a
keywords: ["PCMCIA WDK buses , attribute memory", "attribute memory WDK PCMCIA bus", "attribute memory WDK PCMCIA bus , about attribute memory"]
---

# Access Attribute Memory of a PCMCIA Device


## <a href="" id="ddk-access-attribute-memory-of-a-pcmcia-device-kg"></a>


This section describes how drivers for PCMCIA devices in Microsoft Windows 2000 and later operating systems can access the attribute memory of a PCMCIA device:

-   [Requirements for Accessing Attribute Memory of a PCMCIA Device](https://msdn.microsoft.com/library/windows/hardware/ff537665)

-   [Access PCMCIA Attribute Memory by Using a Plug and Play I/O Request](https://msdn.microsoft.com/library/windows/hardware/ff536898)

    This is a simple method that is sufficient for most purposes, but can only run at IRQL &lt; DISPATCH\_LEVEL.

-   [Access PCMCIA Attribute Memory by Using a BUS\_INTERFACE\_STANDARD Interface](https://msdn.microsoft.com/library/windows/hardware/ff536894)

    This method eliminates the overhead of an I/O request and can run at IRQL &lt;= DISPATCH\_LEVEL

-   [Access PCMCIA Attribute Memory Through a Permanent Memory Window](https://msdn.microsoft.com/library/windows/hardware/ff536901)

    A driver's ISR can use this method to directly access memory while running at IRQL DIRQL.

-   [Access PCMCIA Attribute Memory by Using a PCMCIA\_INTERFACE\_STANDARD Interface](https://msdn.microsoft.com/library/windows/hardware/ff536897)

    Memory card drivers can use this method at IRQL &lt;= DISPATCH\_LEVEL.

These methods are supported by *pcmcia.sys*, the system driver for a PCMCIA bus in Windows 2000 and later operating systems.

 

 





