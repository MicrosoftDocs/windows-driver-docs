---
title: Handling SRB_FUNCTION_RESET_DEVICE
description: Handling SRB_FUNCTION_RESET_DEVICE
ms.assetid: d95bca21-306e-4598-a8c6-04990885e23d
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- SRB_FUNCTION_RESET_DEVICE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling SRB\_FUNCTION\_RESET\_DEVICE


## <span id="ddk_handling_srb_function_reset_device_kg"></span><span id="DDK_HANDLING_SRB_FUNCTION_RESET_DEVICE_KG"></span>


The ScsiPort driver no longer sends this SRB to its miniport drivers. Only Storport miniport drivers might have to handle this SRB.

If the HBA has the ability to reset a target device, as indicated when [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) sets up the [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900), the port driver requests a device reset when an uncompleted request times out.

The system port driver calls the miniport driver's *HwScsiStartIo* routine with an SRB in which the **Function** member is set to SRB\_FUNCTION\_RESET\_DEVICE. The miniport driver is responsible for completing any requests that are uncompleted on the device when it receives a reset-device request.

If the device reset fails or times out, or if the time-out occurs while the port driver is waiting for a **NextRequest** notification, the port driver calls [*HwScsiResetBus*](https://msdn.microsoft.com/library/windows/hardware/ff557318).

 

 




