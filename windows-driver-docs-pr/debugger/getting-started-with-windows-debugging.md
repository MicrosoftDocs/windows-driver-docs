---
title: Getting Started with Windows Debugging
description: This section covers how to get started with Windows Debugging. If your goal is to use the debugger to analyze a crash dump, see Crash dump analysis using the Windows debuggers (WinDbg).
ms.assetid: 4981928E-A33D-4F60-AAA0-124C360B7E03
ms.author: domars
ms.date: 08/23/2018
ms.localizationpriority: medium
---

# Getting Started with Windows Debugging


This section covers how to get started with Windows Debugging. If your goal is to use the debugger to analyze a crash dump, see [Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md).

To get started with Windows Debugging, complete the following tasks.

1. Determine which devices will serve as the host system and the target system.
   The debugger runs on the host system and the code that you want to debug runs on the target system.

   **Host &lt;--------------------------------------------------&gt; Target**

   ![host and target pcs connected with a double arrow](images/targethost1.png)

   Because it is common to stop instruction execution on the processor during debugging, typically, two systems are used. In some situations, it is possible that the second system is a virtual system, for example, a virtual PC that is running on the same PC. However, if your code is communicating to low level hardware, using a virtual PC may not be the best approach. For more information, see [Setting Up Network Debugging of a Virtual Machine Host](setting-up-network-debugging-of-a-virtual-machine-host.md).

2. Determine if you will be doing kernel or user mode debugging.

   *Kernel mode* - Kernel mode is the processor access mode in which the operating system and privileged programs run. Kernel mode code has permission to access any part of the system, and is not restricted like user mode code. It can gain access to any part of any other process running in either user mode or kernel mode. Much of the core OS functionality and many hardware device drivers run in kernel mode.

   *User mode* - Applications and subsystems run on the computer in user mode. Processes that run in user mode do so within their own virtual address spaces. They are restricted from gaining direct access to many parts of the system, including system hardware, memory that was not allocated for their use, and other portions of the system that might compromise system integrity. Because processes that run in user mode are effectively isolated from the system and other user mode processes, they cannot interfere with these resources.

   If your goal is to debug a driver, determine if the driver is a kernel mode driver (typically described as a WDM or KMDF driver) or a user mode driver (UMDF).

   For some issues, it can be difficult to determine which mode the code is executing in. In that case, you may need to pick one mode and look to see what information is available in that mode. Some issues require using the debugger in both user and kernel mode.

   Depending on what mode you decide to debug in, you will need to configure and use the debuggers in different ways. Some debug commands operate the same, and some commands operate differently in different modes.

   For information about using the debugger in kernel mode, see the following topics:
   - [Getting Started with WinDbg (Kernel-Mode)](getting-started-with-windbg--kernel-mode-.md) 
   - [Debug Universal Drivers - Step by Step Lab (Echo Kernel-Mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md) 
   - [Debug Drivers - Step by Step Lab (Sysvad Kernel-Mode)](debug-universal-drivers--kernel-mode-.md). 
    
     For information about using the debugger in user mode, see [Getting Started with WinDbg (User-Mode)](getting-started-with-windbg.md).

3. Chose your debugger environment.

   WinDbg works well in most situations, but there are times when you may want to use another debugger such as console debuggers for automation or even Visual Studio. For more information, see [Debugging Environments](debuggers-in-the-debugging-tools-for-windows-package.md).

4. Determine how you will connect the target and host system.

   Typically, an Ethernet network connection is used to connect the target and host system. If you are doing early bring up work, or don't have an Ethernet connection on the device, other network connection options are available. For more information, see these topics:
   -   [Setting Up KDNET Network Kernel Debugging Automatically](setting-up-a-network-debugging-connection-automatically.md)
   -   [Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)
   -   [Setting Up KDNET Network Kernel Debugging Manually](setting-up-a-network-debugging-connection.md)
   -   [Setting Up Network Debugging of a Virtual Machine Host](setting-up-network-debugging-of-a-virtual-machine-host.md)

5. Choose either the 32-bit or 64-bit debugging tools.

   This choice is dependent on the version of Windows that is running on the target and host systems and whether you are debugging 32-bit or 64-bit code. For more information, see [Choosing the 32-Bit or 64-Bit Debugging Tools](choosing-a-32-bit-or-64-bit-debugger-package.md).

6. Configure symbols.

   You must load the proper symbols to use all of the advanced functionality that WinDbg provides. If you do not have symbols properly configured, you will receive messages indicating that symbols are not available when you attempt to use functionality that is dependent on symbols. For more information, see [Symbols for Windows debugging (WinDbg, KD, CDB, NTSD)](symbols.md).

7. Configure source code.
   If your goal is to debug your own source code, you will need to configure a path to your source code. For more information, see [Source Path](source-path.md).

8. Become familiar with debugger operation.
   The [Debugger Operation](debugger-operation-win8.md) section of the documentation describes debugger operation for various tasks. For example, the [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md) topic explains how to load debugger extensions. To learn more about working with WinDbg, see [Debugging Using WinDbg](debugging-using-windbg.md).

9. Become familiar with debugging techniques.
   [Standard Debugging Techniques](standard-debugging-techniques.md) apply to most debugging scenarios, and examples include setting breakpoints, inspecting the call stack, and finding a memory leak. [Specialized Debugging Techniques](specialized-debugging-techniques.md) apply to particular technologies or types of code. Examples are Plug and Play debugging, Kernel Mode Driver Framework debugging, and RPC debugging.

10. Use the debugger reference commands.
    Over time, you will use different debug commands as you work in the debugger. Use the [.hh (Open HTML Help File)](-hh--open-html-help-file-.md) command in the debugger to display help information about any debug command. For more information about the available commands, see [Debugger Reference](debugger-reference.md).

11. Use debugging extensions for specific technologies.
    There are a number of debugging extensions that provide parsing of domain specific data structures. For more information, see [Specialized Extensions](specialized-extensions.md).

12. Learn about related Windows internals, such as memory usage, context, threads and processes. This documentation assumes a knowledge of Windows internals. Review resources such as this book to learn more about Windows Internals. 
    -   Windows Internals by Mark E. Russinovich, David A. Solomon and Alex Ionescu

13. Review additional debugging resources.
    -   Inside Windows Debugging: A Practical Guide to Debugging and Tracing Strategies in Windows® by Tarik Soulami
    -   Advanced Windows Debugging by Mario Hewardt and Daniel Pravat
    -   [The Defrag Tools Show WinDbg Episodes 13-29](https://channel9.msdn.com/Shows/Defrag-Tools)


## See Also

-   [Getting Started with WinDbg (Kernel-Mode)](getting-started-with-windbg--kernel-mode-.md)
-   [Getting Started with WinDbg (User-Mode)](getting-started-with-windbg.md)
-   [Choosing the 32-Bit or 64-Bit Debugging Tools](choosing-a-32-bit-or-64-bit-debugger-package.md)
-   [Debugging Environments](debuggers-in-the-debugging-tools-for-windows-package.md)
-   [Setting Up Debugging (Kernel-Mode and User-Mode)](getting-set-up-for-debugging.md)
-   [Debug Universal Drivers - Step by Step Lab (Echo Kernel-Mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md)
-   [Debug Drivers - Step by Step Lab (Sysvad Kernel-Mode)](debug-universal-drivers--kernel-mode-.md)



