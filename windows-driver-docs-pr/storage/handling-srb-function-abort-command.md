---
title: Handling SRB\_FUNCTION\_ABORT\_COMMAND
description: Handling SRB\_FUNCTION\_ABORT\_COMMAND
ms.assetid: 74d46df6-2e3e-45d8-bedb-a81a80a0aec1
keywords: ["SCSI miniport drivers WDK storage , HwScsiStartIo", "HwScsiStartIo", "SRB_FUNCTION_ABORT_COMMAND"]
---

# Handling SRB\_FUNCTION\_ABORT\_COMMAND


## <span id="ddk_handling_srb_function_abort_command_kg"></span><span id="DDK_HANDLING_SRB_FUNCTION_ABORT_COMMAND_KG"></span>


An *HwScsiStartIo* routine is also responsible for handling incoming SRBs with the **Function** member set to SRB\_FUNCTION\_ABORT\_COMMAND.

For an abort request, the miniport driver's *HwScsiStartIo* routine should verify that the given SRB has not been aborted already by calling **ScsiPortGetSrb** for the target logical unit and comparing the returned pointer to the current SRB's **NextSrb** value. If they are unequal, the current SRB has already been aborted, and the miniport driver's *HwScsiStartIo* routine should do the following:

1.  Set the input SRB's **SrbStatus** to SRB\_STATUS\_ABORT\_FAILED.

2.  Call [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657) with the *NotificationType***RequestComplete** and with the input SRB.

3.  Call **ScsiPortNotification** again with the *NotificationType***NextRequest**, or with **NextLuRequest** if the HBA supports tagged queuing or multiple requests per logical unit.

Otherwise, the *HwScsiStartIo* routine does the following:

1.  Sets up context for the request in its device, logical unit, and/or SRB extensions.

2.  Programs the HBA to abort the given **NextSrb** request.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20SRB_FUNCTION_ABORT_COMMAND%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




