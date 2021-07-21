---
title: ATA Miniport Drivers
description: ATA Miniport Drivers
keywords:
- ATA miniport drivers WDK
- storage ATA miniport drivers WDK
- storage miniport drivers WDK , ATA miniport drivers
- miniport drivers WDK storage , ATA miniport drivers
ms.date: 10/08/2019
ms.localizationpriority: medium
---

# ATA Miniport Drivers

> [!NOTE]
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](./storport-driver-overview.md) and [Storport miniport](./storport-miniport-drivers.md) driver models.

ATA miniport drivers work with the ATA port driver. This page lists the routines implemented within ATA miniport drivers that the ATA port driver calls. See [ATA Port Driver Support Routines](ata-port-driver-support-routines.md) for a list of system-supplied ATA port driver routines that ATA miniport drivers can call.

## ATA Controller Interface Routines

Every vendor-supplied miniport driver is required to implement a set of routines that define the controller interface. By using these routines, the miniport driver communicates with the system-supplied controller driver, *pciidex.sys*.

A vendor-supplied miniport driver communicates with the controller driver to initialize both port and miniport drivers and to exchange parameters that are required to configure the host bus adapter (HBA). If a routine is not explicitly identified in this section as optional, it is required. If you choose not to implement an optional routine, you must make sure that the miniport driver sets the corresponding function pointers in the [IDE_CONTROLLER_INTERFACE](/windows-hardware/drivers/ddi/irb/ns-irb-_ide_controller_interface) structure to NULL.

- DriverEntry
- AtaAdapterControl
- AtaControllerChannelEnabled
- AtaControllerTransferModeSelect

## ATA Channel Interface Routines

Vendor-supplied miniport drivers can optionally implement a set of routines that define the channel interface. By using these routines, the miniport driver can process every request that is sent to the hardware. The miniport driver must not implement the channel interface partially. If the miniport driver supports the [**AtaChannelInitRoutine**](/windows-hardware/drivers/ddi/irb/nf-irb-ataportinitializeex) routine, it should also implement the following routines:

- AtaChannelInitRoutine
- IdeHwInitialize
- IdeHwBuildIo
- IdeHwStartIo
- IdeHwInterrupt
- IdeHwReset
- IdeHwControl
