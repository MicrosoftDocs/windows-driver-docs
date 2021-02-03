---
title: Releasing Contexts
description: Releasing Contexts
keywords:
- contexts WDK file system minifilter , releasing
- releasing contexts
ms.date: 01/22/2021
ms.localizationpriority: medium
---

# Releasing Contexts

A minifilter releases a context by calling [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext). Every successful call to one of the following routines must eventually be matched by a call to **FltReleaseContext**:

- Context creation routine:
  - [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext)

- Context get routines:
  - [**FltGetInstanceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetinstancecontext)
  - [**FltGetFileContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetfilecontext)
  - [**FltGetStreamContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetstreamcontext)
  - [**FltGetStreamHandleContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetstreamhandlecontext)
  - [**FltGetTransactionContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgettransactioncontext)
  - [**FltGetVolumeContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetvolumecontext)

- Context set routines:
  - [**FltSetFileContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetfilecontext)
  - [**FltSetInstanceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetinstancecontext)
  - [**FltSetStreamContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetstreamcontext)
  - [**FltSetStreamHandleContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetstreamhandlecontext)
  - [**FltSetTransactionContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsettransactioncontext)
  - [**FltSetVolumeContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetvolumecontext)

- Context reference increment routine:
  - [**FltReferenceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreferencecontext)

Note that the *OldContext* pointer returned by **FltSet***Xxx***Context** and the *Context* pointer returned by [**FltDeleteContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletecontext) must also be released when they are no longer needed.

In the following code example, taken from the [CTX sample minifilter](https://github.com/microsoft/Windows-driver-samples/tree/master/filesys/miniFilter/ctx), the **CtxInstanceSetup** routine creates and sets an instance context and then calls [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext):

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

Note that [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext) is called regardless of whether the call to [**FltSetInstanceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetinstancecontext) succeeds:

- If [**FltSetInstanceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetinstancecontext) succeeds, it adds its own reference to the instance context (that is, it increments the reference count on the instance context). Thus, the reference set by [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext) is no longer needed, and the call to [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext) removes it.

- If [**FltSetInstanceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetinstancecontext) fails, the instance context has only one reference, namely the one set by [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext). When [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext) returns, the instance context has a reference count of zero, and it is freed by the filter manager.
