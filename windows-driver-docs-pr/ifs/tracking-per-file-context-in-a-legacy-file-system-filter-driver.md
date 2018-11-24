---
title: Tracking Per-File Context in a Legacy File System Filter Driver
description: Tracking Per-File Context in a Legacy File System Filter Driver
ms.assetid: 6be3ff10-47e4-47f5-8f15-88a80a16f451
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tracking Per-File Context in a Legacy File System Filter Driver


<div class="alert">
<strong>Note</strong>   For optimal reliability and performance, we recommend using <a href="filter-manager-and-minifilter-driver-architecture.md" data-raw-source="[file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md)">file system minifilter drivers</a> instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see <a href="advantages-of-the-filter-manager-model.md" data-raw-source="[Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md)">Advantages of the Filter Manager Model</a>. To port your legacy driver to a minifilter driver, see <a href="guidelines-for-porting-legacy-filter-drivers.md" data-raw-source="[Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md)">Guidelines for Porting Legacy Filter Drivers</a>.
</div>
 

A legacy file system filter driver can record context information for a file by associating a [**FSRTL\_PER\_FILE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff547352) object with a user-defined context information structure.

<div class="alert">
<strong>Note</strong>   Not all file systems support per-file context objects. To find out whether a file is associated with a file system that supports them, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547274" data-raw-source="[**FsRtlSupportsPerFileContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547274)"><strong>FsRtlSupportsPerFileContexts</strong></a> macro.
</div>
 

Use the [**FsRtlInitPerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff546161) macro to initialize the FSRTL\_PER\_FILE\_CONTEXT object. Then use the [**FsRtlInsertPerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff546184) routine to associate the file with an arbitrary context object.

Use the [**FsRtlGetPerFileContextPointer**](https://msdn.microsoft.com/library/windows/hardware/ff546051) macro to get a pointer that is used by the file system runtime library (FSRTL) package to track file contexts.

A filter driver can use the [**FsRtlLookupPerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff546930) routine to find a file context object that is associated with a file. The routine can specify the owner of a structure or an instance of a structure to narrow the search.

The filter driver can remove a context object by using [**FsRtlRemovePerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff547226). The routine can specify the owner of a structure or an instance of a structure to narrow the search.

<div class="alert">
<strong>Note</strong>   Only use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547226" data-raw-source="[**FsRtlRemovePerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff547226)"><strong>FsRtlRemovePerFileContext</strong></a> routine to remove context objects while the file is still open. Do not confuse it with <a href="https://msdn.microsoft.com/library/windows/hardware/ff547290" data-raw-source="[**FsRtlTeardownPerFileContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547290)"><strong>FsRtlTeardownPerFileContexts</strong></a>.
</div>
 

File systems call [**FsRtlTeardownPerFileContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547290) to free any filter contexts that are still associated with a per-file control block structure (FCB) that they are tearing down. The **FsRtlTeardownPerFileContexts** routine calls the [**FreeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551123) routine that is specified in the FSRTL\_PER\_FILE\_CONTEXT object for each filter context.

 

 




