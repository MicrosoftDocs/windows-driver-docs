---
title: Disabling the Watchdog Timer While Testing Display Drivers
description: Disabling the Watchdog Timer While Testing Display Drivers
ms.assetid: dc0c9e64-044b-4b2c-8011-9bdbf121307c
keywords:
- display drivers WDK Windows 2000 , debugging
- debugging drivers WDK Windows 2000 display
- watchdog timers WDK Windows 2000 display
- timers WDK Windows 2000 display
- VGA WDK Windows 2000 display
- switching to VGA mode WDK Windows 2000 display
- thread watchdog timers WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Disabling the Watchdog Timer While Testing Display Drivers


## <span id="ddk_disabling_the_watchdog_timer_while_testing_display_drivers_gg"></span><span id="DDK_DISABLING_THE_WATCHDOG_TIMER_WHILE_TESTING_DISPLAY_DRIVERS_GG"></span>


In Microsoft Windows XP SP1 and later operating systems, GDI uses a watchdog timer to monitor the time that threads spend executing in the display driver. The watchdog defines a time threshold. If a thread spends more time in a display driver than the threshold specifies, the watchdog tries to recover by switching to VGA graphics mode. If the attempt fails, the watchdog generates bug check 0xEA, THREAD\_STUCK\_IN\_DEVICE\_DRIVER.

If, during debugging and testing, you use software emulation for the rendering that a display adapter will eventually perform, you might need to increase the watchdog time threshold. Otherwise, it is likely that the emulation code, which renders significantly more slowly than hardware does, will exceed the threshold.

To specify the watchdog time threshold for display drivers, create the following REG\_DWORD entry in the registry:

```registry
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Watchdog\Display\BreakPointDelay
```

Set the value of **BreakPointDelay** to the watchdog time threshold, in 10-second units. For example, a value of 200 specifies a threshold of 2,000 seconds.

If you test your display driver without an attached debugger, you can prevent the watchdog timer from generating a bug check. To do so, create the following REG\_DWORD entry in the registry, and set its value to 1:

```registry
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Watchdog\Display\DisableBugCheck
```

The techniques described in this topic are only for debugging and testing. Do not release a driver that creates or alters **BreakPointDelay** or **DisableBugCheck**.

 

 





