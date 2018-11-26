---
title: Calling ScsiPortXxx from HwScsiFindAdapter
description: Calling ScsiPortXxx from HwScsiFindAdapter
ms.assetid: 17cfca31-ff93-4882-872c-ab8af6cdc3cf
keywords:
- HwScsiFindAdapter
- SCSI miniport drivers WDK storage , HwScsiFindAdapter
- calling ScsiPortXxx routines WDK storage
- ScsiPortXxx calls
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling ScsiPortXxx from HwScsiFindAdapter


## <span id="ddk_calling_scsiportxxx_from_hwscsifindadapter_kg"></span><span id="DDK_CALLING_SCSIPORTXXX_FROM_HWSCSIFINDADAPTER_KG"></span>


Certain **ScsiPort***Xxx* routines can be called *only* from the miniport driver's *HwScsiFindAdapter* routine(s), in particular, the following:

-   [**ScsiPortValidateRange**](https://msdn.microsoft.com/library/windows/hardware/ff564761) to verify that a miniport driver-supplied, bus-relative access range has not already been claimed in the registry by another driver for its device.

-   [**ScsiPortGetDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff564629) to map the (bus-relative) "physical" address range for an HBA to a system-assigned logical address range that the driver can use to communicate with the HBA by calling the **ScsiPortRead***Xxx* and **ScsiPortWrite***Xxx* routines with the mapped logical range addresses.

-   [**ScsiPortFreeDeviceBase**](https://msdn.microsoft.com/library/windows/hardware/ff564623) to release such a mapped range if *HwScsiFindAdapter* does not find an HBA it can support on a given I/O bus, as indicated by the PORT\_CONFIGURATION\_INFORMATION **SystemIoBusNumber** value.

-   [**ScsiPortGetUncachedExtension**](https://msdn.microsoft.com/library/windows/hardware/ff564639) to allocate a DMA buffer shared between the system and a bus-master HBA.

In addition to these four routines, there is one routine that can only be called from the miniport driver's *HwScsiFindAdapter* routine *or* from *HwScsiAdapterControl* when the control type is **ScsiSetRunningConfig**:

-   [**ScsiPortGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff564624) to get BUS\_DATA\_TYPE-specific configuration information, such as bus-relative device memory (access) ranges, interrupt vector or IRQL, and DMA channel or port.

For more information about these **ScsiPort***Xxx* routines, see [SCSI Port Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff565375).

 

 




