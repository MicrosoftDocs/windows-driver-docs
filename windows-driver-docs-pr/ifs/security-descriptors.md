---
title: Security Descriptors in File Systems
description: Describes file system support of security descriptors
keywords:
- security WDK file systems , descriptors
- security descriptors WDK file systems
- descriptors WDK file systems
- security descriptors WDK file systems , about security descriptors
- descriptors WDK file systems , about security descriptors
- storage WDK file systems
- offline security descriptor storage WDK file systems
ms.date: 09/05/2024
---

# Security descriptors in file systems

Windows file systems can support the storage and management of [security descriptors](../kernel/security-descriptors.md) associated with individual storage units within the file system. The granularity of security control is entirely up to the file system. For example:

- One file system might maintain a single security descriptor that covers everything on a given storage volume
- A different file system might provide security descriptors that cover different parts of a single given file.

The models that most developers are comfortable with are the models provided by the existing Windows file systems:

- NTFS supports a per file (or directory) security descriptor model. NTFS is efficient in its storage of security descriptors, storing only a single copy of each security descriptor, even if it's used by many different files.

- FAT, CDFS, UDFS don't support security descriptors.

- RDBSS and the SMB Network Redirector provide support comparable to the support provided by the remote volume.

These file systems, however, don't represent all possible implementations of Windows security for file systems.

A Windows security descriptor consists of four distinct pieces:

- The security identifier (SID) of the owner of the object. An object's owner always has the ability to reset the security on the object. This ability ensures that, for example, all access to an object can be removed. Because even if owners remove their ability to perform all operations, this inherent right allows them to restore their security rights on the object.

- An optional security identifier (SID) of the default group of the object. The concept of group ownership is one that isn't required in Windows, but is useful for some applications.

- The system access control list (SACL) that describes the auditing policy of the security descriptor.

- The discretionary access control list (DACL) that describes the access policy of the security descriptor.

The following figure illustrates a windows security descriptor.

:::image type="content" source="images/fssecurity-01.png" alt-text="diagram illustrating a windows security descriptor.":::

Security descriptors are variable-sized objects, with each of the individual subcomponents being variable in size as well. To facilitate offline storage of security descriptors, a security descriptor can be in self-relative format, in which case the header is the offset within the buffer to the specific component of the security descriptor. An in-memory format consists of pointer values to the various parts of the security descriptor. For a file system, the self-relative format is normally the most useful because it allows for simple storage and retrieval of the security descriptor from persistent storage. Applications that build security descriptors are more likely to use the in-memory format. The security reference monitor provides conversion routines to convert from one format to the other.

This section includes the following articles:

[Security Identifier](security-identifier.md)

[Access Mask](access-mask.md)

[Access Control Entry](access-control-entry.md)

[Access Control List](access-control-list.md)
