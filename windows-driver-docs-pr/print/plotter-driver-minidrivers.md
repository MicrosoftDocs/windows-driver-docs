---
title: Plotter Driver Minidrivers
description: Plotter Driver Minidrivers
ms.assetid: f7223a0a-df02-4a4f-a3d6-7910aed926eb
keywords:
- Plotter Driver WDK print , minidrivers
- MSPlot WDK print , minidrivers
- minidrivers WDK MSPlot
- PCD files WDK MSPlot
- .pcd files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Plotter Driver Minidrivers





Model-specific minidrivers for the Microsoft Plotter Driver are vendor-supplied binary .pcd files created from text files that describe a device's characteristics.

### <a href="" id="ddk-pcd-files-gg"></a>PCD Files

To generate a .[*pcd*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-plotter-characterization-data--pcd-) file, you must first create a text file using the [PCD source file format](pcd-source-file-format.md). You must then run plotgpc.exe, which is included with the Windows Driver Kit (WDK). This program will convert a text file into a binary .pcd file. Use the following command syntax:

**plotgpc***source-file-path* .txt *target-file-path* .pcd

For both the source and destination files, you must explicitly specify file name extensions; defaults are not supported.

A sample text file that can be used as input to plotgpc.exe is included in the [sample plotter driver files](sample-plotter-driver-files.md).

 

 




