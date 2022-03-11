---
title: SCSI miniport driver overview
description: SCSI Miniport Drivers
keywords:
- SCSI miniport drivers WDK storage
- storage miniport drivers WDK , SCSI miniport drivers
- miniport drivers WDK storage , SCSI miniport drivers
- SCSI miniport drivers WDK storage , about SCSI miniport drivers
- HBA WDK SCSI
ms.date: 03/10/2022
ms.custom: contperf-fy22q3
---

# SCSI miniport driver overview

This section provides implementation details to develop a SCSI miniport driver. A vendor-supplied SCSI miniport driver works together with the system-supplied [SCSI port driver](scsi-port-driver-overview.md).

> [!NOTE]
>
> Vendors are encouraged to implement [Storport miniport drivers](storport-miniport-drivers.md) and use the [Storport port driver](storport-driver-overview.md) where possible.

SCSI miniport drivers are host bus adapter (HBA)-specific but operating system-independent. Each miniport driver:

* Links itself with the system-supplied SCSI port driver, which is a dynamic-link library (DLL).
* Calls only the port driver's **ScsiPort***Xxx* routines to communicate with the system and its HBA.

SCSI miniport drivers run on Microsoft operating systems that support Microsoft Win32 applications and also export the [**ScsiPort***Xxx* routines](scsi-port-driver-support-routines.md).
