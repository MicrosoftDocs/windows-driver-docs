---
title: Local Kernel-Mode Debugging
description: Local Kernel-Mode Debugging
ms.assetid: e66dc23b-9254-4148-9828-d27c30bfa492
keywords: ["local kernel debugging", "local kernel debugging, commands available", "local kernel debugging, LiveKD tool", "LiveKD tool"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Local Kernel-Mode Debugging


Debugging Tools for Windows supports *local kernel debugging*. This is kernel-mode debugging on a single computer. In other words, the debugger runs on the same computer that is being debugged.

## <span id="starting_local_kernel_debugging"></span><span id="STARTING_LOCAL_KERNEL_DEBUGGING"></span>Setting Up Local Kernel-Mode Debugging


For information on setting up local kernel-mode debugging, see [Setting Up Local Kernel-Mode Debugging of a Single Computer Manually](setting-up-local-kernel-debugging-of-a-single-computer-manually.md).

## <span id="Starting_the_Debugging_Session"></span><span id="starting_the_debugging_session"></span><span id="STARTING_THE_DEBUGGING_SESSION"></span>Starting the Debugging Session


### <span id="Using_WinDbg"></span><span id="using_windbg"></span><span id="USING_WINDBG"></span>Using WinDbg

Open WinDbg as Administrator. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **Local** tab. Click **OK**.

You can also start a session with WinDbg by opening a Command Prompt window as Administrator and entering the following command:

**windbg -kl**

### <span id="Using_KD"></span><span id="using_kd"></span><span id="USING_KD"></span>Using KD

Open a Command Prompt window as Administrator, and enter the following command:

**kd -kl**

## <span id="commands_that_are_not_available"></span><span id="COMMANDS_THAT_ARE_NOT_AVAILABLE"></span>Commands That Are Not Available


Not all commands are available in a local kernel debugging session. Typically, you cannot use any command that causes the target computer to stop, even momentarily, because you cannot resume operation.

In particular, you cannot use the following commands:

-   Execution commands, such as **g (Go)**, **p (Step)**, **t (Trace)**, **wt (Trace and Watch Data)**, **tb (Trace to Next Branch)**, **gh (Go with Exception Handled)**, and **gn (Go with Exception Not Handled)**

-   Shutdown and dump file commands, such as **.crash**, **.dump**, and **.reboot**

-   Breakpoint commands, such as **bp**, **bu**, **ba**, **bc**, **bd**, **be**, and **bl**

-   Register display commands, such as **r** and variations

-   Stack trace commands, such as **k** and variations

If you are performing local kernel debugging with WinDbg, all of the equivalent menu commands and buttons are also unavailable.

## <span id="commands_that_are_available"></span><span id="COMMANDS_THAT_ARE_AVAILABLE"></span>Commands That Are Available


All memory input and output commands are available. You can freely read from user memory and kernel memory. You can also write to memory. Make sure that you do not write to the wrong part of kernel memory, because it can corrupt data structures and frequently causes the computer to stop responding (that is, *crash*).

## <span id="difficulties_in_performing_local_kernel_debugging"></span><span id="DIFFICULTIES_IN_PERFORMING_LOCAL_KERNEL_DEBUGGING"></span>Difficulties in Performing Local Kernel Debugging


Local kernel debugging is a very delicate operation. Be careful that you do not corrupt or crash the system.

One of the most difficult aspects of local kernel debugging is that the machine state is constantly changing. Memory is paged in and out, the active process constantly changes, and virtual address contexts do not remain constant. However, under these conditions, you can effectively analyze things that change slowly, such as certain device states.

Kernel-mode drivers and the Windows operating system frequently send messages to the kernel debugger by using **DbgPrint** and related functions. These messages are not automatically displayed during local kernel debugging. You can display them by using the [**!dbgprint**](-dbgprint.md) extension.

## <span id="livekd"></span><span id="LIVEKD"></span>LiveKD


The LiveKD tool simulates local kernel debugging. This tool creates a "snapshot" dump file of the kernel memory, without actually stopping the kernel while this snapshot is made. (Therefore, the snapshot might not actually show a single instant state of the computer.)

LiveKD is not part of the Debugging Tools for Windows package. You can download [LiveKd](https://go.microsoft.com/fwlink/p/?linkid=56552) from the Windows Sysinternals site.

 

 





