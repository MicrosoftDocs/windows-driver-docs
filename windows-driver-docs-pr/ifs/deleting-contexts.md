---
title: Deleting Contexts
description: Deleting Contexts
keywords:
- contexts WDK file system minifilter , deleting
- deleting contexts
ms.date: 01/22/2021
ms.localizationpriority: medium
---

# Deleting Contexts

Every context that is [set](setting-contexts.md) by a successful call to **FltSet*Xxx*Context** must eventually be deleted.

The filter manager automatically deletes contexts when the following situations occur:

- The objects that the contexts are attached to are deleted
- A minifilter instance is detached from a volume
- The minifilter driver is unloaded

*Thus, it is rarely necessary for a minifilter to explicitly delete a context.*

A minifilter can delete a context by calling one of the following context delete routines:

- [**FltDeleteContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletecontext)
- [**FltDeleteFileContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletefilecontext)
- [**FltDeleteInstanceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeleteinstancecontext)
- [**FltDeleteStreamContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletestreamcontext)
- [**FltDeleteStreamHandleContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletestreamhandlecontext)
- [**FltDeleteTransactionContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletetransactioncontext)
- [**FltDeleteVolumeContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletevolumecontext)

A context can be deleted only if it is currently [set for an object](setting-contexts.md). A context cannot be deleted if it has not yet been set, or if it has already been replaced by a successful call to **FltSet*Xxx*Context**.

The **FltDelete*Xxx*Context** routines return a pointer to the old context in the *OldContext* parameter, if *OldContext* is non-**NULL** and does not point to NULL_CONTEXT. If *OldContext* is **NULL**, the filter manager decrements the reference count on the context, which is then freed unless the minifilter has an outstanding reference on it.

The following code example shows how to delete a stream context:

```cpp
status = FltDeleteStreamContext(
 FltObjects->Instance,      //Instance
 FltObjects->FileObject,    //FileObject
           &oldContext);              //OldContext
//
// Perform any needed processing
// ...
//
if (oldContext != NULL) {
 FltReleaseContext(oldContext);
}
```

In this example, [**FltDeleteStreamContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletestreamcontext):

- Removes the stream context from the stream.
- Does *not* decrement the context's reference count, because the *OldContext* parameter is non-NULL.
- Returns the address of the deleted context (the context removed from the stream) in the *OldContext* parameter.

Because of the non-NULL *OldContext* parameter, after performing any needed processing, the filter must release the deleted context by calling [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext).
