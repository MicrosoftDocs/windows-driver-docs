---
title: Access Mask
author: windows-driver-content
description: Access Mask
ms.assetid: eb379196-7a10-4d52-8b81-825550ebbbb0
keywords: ["security descriptors WDK file systems , access masks", "descriptors WDK file systems , access masks", "access masks WDK file systems", "generic rights WDK file systems", "standard rights WDK file systems", "specific rights WDK file systems"]
---

# Access Mask


## <span id="ddk_sec_access_mask_if"></span><span id="DDK_SEC_ACCESS_MASK_IF"></span>


The function of the access mask is to describe access rights in a compact form. To simplify access management, the access mask contains a set of four bits, the *generic rights*, which are translated into a set of more detailed rights by using the function [**RtlMapGenericMask**](https://msdn.microsoft.com/library/windows/hardware/ff562027).

The following figure illustrates the access mask.

![diagram illustrating the access mask](images/fssecurity-03.png)

The generic rights are one of the following:

-   GENERIC\_READ—the right to read the information maintained by the object.

-   GENERIC\_WRITE—the right to write the information maintained by the object.

-   GENERIC\_EXECUTE—the right to execute or alternatively look into the object.

-   GENERIC\_ALL—the right to read, write, and execute the object.

Note that these rights can be combined (GENERIC\_READ and GENERIC\_WRITE can both be requested, for example) with the resulting mapping requiring the union of the rights needed for each generic right. This paradigm mimics UNIX "rwx" access bits that are used to control access to UNIX resources. The generic rights in the access mask simplify application development on Windows since these rights mask the different security rights for various object types.

The following set of *standard rights* are applicable to all object types:

-   DELETE—the right to delete the particular object.

-   READ\_CONTROL—the right to read the control (security) information for the object.

-   WRITE\_DAC—the right to modify the control (security) information for the object.

-   WRITE\_OWNER—the right to modify the owner SID of the object. Recall that owners always have the right to modify the object.

-   SYNCHRONIZE—the right to wait on the given object (assuming that this is a valid concept for the object).

The lower 16 bits of the access mask represent the specific rights. The meaning of these specific rights is unique to the object in question. For file systems, the primary interests are the specific rights for file objects. For file objects, specific rights are normally interpreted differently, depending upon whether the file object represents a file or a directory. For files, the normal interpretation is:

-   **FILE\_READ\_DATA**—the right to read data from the given file.

-   **FILE\_WRITE\_DATA**—the right to write data to the given file (within the existing range of the file).

-   **FILE\_APPEND\_DATA**—the right to extend the given file.

-   **FILE\_READ\_EA**—the right to read the extended attributes of the file.

-   **FILE\_WRITE\_EA**—the right to modify the extended attributes of the file.

-   **FILE\_EXECUTE**—the right to locally execute the given file. Executing a file stored on a remote share requires read permission, since the file is read from the server, but executed on the client.

-   **FILE\_READ\_ATTRIBUTES**—the right to read the file's attribute information.

-   **FILE\_WRITE\_ATTRIBUTES**—the right to modify the file's attribute information.

For directories, the same bit values are used, but their interpretation is different in some of the following cases:

-   **FILE\_LIST\_DIRECTORY**—the right to list the contents of the directory.

-   **FILE\_ADD\_FILE**—the right to create a new file within the directory.

-   **FILE\_ADD\_SUBDIRECTORY**—the right to create a new directory (subdirectory) within the directory.

-   **FILE\_READ\_EA**—the right to read the extended attributes of the given directory.

-   **FILE\_WRITE\_EA**—the right to write the extended attributes of the given directory.

-   **FILE\_TRAVERSE**—the right to access objects within the directory. The FILE\_TRAVERSE access right is different than the FILE\_LIST\_DIRECTORY access right. Holding the FILE\_LIST\_DIRECTORY access right allows an entity to obtain a list of the contents of a directory, while the FILE\_TRAVERSE access right gives an entity the right to access the object. A caller without the FILE\_LIST\_DIRECTORY access right could open a file that it knew already existed, but would not be able to obtain a list of the contents of the directory.

-   **FILE\_DELETE\_CHILD**—the right to delete a file or directory within the current directory.

-   **FILE\_READ\_ATTRIBUTES**—the right to read a directory's attribute information.

-   **FILE\_WRITE\_ATTRIBUTES**—the right to modify a directory's attribute information.

The actual mapping of generic rights to standard and specific rights for file objects is defined by the I/O manager. This mapping can be retrieved by a file system using [**IoGetFileObjectGenericMapping**](https://msdn.microsoft.com/library/windows/hardware/ff549231). Normally, this mapping is done during IRP\_MJ\_CREATE processing by the I/O manager prior to calling the file system. But this might be done by a file system checking security on specific operations (specialized FSCTL operations, for example).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Access%20Mask%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


