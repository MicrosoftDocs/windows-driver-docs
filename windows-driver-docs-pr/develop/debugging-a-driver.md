---
ms.assetid: 2274e848-2a0b-445c-82cd-7bcd9e23078a
title: Debugging a Driver
description: Typically, debugging a kernel-mode driver requires two computers.
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging a Driver

Typically, debugging a kernel-mode driver requires two computers. The debugger runs on the *host computer*, and the code being debugged runs on the *target computer*. The target computer is also called the *test computer*. You can debug a user-mode driver on the host computer or on a separate target computer. Before you can debug a driver running on a target computer, you must configure the target computer for debugging.

For information about configuring a target computer and setting up a debug cable, see [Setting Up Kernel-Mode Debugging in Visual Studio](https://msdn.microsoft.com/en-us/windows/hardware/hh439376) and [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn745909).

For information about using Microsoft Visual Studio to debug a driver, see [Debugging Using Visual Studio](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh406281).

For an example of using Visual Studio to debug a kernel-mode driver, see [Writing a KMDF driver based on a template](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439654).

For an introduction to Debugging Tools for Windows, see [Windows Debugging](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff551063).

## <span id="Video_Demonstration"></span><span id="video_demonstration"></span><span id="VIDEO_DEMONSTRATION"></span>Video Demonstration


This video demonstrates how to use the WinDbg debugging engine directly in Visual Studio instead of running WinDbg separately.

<iframe 
src="https://hubs-video.ssl.catalog.video.msn.com/embed/57464a96-8900-4194-b806-813eb1dd6ac6/IA?csid=ux-en-us&MsnPlayerLeadsWith=html&PlaybackMode=Inline&MsnPlayerDisplayShareBar=false&MsnPlayerDisplayInfoButton=false&iframe=true&QualityOverride=HD" width="720" height="405" allowFullScreen="true" frameBorder="0" scrolling="no"></iframe> 
 





