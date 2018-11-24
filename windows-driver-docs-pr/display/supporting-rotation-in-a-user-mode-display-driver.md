---
title: Supporting Rotation in a User-Mode Display Driver
description: Supporting Rotation in a User-Mode Display Driver
ms.assetid: fb80e875-26d4-4928-9268-2c6b36bb5d20
keywords:
- user-mode display drivers WDK Windows Vista , rotation
- rotation WDK display
- surface rotation WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Rotation in a User-Mode Display Driver


A user-mode display driver supports rotation differently, depending on many factors. For example, the user-mode display driver must behave differently for full-screen devices than it does for windowed devices. Also, the primary surfaces are created differently based on whether the desktop window manager (DWM) is running, the graphics adapter supports Microsoft DirectX 9L, or the DirectX 9L application is rotation-aware.

The following topics describe how a user-mode display driver supports rotation for different situations:

[Windowed-Mode Behavior](windowed-mode-behavior.md)

[Full-Screen-Mode Behavior](full-screen-mode-behavior.md)

[DirectX Runtime Behavior](directx-runtime-behavior.md)

 

 





