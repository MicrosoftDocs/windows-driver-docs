---
title: Releasing Contexts
description: Releasing Contexts
ms.assetid: 29d855cd-cca6-486b-86d9-f74810ae12c1
keywords:
- contexts WDK file system minifilter , releasing
- releasing contexts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Releasing Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


A minifilter driver releases a context by calling [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314). Every successful call to one of the following routines must eventually be matched by a call to **FltReleaseContext**:

[**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710)

[**FltGetInstanceContext**](https://msdn.microsoft.com/library/windows/hardware/ff543058)

[**FltGetFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff543025)

[**FltGetStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff543144)

[**FltGetStreamHandleContext**](https://msdn.microsoft.com/library/windows/hardware/ff543155)

[**FltGetTransactionContext**](https://msdn.microsoft.com/library/windows/hardware/ff543175)

[**FltGetVolumeContext**](https://msdn.microsoft.com/library/windows/hardware/ff543189)

[**FltReferenceContext**](https://msdn.microsoft.com/library/windows/hardware/ff544291)

Note that the *OldContext* pointer returned by **FltSet***Xxx***Context** and the *Context* pointer returned by [**FltDeleteContext**](https://msdn.microsoft.com/library/windows/hardware/ff541960) must also be released when they are no longer needed.

In the following code example, taken from the CTX sample minifilter driver, the **CtxInstanceSetup** routine creates and sets an instance context and then calls [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314):

```cpp
status = FltAllocateContext(
           FltObjects->Filter,           //Filter
           FLT_INSTANCE_CONTEXT,         //ContextType
           CTX_INSTANCE_CONTEXT_SIZE,    //ContextSize
           NonPagedPool,                 //PoolType
           &instanceContext);            //ReturnedContext
...
status = FltSetInstanceContext(
           FltObjects->Instance,              //Instance
           FLT_SET_CONTEXT_KEEP_IF_EXISTS,    //Operation
           instanceContext,                   //NewContext
           NULL);                             //OldContext

if (instanceContext != NULL) {
  FltReleaseContext(instanceContext);
}
return status;
```

Note that [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314) is called regardless of whether the call to [**FltSetInstanceContext**](https://msdn.microsoft.com/library/windows/hardware/ff544521) succeeds. In both cases, the caller must call **FltReleaseContext** to release the reference set by [**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710) (not **FltSetInstanceContext**).

If the context is successfully set for the instance, [**FltSetInstanceContext**](https://msdn.microsoft.com/library/windows/hardware/ff544521) adds its own reference to the instance context. Thus, the reference set by [**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710) is no longer needed, and the call to [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314) removes it.

If the call to [**FltSetInstanceContext**](https://msdn.microsoft.com/library/windows/hardware/ff544521) fails, the instance context has only one reference, namely the one set by [**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710). When [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314) returns, the instance context has a reference count of zero, and it is freed by the filter manager.

 

 




