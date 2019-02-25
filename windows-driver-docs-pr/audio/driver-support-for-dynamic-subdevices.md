---
title: Driver Support for Dynamic Subdevices
description: Driver Support for Dynamic Subdevices
ms.assetid: ca355dfc-46ad-4df2-ac48-f3a0780dc3d3
keywords:
- dynamic audio subdevices WDK audio
- dynamic topologies WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Support for Dynamic Subdevices


The code example in [Subdevice Creation](subdevice-creation.md) shows how to use the **PcRegisterSubdevice** routine to register a subdevice. The SB16 sample audio driver in the Windows Driver Kit (WDK) shows how to use the **PcRegisterPhysicalConnection** routine to register the physical connections between subdevices that are contained in the same audio adapter.

The [IUnregisterSubdevice](https://msdn.microsoft.com/library/windows/hardware/ff537030) and [IUnregisterPhysicalConnection](https://msdn.microsoft.com/library/windows/hardware/ff537022) interfaces complement the PcRegister*Xxx* routines. These interfaces contain methods that the sample driver uses to "unregister" devices that were previously registered by calls to the PcRegister*Xxx* routines. As mentioned previously, these two interfaces are available in Windows Server 2003 with SP1 and later and Windows XP with SP2, but not in earlier Windows versions. Thus, the earlier Windows versions lack support for dynamic topologies, although a hot-fix package with dynamic topology support is available for Windows Server 2003, Windows XP, and Windows 2000.

 

 




