---
title: Returning FLT\_PREOP\_SUCCESS\_NO\_CALLBACK
description: Returning FLT\_PREOP\_SUCCESS\_NO\_CALLBACK
ms.assetid: cde708b0-b572-4444-ba4b-158b6906884e
keywords: ["FLT_PREOP_SUCCESS_NO_CALLBACK"]
---

# Returning FLT\_PREOP\_SUCCESS\_NO\_CALLBACK


## <span id="ddk_returning_flt_preop_success_no_callback_if"></span><span id="DDK_RETURNING_FLT_PREOP_SUCCESS_NO_CALLBACK_IF"></span>


If a minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) returns FLT\_PREOP\_SUCCESS\_NO\_CALLBACK, the filter manager does not call the minifilter driver's [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107), if one exists, during I/O completion.

If the minifilter driver's preoperation callback routine returns FLT\_PREOP\_SUCCESS\_NO\_CALLBACK, it must return **NULL** in its *CompletionContext* output parameter.

The FLT\_PREOP\_SUCCESS\_NO\_CALLBACK status value can be returned for all types of I/O operations.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Returning%20FLT_PREOP_SUCCESS_NO_CALLBACK%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




