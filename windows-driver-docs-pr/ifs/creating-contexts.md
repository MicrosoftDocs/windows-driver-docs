---
title: Creating Contexts
description: Creating Contexts
ms.assetid: da62d79d-064b-4ea4-abed-ffb13a9cc13d
keywords:
- contexts WDK file system minifilter , creating
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


Once a minifilter driver has registered the context types that it uses, it can create a context by calling [**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710). This routine selects the appropriate context definition to use according to the criteria described in [Registering Context Types](registering-context-types.md).

In the following code example, taken from the CTX sample minifilter driver, the **CtxInstanceSetup** routine calls [**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710) to create an instance context:

```cpp
status = FltAllocateContext(
 FltObjects->Filter,           //Filter
           FLT_INSTANCE_CONTEXT,         //ContextType
           CTX_INSTANCE_CONTEXT_SIZE,    //ContextSize
 NonPagedPool,                 //PoolType
           &instanceContext);            //ReturnedContext
```

In the CTX sample, the following context definition is registered for instance contexts:

```cpp
{ FLT_INSTANCE_CONTEXT,              //ContextType
  0,                                 //Flags
 CtxContextCleanup,                 //ContextCleanupCallback
  CTX_INSTANCE_CONTEXT_SIZE,         //Size
  CTX_INSTANCE_CONTEXT_TAG },        //PoolTag
```

This is a fixed-size context definition, because the **Size** member is a constant. (If the **Size** member were FLT\_VARIABLE\_SIZED\_CONTEXTS, it would be a variable-size context definition.) Note that the FLTFL\_CONTEXT\_REGISTRATION\_NO\_EXACT\_SIZE\_MATCH flag is not set in the **Flags** member. In this case, if the value of the *Size* parameter of [**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710) matches that of the **Size** member of the context definition, **FltAllocateContext** allocates the instance context from the appropriate nonpaged lookaside list. If the values do not match, **FltAllocateContext** fails with a return value of STATUS\_FLT\_CONTEXT\_ALLOCATION\_NOT\_FOUND.

[**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710) initializes the reference count on the new context to one. When the context is no longer needed, the minifilter driver must release this reference. Thus, every call to **FltAllocateContext** must be matched by a subsequent call to [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314).

 

 




