---
title: Creating Contexts
description: Creating Contexts
keywords:
- contexts WDK file system minifilter , creating
ms.date: 01/22/2021
---

# Creating Contexts

Once a minifilter has registered the context types that it uses, it can create a context by calling [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext). This routine selects the appropriate context definition to use according to the criteria described in [Registering Context Types](registering-context-types.md).

Before allocating a context and attempting to set it, a minifilter can call the following routines to determine whether the underlying file system supports file, stream, or stream handle contexts:
- [**FltSupportsFileContexts**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsupportsfilecontexts) or [**FltSupportsFileContextsEx**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsupportsfilecontextsex)
- [**FltSupportsStreamContexts**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsupportsstreamcontexts)
- [**FltSupportsStreamHandleContexts**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsupportsstreamhandlecontexts)

In the following code example, taken from the [CTX sample minifilter](https://github.com/microsoft/Windows-driver-samples/tree/master/filesys/miniFilter/ctx) driver, the **CtxInstanceSetup** routine calls [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext) to create an instance context:

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

The context definition is of fixed-size because the **Size** member is CTX_INSTANCE_CONTEXT_SIZE (versus FLT_VARIABLE_SIZED_CONTEXTS, which is used to indicate a variable-size context definition). Note that the FLTFL_CONTEXT_REGISTRATION_NO_EXACT_SIZE_MATCH flag is not set in the **Flags** member. In this case, if the value of the **ContextSize** parameter of [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext) matches that of the **Size** member of the context definition, **FltAllocateContext** allocates the instance context from the appropriate nonpaged lookaside list. If the values do not match, **FltAllocateContext** fails with a return value of STATUS_FLT_CONTEXT_ALLOCATION_NOT_FOUND.

On success, [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext) initializes the reference count on the new context to one. When the context is no longer needed, the minifilter driver must release this reference. Thus, every call to **FltAllocateContext** must be matched by a subsequent call to [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext).

Once a context is created, a minifilter can [set it for an object](setting-contexts.md).
