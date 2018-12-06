---
title: Using Nt and Zw Versions of the Native System Services Routines
description: Using Nt and Zw Versions of the Native System Services Routines
ms.assetid: 89627ddb-621d-4d27-acd6-16308689165d
keywords: ["Native System Services API WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
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

 

 




