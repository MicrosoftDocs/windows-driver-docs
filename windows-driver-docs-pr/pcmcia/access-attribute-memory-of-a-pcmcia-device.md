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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20Access%20Attribute%20Memory%20of%20a%20PCMCIA%20Device%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




