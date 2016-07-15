---
title: Installing IEEE 1394 Device Drivers
description: Installing IEEE 1394 Device Drivers
MS-HAID:
- '1394-design\_7fceb873-a7f2-4e00-8345-623bf233a6ed.xml'
- 'IEEE.installing\_ieee\_1394\_device\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3f99bec7-e657-4de7-bce4-36a779cc0442
keywords: ["IEEE 1394 WDK buses , driver installations", "1394 WDK buses , driver installations"]
---

# Installing IEEE 1394 Device Drivers


## <a href="" id="ddk-installing-ieee-1394-device-drivers-kg"></a>


This section provides installation information, specific to IEEE 1394 device drivers in Microsoft Windows 2000 and later operating systems.

Vendors supplying their own IEEE 1394 device driver should make that driver a member of the Base setup class in the [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of the driver's INF file. For example:

```
[Version]
Signature="$WINDOWS NT$"
Class = Base
```

There are no other special requirements associated with installing IEEE 1394 device drivers.

For general information about device installation in Windows 2000 and later operating systems, see [Device Installation Overview](https://msdn.microsoft.com/library/windows/hardware/ff549455).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20Installing%20IEEE%201394%20Device%20Drivers%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




