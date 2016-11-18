---
title: \_Flt\_CompletionContext\_Outptr\_ Annotation
description: Use the \_Flt\_CompletionContext\_Outptr\_ annotation when you declare the file system minifilter pre-operation callback function PFLT\_PRE\_OPERATION\_CALLBACK.
ms.assetid: C3B285EA-0DAB-48D4-AE2F-CB4FBB30EF15
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20_Flt_CompletionContext_Outptr_%20Annotation%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





