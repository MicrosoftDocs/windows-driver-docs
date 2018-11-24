---
title: Deleting Contexts
description: Deleting Contexts
ms.assetid: 43a30a75-4344-4fc5-ad57-28b48c2e54a8
keywords:
- contexts WDK file system minifilter , deleting
- deleting contexts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deleting Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


Every context that is set by a successful call to **FltSet***Xxx***Context** must eventually be deleted. However, the filter manager deletes contexts automatically when the objects that they are attached to are deleted, when a minifilter driver instance is detached from a volume, or when the minifilter driver is unloaded. Thus, it is rarely necessary for a minifilter driver to explicitly delete a context.

A minifilter driver can delete a context by calling **FltDelete***Xxx***Context**, where *Xxx* is the context type, or by calling [**FltDeleteContext**](https://msdn.microsoft.com/library/windows/hardware/ff541960).

A context can be deleted only if it is currently set for an object. A context cannot be deleted if it has not yet been set, or if it has already been replaced by a successful call to **FltSet***Xxx***Context**.

In the call to **FltDelete***Xxx***Context**, the old context is returned in the *OldContext* parameter, if it is non-**NULL**. If the *OldContext* parameter is **NULL**, the filter manager decrements the reference count on the context, which is then freed unless the minifilter driver has an outstanding reference on it.

The following code example shows how to delete a stream context:

```cpp
status = FltDeleteStreamContext(
 FltObjects->Instance,      //Instance
 FltObjects->FileObject,    //FileObject
           &oldContext);              //OldContext
...
if (oldContext != NULL) {
 FltReleaseContext(oldContext);
}
```

In this example, [**FltDeleteStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff541997) removes the stream context from the stream, but it does not decrement the context's reference count, because the *OldContext* parameter is non-**NULL**. **FltDeleteStreamContext** returns the address of the deleted context in the *OldContext* parameter. After performing any needed processing, the caller must release the deleted context by calling **FltReleaseContext**.

 

 




