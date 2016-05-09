---
title: The FCB Structure
author: windows-driver-content
description: The FCB Structure
ms.assetid: feb38b24-c028-4c8d-be45-11d9a4659f8d
keywords: ["file control block structure WDK RDBSS", "FCB WDK RDBSS", "data structures WDK file systems", "RDBSS WDK file systems , connection and file structures", "Redirected Drive Buffering Subsystem WDK file systems , connection and file structures", "connection structures WDK RDBSS", "file structures WDK RDBSS", "structures WDK RDBSS", "connection information WDK RDBSS"]
---

# The FCB Structure


## <span id="ddk_the_fcb_structure_if"></span><span id="DDK_THE_FCB_STRUCTURE_IF"></span>


The file control block (FCB) structure is pointed to by the *FsContext* field in the file object. All of the operations that share an FCB refer to the same file. Unfortunately, SMB servers are implemented today in such a way that a name can be an alias, so that two different names could be the same file. The FCB is the focal point of file operations. Since operations on the same FCB are actually on the same file, synchronization is based on the FCB rather than some higher level object.

Whenever an FCB structure is created, a corresponding SRV\_OPEN and FOBX structure is also created. More than one SRV\_OPEN structure can be associated with a given FCB structure, and more than one FOBX structure is associated with a given SRV\_OPEN structure. In most cases, the one SRV\_OPEN structure is associated with an FCB, and the number of FOBX structures associated with a given SRV\_OPEN structure is 1. To improve the spatial locality and the paging behavior in such cases, the allocation for an FCB structure also involves an allocation for one associated SRV\_OPEN and FOBX structure.

RDBSS tries to allocate the associated FCB, SRV\_OPEN, and FOBX structures together in memory to improve paging behavior. RDBSS does not allocate the FCB and NET\_ROOT structures together because the NET\_ROOT structures are not paged, but FCB structures usually are paged (unless they are paging files).

The FCB structure corresponds to every open file and directory. The FCB structure is split up into the following two portions:

-   A non-paged part allocated in non-paged pool

-   A paged part

The former is the NON\_PAGED\_FCB and the later is referred to as FCB.

The FCB contains a pointer to the corresponding NON\_PAGED\_FCB part. A backpointer is maintained from the NON\_PAGED\_FCB to the FCB for debugging purposes in checked builds.

The NON\_PAGED\_FCB contains a structure of special pointers used by Memory Manager and Cache Manager to manipulate section objects. Note that the values for these pointers are normally set outside of the file system.

An FCB structure contains the following:

-   An FSRTL\_COMMON\_HEADER structure

-   A signature and reference count

-   A name and associated table information

-   A backpointer to the associated NET\_ROOT structure

-   A list of associated SRV\_OPEN structures

-   The device object

-   Any additional storage requested by the network mini-redirector or the creator of the FCB structure

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20The%20FCB%20Structure%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


