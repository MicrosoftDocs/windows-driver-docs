---
title: Access Mask
description: Access Mask
keywords:
- security descriptors WDK file systems , access masks
- descriptors WDK file systems , access masks
- access masks WDK file systems
- generic rights WDK file systems
- standard rights WDK file systems
- specific rights WDK file systems
ms.date: 09/05/2024
---

# Access Mask

The function of the access mask is to describe access rights in a compact form. To simplify access management, the access mask contains a set of four bits, the *generic rights*, which are translated into a set of more detailed rights by using the function [**RtlMapGenericMask**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlmapgenericmask).

The following figure illustrates the access mask.

:::image type="content" source="images/fssecurity-03.png" alt-text="Diagram illustrating the access mask.":::

The generic rights are:

- GENERIC_READ—the right to read the information maintained by the object.

- GENERIC_WRITE—the right to write the information maintained by the object.

- GENERIC_EXECUTE—the right to execute or alternatively look into the object.

- GENERIC_ALL—the right to read, write, and execute the object.

These rights can be combined. For example, GENERIC_READ and GENERIC_WRITE can both be requested. The resultant mapping requires the union of the rights needed for each generic right. This paradigm mimics UNIX "rwx" access bits that are used to control access to UNIX resources. The generic rights in the access mask simplify application development on Windows since these rights mask the different security rights for various object types.

The following set of *standard rights* are applicable to all object types:

- DELETE—the right to delete the particular object.

- READ_CONTROL—the right to read the control (security) information for the object.

- WRITE_DAC—the right to modify the control (security) information for the object.

- WRITE_OWNER—the right to modify the owner SID of the object. Recall that owners always have the right to modify the object.

- SYNCHRONIZE—the right to wait on the given object (assuming that waiting is a valid concept for the object).

The lower 16 bits of the access mask represent the specific rights. The meaning of these specific rights is unique to the object in question. For file systems, the primary interests are the specific rights for file objects. For file objects, specific rights are normally interpreted differently, depending upon whether the file object represents a file or a directory. For files, the normal interpretation is:

- **FILE_READ_DATA**—the right to read data from the given file.

- **FILE_WRITE_DATA**—the right to write data to the given file (within the existing range of the file).

- **FILE_APPEND_DATA**—the right to extend the given file.

- **FILE_READ_EA**—the right to read the extended attributes of the file.

- **FILE_WRITE_EA**—the right to modify the extended attributes of the file.

- **FILE_EXECUTE**—the right to locally execute the given file. Executing a file stored on a remote share requires read permission, since the file is read from the server, but executed on the client.

- **FILE_READ_ATTRIBUTES**—the right to read the file's attribute information.

- **FILE_WRITE_ATTRIBUTES**—the right to modify the file's attribute information.

For directories, the same bit values are used, but their interpretation is different in some of the following cases:

- **FILE_LIST_DIRECTORY**—the right to list the contents of the directory.

- **FILE_ADD_FILE**—the right to create a new file within the directory.

- **FILE_ADD_SUBDIRECTORY**—the right to create a new directory (subdirectory) within the directory.

- **FILE_READ_EA**—the right to read the extended attributes of the given directory.

- **FILE_WRITE_EA**—the right to write the extended attributes of the given directory.

- **FILE_TRAVERSE**—the right to access objects within the directory. The FILE_TRAVERSE access right is different than the FILE_LIST_DIRECTORY access right. Holding the FILE_LIST_DIRECTORY access right allows an entity to obtain a list of the contents of a directory, while the FILE_TRAVERSE access right gives an entity the right to access the object. A caller without the FILE_LIST_DIRECTORY access right could open a file that it knew already existed, but wouldn't be able to obtain a list of the contents of the directory.

- **FILE_DELETE_CHILD**—the right to delete a file or directory within the current directory.

- **FILE_READ_ATTRIBUTES**—the right to read a directory's attribute information.

- **FILE_WRITE_ATTRIBUTES**—the right to modify a directory's attribute information.

The I/O Manager defines the actual mapping of generic rights to standard and specific rights for file objects. A file system can retrieve this mapping using [**IoGetFileObjectGenericMapping**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iogetfileobjectgenericmapping). Normally, the I/O Manager does this mapping during IRP_MJ_CREATE processing before calling the file system. But a file system checking security on specific operations (specialized FSCTL operations, for example)  might need to do this mapping itself.
