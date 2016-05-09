---
title: Privileges
author: windows-driver-content
description: Privileges
ms.assetid: a8df1a44-6fb7-4c16-a29d-785d06dd50e4
keywords: ["security WDK file systems , privileges", "privileges WDK file systems", "operation privileges WDK file systems", "SeBackupPrivilege", "SeRestorePrivilege", "SeChangeNotifyPrivilege", "SeManageVolumePrivilege", "volume-level management privileges WDK file systems", "traverse right privileges WDK file systems", "backup privileges WDK file systems", "restore privileges WDK file systems"]
---

# Privileges


## <span id="ddk_privileges_if"></span><span id="DDK_PRIVILEGES_IF"></span>


Privilege is a completely separate mechanism that is used by the operating system to control specific operations. Each privilege has associated with it particular operations that may be performed if the privilege is held and enabled by the caller. Note the two conditions here:

-   The privilege must be held by the caller.

-   The privilege must also be enabled.

The principle here, known as least privilege, requires that privileges be enabled prior to their use, rather than simply assumed, in order to minimize the chance that a user might inadvertently perform an operation they did not intend. For example, **SeRestorePrivilege** would normally allow the caller to bypass the usual checks for write access to a file. An administrator may not wish to actually override the normal security checks when copying a file, but would wish to do so when restoring that same file using a backup/restore utility.

For file systems, there are a number of privileges that are often used to modify the normal behavior (notably, security checks) for the system. These privileges are:

-   **SeBackupPrivilege**--allows file content retrieval, even if the security descriptor on the file might not grant such access. A caller with **SeBackupPrivilege** enabled obviates the need for any ACL-based security check.

-   **SeRestorePrivilege**--allows file content modification, even if the security descriptor on the file might not grant such access. This function can also be used to change the owner and protection.

-   **SeChangeNotifyPrivilege**--allows traverse right. This privilege is an important optimization in Windows, since the cost of performing a security check on every single directory in a path is obviated by holding this privilege.

-   **SeManageVolumePrivilege**--allows specific volume-level management operations, such as lock volume, defragmenting, volume dismount, and setting valid data length on Windows XP and later. Note that this particular privilege is explicitly enforced by a file system driver primarily based upon FSCTL operations. In this case, the file system makes a policy decision to enforce this privilege. The determination of whether this privilege is held by the caller is made by the security reference monitor as part of the normal privilege check.

While there are numerous other privileges, they are normally opaque to file systems and are thus only interpreted by the security reference monitor.

The key Windows routines for managing privileges within a file system are:

-   [**SePrivilegeCheck**](https://msdn.microsoft.com/library/windows/hardware/ff556686)--this routine performs a check for a specific set of necessary privileges.

-   [**SeSinglePrivilegeCheck**](https://msdn.microsoft.com/library/windows/hardware/ff563740)--this routine performs a check for a single specific privilege; it is an optimized version of [**SePrivilegeCheck**](https://msdn.microsoft.com/library/windows/hardware/ff556686).

-   [**SeAccessCheck**](https://msdn.microsoft.com/library/windows/hardware/ff563674)--this routine performs normal access checking on an object (normally a file object for a file system).

-   [**SeFreePrivileges**](https://msdn.microsoft.com/library/windows/hardware/ff556656)--this routine frees the privilege block returned by a previous call to [**SeAccessCheck**](https://msdn.microsoft.com/library/windows/hardware/ff563674).

-   [**SeAppendPrivileges**](https://msdn.microsoft.com/library/windows/hardware/ff554762)--this routine adds enabled privileges to an ACCESS\_STATE structure. Typically, a file system would use the ACCESS\_STATE passed to it during IRP\_MJ\_CREATE processing.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Privileges%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


