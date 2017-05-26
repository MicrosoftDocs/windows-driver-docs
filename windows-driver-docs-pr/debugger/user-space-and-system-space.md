---
title: User Space and System Space
description: User Space and System Space
ms.assetid: 2d988178-cd19-4dc4-8dc1-39b9b6a1aaad
keywords: ["system space", "system space, addresses", "system space, breakpoints", "kernel space", "kernel space, addresses", "kernel space, breakpoints", "user space", "user space, addresses", "user space, breakpoints"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# User Space and System Space


Windows gives each user-mode application a block of virtual addresses. This is known as the *user space* of that application. The other large block of addresses, known as *system space* or *kernel space*, cannot be directly accessed by the application.

When WinDbg or CDB sets a [breakpoint](using-breakpoints.md) in user space, this breakpoint is set at the specified address in the user space of a single process. During user-mode debugging, the current process determines the meaning of virtual addresses. For more information, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

In kernel mode, you can set breakpoints in user space with the **bp**, **bu**, and **ba** commands or with the **Breakpoints** dialog box. You must first use the *process context* to specify the user-mode process that owns that address space by using **.process /i** (or a process-specific breakpoint on some kernel-space function) to switch the target to the correct [process context](changing-contexts.md#process-context).

Breakpoints in user space are always associated with the process whose process context was active when the breakpoints were set. If a user-mode debugger is debugging this process and if a kernel debugger is debugging the computer that the process is running on, this breakpoint breaks into the user-mode debugger, even though the breakpoint was actually set from the kernel debugger. You can break into the system from the kernel debugger at this point, or use the [**.breakin (Break to the Kernel Debugger)**](-breakin--break-to-the-kernel-debugger-.md) command from the user-mode debugger to transfer control to the kernel debugger.

### <span id="determining_the_range_of_user_space_and_system_space"></span><span id="DETERMINING_THE_RANGE_OF_USER_SPACE_AND_SYSTEM_SPACE"></span>Determining the Range of User Space and System Space

If you need to determine the extent of user space and system space on the target computer, you can use the [**dp (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command from a kernel debugger to display the Windows global variable **MmHighestUserAddress**. This variable contains the address of the top of user space. Since system space addresses are always higher than user space addresses, this value allows you to determine whether any given address is in user space or in kernel space.

For example, on a 32-bit target computer with an x86 processor and standard boot parameters, this command will show the following result:

```
kd> dp nt!mmhighestuseraddress L1 
81f71864  7ffeffff 
```

This indicates that user space ranges from the address 0x00000000 to 0x7FFEFFFF, and system space therefore ranges from 0x80000000 up to the highest possible address (which is 0xFFFFFFFF on a standard 32-bit Windows installation).

With a 64-bit target computer, different values will occur. For example, this command might show the following:

```
0: kd> dp nt!mmhighestuseraddress L1 
fffff800`038b4010  000007ff`fffeffff 
```

This indicates that user space ranges from 0x00000000\`00000000 to 0x000007FF\`FFFEFFFF. Therefore, system space includes all addresses from 0x00000800\`00000000 upward.

For more information about Windows memory management, see *Microsoft Windows Internals* by David Solomon and Mark Russinovich (4th edition, Microsoft Press, 2005).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20User%20Space%20and%20System%20Space%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




