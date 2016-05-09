---
title: Returning FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK
description: Returning FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK
ms.assetid: 6247b952-3189-4792-a15b-c3a4b3dc80ae
keywords: ["FLT_PREOP_SUCCESS_WITH_CALLBACK"]
---

# Returning FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK


## <span id="ddk_returning_flt_preop_success_with_callback_if"></span><span id="DDK_RETURNING_FLT_PREOP_SUCCESS_WITH_CALLBACK_IF"></span>


If a minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) returns FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK, the filter manager calls the minifilter driver's [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) during I/O completion.

**Note**   If the minifilter driver's preoperation callback routine returns FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK but the minifilter driver has not registered a postoperation callback routine for the operation, the system asserts on a checked build.

 

If the minifilter driver's preoperation callback routine returns FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK, it can return a non-NULL value in its *CompletionContext* output parameter. This parameter is an optional context pointer that is passed to the corresponding postoperation callback routine. The postoperation callback routine receives this pointer in its *CompletionContext* input parameter.

The FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK status value can be returned for all types of I/O operations.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Returning%20FLT_PREOP_SUCCESS_WITH_CALLBACK%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




