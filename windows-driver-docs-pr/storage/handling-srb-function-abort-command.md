---
title: Handling SRB_FUNCTION_ABORT_COMMAND
description: Handling SRB_FUNCTION_ABORT_COMMAND
ms.assetid: 74d46df6-2e3e-45d8-bedb-a81a80a0aec1
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- SRB_FUNCTION_ABORT_COMMAND
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




