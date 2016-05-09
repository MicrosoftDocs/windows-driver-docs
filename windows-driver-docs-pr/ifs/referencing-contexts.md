---
title: Referencing Contexts
description: Referencing Contexts
ms.assetid: 9ac3aedb-e057-4e19-9de5-709311072b09
keywords: ["contexts WDK file system minifilter , referencing", "referencing contexts"]
---

# Referencing Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


The filter manager uses reference counting to manage the lifetime of a minifilter driver context. A reference count is a number indicating the state of a context. Whenever a context is created, the reference count of the context is initialized to one (this is called the initial reference to the context). Whenever a context is referenced by a system component, the reference count of the context is incremented by one. When a context is no longer needed, its reference count is decremented. A positive reference count means that the context is usable. When the reference count becomes zero, the context is unusable, and the filter manager eventually frees it.

The initial reference to the context is typically released when the object is torn down. However, if a minifilter driver must remove a context from an object, the minifilter driver must somehow release that initial reference to the context. To safely release that initial reference to the context, the minifilter driver calls [**FltDeleteContext**](https://msdn.microsoft.com/library/windows/hardware/ff541960).

A minifilter driver can add its own reference to a context by calling [**FltReferenceContext**](https://msdn.microsoft.com/library/windows/hardware/ff544291) to increment the context's reference count. This added reference must eventually be removed by calling [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Referencing%20Contexts%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




