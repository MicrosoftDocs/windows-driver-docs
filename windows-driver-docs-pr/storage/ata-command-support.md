---
title: ATA Command Support
description: ATA Command Support
ms.assetid: 98149A59-3435-4166-8250-EEFBA44DFD4C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# ATA Command Support


If a storage device supports the ATA command set, StorPort will send ATA commands directly to a target device using the ATA passthrough control codes. Device management applications can use the [**IOCTL\_ATA\_PASS\_THROUGH**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddscsi/ni-ntddscsi-ioctl_ata_pass_through) and [**IOCTL\_ATA\_PASS\_THROUGH\_DIRECT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddscsi/ni-ntddscsi-ioctl_ata_pass_through_direct) control codes for this purpose.

This section contains information about special requirements for issuing certain ATA command requests.

[Security Group Commands](security-group-commands.md)

 

 




