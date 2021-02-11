---
title: File System Support for Contexts
description: File System Support for Contexts
keywords:
- contexts WDK file system minifilter , file system support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File System Support for Contexts

To support file contexts (if applicable), stream contexts, and file object (stream handle) contexts, a file system must use the [**FSRTL_ADVANCED_FCB_HEADER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsrtl_advanced_fcb_header) structure. All Microsoft Windows file systems use this structure, and all third-party file system developers are strongly encouraged to do so as well. For more information, see [**FsRtlSetupAdvancedHeader**](/previous-versions/ff547257(v=vs.85)) and **FSRTL_ADVANCED_FCB_HEADER**.

The NTFS and FAT file systems do not support file, stream, or file object contexts on paging files, in the pre-create or post-close path, or for [**IRP_MJ_NETWORK_QUERY_OPEN**](./flt-parameters-for-irp-mj-network-query-open.md) operations.

A minifilter driver can determine whether a file system supports stream contexts and file object contexts for a given file object by calling [**FltSupportsStreamContexts**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsupportsstreamcontexts) and [**FltSupportsStreamHandleContexts**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsupportsstreamhandlecontexts), respectively.

File contexts are available on Windows Vista and later.

For file systems (such as FAT) that support only a single data stream per file, file contexts are equivalent to stream contexts. Such file systems usually support stream contexts but do not support file contexts. Instead, the filter manager provides this support, using the file system's existing support for stream contexts. For minifilter driver instances attached to these file systems, [**FltSupportsFileContexts**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsupportsfilecontexts) returns **FALSE**, while [**FltSupportsFileContextsEx**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltsupportsfilecontextsex) returns **TRUE** (when a valid non-**NULL** value is passed for the *Instance* parameter).

If a context type is not supported on a file, the minifilter cannot attach a context of that type to that file.

To support file contexts, a file system must:

* Embed a **FileContextSupportPointer** member of type PVOID in its file context structure, usually the file context block (FCB). The file system must initialize this member to **NULL**.

* Use **FsRtlSetupAdvancedHeaderEx** (instead of [**FsRtlSetupAdvancedHeader**](/previous-versions/ff547257(v=vs.85))) to initialize its stream context structure, passing a valid pointer to the **FileContextSupportPointer** member (embedded in the corresponding file context structure) for the *FileContextSupportPointer* parameter. For more information, see **FsRtlSetupAdvancedHeaderEx** and [**FSRTL_ADVANCED_FCB_HEADER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsrtl_advanced_fcb_header).

* Call **FsRtlTeardownPerFileContexts** to free all file context structures that filter and minifilter drivers have associated with a file when the file system deletes its file context structure for the file.
