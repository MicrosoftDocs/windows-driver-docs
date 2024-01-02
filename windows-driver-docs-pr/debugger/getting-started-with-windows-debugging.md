---
title: Get started with Windows debugging
description: Get started with debugging for Windows, and find resources to help you install tools and learn debugging techniques.
ms.date: 12/20/2023
---

# Get started with Windows debugging

This article covers how to get started with debugging for Windows. If your goal is to use the debugger to analyze a crash dump, see [Analyze crash dump files by using WinDbg](crash-dump-files.md).

To get started with Windows debugging, complete the following steps.

## 1. Identify the host and target systems

Two separate computer systems are typically used for debugging because instruction execution on the processor is commonly paused during the process. The debugger runs on the *host* system, and the code that you want to debug runs on the *target* system.

**Host &lt;--------------------------------------------------&gt; Target**

:::image type="content" source="images/target-host-1.png" alt-text="Diagram illustrating the connection between host and target systems with a double arrow.":::

In some situations, it's possible to use a virtual machine as the second system. For example, a virtual PC could run on the same PC as the code that you need to debug. However, if your code communicates with low-level hardware, using a virtual PC might not be the best approach. For more information, see [Setting up network debugging of a virtual machine - KDNET](setting-up-network-debugging-of-a-virtual-machine-host.md).

## 2. Determine the debugger type: kernel mode or user mode

Next, you need to determine whether to use kernel-mode or user-mode debugging.

- The operating system and privileged programs run in *kernel mode*. Kernel-mode code has permission to access any part of the system, and it's not restricted like user-mode code. Kernel-mode code can gain access to any part of any other process running in either user mode or kernel mode. Much of the core OS functionality and many hardware device drivers run in kernel mode.

- Applications and subsystems on the computer run in *user mode*. Processes that run in user mode do so within their own virtual address spaces. They're restricted from gaining direct access to many parts of the system, including system hardware, memory that isn't allocated for their use, and other portions of the system that might compromise system integrity. Processes that run in user mode are effectively isolated from the system and from other user-mode processes, so they can't interfere with these resources.

If your goal is to debug a driver, determine if the driver is a kernel-mode driver or a user-mode driver. Windows Driver Model (WDM) drivers and Kernel-Mode Driver Framework (KMDF) are both kernel-mode drivers. As the name suggests, User-Mode Driver Framework (UMDF) drivers are user-mode drivers.

For some issues, it can be difficult to determine which mode the code executes in. In that case, you might need to pick one mode and see what information is available in that mode. Some issues require using the debugger in both user mode and kernel mode.

Depending on which mode you debug in, you might need to configure and use the debuggers in different ways. Some debugging commands operate the same in both modes, and some commands operate differently.

Learn more about using the debugger in kernel mode:
- [Get started with WinDbg (kernel mode)](getting-started-with-windbg--kernel-mode-.md)
- [Debug universal drivers: step-by-step lab (echo kernel mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md)
- [Debug drivers: step-by-step lab (Sysvad kernel mode)](debug-universal-drivers--kernel-mode-.md)

Learn more about using the debugger in user mode:
- [Get started with WinDbg (user mode)](getting-started-with-windbg.md)

## 3. Choose your debugger environment

The WinDbg debugger works well in most situations, but there are times when you might want to use another debugger, such as console debuggers for automation or Visual Studio. For more information, see [Debugging environments](debuggers-in-the-debugging-tools-for-windows-package.md).

## 4. Determine how to connect the target and host

Typically, target and host systems are connected by an Ethernet network. If you're doing early bring-up work, or you don't have an Ethernet connection on a device, other network connection options are available. For more information, see these articles:
- [Set up KDNET network kernel debugging automatically](setting-up-a-network-debugging-connection-automatically.md)
- [Set up network debugging of a virtual machine - KDNET](setting-up-network-debugging-of-a-virtual-machine-host.md)

## 5. Choose either 32-bit or 64-bit debugging tools

Whether you need a 32-bit or 64-bit debugger depends on the version of Windows that runs on the target and host systems and whether you're debugging 32-bit or 64-bit code. For more information, see [Choosing 32-bit or 64-bit debugging tools](choosing-a-32-bit-or-64-bit-debugger-package.md).

## 6. Configure symbols

To use all of the advanced functionality that WinDbg provides, you must load the proper symbols. If you do not have symbols properly configured, you will receive messages indicating that symbols are not available when you attempt to use functionality that is dependent on symbols. For more information, see [Symbols for Windows debugging](symbols.md).

## 7. Configure source code

If your goal is to debug your own source code, you need to configure a path to your source code. For more information, see [Source path](source-path.md).

## 8. Become familiar with debugger operation

The [Debugger operation](debugger-operation-win8.md) section of this documentation describes debugger operation for various tasks. For example, [Loading debugger extension DLLs](../debuggercmds/loading-debugger-extension-dlls.md) explains how to load debugger extensions. 

## 9. Become familiar with debugging techniques

[Standard debugging techniques](standard-debugging-techniques.md) apply to most debugging scenarios, and examples include setting breakpoints, inspecting the call stack, and finding a memory leak. [Specialized debugging techniques](specialized-debugging-techniques.md) apply to particular technologies or types of code. Examples include Plug and Play debugging, KMDF debugging, and RPC debugging.

## 10. Use the debugger reference commands

You can use different debugging commands as you work in the debugger. Use the [.hh command](../debuggercmds/-hh--open-html-help-file-.md) in the debugger to display help information about any debugging command. For more information about available commands, see [Debugger reference](debugger-reference.md).

## 11. Use debugging extensions for specific technologies

There are multiple debugging extensions that can be used to parse domain-specific data structures. For more information, see [Specialized extensions](../debuggercmds/specialized-extensions.md).

## 12. Learn about related Windows internals

This documentation assumes that you have some knowledge about core Windows internals. To learn more about Windows internals, including memory usage, context, threads, and processes, you can review resources such as [Windows Internals](/sysinternals/resources/windows-internals) by  Pavel Yosifovich, Mark E. Russinovich, David A. Solomon and Alex Ionescu.

## 13. Review additional debugging resources

Other resources include the following books and videos:
- *Inside Windows Debugging: Practical Debugging and Tracing Strategies* by Tarik Soulami
- *Advanced Windows Debugging* by Mario Hewardt and Daniel Pravat
- [*Defrag Tools* video series](/shows/defrag-tools), episodes 13 through 29, all about WinDbg

### See also

- [Get started with WinDbg (kernel mode)](getting-started-with-windbg--kernel-mode-.md)
- [Get started with WinDbg (user mode)](getting-started-with-windbg.md)
- [Choose 32-bit or 64-bit debugging tools](choosing-a-32-bit-or-64-bit-debugger-package.md)
- [Debugging environments](debuggers-in-the-debugging-tools-for-windows-package.md)
- [Set up debugging (kernel mode and user mode)](getting-set-up-for-debugging.md)
- [Debug universal drivers - step by step lab (echo kernel mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md)
- [Debug drivers - step by step lab (Sysvad kernel mode)](debug-universal-drivers--kernel-mode-.md)
