---
title: ATA Port Driver Overview
description: ATA Port Driver Overview
keywords:
- storage port drivers WDK , ATA Port driver
- ATA Port drivers WDK
- ATA Port drivers WDK , about ATA Port drivers
- IDE controllers WDK ATA Port driver
ms.date: 10/08/2019
---

# ATA Port Driver Overview

> [!NOTE]
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](storport-driver-overview.md) and [Storport miniport](./storport-miniport-drivers.md) driver models.

In addition to the [SCSI Port Driver](scsi-port-driver-overview.md) and the [Storport Driver](storport-driver-overview.md), Windows Vista and later versions of the Windows operating system provide the ATA port driver (*Ataport.sys*), a storage port driver that is especially suitable for use with IDE controllers.

The most significant difference between the ATA port driver and other system-supplied storage port drivers is the protocol that the ATA port driver uses to communicate with other drivers. All other system-supplied storage port drivers use SCSI request blocks (SRBs) to communicate both with higher-level drivers, such as storage class drivers, and with miniport drivers. The ATA port driver uses SRBs to communicate with higher-level drivers only. To communicate with its miniport drivers, ATA port uses a packet called an IDE request block (IRB), which is defined by the [IDE_REQUEST_BLOCK](/windows-hardware/drivers/ddi/irb/ns-irb-_ide_request_block) structure. IRBs are better designed than SRBs to the characteristics of ATA devices.

Another difference between the ATA port driver and other system-supplied storage drivers is that the ATA port driver shields ATA miniport drivers from certain requirements that are defined by the SCSI standard. For example, the ATA port driver uses ATA commands to collect the equivalent of SCSI sense data from the ATA miniport driver, translates the data so that it complies with a SCSI sense data format, and passes the data to higher-level drivers as if it were SCSI sense data. Therefore, ATA miniport drivers do not have to respond directly to requests from higher-level drivers for SCSI sense data.

The ATA miniport driver interface closely resembles the SCSI port driver interface. Therefore, if you have already written a SCSI miniport driver, you should be able to easily learn how to write an ATA miniport driver. Drivers for current ATA/ATAPI technologies, such as Serial ATA (SATA), should use the higher performance Storport miniport interface.

Together with the ATA port driver, the operating system provides a default ATA miniport driver and a default controller minidriver. The system-supplied default drivers work for most controller hardware, and we strongly recommend that the default minidrivers be used wherever possible.
