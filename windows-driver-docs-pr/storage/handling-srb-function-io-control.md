---
title: Handling SRB\_FUNCTION\_IO\_CONTROL
description: Handling SRB\_FUNCTION\_IO\_CONTROL
ms.assetid: 92d09a49-d8e8-4d97-b334-c42d5b04ee8d
keywords: ["SCSI miniport drivers WDK storage , HwScsiStartIo", "HwScsiStartIo", "SRB_FUNCTION_IO_CONTROL"]
---

# Handling SRB\_FUNCTION\_IO\_CONTROL


## <span id="ddk_handling_srb_function_io_control_kg"></span><span id="DDK_HANDLING_SRB_FUNCTION_IO_CONTROL_KG"></span>


Whether a miniport driver handles SRB\_FUNCTION\_IO\_CONTROL requests depends on whether the HBA is to provide dedicated support for a user-mode application. Supporting this request allows a set of driver-defined ("private") I/O control requests to be sent directly to the miniport driver. For SRBs with the **Function** member set to SRB\_FUNCTION\_IO\_CONTROL, the **DataBuffer** member contains a pointer to a system-defined SRB\_IO\_CONTROL structure containing the driver-defined and application-specified **ControlCode**.

All system-defined, required device I/O control requests sent to NT-based operating system storage class drivers are mapped to SRBs with the **Function** member set to SRB\_FUNCTION\_EXECUTE\_SCSI, not to SRB\_FUNCTION\_IO\_CONTROL.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20SRB_FUNCTION_IO_CONTROL%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




