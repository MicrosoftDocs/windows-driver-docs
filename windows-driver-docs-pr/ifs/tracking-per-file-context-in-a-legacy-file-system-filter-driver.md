---
title: Tracking Per-File Context in a Legacy File System Filter Driver
description: Tracking Per-File Context in a Legacy File System Filter Driver
ms.assetid: 6be3ff10-47e4-47f5-8f15-88a80a16f451
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tracking Per-File Context in a Legacy File System Filter Driver

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](https://docs.microsoft.com/windows-hardware/drivers/ifs/filter-manager-concepts) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

A legacy file system filter driver can record context information for a file by associating a [**FSRTL_PER_FILE_CONTEXT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/ns-ntifs-_fsrtl_per_file_context) object with a user-defined context information structure.

> [!NOTE]
> Not all file systems support per-file context objects. To find out whether a file is associated with a file system that supports them, use the [**FsRtlSupportsPerFileContexts**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlsupportsperfilecontexts) macro.

Use the [**FsRtlInitPerFileContext**](https://docs.microsoft.com/previous-versions/ff546161(v=vs.85)) macro to initialize the FSRTL_PER_FILE_CONTEXT object. Then use the [**FsRtlInsertPerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff546184) routine to associate the file with an arbitrary context object.

Use the [**FsRtlGetPerFileContextPointer**](https://docs.microsoft.com/previous-versions/ff546051(v=vs.85)) macro to get a pointer that is used by the file system runtime library (FSRTL) package to track file contexts.

A filter driver can use the [**FsRtlLookupPerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff546930) routine to find a file context object that is associated with a file. The routine can specify the owner of a structure or an instance of a structure to narrow the search.

The filter driver can remove a context object by using [**FsRtlRemovePerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff547226). The routine can specify the owner of a structure or an instance of a structure to narrow the search.

> [!NOTE]
> Only use the [**FsRtlRemovePerFileContext**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlremoveperfilecontext) routine to remove context objects while the file is still open. Do not confuse it with [**FsRtlTeardownPerFileContexts**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperfilecontexts).

File systems call [**FsRtlTeardownPerFileContexts**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlteardownperfilecontexts) to free any filter contexts that are still associated with a per-file control block structure (FCB) that they are tearing down. The **FsRtlTeardownPerFileContexts** routine calls the [**FreeCallback**](https://docs.microsoft.com/windows-hardware/drivers/ifs/pfree-function) routine that is specified in the FSRTL_PER_FILE_CONTEXT object for each filter context.
