---
title: Driver Support for Dynamic Subdevices
description: Driver Support for Dynamic Subdevices
keywords:
- dynamic audio subdevices WDK audio
- dynamic topologies WDK audio
ms.date: 12/22/2020
ms.localizationpriority: medium
---

# Driver Support for Dynamic Subdevices

The code example in [Subdevice Creation](subdevice-creation.md) shows how to use the **PcRegisterSubdevice** routine to register a subdevice. The Sysvad sample driver, which is discussed in [Sample Audio Drivers](sample-audio-drivers.md), shows how to use the **PcRegisterPhysicalConnection** routine to register the physical connections between subdevices that are contained in the same audio adapter.

The [IUnregisterSubdevice](/windows-hardware/drivers/ddi/portcls/nn-portcls-iunregistersubdevice) and [IUnregisterPhysicalConnection](/windows-hardware/drivers/ddi/portcls/nn-portcls-iunregisterphysicalconnection) interfaces complement the PcRegister*Xxx* routines. These interfaces contain methods that the sample driver uses to "unregister" devices that were previously registered by calls to the PcRegister*Xxx* routines. As mentioned previously, these two interfaces are available in Windows Server 2003 with SP1 and later and Windows XP with SP2, but not in earlier Windows versions.
