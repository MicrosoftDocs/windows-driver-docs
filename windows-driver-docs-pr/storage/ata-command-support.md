---
title: ATA Command Support
description: ATA Command Support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ATA Command Support


If a storage device supports the ATA command set, StorPort will send ATA commands directly to a target device using the ATA passthrough control codes. Device management applications can use the [**IOCTL\_ATA\_PASS\_THROUGH**](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_ata_pass_through) and [**IOCTL\_ATA\_PASS\_THROUGH\_DIRECT**](/windows-hardware/drivers/ddi/ntddscsi/ni-ntddscsi-ioctl_ata_pass_through_direct) control codes for this purpose.

This section contains information about special requirements for issuing certain ATA command requests.

[Security Group Commands](security-group-commands.md)

 

