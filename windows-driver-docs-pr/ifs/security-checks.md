---
title: Security Checks
description: Security Checks
ms.assetid: 2883910a-72f3-4be9-b1dd-6fb02abffe73
keywords:
- security WDK file systems , security checks
- security checks WDK file systems
- security checks WDK file systems , about security checks
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Security Checks


## <span id="ddk_security_checks_if"></span><span id="DDK_SECURITY_CHECKS_IF"></span>


The bulk of the file system's responsibility with respect to security is in the area of security checks. These are implemented within the file system because it is the part of Windows that actually "owns" the object. The goal of the security implementation is to separate the policy (implemented by the file system) for protecting its objects, and the mechanism (implemented by the Security Reference Monitor) for making access decisions.

In other words, the file system developer is responsible for making calls to the Security Reference Monitor at the appropriate time to validate correct access to a file system resource. The file system need not understand the details of how the Security Reference Monitor makes these security decisions. This section describes points where a file system might consider adding security checks.

This section includes the following topics:

[Applying Security Descriptors on the Device Object](applying-security-descriptors-on-the-device-object.md)

[IRP\_MJ\_CREATE](irp-mj-create-dispatch-routine.md)

[IRP\_MJ\_QUERY\_SECURITY and IRP\_MJ\_SET\_SECURITY](irp-mj-query-security-and-irp-mj-set-security.md)

[IRP\_MJ\_DIRECTORY\_CONTROL](irp-mj-directory-control2.md)

[IRP\_MJ\_FILE\_SYSTEM\_CONTROL](https://msdn.microsoft.com/library/windows/hardware/ff548670)

[IRP\_MJ\_SET\_INFORMATION](https://msdn.microsoft.com/library/windows/hardware/ff549366)

[Impersonation](impersonation.md)

[Process and Thread Termination Issues](process-and-thread-termination-issues.md)

 

 




