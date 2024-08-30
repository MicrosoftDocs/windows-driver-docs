---
title: Reporting Graphics Memory
description: Reporting Graphics Memory
keywords:
- graphics memory, WDDM display
- video memory manager, reporting graphics memory
ms.date: 08/29/2024
---

# Reporting Graphics Memory

WDDM's [video memory manager](video-memory-management-and-gpu-scheduling.md) (*VidMm*) reports an accurate account of each graphics memory contributor to clients. These reports of available memory can be found through the **Display** application.

The following clients use this report:

* The [Windows System Assessment Tool](/windows-hardware/manufacture/desktop/configure-windows-system-assessment-test-scores) (WinSAT) checks for the available graphics memory and takes the action to turn off or turn on the Premium Aero Glass experience based on the amount of available memory.

* The Desktop Window Manager (DWM; *Dwm.exe*) depends on the exact state of the available graphics memory on computers with [WDDM](windows-vista-display-driver-model-design-guide.md) display drivers.

* DirectX games and other graphics applications must be able to get accurate values that describe the state of the graphics memory. An inaccurate graphics memory number could drastically change the game experience for the user.

Operating systems prior to Windows Vista report graphics memory as a single number through the Control Panel **Display** application. The OS receives this number directly from the display driver.

Related articles include:

* [Calculating Graphics Memory](calculating-graphics-memory.md)

* [Examples of Graphics Memory Reporting](examples-of-graphics-memory-reporting.md)

* [Retrieving Graphics Memory Numbers](retrieving-graphics-memory-numbers.md)
