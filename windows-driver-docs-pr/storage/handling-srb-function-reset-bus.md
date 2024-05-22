---
title: Handling SRB_FUNCTION_RESET_BUS
description: Handling SRB_FUNCTION_RESET_BUS
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- SRB_FUNCTION_RESET_BUS
ms.date: 04/20/2017
---

# Handling SRB\_FUNCTION\_RESET\_BUS


## <span id="ddk_handling_srb_function_reset_bus_kg"></span><span id="DDK_HANDLING_SRB_FUNCTION_RESET_BUS_KG"></span>


The system port driver always sends its own reset-bus requests directly to the miniport driver's [*HwScsiResetBus*](/previous-versions/windows/hardware/drivers/ff557318(v=vs.85)) routine, described in [SCSI Miniport Driver's HwScsiResetBus Routine](scsi-miniport-driver-s-hwscsiresetbus-routine.md).

However, it is possible for the [**HwScsiStartIo**](/previous-versions/windows/hardware/drivers/ff557323(v=vs.85)) routine to be called with an SRB in which the **Function** member is set to SRB\_FUNCTION\_RESET\_BUS if an NT-based operating system storage class driver requests this operation. The *HwScsiStartIo* routine can simply call the *HwScsiResetBus* routine to satisfy an incoming bus-reset request.

 

