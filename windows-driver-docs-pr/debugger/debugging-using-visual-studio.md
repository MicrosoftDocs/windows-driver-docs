---
title: Debugging Using Visual Studio
description: Starting with Windows Driver Kit (WDK) 8, the driver development environment and the Windows debuggers are integrated into Microsoft Visual Studio.
ms.assetid: B961B0C9-FF6C-4F6B-AC15-CA1B405A4C4C
ms.author: domars
ms.date: 05/11/2018
ms.localizationpriority: medium
---

# Debugging Using Visual Studio

Starting with Windows Driver Kit (WDK) 8, the driver development environment and the Windows debuggers are integrated into Microsoft Visual Studio. In this integrated environment, most of the tools you need for coding, building, packaging, testing, debugging, and deploying a driver are available in the Visual Studio user interface.

> [!IMPORTANT]
> This feature is not available in Windows 10, version 1507 and later versions of the WDK.
>
 
To get the integrated environment, first install Visual Studio, and then install the Windows Driver Kit (WDK). For more information, see [Windows Driver Kit (WDK)](https://go.microsoft.com/fwlink/p?linkid=391063).

Typically kernel-mode debugging requires two computers. The debugger runs on the *host computer*, and the code being debugged runs on the *target computer*. The target computer is also called the *test computer*. You can do user-mode debugging on a single computer, but in some cases you might want to debug a user-mode process that is running on a separate target computer.

In the Visual Studio environment, you can configure target computers for kernel-mode and user-mode debugging. You can establish a kernel-mode debugging session. You can attach to a user-mode process or launch and debug a user mode process on the host computer or a target computer. You can analyze dump files. In Visual Studio you can sign, deploy, install, and load a driver on a target computer.

These topics show you how to use Visual Studio to perform several of the tasks involved in debugging a driver.

## <span id="in_this_section"></span>In this section


-   [Debugging a User-Mode Process Using Visual Studio](debugging-a-user-mode-process-using-visual-studio.md)
-   [Opening a Dump File Using Visual Studio](opening-a-crash-dump-file-using-visual-studio.md)
-   [Kernel-Mode Debugging in Visual Studio](performing-kernel-mode-debugging-using-visual-studio.md)
-   [Ending a Debugging Session in Visual Studio](ending-a-debugging-session-in-visual-studio.md)
-   [Setting Symbol and Executable Image Paths in Visual Studio](setting-symbol-and-source-paths-in-visual-studio.md)
-   [Remote Debugging Using Visual Studio](remote-debugging-using-visual-studio.md)
-   [Entering Debugger Commands in Visual Studio](entering-debugger-commands-in-visual-studio.md)
-   [Setting Breakpoints in Visual Studio](setting-breakpoints-in-visual-studio.md)
-   [Viewing the Call Stack in Visual Studio](viewing-the-call-stack-in-visual-studio.md)
-   [Source Code Debugging in Visual Studio](viewing-source-and-assembly-code-in-visual-studio.md)
-   [Viewing and Editing Memory and Registers in Visual Studio](viewing-memory--variables--and-registers-in-visual-studio.md)
-   [Controlling Threads and Processes in Visual Studio](viewing-threads-and-processes-in-visual-studio.md)
-   [Configuring Exceptions and Events in Visual Studio](configuring-exceptions-and-events-in-visual-studio.md)
-   [Keeping a Log File in Visual Studio](keeping-a-log-file-in-visual-studio.md)

 

 





