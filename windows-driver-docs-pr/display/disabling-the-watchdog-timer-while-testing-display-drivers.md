---
title: Disabling the Watchdog Timer While Testing Display Drivers
description: Disabling the Watchdog Timer While Testing Display Drivers
ms.assetid: dc0c9e64-044b-4b2c-8011-9bdbf121307c
keywords: ["display drivers WDK Windows 2000 , debugging", "debugging drivers WDK Windows 2000 display", "watchdog timers WDK Windows 2000 display", "timers WDK Windows 2000 display", "VGA WDK Windows 2000 display", "switching to VGA mode WDK Windows 2000 display", "thread watchdog timers WDK Windows 2000 display"]
---

# Disabling the Watchdog Timer While Testing Display Drivers


## <span id="ddk_disabling_the_watchdog_timer_while_testing_display_drivers_gg"></span><span id="DDK_DISABLING_THE_WATCHDOG_TIMER_WHILE_TESTING_DISPLAY_DRIVERS_GG"></span>


In Microsoft Windows XP SP1 and later operating systems, GDI uses a watchdog timer to monitor the time that threads spend executing in the display driver. The watchdog defines a time threshold. If a thread spends more time in a display driver than the threshold specifies, the watchdog tries to recover by switching to VGA graphics mode. If the attempt fails, the watchdog generates bug check 0xEA, THREAD\_STUCK\_IN\_DEVICE\_DRIVER.

If, during debugging and testing, you use software emulation for the rendering that a display adapter will eventually perform, you might need to increase the watchdog time threshold. Otherwise, it is likely that the emulation code, which renders significantly more slowly than hardware does, will exceed the threshold.

To specify the watchdog time threshold for display drivers, create the following REG\_DWORD entry in the registry:

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Watchdog\Display\BreakPointDelay
```

Set the value of **BreakPointDelay** to the watchdog time threshold, in 10-second units. For example, a value of 200 specifies a threshold of 2,000 seconds.

If you test your display driver without an attached debugger, you can prevent the watchdog timer from generating a bug check. To do so, create the following REG\_DWORD entry in the registry, and set its value to 1:

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Watchdog\Display\DisableBugCheck
```

The techniques described in this topic are only for debugging and testing. Do not release a driver that creates or alters **BreakPointDelay** or **DisableBugCheck**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Disabling%20the%20Watchdog%20Timer%20While%20Testing%20Display%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




