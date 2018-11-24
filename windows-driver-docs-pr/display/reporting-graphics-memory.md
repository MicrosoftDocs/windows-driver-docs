---
title: Reporting Graphics Memory
description: Reporting Graphics Memory
ms.assetid: a8a3dc08-1863-47ac-b41e-58ef38739c42
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Graphics Memory


The video memory manager reports to clients about the memory information that the display miniport driver supplies.

Operating systems prior to Windows Vista report graphics memory as a single number through the Control Panel **Display** application. Display drivers provide this number to the operating system; the operating system then reports the number to the user through the **Display** application.

The video memory manager of the [Windows Display Driver Model (WDDM)](windows-vista-display-driver-model-design-guide.md) reports an accurate account of each graphics memory contributor. The following clients use this report:

-   The Windows System Assessment Tool (WinSAT) checks for the available graphics memory and takes the action to turn off or turn on the Premium Aero Glass experience based on the amount of available memory.

-   The Desktop Window Manager (DWM) (Dwm.exe) depends on the exact state of the available graphics memory on computers with [Windows Display Driver Model (WDDM)](windows-vista-display-driver-model-design-guide.md) display drivers.

-   Microsoft DirectX games and other graphics applications must be able to get accurate values that describe the state of the graphics memory. An inaccurate graphics memory number could drastically change the game experience for the user.

The following sections describe how the video memory manager calculates graphics memory numbers and provide examples of how the memory numbers are reported:

[Calculating Graphics Memory](calculating-graphics-memory.md)

[Examples of Graphics Memory Reporting](examples-of-graphics-memory-reporting.md)

[Retrieving Graphics Memory Numbers](retrieving-graphics-memory-numbers.md)

 

 





