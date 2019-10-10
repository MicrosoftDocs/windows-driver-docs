---
title: SCSI Port Driver Support Routines
description: Describes the SCSI port driver routines.
ms.assetid: b4bd6afe-77a2-4bd1-a762-5887f77cc737
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
| *ScsiPortXxx* | [srb.h header](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/srb/) |
| *ScsiPortWmiXxx* | [scsiwmi.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/scsiwmi/) |

For a list of SCSI miniport driver routines, see [SCSI Miniport Driver Routines](scsi-miniport-driver-routines.md).
