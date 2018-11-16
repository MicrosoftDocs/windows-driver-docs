---
title: SCSI Miniport Driver's HwScsiStartIo Routine
description: SCSI Miniport Driver's HwScsiStartIo Routine
ms.assetid: cb818e5f-b91f-44cb-972b-22f75459edeb
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- incoming I/O requests WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Miniport Driver's HwScsiStartIo Routine


## <span id="ddk_scsi_miniport_drivers_hwscsistartio_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSISTARTIO_ROUTINE_KG"></span>


As its name suggests, a [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323) routine is the entry point for incoming requests to peripheral devices on the HBA-driven bus(es). *HwScsiStartIo* is called with pointers to a SCSI request block (SRB) and to the miniport driver's device extension for per-HBA state. For information about the syntax of this routine see **HwScsiStartIo**.

If the miniport driver's **DriverEntry** routine also requested that memory be allocated for logical unit extensions (see [Calling ScsiPortInitialize](calling-scsiportinitialize.md)), the *HwScsiStartIo* routine calls **ScsiPortGetLogicalUnit** with the input device extension pointer and the **PathId**, **TargetId**, and **Lun** values from the input SRB.

If the **DriverEntry** routine requested that memory be allocated for SRB extensions, the **SrbExtension** member in each SRB contains a pointer to the miniport driver's per-request storage area. Note that a miniport driver must request that memory be allocated for **SrbExtension**s if it maintains per-request state information. It cannot use an SRB for this purpose.

 

 




