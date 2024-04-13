---
title: Multiple-Monitor Support in the Display Driver
description: Multiple-Monitor Support in the Display Driver
keywords:
- display drivers WDK Windows 2000 , multiple monitors
- multiple monitors WDK
- multiple-monitor systems WDK Windows 2000 display
ms.date: 03/18/2022
---

# Multiple-Monitor Support in an XDDM Display Driver

Multiple-monitor support is provided by Windows 2000 and later; therefore, display driver writers must not implement any special code to provide this support.

Display drivers must be implemented without using global variables. All state must exist in the *PDEV* for a particular display driver. GDI will call [**DrvEnablePDEV**](/windows/win32/api/winddi/nf-winddi-drvenablepdev) for every hardware device extension that is created by the video miniport driver.

To track window changes in a multiple-monitor system, a driver can request GDI to create WNDOBJ objects with desktop coordinates. The driver does this by calling [**EngCreateWnd**](/windows/win32/api/winddi/nf-winddi-engcreatewnd) using the flag WO\_RGN\_DESKTOP\_COORD. See [Tracking Window Changes](tracking-window-changes.md) for more information.

In a multiple-monitor system, GDI stores the device's desktop position in the **dmPosition** member of the [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure.
