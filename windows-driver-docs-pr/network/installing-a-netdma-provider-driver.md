---
title: Installing a NetDMA Provider Driver
description: Installing a NetDMA Provider Driver
ms.assetid: 05ad6b7b-0f15-43a8-aee6-34e021ec35c4
keywords:
- memory-to-memory data transfers WDK NetDMA , installing provider drivers
- data transfers WDK NetDMA , installing provider drivers
- transferring data WDK NetDMA , installing provider drivers
- NetDMA WDK networking , installing provider drivers
- NetDMA p
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a NetDMA Provider Driver


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




A NetDMA provider driver is implemented as a kernel-mode Microsoft Windows Driver Model (WDM) device driver.

During the boot process, the Plug and Play (PnP) manager detects a dynamic memory access (DMA) engine as a PCI bus master device and loads the NetDMA provider driver as the device driver for the DMA engine.

Set the **Class** INF file entry to **System** in the DMA engine INF file. The following example shows a sample **Class** entry for the INF file.

```cpp
Class = System
```

For general information about installing drivers, see [Device Installation Overview](https://msdn.microsoft.com/library/windows/hardware/ff549455).

 

 





