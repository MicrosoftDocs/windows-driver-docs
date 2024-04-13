---
title: Managing Privileges in a File System
description: Describes how to manage privileges in a file system
keywords:
- security WDK file systems , privileges
- privileges WDK file systems
- operation privileges WDK file systems
- SeBackupPrivilege
- SeRestorePrivilege
- SeChangeNotifyPrivilege
- SeManageVolumePrivilege
- volume-level management privileges WDK file systems
- traverse right privileges WDK file systems
- backup privileges WDK file systems
- restore privileges WDK file systems
ms.date: 04/20/2017
---

# Managing privileges in a file system

Privilege is a completely separate mechanism that is used by the operating system to control specific operations. Each privilege has associated with it particular operations that may be performed if the privilege is held and enabled by the caller. Note the two conditions here:

- The privilege must be held by the caller.

- The privilege must also be enabled.

The principle here, known as least privilege, requires that privileges be enabled prior to their use, rather than simply assumed, in order to minimize the chance that a user might inadvertently perform an operation they did not intend. For example, **SeRestorePrivilege** would normally allow the caller to bypass the usual checks for write access to a file. An administrator may not wish to actually override the normal security checks when copying a file, but would wish to do so when restoring that same file using a backup/restore utility.

For file systems, there are a number of privileges that are often used to modify the normal behavior (notably, security checks) for the system. These privileges are:

- **SeBackupPrivilege** allows file content retrieval, even if the security descriptor on the file might not grant such access. A caller with **SeBackupPrivilege** enabled obviates the need for any ACL-based security check.

- **SeRestorePrivilege** allows file content modification, even if the security descriptor on the file might not grant such access. This function can also be used to change the owner and protection.

- **SeChangeNotifyPrivilege** allows traverse right. This privilege is an important optimization in Windows, since the cost of performing a security check on every single directory in a path is obviated by holding this privilege.

- **SeManageVolumePrivilege** allows specific volume-level management operations, such as lock volume, defragmenting, volume dismount, and setting valid data length on Windows XP and later. Note that this particular privilege is explicitly enforced by a file system driver primarily based upon FSCTL operations. In this case, the file system makes a policy decision to enforce this privilege. The determination of whether this privilege is held by the caller is made by the security reference monitor as part of the normal privilege check.

While there are numerous other privileges, they are normally opaque to file systems and are thus only interpreted by the security reference monitor.

The key Windows routines for managing privileges within a file system are:

- [**SePrivilegeCheck**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seprivilegecheck)--this routine performs a check for a specific set of necessary privileges.

- [**SeSinglePrivilegeCheck**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-sesingleprivilegecheck)--this routine performs a check for a single specific privilege; it is an optimized version of [**SePrivilegeCheck**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seprivilegecheck).

- [**SeAccessCheck**](/windows-hardware/drivers/ddi/wdm/nf-wdm-seaccesscheck)--this routine performs normal access checking on an object (normally a file object for a file system).

- [**SeFreePrivileges**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-sefreeprivileges)--this routine frees the privilege block returned by a previous call to [**SeAccessCheck**](/windows-hardware/drivers/ddi/wdm/nf-wdm-seaccesscheck).

- [**SeAppendPrivileges**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seappendprivileges)--this routine adds enabled privileges to an ACCESS_STATE structure. Typically, a file system would use the ACCESS_STATE passed to it during IRP_MJ_CREATE processing.
