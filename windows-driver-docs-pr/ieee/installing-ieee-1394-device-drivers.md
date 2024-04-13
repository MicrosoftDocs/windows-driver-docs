---
title: Installing IEEE 1394 Device Drivers
description: Installing IEEE 1394 Device Drivers
keywords:
- IEEE 1394 WDK buses , driver installations
- 1394 WDK buses , driver installations
ms.date: 03/03/2023
---

# Installing IEEE 1394 Device Drivers





This section provides installation information, specific to IEEE 1394 device drivers in Microsoft Windows 2000 and later operating systems.

Vendors supplying their own IEEE 1394 device driver should make that driver a member of the Base setup class in the [**INF Version Section**](../install/inf-version-section.md) of the driver's INF file. For example:

```cpp
[Version]
Signature="$WINDOWS NT$"
Class = Base
```

There are no other special requirements associated with installing IEEE 1394 device drivers.

For general information about device installation in Windows 2000 and later operating systems, see [Device Installation Overview](../install/overview-of-device-and-driver-installation.md).

 

