---
title: File Streams, Stream Contexts, and Per-Stream Contexts
description: File Streams, Stream Contexts, and Per-Stream Contexts
keywords:
- filter drivers WDK file system , per-stream context tracking
- file system filter drivers WDK , per-stream context tracking
- per-stream context tracking WDK file system
- tracking per-stream context WDK file system
- file streams WDK
- stream control blocks WDK file system
- SCB WDK file system
- stream context WDK file system
ms.date: 02/23/2023
---

# File Streams, Stream Contexts, and Per-Stream Contexts

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

A *file stream* is a sequence of bytes used to hold file data. Usually a file has only one file stream, namely the file's default data stream. However, on file systems that support multiple data streams, each file can have multiple file streams. One of these streams is the default data stream, which is unnamed. The others are named alternate data streams. When you open a file, you're actually opening a stream of the given file.

When a file system opens a file stream for the first time, it creates a file-system-specific *stream context* structure, such as a file control block (FCB) or stream control block (SCB), and stores the address of this structure in the **FsContext** member of the resulting file object.

For local file systems, if the already opened file stream is opened again (for shared read access, for example), the I/O subsystem creates another file object, but the file system doesn't create a new stream context. Both file objects receive the address of the same stream context structure. Thus, for local file systems, the stream context pointer uniquely identifies a file stream.

For network file systems that support per-stream contexts, the behavior is the same as for local file systems if the already opened file stream is opened again using the same network share name or IP address. The I/O subsystem creates a new file object, but the file system doesn't create a new stream context. Instead, it assigns the same **FsContext** pointer value to both file objects. However, if the file stream is opened using a different path (for example, a different share name, or an IP address for a file previously opened using a share name), the file system does create a new stream context. Thus, for network file systems that support per-stream contexts, the **FsContext** pointer doesn't uniquely identify a file stream.

A *per-stream context* is a filter-defined structure that contains a [**FSRTL_PER_STREAM_CONTEXT**](/previous-versions/ff547357(v=vs.85)) structure as one of its members. Filter drivers use this structure to track information about each file stream that the file system opens.

## File System Support for Per-Stream Contexts

On Windows XP and later, file systems that support per-stream contexts must use stream context structures that contain a [**FSRTL_ADVANCED_FCB_HEADER**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsrtl_advanced_fcb_header) structure.

The file system owns the global list of per-stream contexts associated with a particular file stream. When the file system creates a new stream context (FSRTL_ADVANCED_FCB_HEADER object) for a file stream, it calls [**FsRtlSetupAdvancedHeader**](/previous-versions/ff547257(v=vs.85)) to initialize this list. When a legacy file system filter driver calls [**FsRtlInsertPerStreamContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinsertperstreamcontext), the per-stream context created by the filter is added to the global list.

When the file system deletes its stream context for a file stream, it calls [**FsRtlTeardownPerStreamContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperstreamcontexts) to free all per-stream contexts that filters have associated with the file stream. This routine calls the [**FreeCallback**](/previous-versions/ff547357(v=vs.85)) routine for each per-stream context in the global list. The **FreeCallback** routine must assume that the file object for the file stream has already been freed.

To query whether the file system supports per-stream contexts for the file stream represented by a given file object, call [**FsRtlSupportsPerStreamContexts**](/previous-versions/ff547285(v=vs.85)) on the file object. A file system might support per-stream contexts for some types of files but not for others. For example, NTFS and FAT don't currently support per-stream contexts for paging files. Thus if **FsRtlSupportsPerStreamContexts** returns TRUE for one file stream, this doesn't imply that it returns TRUE for all file streams.
