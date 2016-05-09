---
title: Tracking Per-File Context in a Legacy File System Filter Driver
author: windows-driver-content
description: Tracking Per-File Context in a Legacy File System Filter Driver
ms.assetid: 6be3ff10-47e4-47f5-8f15-88a80a16f451
---

# Tracking Per-File Context in a Legacy File System Filter Driver


**Note**  For optimal reliability and performance, we recommend using [file system minifilter drivers](filter-manager-and-minifilter-driver-architecture.md) instead of legacy file system filter drivers. Also, legacy file system filter drivers can’t attach to direct access (DAX) volumes. For more about file system minifilter drivers, see [Advantages of the Filter Manager Model](advantages-of-the-filter-manager-model.md). To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

 

A legacy file system filter driver can record context information for a file by associating a [**FSRTL\_PER\_FILE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff547352) object with a user-defined context information structure.

**Note**   Not all file systems support per-file context objects. To find out whether a file is associated with a file system that supports them, use the [**FsRtlSupportsPerFileContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547274) macro.

 

Use the [**FsRtlInitPerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff546161) macro to initialize the FSRTL\_PER\_FILE\_CONTEXT object. Then use the [**FsRtlInsertPerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff546184) routine to associate the file with an arbitrary context object.

Use the [**FsRtlGetPerFileContextPointer**](https://msdn.microsoft.com/library/windows/hardware/ff546051) macro to get a pointer that is used by the file system runtime library (FSRTL) package to track file contexts.

A filter driver can use the [**FsRtlLookupPerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff546930) routine to find a file context object that is associated with a file. The routine can specify the owner of a structure or an instance of a structure to narrow the search.

The filter driver can remove a context object by using [**FsRtlRemovePerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff547226). The routine can specify the owner of a structure or an instance of a structure to narrow the search.

**Note**   Only use the [**FsRtlRemovePerFileContext**](https://msdn.microsoft.com/library/windows/hardware/ff547226) routine to remove context objects while the file is still open. Do not confuse it with [**FsRtlTeardownPerFileContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547290).

 

File systems call [**FsRtlTeardownPerFileContexts**](https://msdn.microsoft.com/library/windows/hardware/ff547290) to free any filter contexts that are still associated with a per-file control block structure (FCB) that they are tearing down. The **FsRtlTeardownPerFileContexts** routine calls the [**FreeCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551123) routine that is specified in the FSRTL\_PER\_FILE\_CONTEXT object for each filter context.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Tracking%20Per-File%20Context%20in%20a%20Legacy%20File%20System%20Filter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


