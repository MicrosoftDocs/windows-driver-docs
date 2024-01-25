---
title: Task Manager Live Memory Dump
description: This topic describes how to take a live kernel memory dump using task manger.
ms.date: 09/18/2023
---

# Task Manager live memory dump

## Overview

Task Manager can be used to create a live kernel memory dump. This is in addition to the existing capability of using Task Manager to create a memory dump of a specific process.

A live kernel memory dump contains a consistent snapshot of kernel memory (and optionally, other types of memory) and saves it to a dump file. Unlike other methods to manually generate a kernel memory dump, this method does not cause a system crash.

Programmers with access to appropriate symbol files and source code can analyze the dump file to examine system state and diagnose problems.

The option to create a live kernel memory dump is available on the *System* process, similar to how an option to create a memory dump file is available on user-mode processes.

A *Full live kernel memory dump* contains active kernel memory, with optional inclusion of hypervisor memory and user-mode memory.  The options to capture hypervisor and user pages are available for full live kernel dumps.  Alternatively, a *Kernel stacks memory dump* is a smaller file, limited to kernel processor states and all kernel thread stacks.  

For general information about live kernel memory dumps, see [Kernel Live Memory Dump Code Reference](bug-check-code-reference-live-dump.md).

The Task Manager live dump feature was released in early 2023 and was first available in Windows Insider Preview builds in the Canary Channel (Build 25276 and higher) and Dev Channel (Build 23419 and higher) and in July 2023, is available in Windows [OS build 22621.1992](https://support.microsoft.com/topic/july-11-2023-kb5028185-os-build-22621-1992-605fa18f-bd49-41d8-80b1-245080e26c3d) and later.

## Create a live kernel memory dump of the system using Task Manager

To capture a live kernel memory dump using Task Manager, complete the following steps.

1. Start Windows Task Manager.

2. Navigate to **Processes** or **Details**.

3. Locate the *System* process.

4. Right click and select **Create live kernel memory dump file**.

5. From the pull down menu, select either a **Full live kernel memory dump** or a **Kernel Stacks memory dump**.

:::image type="content" source="images/task-manager-live-dump-ui.png" alt-text="Screenshot of Task Manager live memory dump user interface.":::

## Creating a memory dump for a user-mode process

A similar procedure is used in Task Manager to create a memory dump of a process. Highlight the desired user-mode process and then right click and select **Create memory dump file**. For more information about user-mode dump files, see [User-Mode Dump Files](user-mode-dump-files.md).

## Live kernel memory dump file advanced options

The live kernel memory dump file options are available under the Task Manager settings.

:::image type="content" source="images/task-manager-live-dump-options-ui.png" alt-text="Screenshot of Task Manager live memory dump advanced options user interface.":::

The top button will revert the live kernel memory dump settings to their defaults.

When *The abort if memory pressure* option is selected the live dump process will be stopped if memory availability is not considered to be sufficient. This is the default setting to minimize the potential impact of capturing the live kernel dump on system responsiveness.

The Kernel live memory dump file settings provides several options for what information to include in the memory dump.

- *Capture Hypervisor memory pages* (with or without nonessential pages)
- *Capture User Pages*

Adding additional information to the dump file increases its size and will use additional memory as the memory dump is being recorded.

### Capture Hypervisor memory pages

Select the *Capture Hypervisor memory pages* option, to capture memory regions that are used by the hypervisor to support Hyper-V and virtual machines. For more information see [Hyper-V on Windows](/virtualization/hyper-v-on-windows/).

You can include or not include nonessential hypervisor memory pages.

### Capture User Pages

Enable *Capture User Pages* if the problem you are troubleshooting requires user-mode memory.  

For general information about Windows memory and page usage, see [Windows Internals by Pavel Yosifovich, Alex Ionescu, Mark Russinovich and David Solomon](/sysinternals/resources/windows-internals).

## Live memory dump file location

When the memory dump completes, a dialog box is displayed that provides the location of the memory dump `.dmp` file. Click on *Open File Location* to open the folder.

### Live kernel memory dumps

The live kernel memory dumps by default are stored here.

`%LocalAppData%\Microsoft\Windows\TaskManager\LiveKernelDumps`

%LocalAppData% is typically `C:\Users\<YourUserName>\AppData\Local\`

### Live user-mode memory dumps

Live user-mode memory dump files are stored in the %localappdata%\Temp directory, which is typically located in the Users directory.

`C:\Users\<YourUserName>\AppData\Local\Temp`

## Troubleshooting taking a live memory dump

If the live memory dump return an error, check the error message for details. For example:

- Task Manager needs to be running as an Administrator level user.

- With timeout issues, try taking the dump again in a few minutes.

- Wait for any requested dump to complete before taking any additional memory dumps.

- It is possible the live kernel memory dump creation succeeds, but may not contain the complete contents of memory. The capture temporarily requires enough available free physical memory to hold a copy of the memory to be written to the dump file.  Closing unneeded applications or disabling the capture of hyper-V and user-mode memory pages may increase the amount of memory that can be saved to the dump file.

## Analyzing live memory dump files

When a live memory dump occurs, the dump file can be analyzed using the same techniques used for other memory dump files. To understand the contents of memory during a failure, knowledge of processor memory registers and assembly programming is typically required. In addition, access to the failing source code will enable the issue to be fixed by the developer.

For more information, see:

- [Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

- [!analyze](../debuggercmds/-analyze.md)

- [Kernel Live Memory Dump Code Reference](bug-check-code-reference-live-dump.md)

## Bug Check Code: 0x161 - LIVE_SYSTEM_DUMP

The bug check code for a Task Manager live memory dump is [Bug Check 0x161: LIVE_SYSTEM_DUMP](bug-check-0x161--live-system-dump.md).

## See also

- [Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md).

- [Bug Check 0x161: LIVE_SYSTEM_DUMP](bug-check-0x161--live-system-dump.md)
 
- [Generate a kernel or complete crash dump](/troubleshoot/windows-client/performance/generate-a-kernel-or-complete-crash-dump)
