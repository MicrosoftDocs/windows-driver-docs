---
title: Choosing the 32-Bit or 64-Bit Debugging Tools
description: When you install Debugging Tools for Windows, you get both a 32-bit set of tools and a 64-bit set of tools.
ms.assetid: 26aaaf11-1005-4ae7-8f27-4ae0812faa81
keywords: ["32-bit debugger package", "32-bit debugging tools", "64-bit debugger package", "64-bit debugging tools", "installation, choosing between 32-bit and 64-bit packages"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Choosing the 32-Bit or 64-Bit Debugging Tools


When you install Debugging Tools for Windows, you get both a 32-bit set of tools and a 64-bit set of tools. If you use the Microsoft Visual Studio [debugging environment](debuggers-in-the-debugging-tools-for-windows-package.md), you don't have to be concerned about whether to use the 32- or 64-bit set because Visual Studio automatically chooses the correct debugging tools.

If you are using one of the other debugging environments (WinDbg, KD, CDB, or NTSD), you have to make the choice yourself. To determine which set of debugging tools to use, you need to know the type of processor that is running on your host computer and whether the host computer is running a 32- or 64-bit version of Windows.

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*.

### <span id="Host_computer_running_a_32-bit_version_of_Windows"></span><span id="host_computer_running_a_32-bit_version_of_windows"></span><span id="HOST_COMPUTER_RUNNING_A_32-BIT_VERSION_OF_WINDOWS"></span>Host computer running a 32-bit version of Windows

If your host computer is running a 32-bit version of Windows, use the 32-bit debugging tools. (This situation applies to both x86-based and x64-based targets.)

### <span id="x64-based_host_computer_running_a_64-bit_version_of_Windows"></span><span id="x64-based_host_computer_running_a_64-bit_version_of_windows"></span><span id="X64-BASED_HOST_COMPUTER_RUNNING_A_64-BIT_VERSION_OF_WINDOWS"></span>x64-based host computer running a 64-bit version of Windows

If your host computer uses an x64-based processor and is running a 64-bit version of Windows, the following rules apply:

-   If you are analyzing a dump file, you can use either the 32-bit debugging tools or the 64-bit debugging tools. (It is not important whether the dump file is a user-mode dump file or a kernel-mode dump file, and it is not important whether the dump file was made on an x86-based or an x64-based platform.)

-   If you are performing live kernel-mode debugging, you can use either the 32-bit debugging tools or the x64 debugging tools. (This situation applies to both x86-based and x64-based targets.)

-   If you are debugging live user-mode code that is running on the same computer as the debugger, use the 64-bit tools for debugging 64-bit code and 32-bit code running on WOW64. To set the debugger for 32-bit or 64-bit mode, use the [**.effmach**](-effmach--effective-machine-.md) command.

-   If you are debugging live 32-bit user-mode code that is running on a separate target computer, use the 32-bit debugging tools.

## <span id="related_topics"></span>Related topics


[Windows Debugging](index.md)

 

 






