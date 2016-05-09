---
title: Denial of Service
author: windows-driver-content
description: Denial of Service
ms.assetid: b8b28d42-b680-482a-a7a1-6b2f5614ebfb
keywords: ["threat models WDK file systems , denial of service", "security threat models WDK file systems , denial of service", "denial-of-service attacks WDK file systems", "buffers WDK file systems", "bandwidth WDK file systems", "disk space attacks WDK file systems", "malicious applications WDK file systems"]
---

# Denial of Service


## <span id="ddk_denial_of_service_if"></span><span id="DDK_DENIAL_OF_SERVICE_IF"></span>


A denial-of-service occurs when access to a particular service should have been granted, but in fact was improperly rejected. For example, any operation that an unprivileged application can perform that causes the system to become unusable is effectively a denial-of-service. This would include any operation or sequence of operations that:

-   Crashes the system.

-   Causes premature termination of threads or processes.

-   Creates a deadlock condition. A deadlock occurs when two or more threads are stopped waiting in a permanent state of stalemate. Each thread is waiting for a resource held by one of the other threads.

-   Creates a live lock condition. A live lock can occur when two or more processors cannot progress because they are waiting to acquire a resource (typically a lock on a queue) and the thread which owns that resource is in a similar non-progressing state.

Such problems often arise within drivers because they contain latent bugs that can be exploited by normal applications. Exploits of this type can be simple and are difficult to protect against. Common causes of such problems in drivers include:

-   Improper user buffer validation.

-   Buffer overflow or underflow.

For file systems and file system filter drivers, there are numerous cases of such problems. For example, the MAX\_PATH value is defined as 260 for historical reasons on the Win32 subsystem. Many driver components assume that this indicates the size of the largest path. Unfortunately, this is not the case as the maximum path on an NTFS file system is 32,767 Unicode characters (65,534 bytes). If a filter driver were to encode a MAX\_PATH length assumption into its code base, a simple denial-of-service attack would arise from an application creating a path larger than this within a path managed by the filter driver.

Another common problem is that applications often embed user-mode pointers into private FSCTL requests. A file system is subject to three broad categories of denial-of-service attacks:

-   Consuming all available disk space.

-   Using all available disk bandwidth.

-   Blocking access to files to which users should have access.

Typically, there is little that a file system developer can do to prevent these types of attacks. However, there are steps that can be taken by developers to allow administrators to limit these types of denial-of-service attacks.

The simplest denial-of-service attack involving the file system is to use up all of the free disk space. It is simple to write an application to do this and the consequences are far reaching. Many applications and services in the system will not function if they can no longer write to disk. The mitigating technology is disk quotas, which can limit how much disk space is available for files owned by a user when used properly by administrators. Therefore, it makes sense to include support for disk quotas when developing a file system.

A malicious or poorly written application could also try to consume all disk bandwidth. The consequences for regular users subject to this type of attack is a sluggish or unresponsive system. Currently, the operating system has no mechanism to throttle the bandwidth consumed by applications. A file system also consumes kernel memory for each open file object and file handle. A malicious application could try to continuously open a large number of files and keep them open until memory is exhausted. The primary mitigating technique for these issues is auditing and logging so that an administrator can monitor the computer for applications that perform a large amount of I/O or use large amounts of other resources. Again, it would be judicious for file system and file system filter drivers to include auditing support to be better able to minimize this type of denial of service.

A malicious application can try to prevent other users from accessing files needed for normal use. An important strategy to minimize these issues is to ensure that security information associated with file objects is properly implemented when developing file systems.

Finally, all drivers need to be concerned about consuming all available memory or other resources in response to requests from a malicious or aberrant application.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Denial%20of%20Service%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


