---
title: SCSI Port Driver Support Routines
description: Describes the SCSI port driver routines.
keywords:
- SCSI port driver support routines
- storage WDK
- storage support routines
ms.date: 10/08/2019
ms.localizationpriority: medium
---

# SCSI Port Driver Support Routines

An operating system-specific SCSI port driver provides *ScsiPortXxx* routines to support operating system-independent SCSI miniport drivers that are linked with a Microsoft-supplied, operating system-specific SCSI port driver. The SCSI port driver is a kernel-mode dynamic-link library.

Lists and reference pages for *ScsiPortXxx* routines can be found in the following locations:

| Routines | Header |
| ------- | ------- |
| *ScsiPortXxx* | [srb.h header](/windows-hardware/drivers/ddi/srb/) |
| *ScsiPortWmiXxx* | [scsiwmi.h](/windows-hardware/drivers/ddi/scsiwmi/) |

For a list of SCSI miniport driver routines, see [SCSI Miniport Driver Routines](scsi-miniport-driver-routines.md).
