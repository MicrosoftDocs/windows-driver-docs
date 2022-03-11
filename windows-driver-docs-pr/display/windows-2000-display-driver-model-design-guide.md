---
title: XDDM overview
description: Windows 2000 Display Driver Model (XDDM) Design Guide
keywords:
- display devices WDK
- display driver model WDK Windows 2000
- Windows 2000 display driver model WDK
- display drivers WDK , Windows 2000
ms.date: 03/10/2022
---

# XDDM overview

The Windows 2000 Display Driver Model (XDDM) is the legacy display/graphics driver architecture that was used for Windows 2000 through Windows Vista and Windows 7.

> [!NOTE]
>
> The XDDM design guide is preserved for historical purposes only. Current driver developers should use the [Windows Display Driver Model (WDDM)](windows-vista-display-driver-model-design-guide.md).

Display adapter drivers that run on Windows Vista can adhere to the WDDM or XDDM.

XDDM and VGA drivers will not compile or run on Windows 8 and later versions. If display hardware is attached to a Windows 8 computer without a driver that is certified to support WDDM 1.2 or later, the system defaults to running the [Microsoft Basic Display Driver](microsoft-basic-display-driver.md).

The following sections describe XDDM:

- [Introduction to Display (Windows 2000 Model)](introduction-to-display--windows-2000-model-.md)

- [Display Drivers (Windows 2000 Model)](display-drivers--windows-2000-model-.md)

- [DirectDraw](directdraw.md)

- [Direct3D DDI](direct3d.md)

- [DirectX Video Acceleration](directx-video-acceleration.md)

- [Video Miniport Drivers in the Windows 2000 Display Driver Model](video-miniport-drivers-in-the-windows-2000-display-driver-model.md)

- [Implementation Tips and Requirements for the Windows Display Driver Model (WDDM)](implementation-tips-and-requirements-for-the-windows-vista-display-dri.md)

- [GDI](gdi.md)
