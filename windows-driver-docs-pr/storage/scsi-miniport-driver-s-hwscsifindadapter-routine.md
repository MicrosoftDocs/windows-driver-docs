---
title: SCSI Miniport Driver's HwScsiFindAdapter Routine
description: SCSI Miniport Driver's HwScsiFindAdapter Routine
ms.assetid: c89ad751-ff29-4aa7-b907-cb490d060906
keywords:
- HwScsiFindAdapter
- SCSI miniport drivers WDK storage , HwScsiFindAdapter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Miniport Driver's HwScsiFindAdapter Routine


## <span id="ddk_scsi_miniport_drivers_hwscsifindadapter_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIFINDADAPTER_ROUTINE_KG"></span>


The operating system-specific port driver fills in as much of the [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900) in the configuration information buffer as it can from the miniport driver's [**HW\_INITIALIZATION\_DATA (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff557456) specification and other sources in the system before calling the given *HwScsiFindAdapter* routine with a pointer to the configuration information buffer.

In general, an *HwScsiFindAdapter* routine is responsible for using the supplied configuration information and/or for calling **ScsiPort***Xxx* to collect sufficient configuration information to determine whether it supports an HBA on the I/O bus identified by the **SystemIoBusNumber** in the PORT\_CONFIGURATION\_INFORMATION supplied by the port driver. If so, *HwScsiFindAdapter* is responsible for filling in any remaining configuration information for the supported HBA in the PORT\_CONFIGURATION\_INFORMATION, for setting up the miniport driver's device extension with driver-determined state about that HBA, and for setting the *Again* parameter to an appropriate value before it returns control.

See [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900) and [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) for more information.

 

 




