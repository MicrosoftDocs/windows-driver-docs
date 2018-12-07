---
title: Windowed-Mode Behavior
description: Windowed-Mode Behavior
ms.assetid: a852b1d7-5722-4092-a5ff-338dbb2f77b3
keywords:
- windowed-mode rotation WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windowed-Mode Behavior


The Microsoft Direct3D runtime for a windowed-mode device never calls functions of a user-mode display driver to lock a rotated primary surface, to render to a rotated primary surface, or to perform bit-block transfers (bitblt) to or from a rotated primary. That is, the Direct3D runtime for a windowed-mode device handles all of these situations.

The Direct3D runtime for a windowed-mode device might not call the user-mode display driver's [**OpenResource**](https://msdn.microsoft.com/library/windows/hardware/ff568611) function to open the shared primary surface and to inform the user-mode display driver of the orientation of the primary surface. However, if the desktop window manager (DWM) is not running, the Direct3D runtime calls *OpenResource*, and the user-mode display driver is informed about the orientation of the primary. The user-mode display driver must be aware of the primary surface orientation only if the driver must access the primary surface (through a bitblt or lock) for its own purposes; the Direct3D runtime for a windowed-mode device will never request the user-mode display driver to access a rotated primary surface. Therefore, if the user-mode display driver must access the primary surface for its own internal purposes, the driver requires a mechanism in addition to a call to its **OpenResource** function because *OpenResource* is not always called.

The DWM or the display miniport driver's [**DxgkDdiPresent**](https://msdn.microsoft.com/library/windows/hardware/ff559743) function rotates windowed-mode data.

 

 





