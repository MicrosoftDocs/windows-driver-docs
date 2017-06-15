---
title: Access Rights
author: windows-driver-content
description: Access Rights
MS-HAID:
- 'Objects\_c26d43e6-f24e-4004-a6f5-0bab30bf71bf.xml'
- 'kernel.access\_rights'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 518e60db-7058-4ebe-8640-eb8f6b9e7645
keywords: ["access rights WDK objects", "generic access rights WDK objects", "standard access rights WDK objects", "specific access rights WDK objects", "object access rights WDK kernel"]
---

# Access Rights


An *access right* is the right to perform a particular operation on the object. For example, the FILE\_READ\_DATA access right specifies the right to read from a file.

When you open a handle to an object, you specify a set of access rights corresponding to the operations that may be performed on the object. The system checks the specified access rights against the object's security descriptor to see if each operation is permitted for the current user. (For more information, see [Security Descriptors](https://msdn.microsoft.com/library/windows/hardware/ff556612).)

Access rights come in two types:

A *specific* access right is a right to perform a single operation. Specific access rights can depend on the type of object.

A *generic* access right is a right to perform one of a set of similar operations. Generic access rights are independent of the type of object.

*Standard access rights* are specific access rights that apply to all types of objects. For example, the DELETE access right is the right to delete an object, regardless of type. For more information about the available standard access rights, see [**ACCESS\_MASK**](access-mask.md).

Objects also have specific access rights that depend on the type of the object. For example, the FILE\_READ\_DATA represents the right to read from a file, while the KEY\_QUERY\_VALUE represents the right to read the value entries for a registry key.

An object type can have zero, one, or more access rights that correspond to the general notion of reading from or writing to an object. For example, in addition to FILE\_READ\_DATA, file objects have the FILE\_READ\_ATTRIBUTES access right, which represents to read a file's metadata (such as file creation time). Key objects have both KEY\_QUERY\_VALUE and KEY\_ENUMERATE\_SUBKEYS, which represents the right to read the subkeys of a key.

To simplify specifying all access rights that correspond to a general notion such as reading or writing, the system provides generic access rights. The system maps a generic access right to the appropriate set of specific access rights for the object.

The system provides the following generic access rights:

-   GENERIC\_READ

-   GENERIC\_WRITE

-   GENERIC\_EXECUTE

-   GENERIC\_ALL

Thus, the system maps GENERIC\_READ to a set of rights that includes FILE\_READ\_DATA and FILE\_READ\_ATTRIBUTES for a file, and KEY\_QUERY\_VALUE and KEY\_ENUMERATE\_SUBKEYS for a key. For more information about each generic access right, see [**ACCESS\_MASK**](access-mask.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Access%20Rights%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


