---
title: Referencing Contexts
description: Referencing Contexts
keywords:
- contexts WDK file system minifilter , referencing
- referencing contexts
ms.date: 01/22/2021
ms.localizationpriority: medium
---

# Referencing Contexts

The filter manager uses reference counting to manage the lifetime of a minifilter context. A reference count is a number indicating the state of a context.

Whenever a context is successfully created, the reference count of the context is initialized to one (this is called the initial reference to the context).

Whenever a context is referenced, for example by a successful context [set](setting-contexts.md) or [get](getting-contexts.md), the reference count of the context is incremented by one.

When a context is no longer needed, its reference count must be decremented. A positive reference count means that the context is usable. When the reference count becomes zero, the context is unusable, and the filter manager eventually frees it.

The initial reference to the context is typically released when the object is torn down. However, if a minifilter must remove a context from an object, the minifilter must somehow release that initial reference to the context. To safely release that initial reference to the context, the minifilter driver calls [**FltDeleteContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletecontext).

A minifilter can add its own reference to a context by calling [**FltReferenceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreferencecontext) to increment the context's reference count. This added reference must eventually be removed by calling [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext).
