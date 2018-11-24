---
title: Disabling EA Recovery
description: Disabling EA Recovery
ms.assetid: a414f1b0-acfc-4617-bf68-202bdef829ce
keywords:
- display drivers WDK Windows 2000 , debugging
- debugging drivers WDK Windows 2000 display
- EA recovery WDK Windows 2000 display
- disabled EA recovery WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Disabling EA Recovery


## <span id="ddk_disabling_ea_recovery_gg"></span><span id="DDK_DISABLING_EA_RECOVERY_GG"></span>


In Microsoft Windows XP SP1 and later operating systems, GDI uses a watchdog timer to monitor the time that threads spend executing in the display driver. The watchdog defines a time threshold. If a thread spends more time in a display driver than the threshold specifies, the watchdog tries to recover by switching to VGA graphics mode. If the attempt fails, the watchdog generates bug check 0xEA, THREAD\_STUCK\_IN\_DEVICE\_DRIVER.

Before attempting to recover, the watchdog will break into any debugger that is attached to the computer. You can then debug the code--as long as you have first disabled EA recovery.

In Windows XP SP1, disable EA recovery by setting the global variable **WdDisableRecovery**, which is located in *watchdog.sys*, to 1. To do so, you can enter the following **WinDbg** command:

```cmd
ed watchdog!WdDisableRecovery 1
```

In Microsoft Windows Server 2003, disable EA recovery by setting the global variable **VpDisableRecovery**, which is located in *videoprt.sys*, to 1. To do so, you can enter the following **WinDbg** command:

```cmd
ed videoprt!VpDisableRecovery 1
```

After you have disabled EA recovery, put breakpoints in your display driver where you suspect the code is looping, and resume execution.

 

 





