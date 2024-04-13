---
title: Crash Dump and Hibernation Support
description: Crash Dump and Hibernation Support
keywords:
- crash dump WDK
ms.date: 04/20/2017
---

# Crash Dump and Hibernation Support


A Storport virtual miniport driver must support the [**SCSI\_REQUEST\_BLOCK**](/windows-hardware/drivers/ddi/srb/ns-srb-_scsi_request_block) (SRB) function code SRB\_FUNCTION\_DUMP\_POINTERS. When a miniport driver receives this type of SRB, the DataBuffer SRB member points to a [**MINIPORT\_DUMP\_POINTERS**](/windows-hardware/drivers/ddi/storport/ns-storport-_miniport_dump_pointers) structure. This SRB is sent to a virtual miniport driver that is used to control the disk that holds the crash dump data after the SRB returns from the miniport driver's [**HwStorInitialize**](/windows-hardware/drivers/ddi/storport/nc-storport-hw_initialize) routine.

 

