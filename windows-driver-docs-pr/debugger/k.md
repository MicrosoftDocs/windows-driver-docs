---
title: K (Windows Debugger Glossary)
description: Glossary page - K
Robots: noindex, nofollow
ms.assetid: 93b65114-f680-41f7-b754-699f773955ba
---

# K


<span id="kd_connection_server"></span><span id="KD_CONNECTION_SERVER"></span>**KD connection server**  
A proxy used during some forms of kernel-mode remote debugging. It listens for connections from smart client and performs memory, processor, or Windows operations as requested by these remote clients.

See also debugging server.

For more information, see [KD Connection Servers (Kernel Mode)](kd-connection-servers--kernel-mode-.md).

<span id="kernel"></span><span id="KERNEL"></span>**kernel**  
The kernel is the portion of the Windows operating system that manages and controls access to hardware resources. It performs thread scheduling and dispatching, interrupt and exception handling, and multiprocessor synchronization.

<span id="kernel_error"></span><span id="KERNEL_ERROR"></span>**kernel error**  
See bug check.

<span id="kernel_mode"></span><span id="KERNEL_MODE"></span>**kernel mode**  
Kernel-mode code has permission to access any part of the system, and is not restricted like user-mode code. It can gain access to any part of any other process running in either user mode or kernel mode.

Performance-sensitive operating system components run in kernel mode. In this way they can interact with the hardware and with each other without the overhead of context switch. All the kernel-mode components are fully protected from applications running in user mode. They can be grouped as follows:

-   Executive.

    This contains the base operating system components such as memory management, process and thread management, security, I/O, interprocess communication.

-   Kernel.

    This performs low-level functions such as thread scheduling, interrupt and exception dispatching, and multiprocessor synchronization. It also provides a set of routines and basic objects used by the Executive to implement higher-level semantics.

-   Hardware Abstraction Layer (HAL).

    This handles all direct interface to hardware. It thus isolates the Windows Kernel, device drivers, and Windows Executive from platform-specific hardware differences.

-   Window and Graphics Subsystem.

    This implements the graphical user interface (GUI) functions.

When a process erroneously accesses a portion of memory that is in use by another application or by the system, the lack of restrictions on kernel-mode processes forces Windows to stop the entire system. This is referred to as a bug check.

Malfunctioning hardware devices or device drivers, which reside in kernel mode, are often the culprits in bug checks.

<span id="kernel_mode_target"></span><span id="KERNEL_MODE_TARGET"></span>**kernel-mode target**  
See target computer.

<span id="kernel_mode_debugging"></span><span id="KERNEL_MODE_DEBUGGING"></span>**kernel-mode debugging**  
A debugger session in which the target is running in kernel mode.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20K%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




