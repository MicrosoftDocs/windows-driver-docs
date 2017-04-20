---
title: Reporting Graphics Memory
description: Reporting Graphics Memory
ms.assetid: a8a3dc08-1863-47ac-b41e-58ef38739c42
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Reporting%20Graphics%20Memory%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




