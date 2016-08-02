---
title: Storage Miniport Drivers
author: windows-driver-content
description: Storage Miniport Drivers
ms.assetid: 374d8370-02a9-43ab-ab47-27fa9f4051ea
keywords: ["storage miniport drivers WDK", "miniport drivers WDK storage", "storage drivers WDK , miniport drivers"]
---

# Storage Miniport Drivers


## <span id="ddk_storage_miniport_drivers_kg"></span><span id="DDK_STORAGE_MINIPORT_DRIVERS_KG"></span>


This section contains the following topics:

[SCSI Miniport Drivers](scsi-miniport-drivers.md)

[Storport Miniport Drivers](storport-miniport-drivers.md)

[IDE Controller Minidrivers](ide-controller-minidrivers.md)

[ATA Miniport Drivers](ata-miniport-drivers.md)

The best practice for storage miniport drivers is to avoid calling operating system routines other than the routines that the port driver support libraries provide. For example, storage miniport drivers should not call [**KeQuerySystemTime**](https://msdn.microsoft.com/library/windows/hardware/ff553068). Instead, miniport drivers should call routines like [**ScsiPortQuerySystemTime**](https://msdn.microsoft.com/library/windows/hardware/ff564708) or [**StorPortQuerySystemTime**](https://msdn.microsoft.com/library/windows/hardware/ff567465). Storage miniport drivers should not call [**MmGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554547). Instead, miniport drivers should call routines like [**ScsiPortGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff564636) and [**StorPortGetPhysicalAddress**](https://msdn.microsoft.com/library/windows/hardware/ff567095).

Do not use [Hardware Abstraction Layer Routines](https://msdn.microsoft.com/library/windows/hardware/ff546644) in miniport drivers.

The following list indicates the port driver support library that each type of storage miniport driver should use:

-   SCSI Port miniport drivers: [SCSI Port Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff565375)

-   Storport miniport drivers: [Storport Driver Support Routines](https://msdn.microsoft.com/library/windows/hardware/ff567548)

-   IDE miniport drivers: [PciIdeX Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff563803)

-   ATA Port miniport drivers: [ATA Port Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff551343)

 

 


--------------------


