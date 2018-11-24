---
title: Referencing Contexts
description: Referencing Contexts
ms.assetid: 9ac3aedb-e057-4e19-9de5-709311072b09
keywords:
- contexts WDK file system minifilter , referencing
- referencing contexts
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Referencing Contexts


## <span id="ddk_registering_the_minifilter_if"></span><span id="DDK_REGISTERING_THE_MINIFILTER_IF"></span>


The filter manager uses reference counting to manage the lifetime of a minifilter driver context. A reference count is a number indicating the state of a context. Whenever a context is created, the reference count of the context is initialized to one (this is called the initial reference to the context). Whenever a context is referenced by a system component, the reference count of the context is incremented by one. When a context is no longer needed, its reference count is decremented. A positive reference count means that the context is usable. When the reference count becomes zero, the context is unusable, and the filter manager eventually frees it.

The initial reference to the context is typically released when the object is torn down. However, if a minifilter driver must remove a context from an object, the minifilter driver must somehow release that initial reference to the context. To safely release that initial reference to the context, the minifilter driver calls [**FltDeleteContext**](https://msdn.microsoft.com/library/windows/hardware/ff541960).

A minifilter driver can add its own reference to a context by calling [**FltReferenceContext**](https://msdn.microsoft.com/library/windows/hardware/ff544291) to increment the context's reference count. This added reference must eventually be removed by calling [**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314).

 

 




