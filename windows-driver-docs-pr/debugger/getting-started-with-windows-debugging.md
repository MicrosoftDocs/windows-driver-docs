---
title: Get started with Windows debugging
description: Learn how to get started with Windows debugging. Install WinDbg, configure your debugging environment, and master kernel-mode and user-mode debugging techniques.
ms.date: 11/04/2025
ms.topic: get-started
---

# Get started with Windows debugging

This article explains how to get started with Windows debugging using WinDbg and other debugging tools. You'll learn how to:

- Install the debugger and set up host and target systems
- Configure your debugging environment
- Master essential debugging techniques for kernel-mode and user-mode scenarios

**Note:** If you want to analyze a crash dump instead, see [Analyze crash dump files by using WinDbg](crash-dump-files.md).

To get started with Windows debugging, complete the following steps.


## 1. Install the Windows Debugger

Install WinDbg to begin debugging Windows applications and drivers. For detailed installation steps, see [Install WinDbg](index.md).


## 2. Identify the host and target systems

Two separate computer systems are typically used for debugging because instruction execution on the processor is commonly paused during the process. The debugger runs on the *host* system, and the code that you want to debug runs on the *target* system.

**Host &lt;--------------------------------------------------&gt; Target**

:::image type="content" source="images/target-host-1.png" alt-text="Screenshot of a diagram showing a double arrow connecting host and target debugging systems.":::

In some situations, it's possible to use a virtual machine as the second system. For example, a virtual PC could run on the same PC as the code that you need to debug. However, if your code communicates with low-level hardware, using a virtual PC might not be the best approach. For more information, see [Setting up network debugging of a virtual machine - KDNET](setting-up-network-debugging-of-a-virtual-machine-host.md).

## 3. Determine the debugger type: kernel mode or user mode

Next, you need to determine whether to use kernel-mode or user-mode debugging.

- The operating system and privileged programs run in *kernel mode*. Kernel-mode code has permission to access any part of the system, and it's not restricted like user-mode code. Kernel-mode code can access any part of any other process running in either user mode or kernel mode. Much of the core OS functionality and many hardware device drivers run in kernel mode.

- Applications and subsystems on the computer run in *user mode*. Processes that run in user mode do so within their own virtual address spaces. They're restricted from gaining direct access to many parts of the system, including system hardware, memory that isn't allocated for their use, and other portions of the system that might compromise system integrity. Processes that run in user mode are effectively isolated from the system and from other user-mode processes, so they can't interfere with these resources.

If your goal is to debug a driver, determine if the driver is a kernel-mode driver or a user-mode driver. Windows Driver Model (WDM) drivers and Kernel-Mode Driver Framework (KMDF) are both kernel-mode drivers. As the name suggests, User-Mode Driver Framework (UMDF) drivers are user-mode drivers.

For some issues, it can be difficult to determine which mode the code executes in. In that case, you might need to pick one mode and see what information is available in that mode. Some issues require using the debugger in both user mode and kernel mode.

Depending on which mode you debug in, you might need to configure and use the debuggers in different ways. Some debugging commands operate the same in both modes, and some commands operate differently.

### Next steps for kernel-mode debugging

