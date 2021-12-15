---
title: Supporting minifilter contexts
description: Filter manager provides support for minifilter contexts
keywords:
- filter manager WDK file system minifilter , contexts
- file system minifilter drivers WDK , contexts
- minifilter drivers WDK , context
- contexts WDK file system minifilter
ms.date: 01/22/2021
---

# Supporting minifilter contexts

The filter manager provides support that allows minifilter drivers to associate contexts with objects to preserve state across I/O operations. Objects that can have contexts include files, volumes, instances, streams, stream handles, and transactions. See [About minifilter contexts](managing-contexts-in-a-minifilter-driver.md) for minifilter implementation details.

Third-party file systems must use the [**FSRTL_ADVANCED_FCB_HEADER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsrtl_advanced_fcb_header) structure (instead of the [**FSRTL_COMMON_FCB_HEADER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsrtl_common_fcb_header) structure) to work properly with stream and stream handle contexts.

Contexts can be allocated from paged or nonpaged pool except for volume contexts, which must be allocated from nonpaged pool.

Contexts are freed automatically when all outstanding references have been released. If the minifilter driver defines a [context cleanup callback routine](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_context_cleanup_callback), the filter manager calls the routine before the context is freed.

The filter manager takes care of deleting contexts when the associated object is deleted, when an instance is detached, and when the minifilter driver is unloaded.

Contexts are not supported for paging files or during the following operations:

- Preoperation processing for create requests

- Postoperation processing for close requests

- Processing of IRP_MJ_NETWORK_QUERY_OPEN requests

See the [CTX sample](https://github.com/microsoft/Windows-driver-samples/tree/master/filesys/miniFilter/ctx) for an example of a minifilter driver that uses contexts.

## Filter manager support routines for context management

The filter manager provides many support context support routines for minifilters:

- Creating and registering contexts:

  - [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext)
  - [**FltRegisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltregisterfilter)

- Setting contexts:

  - [**FltSetFileContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetfilecontext)
  - [**FltSetInstanceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetinstancecontext)
  - [**FltSetStreamContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetstreamcontext)
  - [**FltSetStreamHandleContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetstreamhandlecontext)
  - [**FltSetTransactionContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsettransactioncontext)
  - [**FltSetVolumeContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsetvolumecontext)

- Querying contexts:

  - [**FltSupportsStreamContexts**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsupportsstreamcontexts)
  - [**FltSupportsStreamHandleContexts**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsupportsstreamhandlecontexts)

- Getting and referencing contexts:

  - [**FltGetContexts**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetcontexts)
  - [**FltGetContextsEx**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetcontextsex)
  - [**FltGetFileContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetfilecontext)
  - [**FltGetInstanceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetinstancecontext)
  - [**FltGetSectionContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetsectioncontext)
  - [**FltGetStreamContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetstreamcontext)
  - [**FltGetStreamHandleContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetstreamhandlecontext)
  - [**FltGetTransactionContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgettransactioncontext)
  - [**FltGetVolumeContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetvolumecontext)
  - [**FltReferenceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreferencecontext)

- Releasing and deleting contexts:

  - [**FltDeleteContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletecontext)
  - [**FltDeleteFileContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletefilecontext)
  - [**FltDeleteInstanceContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeleteinstancecontext)
  - [**FltDeleteStreamContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletestreamcontext)
  - [**FltDeleteStreamHandleContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletestreamhandlecontext)
  - [**FltDeleteTransactionContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletetransactioncontext)
  - [**FltDeleteVolumeContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdeletevolumecontext)
  - [**FltReleaseContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontext)
  - [**FltReleaseContexts**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontexts)
  - [**FltReleaseContextsEx**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasecontextsex)
