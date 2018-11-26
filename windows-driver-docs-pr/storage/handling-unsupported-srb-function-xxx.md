---
title: Handling Unsupported SRB_FUNCTION_XXX
description: Handling Unsupported SRB_FUNCTION_XXX
ms.assetid: 95b9288c-290f-4908-9de3-11d68ed624e2
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- unsupported SRB_FUNCTION_XXX
- SRB_FUNCTION_XXX unsupported
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Unsupported SRB\_FUNCTION\_XXX


## <span id="ddk_handling_unsupported_srb_function_xxx_kg"></span><span id="DDK_HANDLING_UNSUPPORTED_SRB_FUNCTION_XXX_KG"></span>


Every *HwScsiStartIo* routine must handle the receipt of an unsupported SRB\_FUNCTION\_*XXX* as follows:

1.  Set the input SRB's **SrbStatus** to SRB\_STATUS\_INVALID\_REQUEST.

2.  Call [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657) with the *NotificationType***RequestComplete** and with the input SRB.

3.  Call **ScsiPortNotification** again with the *NotificationType***NextRequest**, or with **NextLuRequest** if the HBA supports tagged queuing or multiple requests per logical unit.

4.  Return control.

 

 




