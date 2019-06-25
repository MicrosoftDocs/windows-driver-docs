---
ms.assetid: 2274e848-2a0b-445c-82cd-7bcd9e23078a
title: Debugging a Driver
description: Typically, debugging a kernel-mode driver requires two computers.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Debugging a Driver

Typically, debugging a kernel-mode driver requires two computers. The debugger runs on the *host computer*, and the code being debugged runs on the *target computer*. The target computer is also called the *test computer*. You can debug a user-mode driver on the host computer or on a separate target computer. Before you can debug a driver running on a target computer, you must configure the target computer for debugging.

For information about configuring a target computer and setting up a debug cable, see [Setting Up Kernel-Mode Debugging in Visual Studio](https://docs.microsoft.com/windows-hardware/drivers/debugger/setting-up-kernel-mode-debugging-in-visual-studio) and [Provision a computer for driver deployment and testing (WDK 8.1)](https://docs.microsoft.com/windows-hardware/drivers/gettingstarted/provision-a-target-computer-wdk-8-1).

For information about using Microsoft Visual Studio to debug a driver, see [Debugging Using Visual Studio](https://docs.microsoft.com/windows-hardware/drivers/debugger/debugging-using-visual-studio).

For an example of using Visual Studio to debug a kernel-mode driver, see [Writing a KMDF driver based on a template](https://docs.microsoft.com/windows-hardware/drivers/gettingstarted/writing-a-kmdf-driver-based-on-a-template).

For an introduction to Debugging Tools for Windows, see [Windows Debugging](https://docs.microsoft.com/windows-hardware/drivers/debugger/index).

## <span id="Video_Demonstration"></span><span id="video_demonstration"></span><span id="VIDEO_DEMONSTRATION"></span>Video Demonstration


This video demonstrates how to use the WinDbg debugging engine directly in Visual Studio instead of running WinDbg separately.

>[!VIDEO https://www.microsoft.com/videoplayer/embed/57464a96-8900-4194-b806-813eb1dd6ac6]





