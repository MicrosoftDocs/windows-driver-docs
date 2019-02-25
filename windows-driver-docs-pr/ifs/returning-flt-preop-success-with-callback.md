---
title: Returning FLT_PREOP_SUCCESS_WITH_CALLBACK
description: Returning FLT_PREOP_SUCCESS_WITH_CALLBACK
ms.assetid: 6247b952-3189-4792-a15b-c3a4b3dc80ae
keywords:
- FLT_PREOP_SUCCESS_WITH_CALLBACK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK


## <span id="ddk_returning_flt_preop_success_with_callback_if"></span><span id="DDK_RETURNING_FLT_PREOP_SUCCESS_WITH_CALLBACK_IF"></span>


If a minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) returns FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK, the filter manager calls the minifilter driver's [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) during I/O completion.

**Note**   If the minifilter driver's preoperation callback routine returns FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK but the minifilter driver has not registered a postoperation callback routine for the operation, the system asserts on a checked build.

 

If the minifilter driver's preoperation callback routine returns FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK, it can return a non-NULL value in its *CompletionContext* output parameter. This parameter is an optional context pointer that is passed to the corresponding postoperation callback routine. The postoperation callback routine receives this pointer in its *CompletionContext* input parameter.

The FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK status value can be returned for all types of I/O operations.

 

 




