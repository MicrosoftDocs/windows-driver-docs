---
title: Handling SRB\_FUNCTION\_RESET\_DEVICE
description: Handling SRB\_FUNCTION\_RESET\_DEVICE
ms.assetid: d95bca21-306e-4598-a8c6-04990885e23d
keywords: ["SCSI miniport drivers WDK storage , HwScsiStartIo", "HwScsiStartIo", "SRB_FUNCTION_RESET_DEVICE"]
---

# Handling SRB\_FUNCTION\_RESET\_DEVICE


## <span id="ddk_handling_srb_function_reset_device_kg"></span><span id="DDK_HANDLING_SRB_FUNCTION_RESET_DEVICE_KG"></span>


The ScsiPort driver no longer sends this SRB to its miniport drivers. Only Storport miniport drivers might have to handle this SRB.

If the HBA has the ability to reset a target device, as indicated when [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) sets up the [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900), the port driver requests a device reset when an uncompleted request times out.

The system port driver calls the miniport driver's *HwScsiStartIo* routine with an SRB in which the **Function** member is set to SRB\_FUNCTION\_RESET\_DEVICE. The miniport driver is responsible for completing any requests that are uncompleted on the device when it receives a reset-device request.

If the device reset fails or times out, or if the time-out occurs while the port driver is waiting for a **NextRequest** notification, the port driver calls [*HwScsiResetBus*](https://msdn.microsoft.com/library/windows/hardware/ff557318).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20SRB_FUNCTION_RESET_DEVICE%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




