---
title: Setting Contexts
description: Setting Contexts
keywords:
- contexts WDK file system minifilter , setting
- attaching contexts
ms.date: 01/22/2021
---

# Setting Contexts

After [creating a new context](creating-contexts.md), a minifilter driver can attach it to an object by calling one of the following set routines:

- [**FltSetFileContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetfilecontext)
- [**FltSetInstanceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetinstancecontext)
- [**FltSetStreamContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetstreamcontext)
- [**FltSetStreamHandleContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetstreamhandlecontext)
- [**FltSetTransactionContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsettransactioncontext)
- [**FltSetVolumeContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetvolumecontext)

The set routine does the following, depending on the value of the *Operation* parameter:

- If **Operation** == **FLT_SET_CONTEXT_KEEP_IF_EXISTS**:
  - If the minifilter has not already set a context of the same type for the object, the set routine:
    - Attaches the newly allocated context to the object.
    - Increments the reference count.
  - Else if the minifilter has already set a context, the set routine:
    - Returns STATUS_FLT_CONTEXT_ALREADY_DEFINED (an NTSTATUS error code).
    - Does not replace the existing context.
    - Does not increment the reference count.
    - Stores a pointer to the existing context in the *OldContext* parameter if it is non-**NULL**. When this pointer is no longer needed, the minifilter driver must release it by calling [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext).

- If **Operation** == **FLT_SET_CONTEXT_REPLACE_IF_EXISTS**:
  - The set routine always attaches the new context to the object.
  - If the minifilter driver has already set a context, the set routine:
    - Deletes the existing context, sets the new context, and increments the reference count on the new context.
    - If the *OldContext* parameter is non-**NULL**, it receives a pointer to the deleted context. When this pointer is no longer needed, the minifilter driver must release it by calling **FltReleaseContext**.

Once a context type has been set, a minifilter can [get a context](getting-contexts.md) during subsequent I/O operation(s) to determine whether it needs to take any action.

Every successful context set must eventually be [deleted](deleting-contexts.md).

In the following code example, taken from the [CTX sample minifilter](https://github.com/Microsoft/Windows-driver-samples/tree/main/filesys/miniFilter/ctx), the **CtxInstanceSetup** routine creates and sets an instance context:

```cpp
status = FltAllocateContext(
           FltObjects->Filter,              //in: Filter
           FLT_INSTANCE_CONTEXT,            //in: ContextType
           CTX_INSTANCE_CONTEXT_SIZE,       //in: ContextSize
           NonPagedPool,                    //in: PoolType
           &instanceContext);               //out: ReturnedContext
...
status = FltSetInstanceContext(
           FltObjects->Instance,            //in: Instance
           FLT_SET_CONTEXT_KEEP_IF_EXISTS,  //in: Operation
           instanceContext,                 //in: NewContext
           NULL);                           //out: OldContext

if (instanceContext != NULL) {
  FltReleaseContext(instanceContext);
}
return status;
```

Note that after the call to [**FltSetInstanceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetinstancecontext), there is a call to **FltReleaseContext** to release the reference count that was set by [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext) (*not* **FltSetInstanceContext**). This is explained in [Releasing Contexts](releasing-contexts.md).
