---
title: Returning FLT_PREOP_SUCCESS_NO_CALLBACK
description: Returning FLT_PREOP_SUCCESS_NO_CALLBACK
ms.assetid: cde708b0-b572-4444-ba4b-158b6906884e
keywords:
- FLT_PREOP_SUCCESS_NO_CALLBACK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning FLT\_PREOP\_SUCCESS\_NO\_CALLBACK


## <span id="ddk_returning_flt_preop_success_no_callback_if"></span><span id="DDK_RETURNING_FLT_PREOP_SUCCESS_NO_CALLBACK_IF"></span>


If a minifilter driver's [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) returns FLT\_PREOP\_SUCCESS\_NO\_CALLBACK, the filter manager does not call the minifilter driver's [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107), if one exists, during I/O completion.

If the minifilter driver's preoperation callback routine returns FLT\_PREOP\_SUCCESS\_NO\_CALLBACK, it must return **NULL** in its *CompletionContext* output parameter.

The FLT\_PREOP\_SUCCESS\_NO\_CALLBACK status value can be returned for all types of I/O operations.

 

 




