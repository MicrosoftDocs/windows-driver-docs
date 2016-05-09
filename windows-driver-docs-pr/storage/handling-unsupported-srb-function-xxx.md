---
title: Handling Unsupported SRB\_FUNCTION\_XXX
description: Handling Unsupported SRB\_FUNCTION\_XXX
ms.assetid: 95b9288c-290f-4908-9de3-11d68ed624e2
keywords: ["SCSI miniport drivers WDK storage , HwScsiStartIo", "HwScsiStartIo", "unsupported SRB_FUNCTION_XXX", "SRB_FUNCTION_XXX unsupported"]
---

# Handling Unsupported SRB\_FUNCTION\_XXX


## <span id="ddk_handling_unsupported_srb_function_xxx_kg"></span><span id="DDK_HANDLING_UNSUPPORTED_SRB_FUNCTION_XXX_KG"></span>


Every *HwScsiStartIo* routine must handle the receipt of an unsupported SRB\_FUNCTION\_*XXX* as follows:

1.  Set the input SRB's **SrbStatus** to SRB\_STATUS\_INVALID\_REQUEST.

2.  Call [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657) with the *NotificationType***RequestComplete** and with the input SRB.

3.  Call **ScsiPortNotification** again with the *NotificationType***NextRequest**, or with **NextLuRequest** if the HBA supports tagged queuing or multiple requests per logical unit.

4.  Return control.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20Unsupported%20SRB_FUNCTION_XXX%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




