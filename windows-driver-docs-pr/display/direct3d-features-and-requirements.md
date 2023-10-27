---
title: Direct3D features and requirements in WDDM 1.2
description: Direct3D offers a rich collection of 3-D graphics APIs, which are widely used by software applications for complex visualization and game development.
ms.date: 04/20/2017
---

# Direct3D features and requirements in WDDM 1.2

Direct3D offers a rich collection of 3-D graphics APIs, which are widely used by software applications for complex visualization and game development. This section describes feature improvements and Windows 8 Direct3D software and hardware requirements.

Depending on the capability of the graphics adapter, Direct3D allows applications to use hardware acceleration for the entire 3-D rendering pipeline or for partial acceleration. Newer versions of the Direct3D APIs such as Direct3D 9Ex and Direct3D 10 are available only starting with Windows Vista because the Windows Display Driver Model (WDDM) provides the display driver interfaces needed for the functionality. This figure shows the incremental versions of Direct3D APIs that are supported on the various versions of WDDM:

:::image type="content" source="images/direct3dapissupportedwddm.jpg" alt-text="Diagram that shows Direct3D APIs supported on various versions of WDDM.":::
