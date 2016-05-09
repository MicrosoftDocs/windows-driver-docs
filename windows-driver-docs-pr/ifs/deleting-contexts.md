---
title: Deleting Contexts
description: Deleting Contexts
ms.assetid: 43a30a75-4344-4fc5-ad57-28b48c2e54a8
keywords: ["contexts WDK file system minifilter , deleting", "deleting contexts"]
---

# Deleting Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


Every context that is set by a successful call to **FltSet***Xxx***Context** must eventually be deleted. However, the filter manager deletes contexts automatically when the objects that they are attached to are deleted, when a minifilter driver instance is detached from a volume, or when the minifilter driver is unloaded. Thus, it is rarely necessary for a minifilter driver to explicitly delete a context.

A minifilter driver can delete a context by calling **FltDelete***Xxx***Context**, where *Xxx* is the context type, or by calling [**FltDeleteContext**](https://msdn.microsoft.com/library/windows/hardware/ff541960).

A context can be deleted only if it is currently set for an object. A context cannot be deleted if it has not yet been set, or if it has already been replaced by a successful call to **FltSet***Xxx***Context**.

In the call to **FltDelete***Xxx***Context**, the old context is returned in the *OldContext* parameter, if it is non-**NULL**. If the *OldContext* parameter is **NULL**, the filter manager decrements the reference count on the context, which is then freed unless the minifilter driver has an outstanding reference on it.

The following code example shows how to delete a stream context:

```
status = FltDeleteStreamContext(
 FltObjects->Instance,      //Instance
 FltObjects->FileObject,    //FileObject
           &amp;oldContext);              //OldContext
...
if (oldContext != NULL) {
 FltReleaseContext(oldContext);
}
```

In this example, [**FltDeleteStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff541997) removes the stream context from the stream, but it does not decrement the context's reference count, because the *OldContext* parameter is non-**NULL**. **FltDeleteStreamContext** returns the address of the deleted context in the *OldContext* parameter. After performing any needed processing, the caller must release the deleted context by calling **FltReleaseContext**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Deleting%20Contexts%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




