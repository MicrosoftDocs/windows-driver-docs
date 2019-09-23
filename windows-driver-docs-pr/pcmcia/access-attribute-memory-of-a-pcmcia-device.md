---
title: Access Attribute Memory of a PCMCIA Device
description: Access Attribute Memory of a PCMCIA Device
ms.assetid: 270b8821-6322-4694-83eb-de319197dd6a
keywords:
- PCMCIA WDK buses , attribute memory
- attribute memory WDK PCMCIA bus
- attribute memory WDK PCMCIA bus , about attribute memory
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Access Attribute Memory of a PCMCIA Device





This section describes how drivers for PCMCIA devices in Microsoft Windows 2000 and later operating systems can access the attribute memory of a PCMCIA device:

-   [Requirements for Accessing Attribute Memory of a PCMCIA Device](https://docs.microsoft.com/windows-hardware/drivers/pcmcia/requirements-for-accessing-attribute-memory-of-a-pcmcia-device)

-   [Access PCMCIA Attribute Memory by Using a Plug and Play I/O Request](https://docs.microsoft.com/windows-hardware/drivers/pcmcia/access-pcmcia-attribute-memory-by-using-a-plug-and-play-i-o-request)

    This is a simple method that is sufficient for most purposes, but can only run at IRQL &lt; DISPATCH\_LEVEL.

-   [Access PCMCIA Attribute Memory by Using a BUS\_INTERFACE\_STANDARD Interface](https://docs.microsoft.com/windows-hardware/drivers/pcmcia/access-pcmcia-attribute-memory-by-using-a-bus-interface-standard-inter)

    This method eliminates the overhead of an I/O request and can run at IRQL &lt;= DISPATCH\_LEVEL

-   [Access PCMCIA Attribute Memory Through a Permanent Memory Window](https://docs.microsoft.com/windows-hardware/drivers/pcmcia/access-pcmcia-attribute-memory-through-a-permanent-memory-window)

    A driver's ISR can use this method to directly access memory while running at IRQL DIRQL.

-   [Access PCMCIA Attribute Memory by Using a PCMCIA\_INTERFACE\_STANDARD Interface](https://docs.microsoft.com/windows-hardware/drivers/pcmcia/access-pcmcia-attribute-memory-by-using-a-pcmcia-interface-standard-in)

    Memory card drivers can use this method at IRQL &lt;= DISPATCH\_LEVEL.

These methods are supported by *pcmcia.sys*, the system driver for a PCMCIA bus in Windows 2000 and later operating systems.

 

 





