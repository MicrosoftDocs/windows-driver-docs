---
title: Disabling Timeout Recovery for Display Drivers
description: Disabling Timeout Recovery for Display Drivers
ms.assetid: 71fa0273-be21-4603-8491-09078a38cdf2
keywords: ["display drivers WDK Windows 2000 , timeout recovery", "timeout recovery WDK Windows 2000 display"]
---

# Disabling Timeout Recovery for Display Drivers


In Microsoft Windows XP SP1 and later operating systems, GDI uses a watchdog timer to monitor the time that threads spend executing in the display driver. The watchdog defines a time threshold. If a thread spends more time in a display driver than the threshold specifies, the watchdog tries to recover by switching to VGA graphics mode. If the attempt fails, the watchdog generates bug check 0xEA, THREAD\_STUCK\_IN\_DEVICE\_DRIVER.

Because timeout recovery code is complex, it might cause incompatibility with display drivers. To resolve the compatibility problems, timeout recovery can be disabled.

To disable timeout recovery, create the following REG\_DWORD entry in the registry, and set its value to 0:

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Watchdog\Display\EaRecovery
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Disabling%20Timeout%20Recovery%20for%20Display%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




