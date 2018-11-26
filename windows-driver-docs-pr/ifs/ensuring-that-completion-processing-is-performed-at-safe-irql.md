---
title: Ensuring that Completion Processing is Performed at Safe IRQL
description: Ensuring that Completion Processing is Performed at Safe IRQL
ms.assetid: 54487fba-2ced-4bcd-afa6-d56b351aa7d6
keywords:
- postoperation callback routines WDK file system minifilter , completion processing
- completing I/O requests WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Ensuring that Completion Processing is Performed at Safe IRQL


## <span id="ddk_ensuring_that_completion_processing_is_performed_at_safe_irql_if"></span><span id="DDK_ENSURING_THAT_COMPLETION_PROCESSING_IS_PERFORMED_AT_SAFE_IRQL_IF"></span>


As noted in [Writing Postoperation Callback Routines](writing-postoperation-callback-routines.md), the [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) for an IRP-based I/O operation can be called at IRQL = DISPATCH\_LEVEL, unless the minifilter driver's preoperation callback routine synchronized the operation by returning FLT\_PREOP\_SYNCHRONIZE or the operation is a create operation, which is inherently synchronous. (For more information about this return value, see [Returning FLT\_PREOP\_SYNCHRONIZE](returning-flt-preop-synchronize.md).)

However, for IRP-based I/O operations that are not already synchronized, minifilter drivers can use to two techniques to ensure that completion processing is performed at IRQL &lt;= APC\_LEVEL.

The first technique is for the postoperation callback routine to pend the I/O operation until completion processing can be performed at IRQL &lt;= APC\_LEVEL. This technique is described in [Pending an I/O Operation in a Postoperation Callback Routine](pending-an-i-o-operation-in-a-postoperation-callback-routine.md).

The second technique is for the minifilter driver's postoperation callback routine to call [**FltDoCompletionProcessingWhenSafe**](https://msdn.microsoft.com/library/windows/hardware/ff542047). **FltDoCompletionProcessingWhenSafe** pends the I/O operation only if the current IRQL is &gt;= DISPATCH\_LEVEL. Otherwise, this routine executes the minifilter driver's **SafePostCallback** routine immediately. This technique is described in **FltDoCompletionProcessingWhenSafe**.

 

 




