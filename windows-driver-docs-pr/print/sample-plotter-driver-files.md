---
title: Sample Plotter Driver Files
description: Sample Plotter Driver Files
ms.assetid: d72bcb9a-62d7-4deb-9d6c-7431e67be77c
keywords:
- Plotter Driver WDK print , samples
- MSPlot WDK print , samples
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample Plotter Driver Files





The Windows Driver Kit (WDK) includes the following MSPlot sample code:

-   Source code for the [plotter driver user interface](plotter-driver-user-interface.md) DLL (plotui.dll)

-   Source code for the [plotter driver renderer](plotter-driver-renderer.md) (plotter.dll)

-   Source code for plotgpc.exe, which generates .pcd files.

-   A sample minidriver text file, which can be used as input to plotgpc.exe.

Samples are located in a subdirectory of the directory tree that contain the WDK samples. The plotter driver renderer (plotter.dll) can be compiled as either a user-mode or a kernel-mode DLL. For more information, see [Choosing User Mode or Kernel Mode](choosing-user-mode-or-kernel-mode.md).

 

 




