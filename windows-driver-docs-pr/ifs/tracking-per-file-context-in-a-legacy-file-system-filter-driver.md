---
title: Tracking Per-File Context in a Legacy File System Filter Driver
description: Tracking Per-File Context in a Legacy File System Filter Driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tracking Per-File Context in a Legacy File System Filter Driver

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

A legacy file system filter driver can record context information for a file by associating a [**FSRTL_PER_FILE_CONTEXT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsrtl_per_file_context) object with a user-defined context information structure.

> [!NOTE]
> Not all file systems support per-file context objects. To find out whether a file is associated with a file system that supports them, use the [**FsRtlSupportsPerFileContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlsupportsperfilecontexts) macro.

Use the [**FsRtlInitPerFileContext**](/previous-versions/ff546161(v=vs.85)) macro to initialize the FSRTL_PER_FILE_CONTEXT object. Then use the [**FsRtlInsertPerFileContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlinsertperfilecontext) routine to associate the file with an arbitrary context object.

Use the [**FsRtlGetPerFileContextPointer**](/previous-versions/ff546051(v=vs.85)) macro to get a pointer that is used by the file system runtime library (FSRTL) package to track file contexts.

A filter driver can use the [**FsRtlLookupPerFileContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtllookupperfilecontext) routine to find a file context object that is associated with a file. The routine can specify the owner of a structure or an instance of a structure to narrow the search.

The filter driver can remove a context object by using [**FsRtlRemovePerFileContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlremoveperfilecontext). The routine can specify the owner of a structure or an instance of a structure to narrow the search.

> [!NOTE]
> Only use the [**FsRtlRemovePerFileContext**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlremoveperfilecontext) routine to remove context objects while the file is still open. Do not confuse it with [**FsRtlTeardownPerFileContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperfilecontexts).

File systems call [**FsRtlTeardownPerFileContexts**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperfilecontexts) to free any filter contexts that are still associated with a per-file control block structure (FCB) that they are tearing down. The **FsRtlTeardownPerFileContexts** routine calls the [**FreeCallback**](./pfree-function.md) routine that is specified in the FSRTL_PER_FILE_CONTEXT object for each filter context.
