---
title: Ensuring that Completion Processing is Performed at Safe IRQL
author: windows-driver-content
description: Ensuring that Completion Processing is Performed at Safe IRQL
ms.assetid: 54487fba-2ced-4bcd-afa6-d56b351aa7d6
keywords: ["postoperation callback routines WDK file system minifilter , completion processing", "completing I/O requests WDK file system"]
---

# Ensuring that Completion Processing is Performed at Safe IRQL


## <span id="ddk_ensuring_that_completion_processing_is_performed_at_safe_irql_if"></span><span id="DDK_ENSURING_THAT_COMPLETION_PROCESSING_IS_PERFORMED_AT_SAFE_IRQL_IF"></span>


As noted in [Writing Postoperation Callback Routines](writing-postoperation-callback-routines.md), the [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) for an IRP-based I/O operation can be called at IRQL = DISPATCH\_LEVEL, unless the minifilter driver's preoperation callback routine synchronized the operation by returning FLT\_PREOP\_SYNCHRONIZE or the operation is a create operation, which is inherently synchronous. (For more information about this return value, see [Returning FLT\_PREOP\_SYNCHRONIZE](returning-flt-preop-synchronize.md).)

However, for IRP-based I/O operations that are not already synchronized, minifilter drivers can use to two techniques to ensure that completion processing is performed at IRQL &lt;= APC\_LEVEL.

The first technique is for the postoperation callback routine to pend the I/O operation until completion processing can be performed at IRQL &lt;= APC\_LEVEL. This technique is described in [Pending an I/O Operation in a Postoperation Callback Routine](pending-an-i-o-operation-in-a-postoperation-callback-routine.md).

The second technique is for the minifilter driver's postoperation callback routine to call [**FltDoCompletionProcessingWhenSafe**](https://msdn.microsoft.com/library/windows/hardware/ff542047). **FltDoCompletionProcessingWhenSafe** pends the I/O operation only if the current IRQL is &gt;= DISPATCH\_LEVEL. Otherwise, this routine executes the minifilter driver's **SafePostCallback** routine immediately. This technique is described in **FltDoCompletionProcessingWhenSafe**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Ensuring%20that%20Completion%20Processing%20is%20Performed%20at%20Safe%20IRQL%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


