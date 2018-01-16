---
title: Debugging WinLogon
description: Debugging WinLogon
ms.assetid: 408727cd-fb59-44fe-b896-88317d2bc087
keywords: ["WinLogon debugging", "NTSD, debugging CSRSS", "controlling the user-mode debugger from the kernel debugger, debugging WinLogon"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging WinLogon


## <span id="ddk_debugging_winlogon_with_ntsd_dbg"></span><span id="DDK_DEBUGGING_WINLOGON_WITH_NTSD_DBG"></span>


WinLogon is the user-mode process that handles the task of interactive users logging on and logging off, and handles all instances of CTRL+ALT+DELETE.

### <span id="controlling_ntsd_from_the_kernel_debugger"></span><span id="CONTROLLING_NTSD_FROM_THE_KERNEL_DEBUGGER"></span>Controlling NTSD from the Kernel Debugger

The easiest way to debug WinLogon is to use NTSD and [control it from the kernel debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md).

### <span id="enabling_winlogon_debugging"></span><span id="ENABLING_WINLOGON_DEBUGGING"></span>Enabling WinLogon Debugging

Because you will be redirecting the user-mode debugger output to the kernel debugger, you will need to set up a kernel debugging connection. See [Getting Set Up for Debugging](getting-set-up-for-debugging.md).

To attach a debugger to WinLogon, you must go through the registry so the process is debugged from the time it starts up. To set up WinLogon debugging, set **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\WinLogon.EXE\\Debugger** to:

```
ntsd -d -x -g 
```

The **-d** option passes control to the kernel debugger. The **-x** option causes the debugger to capture access violations as second-chance exceptions. The **-g** option causes the WinLogon process to run after the attachment. Do not add the **-g** if you want to start debugging before Winlogon.exe begins (for example, if you want to set an initial breakpoint).

In addition, you should set the GlobalFlag value under the **winlogon.exe** key to REG\_DWORD "0x000400F0". This sets heap checking and FLG\_ENABLE\_KDEBUG\_SYMBOL\_LOAD. However, since this second flag only affects the kernel debugger, symbols must also be copied to the target computer before starting the debugger.

The registry change requires a reboot to take effect.

### <span id="performing_the_debugging"></span><span id="PERFORMING_THE_DEBUGGING"></span>Performing the Debugging

After the next reboot, the debugger will break into WinLogon automatically.

See [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md) for an explanation of how to proceed.

You will have to set your symbol path to a location on your host computer or to some other location on your network. When WinLogon is being debugged, network authentication on the target computer will not work properly.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20WinLogon%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




