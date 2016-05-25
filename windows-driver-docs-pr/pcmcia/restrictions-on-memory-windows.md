---
title: Restrictions on Memory Windows
description: Restrictions on Memory Windows
MS-HAID:
- 'mcch2\_cbc5ac4e-b10e-4da6-9c3f-d36c5a19f40a.xml'
- 'PCMCIA.restrictions\_on\_memory\_windows'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 664320e6-b155-470b-9b86-8b463663961f
keywords: ["PCMCIA WDK buses , memory windows", "memory windows WDK PCMCIA bus"]
---

# Restrictions on Memory Windows


## <a href="" id="ddk-restrictions-on-memory-windows-kr"></a>


This section describes the restrictions imposed by Windows 2000 and later operating systems on memory windows of PCMCIA memory cards.

The resource requirements of a PCMCIA memory card are normally specified by the bus driver when it enumerates the device at the request of the Plug and Play manager. Specific memory windows can also be specified in an [**INF DDInstall.LogConfigOverride section**](https://msdn.microsoft.com/library/windows/hardware/ff547339) of a device driver's INF file. A maximum of two memory windows can be requested for a PCMCIA memory card.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20Restrictions%20on%20Memory%20Windows%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




