---
title: Security Checks
description: Security Checks
ms.assetid: 2883910a-72f3-4be9-b1dd-6fb02abffe73
keywords: ["security WDK file systems , security checks", "security checks WDK file systems", "security checks WDK file systems , about security checks"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Security%20Checks%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




