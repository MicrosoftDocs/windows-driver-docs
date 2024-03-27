---
title: Security Checks in File Systems
description: Security Checks
keywords:
- security WDK file systems , security checks
- security checks WDK file systems
- security checks WDK file systems , about security checks
ms.date: 04/20/2017
---

# Security checks in file systems

The bulk of the file system's responsibility with respect to security is in the area of security checks. These are implemented within the file system because it is the part of Windows that actually "owns" the object. The goal of the security implementation is to separate the policy (implemented by the file system) for protecting its objects, and the mechanism (implemented by the Security Reference Monitor) for making access decisions.

In other words, the file system developer is responsible for making calls to the Security Reference Monitor at the appropriate time to validate correct access to a file system resource. The file system need not understand the details of how the Security Reference Monitor makes these security decisions. This section describes points where a file system might consider adding security checks.

This section includes the following topics:

[Applying Security Descriptors on the Device Object](applying-security-descriptors-on-the-device-object.md)

[Security checks on IRP_MJ_CREATE](irp-mj-create-dispatch-routine.md)

[Security checks on IRP_MJ_QUERY_SECURITY and IRP_MJ_SET_SECURITY](irp-mj-query-security-and-irp-mj-set-security.md)

[Security checks on IRP_MJ_DIRECTORY_CONTROL](irp-mj-directory-control2.md)

[Security checks on IRP_MJ_FILE_SYSTEM_CONTROL](./irp-mj-file-system-control.md)

[Security checks on IRP_MJ_SET_INFORMATION](./irp-mj-set-information.md)

[Impersonation](impersonation.md)

[Process and Thread Termination Issues](process-and-thread-termination-issues.md)
