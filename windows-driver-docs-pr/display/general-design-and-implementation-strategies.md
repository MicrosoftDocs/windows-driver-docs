---
title: General Design and Implementation Strategies
description: General Design and Implementation Strategies
ms.assetid: c631062c-87ec-4bad-9de2-1844d0c81661
keywords:
- display driver model WDK Windows 2000 , strategies
- Windows 2000 display driver model WDK , strategies
- video miniport drivers WDK Windows 2000 , strategies
- display drivers WDK Windows 2000 , strategies
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# General Design and Implementation Strategies


## <span id="ddk_general_design_and_implementation_strategies_gg"></span><span id="DDK_GENERAL_DESIGN_AND_IMPLEMENTATION_STRATEGIES_GG"></span>


To design an effective Windows 2000 and later display driver and video miniport driver, consider the following strategies:

-   Modify an existing Windows Driver Kit (WDK) sample driver that was designed for a similar type of graphics adapter to reduce driver design time.

-   Use C to write as much of the driver as possible to maximize portability, using assembly language only when necessary for time-critical operations that are not well supported by the hardware. Although coding in assembly increases the potential for optimization, time and portability issues outweigh its benefits.

-   Use video miniport drivers for operations that manage resources, perform physical device memory mapping, ensure that register outputs occur in close proximity, or respond to interrupts. Miniport drivers are predominately used for handling variations within a hardware family and for minimizing display driver hardware-type dependencies.

For additional information of interest to display driver writers, see [Graphics DDI Functions for Display Drivers](graphics-ddi-functions-for-display-drivers.md). This topic and the subtopics following it discuss the graphics DDI functions that are required, conditionally required, and optional for a display driver. [Video Miniport Drivers in the Windows 2000 Display Driver Model](video-miniport-drivers-in-the-windows-2000-display-driver-model.md) and its subtopics contain similar information aimed at video miniport driver writers.

You should also consider the following facts:

-   The display driver and video miniport driver operate in the same privileged kernel-mode address space as the rest of the NT executive. A fault in either driver will cause the rest of the system to fault.

-   Display drivers and video miniport drivers can be preempted at any time.

-   The code and data sections of a display driver are both entirely pageable.

-   Exported functions must execute the standard NT-based operating system *prolog* on entry and the *epilog* on exit. For more information, see the Microsoft Windows SDK documentation.

For information that is specific to display drivers, see [Graphics DDI Functions for Display Drivers](graphics-ddi-functions-for-display-drivers.md). That section contains information about required, conditionally required, and optionally required graphics DDI functions.

 

 





