---
title: Drawing and Filling Paths
description: Drawing and Filling Paths
ms.assetid: bc31aeba-d1f1-4e38-a8df-19e8d7e178c7
keywords:
- GDI WDK Windows 2000 display , paths
- graphics drivers WDK Windows 2000 display , paths
- drawing WDK GDI , paths
- filling paths WDK GDI
- paths WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Drawing and Filling Paths


## <span id="ddk_drawing_and_filling_paths_gg"></span><span id="DDK_DRAWING_AND_FILLING_PATHS_GG"></span>


The graphics driver considers a path to be a sequence of lines, and/or curves, defined by a path object ([**PATHOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff568849) structure). To handle the filling of closed paths, the driver supports the function [**DrvFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556220).

GDI can call [**DrvFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556220) to fill a path on a device-managed surface. GDI compares the requirements of the fill with the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure's flags GCAPS\_BEZIERS, GCAPS\_ALTERNATEFILL, and GCAPS\_WINDINGFILL, to decide whether to call the driver. If GDI does call the driver, the driver either performs the operation or returns, informing GDI that the path or clipping requested is too complex to be handled by the device. In the latter case, GDI breaks the request down into several simpler operations.

A driver can also support the optional [**DrvStrokeAndFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556311) function to fulfill requests for path fills. This function fills and strokes a path at the same time. Many GDI primitives require this functionality. If a wide line is used for stroking, the filled area must be reduced to compensate for the increased width of the bounding path.

When the driver returns **FALSE** from either the [**DrvFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556220) or [**DrvStrokeAndFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556311) functions, GDI converts the fill-path request to a set of simpler operations and calls the driver function again. If the device returns **FALSE** again on the second call to **DrvFillPath**, GDI converts the path to a clip object and then calls [**EngFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff564860). For a **FALSE** return when **DrvStrokeAndFillPath** is recalled, GDI can convert the call into separate calls to [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316) and **DrvFillPath**.

 

 





