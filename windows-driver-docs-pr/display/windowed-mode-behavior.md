---
title: Windowed-Mode Behavior
description: Windowed-Mode Behavior
ms.assetid: a852b1d7-5722-4092-a5ff-338dbb2f77b3
keywords:
- windowed-mode rotation WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windowed-Mode Behavior


The Microsoft Direct3D runtime for a windowed-mode device never calls functions of a user-mode display driver to lock a rotated primary surface, to render to a rotated primary surface, or to perform bit-block transfers (bitblt) to or from a rotated primary. That is, the Direct3D runtime for a windowed-mode device handles all of these situations.

The Direct3D runtime for a windowed-mode device might not call the user-mode display driver's [**OpenResource**](https://msdn.microsoft.com/library/windows/hardware/ff568611) function to open the shared primary surface and to inform the user-mode display driver of the orientation of the primary surface. However, if the desktop window manager (DWM) is not running, the Direct3D runtime calls *OpenResource*, and the user-mode display driver is informed about the orientation of the primary. The user-mode display driver must be aware of the primary surface orientation only if the driver must access the primary surface (through a bitblt or lock) for its own purposes; the Direct3D runtime for a windowed-mode device will never request the user-mode display driver to access a rotated primary surface. Therefore, if the user-mode display driver must access the primary surface for its own internal purposes, the driver requires a mechanism in addition to a call to its **OpenResource** function because *OpenResource* is not always called.

The DWM or the display miniport driver's [**DxgkDdiPresent**](https://msdn.microsoft.com/library/windows/hardware/ff559743) function rotates windowed-mode data.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Windowed-Mode%20Behavior%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




