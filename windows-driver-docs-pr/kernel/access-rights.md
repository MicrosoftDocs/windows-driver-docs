---
title: Access Rights
description: Access Rights
ms.assetid: 518e60db-7058-4ebe-8640-eb8f6b9e7645
keywords: ["access rights WDK objects", "generic access rights WDK objects", "standard access rights WDK objects", "specific access rights WDK objects", "object access rights WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
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

 

 




