---
title: Disabling Timeout Recovery for Display Drivers
description: Disabling Timeout Recovery for Display Drivers
ms.assetid: 71fa0273-be21-4603-8491-09078a38cdf2
keywords:
- display drivers WDK Windows 2000 , timeout recovery
- timeout recovery WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Disabling Timeout Recovery for Display Drivers


In Microsoft Windows XP SP1 and later operating systems, GDI uses a watchdog timer to monitor the time that threads spend executing in the display driver. The watchdog defines a time threshold. If a thread spends more time in a display driver than the threshold specifies, the watchdog tries to recover by switching to VGA graphics mode. If the attempt fails, the watchdog generates bug check 0xEA, THREAD\_STUCK\_IN\_DEVICE\_DRIVER.

Because timeout recovery code is complex, it might cause incompatibility with display drivers. To resolve the compatibility problems, timeout recovery can be disabled.

To disable timeout recovery, create the following REG\_DWORD entry in the registry, and set its value to 0:

```registry
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Watchdog\Display\EaRecovery
```

 

 





