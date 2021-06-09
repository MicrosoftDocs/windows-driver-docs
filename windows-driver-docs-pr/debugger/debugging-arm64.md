---
title: Debugging ARM64
description: Debugging ARM64
keywords: ["Debugging ARM64", "Debugging", "ARM64"]
ms.date: 07/17/2018
ms.localizationpriority: medium
---

# Debugging on ARM64

This topic describes debugging Windows 10 on ARM Processors. For general information about Windows 10 on ARM, see 
[Windows 10 desktop on ARM64](/windows/uwp/porting/apps-on-arm).

In general, developers debugging user mode apps should use the version of the debugger that matches the architecture of the target app. Use the ARM64 version of WinDbg to debug user mode ARM64 applications and use the ARM version of WinDbg to debug user mode ARM32 applications. Use the x86 version of WinDbg to debug user mode x86 applications running on ARM64 processors.  

In rare cases where you need to debug system code – such as WOW64 or CHPE – you can use the ARM64 version of WinDbg. If you are debugging the ARM64 kernel from another machine, use the version of WinDbg that matches the architecture of that other machine.  


## Getting ARM  Debugging Tools for Windows 

You can get debugging tools for ARM64 by downloading the [Windows 10 SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk) (version 10.0.16299 or later).  During the installation, select the *Debugging Tools for Windows* box. 

The debugging tools are located in the `Debuggers` folder in the kit installation directory.  The x86 tools are under `Debuggers\x86`, the ARM32 tools are under `Debuggers\ARM`, and the ARM64 tools are under `Debuggers\ARM64`. 

## Debugging ARM64 Code

ARM64 WinDbg is required to debug ARM64 code. The debugging experience is similar to debugging x86 applications with x86 WinDbg on x86 Windows, except for the following differences. 

- There are 32 general purpose registers - x0 to x28 and fp, lr, sp. 
- Program counter register, pc, is not a general purpose register. 
- All general purpose registers and pc register are 64-bit in width. 
- At most 2 active data breakpoints for execution and 2 active data breakpoints for read/write memory. For more information, see [Processor Breakpoints](./processor-breakpoints---ba-breakpoints-.md). 


## Debugging x86 User Mode Code 

In the rare cases that you need to use ARM64 WinDbg to debug your x86 user mode code, you can use the following WinDbg commands to switch between contexts: 

- .effmach x86: Switch to and see x86 context, simulating the effect of using x86 WinDbg. 
- .effmach arm64: Switch to and see ARM64 context 
- .effmach chpe: Switch to and see CHPE context. 

For more information about the .effmach, see [.effmach (Effective Machine)](-effmach--effective-machine-.md).

When debugging x86 apps in user mode, regardless of which WinDbg version you are using, be aware of these considerations.

- If a thread is not being actively debugged (e.g. single-stepped, encountered a breakpoint), not reporting an exception, and not in a system call, the register context may not be up-to-date. 
- The emulator internally generates Data misaligned, Illegal instruction, In-page I/O error exceptions and handles the ones it generates. When you are using WinDbg, consider configuring these exceptions as *Ignored* under the Debug / Event Filters… menu item.  
- If using ARM64 WinDbg in user mode, single-stepping across x86 & CHPE function boundaries is not supported. To work around this, set breakpoints on the target code. 

For general information about ARM64 and WOW64 see [Running 32-bit Applications](/windows/desktop/WinProg64/running-32-bit-applications) in the 64-bit Windows programming guide. 

For information on debugging applications running under WOW64, see [Debugging WOW64](/windows/desktop/WinProg64/debugging-wow64).



## Debugging in Visual Studio 

For information on debugging ARM in Visual Studio, see [Remote Debugging](/visualstudio/debugger/remote-debugging).



## See Also

[Building ARM64 Drivers with the WDK](../develop/building-arm64-drivers.md)

[Windows Community Standup discussing the Always Connected PC](https://blogs.windows.com/buildingapps/2018/01/22/windows-community-standup-discussing-always-connected-pc/)

-------