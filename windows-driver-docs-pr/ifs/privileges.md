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
ms.date: 04/24/2025
ms.topic: concept-article
---

# Managing privileges in a file system

*Privilege* is a mechanism that the operating system uses to control specific operations. Each privilege has particular operations associated with it that the operation's caller can perform if the following two conditions are met:

* The privilege must be held by the caller.
* The privilege must also be enabled.

The principle of these requirements is known as *least privilege*. Least privilege requires that privileges be enabled before they're used, rather than assumed. This requirement minimizes the chance that a user might inadvertently perform an operation they didn't intend. For example, **SeRestorePrivilege** would normally allow the caller to bypass the usual checks for write access to a file. For example, an administrator might not wish to actually override the normal security checks when copying a file. However, they might wish to do so when restoring that same file using a backup/restore utility.

For file systems, there are many privileges that are often used to modify the normal behavior (notably, security checks) for the system. These privileges are:

* **SeBackupPrivilege** allows file content retrieval, even if the security descriptor on the file might not grant such access. A caller with **SeBackupPrivilege** enabled obviates the need for any ACL-based security check.

* **SeRestorePrivilege** allows file content modification, even if the security descriptor on the file might not grant such access. This function can also be used to change the owner and protection.

* **SeChangeNotifyPrivilege** allows traverse right. This privilege is an important optimization in Windows because it removes the cost of performing a security check on every single directory in a path.

* **SeManageVolumePrivilege** allows specific volume-level management operations, such as lock volume, defragmenting, volume dismount, and setting valid data length on Windows XP and later. A file system driver explicitly enforces this particular privilege primarily based on FSCTL operations. In this case, the file system makes a policy decision to enforce this privilege. The determination of whether this privilege is held by the caller is made by the security reference monitor as part of the normal privilege check.

While there are numerous other privileges, they're normally opaque to file systems and only the [Security Reference Monitor](../kernel/windows-kernel-mode-security-reference-monitor.md) (SRM) interprets them.

The key Windows routines for managing privileges within a file system are:

* [**SePrivilegeCheck**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seprivilegecheck) performs a check for a specific set of necessary privileges.

* [**SeSinglePrivilegeCheck**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-sesingleprivilegecheck) performs a check for a single specific privilege; it's an optimized version of [**SePrivilegeCheck**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seprivilegecheck).

* [**SeAccessCheck**](/windows-hardware/drivers/ddi/wdm/nf-wdm-seaccesscheck) performs normal access checking on an object (normally a file object for a file system).

* [**SeFreePrivileges**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-sefreeprivileges) frees the privilege block returned by a previous call to [**SeAccessCheck**](/windows-hardware/drivers/ddi/wdm/nf-wdm-seaccesscheck).

* [**SeAppendPrivileges**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-seappendprivileges) adds enabled privileges to an ACCESS_STATE structure. Typically, a file system would use the ACCESS_STATE passed to it during IRP_MJ_CREATE processing.
