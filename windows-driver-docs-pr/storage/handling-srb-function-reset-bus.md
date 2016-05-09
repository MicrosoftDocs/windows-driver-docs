---
title: Handling SRB\_FUNCTION\_RESET\_BUS
description: Handling SRB\_FUNCTION\_RESET\_BUS
ms.assetid: 285cbd5c-e364-4f0f-9020-0bc6f3d45cac
keywords: ["SCSI miniport drivers WDK storage , HwScsiStartIo", "HwScsiStartIo", "SRB_FUNCTION_RESET_BUS"]
---

# Handling SRB\_FUNCTION\_RESET\_BUS


## <span id="ddk_handling_srb_function_reset_bus_kg"></span><span id="DDK_HANDLING_SRB_FUNCTION_RESET_BUS_KG"></span>


The system port driver always sends its own reset-bus requests directly to the miniport driver's [*HwScsiResetBus*](https://msdn.microsoft.com/library/windows/hardware/ff557318) routine, described in [SCSI Miniport Driver's HwScsiResetBus Routine](scsi-miniport-driver-s-hwscsiresetbus-routine.md).

However, it is possible for the [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323) routine to be called with an SRB in which the **Function** member is set to SRB\_FUNCTION\_RESET\_BUS if a NT-based operating system storage class driver requests this operation. The *HwScsiStartIo* routine can simply call the *HwScsiResetBus* routine to satisfy an incoming bus-reset request.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20SRB_FUNCTION_RESET_BUS%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




