---
title: Driver design guides for display and graphics devices
description: Display and graphics device driver Design Guide
keywords:
- display driver development WDK , Windows
- graphics driver development WDK , Windows
- miniport drivers WDK display
ms.date: 03/10/2022
ms.custom: contperf-fy22q3
ms.topic: article
---

# Driver design guides for display and graphics devices

The following design guides are provided for developers of display and graphics drivers on Windows. For information about available "Video driver samples", see [Windows driver samples](../samples/index.md).

- [Windows Display Driver Model (WDDM)](windows-vista-display-driver-model-design-guide.md)

  WDDM is the display/graphics driver architecture available starting with Windows Vista. Drivers that adhere to WDDM run on Windows Vista and later.
  
- [Indirect Display Driver (IDD)](indirect-display-driver-model-overview.md)

  IDD is an architecture available starting with the Windows 10 Anniversary Update to support connecting displays without going direct to a GPU.

- [Legacy: Windows 2000 Display Driver Model (XDDM)](windows-2000-display-driver-model-design-guide.md)

  XDDM was the display/graphics driver architecture available for Windows 2000 through Windows Vista and Windows 7 only.
