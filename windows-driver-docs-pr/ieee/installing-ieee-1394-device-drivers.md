---
title: Installing IEEE 1394 Device Drivers
description: Installing IEEE 1394 Device Drivers
ms.assetid: 3f99bec7-e657-4de7-bce4-36a779cc0442
keywords:
- IEEE 1394 WDK buses , driver installations
- 1394 WDK buses , driver installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing IEEE 1394 Device Drivers





This section provides installation information, specific to IEEE 1394 device drivers in Microsoft Windows 2000 and later operating systems.

Vendors supplying their own IEEE 1394 device driver should make that driver a member of the Base setup class in the [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of the driver's INF file. For example:

```cpp
[Version]
Signature="$WINDOWS NT$"
Class = Base
```

There are no other special requirements associated with installing IEEE 1394 device drivers.

For general information about device installation in Windows 2000 and later operating systems, see [Device Installation Overview](https://msdn.microsoft.com/library/windows/hardware/ff549455).

 

 




