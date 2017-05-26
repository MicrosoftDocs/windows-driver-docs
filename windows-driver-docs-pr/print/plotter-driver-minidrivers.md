---
title: Plotter Driver Minidrivers
author: windows-driver-content
description: Plotter Driver Minidrivers
ms.assetid: f7223a0a-df02-4a4f-a3d6-7910aed926eb
keywords:
- Plotter Driver WDK print , minidrivers
- MSPlot WDK print , minidrivers
- minidrivers WDK MSPlot
- PCD files WDK MSPlot
- .pcd files
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Plotter Driver Minidrivers


## <a href="" id="ddk-plotter-driver-minidrivers-gg"></a>


Model-specific minidrivers for the Microsoft Plotter Driver are vendor-supplied binary .pcd files created from text files that describe a device's characteristics.

### <a href="" id="ddk-pcd-files-gg"></a>PCD Files

To generate a .[*pcd*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-plotter-characterization-data--pcd-) file, you must first create a text file using the [PCD source file format](pcd-source-file-format.md). You must then run plotgpc.exe, which is included with the Windows Driver Kit (WDK). This program will convert a text file into a binary .pcd file. Use the following command syntax:

**plotgpc***source-file-path* .txt *target-file-path* .pcd

For both the source and destination files, you must explicitly specify file name extensions; defaults are not supported.

A sample text file that can be used as input to plotgpc.exe is included in the [sample plotter driver files](sample-plotter-driver-files.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Plotter%20Driver%20Minidrivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


