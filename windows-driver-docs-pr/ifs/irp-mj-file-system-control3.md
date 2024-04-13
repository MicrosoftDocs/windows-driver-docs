---
title: Security Checks on IRP_MJ_FILE_SYSTEM_CONTROL
description: Describes how a file system does security checks on IRP_MJ_FILE_SYSTEM_CONTROL
keywords:
- IRP_MJ_FILE_SYSTEM_CONTROL
- security WDK file systems , adding security checks
- security checks WDK file systems , IRP_MJ_FILE_SYSTEM_CONTROL
- file system controls WDK security
- set file information processing WDK file systems
ms.date: 04/20/2017
---

# Security checks on IRP_MJ_FILE_SYSTEM_CONTROL (IFS)

A file system control allows the file system to perform essentially any specialized operation. The existing Windows file systems have a number of specialized controls and for them, as well as any third-party file systems developed for Windows, it is imperative to aggressively check all parameters. In addition, FSCTL operations often have restricted security rights. These can be seen in the [FASTFAT sample code](/samples/microsoft/windows-driver-samples/fastfat-file-system-driver/) (see the **FatInvalidateVolumes** function in fsctrl.c, for example). This is an example of a privilege check. The policy of the FASTFAT file system in this case is to require that the given privilege be enabled on the system.

The I/O manager will enforce FILE_READ_DATA and FILE_WRITE_DATA permissions on specific FSCTL operations, if the file system has set these bits in the file system operation definition using the CTL_CODE macro. All other permissions required must be checked by the file system (FILE_READ_ATTRIBUTES permissions, for example) if this is the policy of the file system.
