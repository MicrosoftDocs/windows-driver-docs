---
title: Plotter Driver Minidrivers
description: Plotter Driver Minidrivers
keywords:
- Plotter Driver WDK print , minidrivers
- MSPlot WDK print , minidrivers
- minidrivers WDK MSPlot
- PCD files WDK MSPlot
- .pcd files
ms.date: 01/30/2023
---

# Plotter Driver Minidrivers

[!include[Print Support Apps](../includes/print-support-apps.md)]

Model-specific minidrivers for the Microsoft Plotter Driver are vendor-supplied binary .pcd files created from text files that describe a device's characteristics.

## PCD Files

To generate a .*pcd* file, you must first create a text file using the [PCD source file format](pcd-source-file-format.md). You must then run plotgpc.exe, which is included with the Windows Driver Kit (WDK). This program will convert a text file into a binary .pcd file. Use the following command syntax:

**plotgpc***source-file-path* .txt *target-file-path* .pcd

For both the source and destination files, you must explicitly specify file name extensions; defaults aren't supported.

A sample text file that can be used as input to plotgpc.exe is included in the [sample plotter driver files](sample-plotter-driver-files.md).
