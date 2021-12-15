---
title: Communicating with a storage port driver
description: How storage miniports communicate with a storage port driver
keywords:
- storage miniport drivers WDK
- miniport drivers WDK storage
- storage drivers WDK , miniport drivers
- Storage miniports should avoid calling operating system routines
ms.date: 03/16/2021
---

# Communicating with a storage port driver

Communication between a storage miniport driver and a system-supplied storage port driver happens as follows:

- A miniport calls a set of storage port driver-supplied support routines

- A miniport implements a standard set of routines for its storage port driver to call, some that are required and some that are optional

The miniport driver routines called by the SCSI port driver, the Storport driver, and the ATA port driver are very similar to one another.

Storage miniport drivers should avoid calling operating system (OS) routines other than the support routines provided by the appropriate port driver support. For example:

- Storage miniport drivers should not call [**KeQuerySystemTime**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequerysystemtime), but should instead call routines like [**ScsiPortQuerySystemTime**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportquerysystemtime) or [**StorPortQuerySystemTime**](/windows-hardware/drivers/ddi/storport/nf-storport-storportquerysystemtime).
- Storage miniport drivers should not call [**MmGetPhysicalAddress**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmgetphysicaladdress), but should instead call routines like [**ScsiPortGetPhysicalAddress**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportgetphysicaladdress) and [**StorPortGetPhysicalAddress**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetphysicaladdress).

> [!NOTE]
> Miniport drivers that seek to be Windows HLK-certified will fail the [Storage Imports Test](/windows-hardware/test/hlk/testref/c75585b2-a3e6-4db0-8847-f6023171d4b9) if they call OS routines, and thus not qualify for the [Windows Hardware Compatibility Program](/windows-hardware/design/compatibility/).

Do not use [Hardware Abstraction Layer Routines](/previous-versions/windows/hardware/drivers/ff546644(v=vs.85)) in miniport drivers.
