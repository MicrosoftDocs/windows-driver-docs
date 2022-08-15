---
title: Referencing Contexts
description: Referencing Contexts
keywords:
- contexts WDK file system minifilter , referencing
- referencing contexts
ms.date: 10/25/2021
---

# Referencing Contexts

Filter Manager uses reference counting to manage the lifetime of a minifilter context. A reference count is a number indicating the state of a context.

Whenever a context is successfully created, FltMgr initializes the reference count of the context to one. This is called the *initial reference* to the context.

Whenever a context is referenced, for example by a successful context [set](setting-contexts.md) or [get](getting-contexts.md), FltMgr increments the reference count of the context by one.

When a context is no longer needed, its reference count must be decremented. A positive reference count means that the context is usable. When the reference count becomes zero, the context is unusable, and FltMgr eventually frees it.

FltMgr releases the initial reference to the context (decrements the reference count to zero) when the object is being torn down, and then calls the filter's optional [context cleanup callback](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_context_cleanup_callback). While this rarely occurs, if a minifilter must remove a context from an object before teardown, the minifilter must safely release that initial reference to the context by calling [**FltDeleteContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletecontext).

A minifilter can add its own reference to a context by calling [**FltReferenceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreferencecontext) to increment the context's reference count. The minifilter must eventually remove this added reference by calling [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext).

The following is a short example of reference count history for a typical object. Assume all Flt API calls succeed.

|Filter callback | Flt API called | Context reference count | Description |
| -------------- | -------------- | ----------------------- | ----------- |
| [*PreCreate*](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_pre_operation_callback)      | [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext)  | 1 | The filter is processing a pre-create and decides it might want to track the file. It allocates a stream context, which causes FltMgr to initialize the reference count to 1. The filter passes the context to its *PostCreate* callback via the **CompletionContext** parameter. |
| [*PostCreate*](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_post_operation_callback)     | [**FltSetStreamContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetstreamcontext) | 2 | The filter passed the context it allocated during *PreCreate* to its *PostCreate* callback. The create succeeded, so the filter attaches the context, which causes FltMgr to increment the reference count.|
| *PostCreate*     | [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext)   | 1 | Because **FltSetStreamContext** incremented the reference count, the filter needs to remove the extra count. The reference count is 1 after the filter releases the context, so the context stays alive. If the filter had decided it didn’t care about this file after all, it could have skipped calling **FltSetStreamContext** and simply called **FltReleaseContext**. In that case the count would have gone to 0, and the context would have been deallocated. |
| *PreRead*        | [**FltGetStreamContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetstreamcontext) | 2 | The filter sees a read I/O and wants to know if it is tracking this file. It requests its stream context and gets it, so it knows that it wants to track this file. FltMgr increments the reference count. |
| *PreRead*        | **FltReleaseContext**   | 1 | The filter is done using its context, so it releases it, causing the reference count to be decremented. Every **FltGet*Context** has to be balanced with a **FltReleaseContext**. |
| *PreCleanup*     | **FltGetStreamContext** | 2 | The filter requests and gets its context, which increments the reference count. |
| *PreCleanup*     | **FltReleaseContext**   | 1 | The filter is done using the context so releases it, which decrements the reference count. |
| [*Context cleanup callback*](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_context_cleanup_callback) |               | 0 | The file system is tearing down the underlying stream object. (In the specific case of a stream object, teardown is triggered by IRP_MJ_CLOSE). FltMgr decrements the reference count to 0 and then calls the filter's context cleanup callback. The filter now has an opportunity to clean up its context. |
