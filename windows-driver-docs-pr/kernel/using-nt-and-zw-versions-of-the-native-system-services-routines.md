---
title: Using Nt and Zw Versions of the Native System Services Routines
author: windows-driver-content
description: Using Nt and Zw Versions of the Native System Services Routines
MS-HAID:
- 'NtAndZw\_0b86a853-fcb1-4246-ae28-68e9e169af15.xml'
- 'kernel.using\_nt\_and\_zw\_versions\_of\_the\_native\_system\_services\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 89627ddb-621d-4d27-acd6-16308689165d
keywords: ["Native System Services API WDK"]
---

# Using Nt and Zw Versions of the Native System Services Routines


The Windows native operating system services API is implemented as a set of routines that run in kernel mode. These routines have names that begin with the prefix **Nt** or **Zw**. Kernel-mode drivers can call these routines directly. User-mode applications can access these routines by using system calls.

With a few exceptions, each native system services routine has two slightly different versions that have similar names but different prefixes. For example, calls to [NtCreateFile](http://go.microsoft.com/fwlink/p/?linkid=157250) and [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424) perform similar operations and are, in fact, serviced by the same kernel-mode system routine. For system calls from user mode, the **Nt** and **Zw** versions of a routine behave identically. For calls from a kernel-mode driver, the **Nt** and **Zw** versions of a routine differ in how they handle the parameter values that the caller passes to the routine.

A kernel-mode driver calls the **Zw** version of a native system services routine to inform the routine that the parameters come from a trusted, kernel-mode source. In this case, the routine assumes that it can safely use the parameters without first validating them. However, if the parameters might be from either a user-mode source or a kernel-mode source, the driver instead calls the **Nt** version of the routine, which determines, based on the history of the calling thread, whether the parameters originated in user mode or kernel mode. For more information about how the routine distinguishes user-mode parameters from kernel-mode parameters, see [**PreviousMode**](previousmode.md).

When a user-mode application calls the **Nt** or **Zw** version of a native system services routine, the routine always treats the parameters that it receives as values that come from a user-mode source that is not trusted. The routine thoroughly validates the parameter values before it uses the parameters. In particular, the routine probes any caller-supplied buffers to verify that the buffers are located in valid user-mode memory and are aligned properly.

Native system services routines make additional assumptions about the parameters that they receive. If a routine receives a pointer to a buffer that was allocated by a kernel-mode driver, the routine assumes that the buffer was allocated in system memory, not in user-mode memory. If the routine receives a handle that was opened by a user-mode application, the routine looks for the handle in the user-mode handle table, not in the kernel-mode handle table.

In a few instances, the meaning of a parameter value differs more significantly between calls from user mode and from kernel mode. For example, the [**ZwNotifyChangeKey**](https://msdn.microsoft.com/library/windows/hardware/ff566488) routine (or its **NtNotifyChangeKey** counterpart) has a pair of input parameters, *ApcRoutine* and *ApcContext*, that mean different things, depending on whether the parameters are from a user-mode or kernel-mode source. For a call from user mode, *ApcRoutine* points to an APC routine and *ApcContext* points to a context value that the operating system supplies when it calls the APC routine. For a call from kernel mode, *ApcRoutine* points to a [**WORK\_QUEUE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff557304) structure, and *ApcContext* specifies the type of work queue item that is described by the **WORK\_QUEUE\_ITEM** structure.

This section includes the following topics:

[**PreviousMode**](previousmode.md)

[Libraries and Headers](libraries-and-headers.md)

[What Does the Zw Prefix Mean?](what-does-the-zw-prefix-mean-.md)

[Specifying Access Rights](access-mask.md)

[NtXxx Routines](ntxxx-routines.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Nt%20and%20Zw%20Versions%20of%20the%20Native%20System%20Services%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


