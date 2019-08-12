---
title: Getting Started with Windows Debugging
description: This section covers how to get started with Windows Debugging. If your goal is to use the debugger to analyze a crash dump, see Crash dump analysis using the Windows debuggers (WinDbg).
ms.assetid: 4981928E-A33D-4F60-AAA0-124C360B7E03
ms.date: 08/23/2018
ms.localizationpriority: medium
---

# Getting Started with Windows Debugging


This section covers how to get started with Windows Debugging. If your goal is to use the debugger to analyze a crash dump, see [Analyze crash dump files by using WinDbg](crash-dump-files.md).

To get started with Windows Debugging, complete the following tasks:

 1. [Determine the host and the target](#determine-the-host-and-the-target).
 1. [Determine the type: kernel-mode or user-mode](#determine-the-type-kernel-mode-or-user-mode).
 1. [Choose your debugger environment](#choose-your-debugger-environment).
 1. [Determine how to connect the target and host](#determine-how-to-connect-the-target-and-host).
 1. [Choose either the 32-bit or 64-bit debugging tools](#choose-either-the-32-bit-or-64-bit-debugging-tools).
 1. [Configure symbols](#configure-symbols).
 1. [Configure source code](#configure-source-code).
 1. [Become familiar with debugger operation](#become-familiar-with-debugger-operation).
 1. [Become familiar with debugging techniques](#become-familiar-with-debugging-techniques).
 1. [Use the debugger reference commands](#use-the-debugger-reference-commands).
 1. [Use debugging extensions for specific technologies](#use-debugging-extensions-for-specific-technologies).
 1. [Learn about related Windows internals](#learn-about-related-windows-internals).
 1. [Review additional debugging resources](#review-additional-debugging-resources).

## Determine the host and the target 

The debugger runs on the *host* system, and the code that you want to debug runs on the *target* system.

   **Host &lt;--------------------------------------------------&gt; Target**

![host and target pcs connected with a double arrow](images/targethost1.png)

Because it is common to stop instruction execution on the processor during debugging, two computer systems are typically used. In some situations, you might be able to use a virtual machine as the second system. For example, you might be able to use a virtual PC that is running on the same PC as the code that you need to debug. However, if your code is communicating to low-level hardware, using a virtual PC may not be the best approach. For more information, see [Setting up network debugging of a virtual machine - KDNET](setting-up-network-debugging-of-a-virtual-machine-host.md).

## Determine the type: kernel-mode or user-mode

Next, you need to determine whether you will do kernel-mode or user-mode debugging.

*Kernel mode* is the processor-access mode in which the operating system and privileged programs run. Kernel-mode code has permission to access any part of the system, and it is not restricted like user-mode code. Kernel-mode code can gain access to any part of any other process running in either user mode or kernel mode. Much of the core OS functionality and many hardware device drivers run in kernel mode.

*User mode* is the mode that applications and subsystems on the computer run in. Processes that run in user mode do so within their own virtual address spaces. They are restricted from gaining direct access to many parts of the system, including system hardware, memory that was not allocated for their use, and other portions of the system that might compromise system integrity. Because processes that run in user mode are effectively isolated from the system and other user-mode processes, they cannot interfere with these resources.

If your goal is to debug a driver, determine if the driver is a kernel-mode driver or a user-mode driver. Kernel-mode drivers are often identified as Windows Driver Model (WDM) drivers or as Kernel-Mode Driver Framework (KMDF) drivers. User-mode drivers are typically identified as User-Mode Driver Framework (UMDF) drivers.

For some issues, it can be difficult to determine which mode the code executes in. In that case, you may need to pick one mode and look to see what information is available in that mode. Some issues require using the debugger in both user mode and kernel mode.

Depending on what mode you decide to debug in, you will need to configure and use the debuggers in different ways. Some debugging commands operate the same in both modes, and some commands operate differently in different modes.

For information about using the debugger in kernel mode, see the following articles:
   - [Getting started with WinDbg (kernel-mode)](getting-started-with-windbg--kernel-mode-.md) 
   - [Debug universal drivers - step by step lab (echo kernel-mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md) 
   - [Debug drivers - step by step lab (Sysvad kernel-mode)](debug-universal-drivers--kernel-mode-.md). 
    
For information about using the debugger in user mode, see [Getting started with WinDbg (user-mode)](getting-started-with-windbg.md).

## Choose your debugger environment

WinDbg works well in most situations, but there are times when you may want to use another debugger, such as console debuggers for automation or Visual Studio. For more information, see [Debugging environments](debuggers-in-the-debugging-tools-for-windows-package.md).

## Determine how to connect the target and host

Typically, target and host systems are connected by an Ethernet network. If you are doing early bring-up work, or you don't have an Ethernet connection on a device, other network connection options are available. For more information, see these articles:
   -   [Setting up KDNET network kernel debugging automatically](setting-up-a-network-debugging-connection-automatically.md)
   -   [Setting up kernel-mode debugging](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)
   -   [Setting up KDNET network kernel debugging manually](setting-up-a-network-debugging-connection.md)
   -   [Setting up network debugging of a virtual machine - KDNET](setting-up-network-debugging-of-a-virtual-machine-host.md)

## Choose either the 32-bit or 64-bit debugging tools

Which debugging tools to choose—32-bit or 64-bit—depends on the version of Windows that is running on the target and host systems and on whether you are debugging 32-bit or 64-bit code. For more information, see [Choosing the 32-Bit or 64-Bit debugging tools](choosing-a-32-bit-or-64-bit-debugger-package.md).

## Configure symbols

To use all of the advanced functionality that WinDbg provides, you must load the proper symbols. If you do not have symbols properly configured, you will receive messages indicating that symbols are not available when you attempt to use functionality that is dependent on symbols. For more information, see [Symbols for Windows debugging (WinDbg, KD, CDB, NTSD)](symbols.md).

## Configure source code

If your goal is to debug your own source code, you will need to configure a path to your source code. For more information, see [Source path](source-path.md).

## Become familiar with debugger operation

The [Debugger operation](debugger-operation-win8.md) section of this documentation describes debugger operation for various tasks. For example, [Loading debugger extension DLLs](loading-debugger-extension-dlls.md) explains how to load debugger extensions. To learn more about working with WinDbg, see [Debugging using WinDbg](debugging-using-windbg.md).

## Become familiar with debugging techniques

[Standard debugging techniques](standard-debugging-techniques.md) apply to most debugging scenarios, and examples include setting breakpoints, inspecting the call stack, and finding a memory leak. [Specialized debugging techniques](specialized-debugging-techniques.md) apply to particular technologies or types of code. Examples include Plug and Play debugging, KMDF debugging, and RPC debugging.

## Use the debugger reference commands

Over time, you will use different debugging commands as you work in the debugger. Use the [.hh (Open HTML Help File)](-hh--open-html-help-file-.md) command in the debugger to display help information about any debugging command. For more information about the available commands, see [Debugger reference](debugger-reference.md).

## Use debugging extensions for specific technologies

There are multiple debugging extensions that provide parsing of domain-specific data structures. For more information, see [Specialized extensions](specialized-extensions.md).

## Learn about related Windows internals

This documentation assumes a knowledge of Windows internals. To learn more about Windows internals (including memory usage, context, threads, and processes), review additional resources, such as [*Windows Internals*](https://docs.microsoft.com/en-us/sysinternals/learn/windows-internals) by Mark Russinovich, David Solomon, and Alex Ionescu.

## Review additional debugging resources

Additional resources include the following books and videos:
-  *Inside Windows Debugging: Practical Debugging and Tracing Strategies* by Tarik Soulami
-   *Advanced Windows Debugging* by Mario Hewardt and Daniel Pravat
-   [Defrag Tools](https://channel9.msdn.com/Shows/Defrag-Tools), episodes 13 through 29, about WinDbg


## See also

-   [Getting started with WinDbg (kernel-mode)](getting-started-with-windbg--kernel-mode-.md)
-   [Getting started with WinDbg (user-mode)](getting-started-with-windbg.md)
-   [Choosing the 32-Bit or 64-Bit debugging tools](choosing-a-32-bit-or-64-bit-debugger-package.md)
-   [Debugging environments](debuggers-in-the-debugging-tools-for-windows-package.md)
-   [Setting up debugging (kernel-mode and user-mode)](getting-set-up-for-debugging.md)
-   [Debug universal drivers - step by step lab (echo kernel-mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md)
-   [Debug drivers - step by step lab (Sysvad kernel-mode)](debug-universal-drivers--kernel-mode-.md)
