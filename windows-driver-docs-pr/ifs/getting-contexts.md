---
title: Getting Contexts
description: Getting Contexts
keywords:
- contexts WDK file system minifilter , getting
ms.date: 01/22/2021
ms.localizationpriority: medium
---

# Getting Contexts

Once a minifilter driver has [set a context](setting-contexts.md) for an object, it can get the context by calling one of the following get routines:

- [**FltGetContexts**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetcontexts)
- [**FltGetContextsEx**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetcontextsex)
- [**FltGetFileContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetfilecontext)
- [**FltGetInstanceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetinstancecontext)
- [**FltGetStreamContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetstreamcontext)
- [**FltGetStreamHandleContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetstreamhandlecontext)
- [**FltGetTransactionContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgettransactioncontext)
- [**FltGetVolumeContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetvolumecontext)

Every successful get routine increments the reference count on the context, requiring that the minifilter call [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext) when it no longer needs the context pointer.

In the following code example, taken from the [SwapBuffers sample minifilter](https://github.com/microsoft/Windows-driver-samples/tree/master/filesys/miniFilter/swapBuffers), the minifilter driver calls [**FltGetVolumeContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetvolumecontext) to get a volume context:

```cpp
status = FltGetVolumeContext(
 FltObjects->Filter,    //Filter
 FltObjects->Volume,    //Volume
                &volCtx);              //Context
...
if (volCtx != NULL) {
 FltReleaseContext(volCtx);
}
```

If the call to [**FltGetVolumeContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetvolumecontext) is successful, the *Context* parameter receives the address of the caller's volume context. **FltGetVolumeContext** increments the reference count on the *Context* pointer. Thus, when this pointer is no longer needed, the minifilter driver must release it by calling [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext).
