---
title: '_Flt_CompletionContext_Outptr_ Annotation'
description: Use the _Flt_CompletionContext_Outptr_ annotation when you declare the file system minifilter pre-operation callback function PFLT_PRE_OPERATION_CALLBACK.
ms.assetid: C3B285EA-0DAB-48D4-AE2F-CB4FBB30EF15
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \_Flt\_CompletionContext\_Outptr\_ Annotation


Use the **\_Flt\_CompletionContext\_Outptr\_** annotation when you declare the file system minifilter pre-operation callback function [**PFLT\_PRE\_OPERATION\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551109). Place this annotation on the *CompletionContext* parameter. This annotation directs the code analysis tool to check that the *CompletionContext* is correct for the FLT\_PREOP\_CALLBACK\_STATUS return value.

If a pre-operation callback function ([**PFLT\_PRE\_OPERATION\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551109)) returns FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK or FLT\_PREOP\_SYNCHRONIZE the *CompletionContext* might or might not be NULL. For any other FLT\_PREOP\_CALLBACK\_STATUS return value the *CompletionContext* must be NULL. The *CompletionContext* is filter-defined state that is passed from the filter’s pre-operation callback to the corresponding post-operation callback function ([**PFLT\_POST\_OPERATION\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551107)). The post-operation callback is only called if the filter returned FLT\_PREOP\_SUCCESS\_WITH\_CALLBACK or FLT\_PREOP\_SYNCHRONIZE from its pre-operation callback function. If the filter doesn’t pass any state from its pre-operation callback function to its post-operation callback function the *CompletionContext* is NULL, and therefore *CompletionContext* in its post-operation callback function will be NULL. Each individual filter decides whether to return state in *CompletionContext* from a pre-operation callback function, so it is up to each individual filter to know whether or not it should look at *CompletionContext* in its post-operation callback function.

## <span id="Example"></span><span id="example"></span><span id="EXAMPLE"></span>Example


The following example shows the function prototype for a [**PFLT\_PRE\_OPERATION\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551109) function called *SwapPreReadBuffers*. The *CompletionContext* parameter receives the context that will be passed to the post-operation callback function and it is declared with **\_Flt\_CompletionContext\_Outptr\_** annotation.

```ManagedCPlusPlus
FLT_PREOP_CALLBACK_STATUS
SwapPreReadBuffers(
    _Inout_ PFLT_CALLBACK_DATA Data,
    _In_ PCFLT_RELATED_OBJECTS FltObjects,
    _Flt_CompletionContext_Outptr_ PVOID *CompletionContext
    );
```

The **\_Flt\_CompletionContext\_Outptr\_** annotation is defined in specstrings.h. Using the annotation can add valuable error checking without adding overhead or complexity to your code.

## <span id="related_topics"></span>Related topics


[**PFLT\_PRE\_OPERATION\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551109)

[**PFLT\_POST\_OPERATION\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551107)

[SAL 2.0 Annotations for Windows Drivers](sal-2-annotations-for-windows-drivers.md)