- [Get started with WinDbg (kernel mode)](getting-started-with-windbg--kernel-mode-.md) - Complete setup and first debugging session
- [Debug universal drivers: step-by-step lab (echo kernel mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md) - Hands-on lab with echo driver
- [Debug drivers: step-by-step lab (Sysvad kernel mode)](debug-universal-drivers--kernel-mode-.md) - Hands-on lab with audio driver

### Next steps for user-mode debugging

- [Get started with WinDbg (user mode)](getting-started-with-windbg.md) - Complete setup and first debugging session

## 4. Choose your debugger environment

The WinDbg debugger works well in most situations, but there are times when you might want to use another debugger, such as console debuggers for automation or Visual Studio. For more information, see [Debugging environments](debuggers-in-the-debugging-tools-for-windows-package.md).

## 5. Determine how to connect the target and host

Typically, you connect target and host systems by using an Ethernet network. If you're doing early bring-up work, or you don't have an Ethernet connection on a device, other network connection options are available. For more information, see these articles:

- [Set up KDNET network kernel debugging automatically](setting-up-a-network-debugging-connection-automatically.md)
- [Set up network debugging of a virtual machine - KDNET](setting-up-network-debugging-of-a-virtual-machine-host.md)

## 6. Choose either 32-bit or 64-bit debugging tools

Whether you need a 32-bit or 64-bit debugger depends on the version of Windows that runs on the target and host systems and whether you're debugging 32-bit or 64-bit code. For more information, see [Choosing 32-bit or 64-bit debugging tools](choosing-a-32-bit-or-64-bit-debugger-package.md).

## 7. Configure symbols

To use all of the advanced functionality that WinDbg provides, you must load the proper symbols. If you don't properly configure symbols, you receive messages indicating that symbols aren't available when you attempt to use functionality that depends on symbols. For more information, see [Symbols for Windows debugging](symbols.md).

## 8. Configure source code

If your goal is to debug your own source code, you need to configure a path to your source code. For more information, see [Source path](source-path.md).

## 9. Become familiar with debugger operation

The [Debugger operation](debugger-operation-win8.md) section of this documentation describes debugger operation for various tasks. For example, [Keeping a Log File in WinDbg](keeping-a-log-file-in-windbg.md) describes how WinDbg can write a log file that records the debugging session.

## 10. Become familiar with debugging techniques

[Standard debugging techniques](standard-debugging-techniques.md) apply to most debugging scenarios, and examples include setting breakpoints, inspecting the call stack, and finding a memory leak. [Specialized debugging techniques](specialized-debugging-techniques.md) apply to particular technologies or types of code. Examples include Plug and Play debugging, KMDF debugging, and RPC debugging.

## 11. Use the debugger reference commands

You can use different debugging commands as you work in the debugger. To get help on any command while debugging, use the `.hh` command followed by the command name.

**Examples:**

```dotnetcli
.hh bp # Get help on breakpoint commands
.hh k # Get help on call stack commands
```

For a complete list of available commands, see [Debugger reference](debugger-reference.md).

## 12. Use debugging extensions for specific technologies

You can use multiple debugging extensions to parse domain-specific data structures. For more information, see [Specialized extensions](../debuggercmds/specialized-extensions.md). For information about how to load debugger extensions, see [Loading debugger extension DLLs](../debuggercmds/loading-debugger-extension-dlls.md). 

## 13. Learn about related Windows internals

This documentation assumes that you have some knowledge about core Windows internals. To learn more about Windows internals, including memory usage, context, threads, and processes, you can review resources such as [Windows Internals](/sysinternals/resources/windows-internals) by  Pavel Yosifovich, Mark E. Russinovich, David A. Solomon, and Alex Ionescu.

## 14. Review additional debugging resources

Other resources include the following books and videos:

- *Inside Windows Debugging: Practical Debugging and Tracing Strategies* by Tarik Soulami
- *Advanced Windows Debugging* by Mario Hewardt and Daniel Pravat
- [*Defrag Tools* video series](/shows/defrag-tools), episodes 13 through 29, all about WinDbg

## Next steps

Choose your debugging mode to continue:

**Kernel-mode debugging** (for drivers and OS components):

- [Get started with WinDbg (kernel mode)](getting-started-with-windbg--kernel-mode-.md)
- [Debug universal drivers - step by step lab (echo kernel mode)](debug-universal-drivers---step-by-step-lab--echo-kernel-mode-.md)

**User-mode debugging** (for applications):

- [Get started with WinDbg (user mode)](getting-started-with-windbg.md)

**Additional setup guidance:**

- [Choose 32-bit or 64-bit debugging tools](choosing-a-32-bit-or-64-bit-debugger-package.md)
- [Set up debugging (kernel mode and user mode)](getting-set-up-for-debugging.md)
- [Debugging environments](debuggers-in-the-debugging-tools-for-windows-package.md)
