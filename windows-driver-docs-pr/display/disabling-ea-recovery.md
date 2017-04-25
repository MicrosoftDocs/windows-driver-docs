---
title: Disabling EA Recovery
description: Disabling EA Recovery
ms.assetid: a414f1b0-acfc-4617-bf68-202bdef829ce
keywords:
- display drivers WDK Windows 2000 , debugging
- debugging drivers WDK Windows 2000 display
- EA recovery WDK Windows 2000 display
- disabled EA recovery WDK Windows 2000 display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Disabling EA Recovery


## <span id="ddk_disabling_ea_recovery_gg"></span><span id="DDK_DISABLING_EA_RECOVERY_GG"></span>


In Microsoft Windows XP SP1 and later operating systems, GDI uses a watchdog timer to monitor the time that threads spend executing in the display driver. The watchdog defines a time threshold. If a thread spends more time in a display driver than the threshold specifies, the watchdog tries to recover by switching to VGA graphics mode. If the attempt fails, the watchdog generates bug check 0xEA, THREAD\_STUCK\_IN\_DEVICE\_DRIVER.

Before attempting to recover, the watchdog will break into any debugger that is attached to the computer. You can then debug the code--as long as you have first disabled EA recovery.

In Windows XP SP1, disable EA recovery by setting the global variable **WdDisableRecovery**, which is located in *watchdog.sys*, to 1. To do so, you can enter the following **WinDbg** command:

```
ed watchdog!WdDisableRecovery 1
```

In Microsoft Windows Server 2003, disable EA recovery by setting the global variable **VpDisableRecovery**, which is located in *videoprt.sys*, to 1. To do so, you can enter the following **WinDbg** command:

```
ed videoprt!VpDisableRecovery 1
```

After you have disabled EA recovery, put breakpoints in your display driver where you suspect the code is looping, and resume execution.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Disabling%20EA%20Recovery%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




