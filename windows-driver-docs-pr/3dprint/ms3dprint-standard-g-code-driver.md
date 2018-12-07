---
title: MS3DPrint Standard G-Code driver
description: The MS3DPrint Standard G-Code driver implements a typical Windows 8.1 or Windows 10 driver for fused filament fabrication 3D printers that run with G-Code, particularly open source printers, including those from the RepRap project.
ms.assetid: F5818F58-C705-458F-9806-3F840BF7EE01
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MS3DPrint Standard G-Code driver


The MS3DPrint Standard G-Code driver implements a generic Windows 8.1 or later driver for fused filament fabrication 3D printers that run with G-Code, particularly open source printers, including those derived from the RepRap project.

This driver set contains both the USB driver which implements the wire protocol and the slicer which converts the geometry to toolpaths. The slicer driver receives 3MF data from the Windows spooler and outputs G-Code for the USB driver. The USB driver sends the G-Code one instruction at a time over a serial connection. 

Both the USB driver and the slicer are under active development and parts of the implementation and specification are subject to change in future revisions.  A set of these drivers is published on Windows Update and automatically offered to supported devices or devices that declare themselves a 3D Printer using the MS_COMP_3DPRINT USB descriptors.
 

## 3D printing SDK driver folder contents


The following table provides information about the location of the drivers, slicers and render filters in the 3D printing SDK.

| Folder                    | Contents                                 |
|---------------------------|------------------------------------------|
| \\Bin                     | Compiled binaries                        |
| \\Bin\\MS3DPrintUSB\_x64  | 64-bit USB Serial Port Driver Package    |
| \\Bin\\MS3DPrintUSB\_x86  | 32-bit USB Serial Port Driver Package    |
| \\Bin\\RenderFiltersV4\_x64 | 64-bit Slicer and Render Filters Package |
| \\Bin\\RenderFiltersV4\_x86 | 64-bit Slicer and Render Filters Package |

 

## In this section


[Driver installation](driver-installation.md)

[Configuring the device](configuring-the-device.md)

[Slicer settings](slicer-settings.md)

[Sample configuration XML](sample-configuration-xml.md)

 




