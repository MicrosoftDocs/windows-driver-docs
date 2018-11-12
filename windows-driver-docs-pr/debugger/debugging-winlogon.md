---
title: Debugging WinLogon
description: Debugging WinLogon
ms.assetid: 408727cd-fb59-44fe-b896-88317d2bc087
keywords: ["WinLogon debugging", "NTSD, debugging CSRSS", "controlling the user-mode debugger from the kernel debugger, debugging WinLogon"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging WinLogon


## <span id="ddk_debugging_winlogon_with_ntsd_dbg"></span><span id="DDK_DEBUGGING_WINLOGON_WITH_NTSD_DBG"></span>


WinLogon is the user-mode process that handles the task of interactive users logging on and logging off, and handles all instances of CTRL+ALT+DELETE.

### <span id="controlling_ntsd_from_the_kernel_debugger"></span><span id="CONTROLLING_NTSD_FROM_THE_KERNEL_DEBUGGER"></span>Controlling NTSD from the Kernel Debugger

The easiest way to debug WinLogon is to use NTSD and [control it from the kernel debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md).

### <span id="enabling_winlogon_debugging"></span><span id="ENABLING_WINLOGON_DEBUGGING"></span>Enabling WinLogon Debugging

Because you will be redirecting the user-mode debugger output to the kernel debugger, you will need to set up a kernel debugging connection. See [Getting Set Up for Debugging](getting-set-up-for-debugging.md).

To attach a debugger to WinLogon, you must go through the registry so the process is debugged from the time it starts up. To set up WinLogon debugging, set **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\WinLogon.EXE\\Debugger** to:

```console
ntsd -d -x -g 
```

The **-d** option passes control to the kernel debugger. The **-x** option causes the debugger to capture access violations as second-chance exceptions. The **-g** option causes the WinLogon process to run after the attachment. Do not add the **-g** if you want to start debugging before Winlogon.exe begins (for example, if you want to set an initial breakpoint).

In addition, you should set the GlobalFlag value under the **winlogon.exe** key to REG\_DWORD "0x000400F0". This sets heap checking and FLG\_ENABLE\_KDEBUG\_SYMBOL\_LOAD. However, since this second flag only affects the kernel debugger, symbols must also be copied to the target computer before starting the debugger.

The registry change requires a reboot to take effect.

### <span id="performing_the_debugging"></span><span id="PERFORMING_THE_DEBUGGING"></span>Performing the Debugging

After the next reboot, the debugger will break into WinLogon automatically.

See [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md) for an explanation of how to proceed.

You will have to set your symbol path to a location on your host computer or to some other location on your network. When WinLogon is being debugged, network authentication on the target computer will not work properly.

 

 





