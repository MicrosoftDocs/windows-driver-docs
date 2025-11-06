---
title: Generate Live Kernel Dumps Using Task Manager
description: Learn how to generate live kernel memory dumps using Task Manager to capture system state for debugging. Includes step-by-step instructions and advanced configuration options.
ms.date: 11/04/2025
ms.topic: concept-article
---

# Task Manager live memory dump

## Overview

Use Task Manager to create a live kernel memory dump. This feature complements the existing capability of Task Manager to create a memory dump for a specific process.

A live kernel memory dump contains a consistent snapshot of kernel memory and optionally other types of memory. It saves this snapshot to a dump file. Unlike other methods for manually generating a kernel memory dump, this method doesn't cause a system crash.

Programmers with access to the appropriate symbol files and source code can analyze the dump file to examine system state and diagnose problems.

You can create a live kernel memory dump from the *System* process. This process is similar to how you can create a memory dump file for user-mode processes.

A *Full live kernel memory dump* contains active kernel memory, with optional inclusion of hypervisor memory and user-mode memory.  The options to capture hypervisor and user pages are available for full live kernel dumps.  Alternatively, a *Kernel stacks memory dump* is a smaller file, limited to kernel processor states and all kernel thread stacks.  

For general information about live kernel memory dumps, see [Kernel Live Memory Dump Code Reference](kernel-live-dump-code-reference.md).

The Task Manager live dump feature was released in early 2023. It was first available in Windows Insider Preview builds in the Canary Channel (Build 25276 and higher) and Dev Channel (Build 23419 and higher). In July 2023, it became available in Windows [OS build 22621.1992](https://support.microsoft.com/topic/july-11-2023-kb5028185-os-build-22621-1992-605fa18f-bd49-41d8-80b1-245080e26c3d) and later.

## Create a live kernel memory dump of the system by using Task Manager

To capture a live kernel memory dump by using Task Manager, complete the following steps.

1. Start Windows Task Manager.

1. Go to **Processes** or **Details**.

1. Find the *System* process.

1. Right-click the process and select **Create live kernel memory dump file**.

1. From the pull-down menu, select either a **Full live kernel memory dump** or a **Kernel Stacks memory dump**.

:::image type="content" source="images/task-manager-live-dump-ui.png" alt-text="Screenshot of Task Manager showing the System process with a context menu displaying Full live kernel memory dump and Kernel Stacks memory dump options.":::

## Create a memory dump for a user-mode process

Use a similar procedure in Task Manager to create a memory dump of a process. Highlight the user-mode process you want, then right-click and select **Create memory dump file**. For more information about user-mode dump files, see [User-Mode Dump Files](user-mode-dump-files.md).

## Live kernel memory dump file advanced options

You can find the live kernel memory dump file options under the Task Manager settings.

:::image type="content" source="images/task-manager-live-dump-options-ui.png" alt-text="Screenshot of Task Manager settings showing live kernel memory dump advanced options including Capture Hypervisor memory pages and Capture User Pages checkboxes.":::

The top button reverts the live kernel memory dump settings to their defaults.

When you select *The abort if memory pressure* option, the live dump process stops if memory availability isn't sufficient. This default setting minimizes the potential impact of capturing the live kernel dump on system responsiveness.

The Kernel live memory dump file settings provide several options for what information to include in the memory dump.

- *Capture Hypervisor memory pages* (with or without nonessential pages)
- *Capture User Pages*

Adding extra information to the dump file increases its size and uses more memory as the memory dump is being recorded.

### Capture Hypervisor memory pages

Select the *Capture Hypervisor memory pages* option to capture memory regions that the hypervisor uses to support Hyper-V and virtual machines. For more information, see [Hyper-V on Windows](/virtualization/hyper-v-on-windows/).

You can choose to include or not include nonessential hypervisor memory pages.

### Capture User Pages

Enable *Capture User Pages* if the problem you're troubleshooting requires user-mode memory.  

For general information about Windows memory and page usage, see [Windows Internals by Pavel Yosifovich, Alex Ionescu, Mark Russinovich and David Solomon](/sysinternals/resources/windows-internals).

## Live memory dump file location

When the memory dump completes, a dialog box appears that provides the location of the memory dump `.dmp` file. Select *Open File Location* to open the folder.

### Live kernel memory dumps

By default, the live kernel memory dumps are stored in the following location:

`%LocalAppData%\Microsoft\Windows\TaskManager\LiveKernelDumps`

%LocalAppData% is typically `C:\Users\<YourUserName>\AppData\Local\`

### Live user-mode memory dumps

The live user-mode memory dump files are stored in the `%localappdata%\Temp` directory, which is typically located in the Users directory.

`C:\Users\<YourUserName>\AppData\Local\Temp`

## Troubleshooting taking a live memory dump

If the live memory dump returns an error, check the error message for details. For example:

- Task Manager needs to be running as an administrator level user.

- With timeout issues, try taking the dump again in a few minutes.

- Wait for any requested dump to complete before taking any additional memory dumps.

- It's possible the live kernel memory dump creation succeeds, but doesn't contain the complete contents of memory. The capture temporarily requires enough available free physical memory to hold a copy of the memory to be written to the dump file.  Closing unneeded applications or disabling the capture of Hyper-V and user-mode memory pages might increase the amount of memory that can be saved to the dump file.

## Analyzing live memory dump files

When a live memory dump occurs, you can analyze the dump file by using the same techniques you use for other memory dump files. To understand the contents of memory during a failure, you typically need knowledge of processor memory registers and assembly programming. In addition, access to the failing source code enables the developer to fix the issue.

For more information, see:

- [Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

- [!analyze](../debuggercmds/-analyze.md)

- [Kernel Live Memory Dump Code Reference](kernel-live-dump-code-reference.md)

## Bug check code: 0x161 - LIVE_SYSTEM_DUMP

The bug check code for a Task Manager live memory dump is [Bug Check 0x161: LIVE_SYSTEM_DUMP](bug-check-0x161--live-system-dump.md).

## See also

- [Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md).

- [Bug Check 0x161: LIVE_SYSTEM_DUMP](bug-check-0x161--live-system-dump.md)
 
- [Generate a kernel or complete crash dump](/troubleshoot/windows-client/performance/generate-a-kernel-or-complete-crash-dump)
