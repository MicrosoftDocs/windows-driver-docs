---
title: Desktop Duplication
description: Windows 8 introduces a new Microsoft DirectX Graphics Infrastructure (DXGI)-based API to make it easier for independent software vendors (ISVs) to support desktop collaboration and remote desktop access scenarios.
ms.date: 12/18/2024
---

# Desktop duplication

Windows 8 introduced a DirectX Graphics Infrastructure (DXGI)-based API called the [Desktop Duplication API](/windows/win32/direct3ddxgi/desktop-dup-api). This API makes it easier for independent software vendors (ISVs) to support desktop collaboration and remote desktop access.

Such applications are widely used in enterprise and educational scenarios. These applications share a common requirement: they need access to the contents of a desktop together with the ability to transport the contents to a remote location.

The API provides access to the desktop contents by using bitmaps and associated metadata for optimizations. It works with the Aero theme enabled, and isn't dependent on the graphics API that applications use. If a user can view the application on the local console, then the content can be viewed remotely as well. This means that even full screen DirectX applications can be duplicated. The API provides protection against accessing protected video content.

The API enables an application to request Windows to provide access to the contents of the desktop along monitor boundaries. The application can duplicate one or more of the active displays. When an application requests duplication, the following occurs:

* Windows renders the desktop and provides a copy to the application.
* Each rendered frame is placed in GPU memory.
* Each rendered frame comes with the following metadata:
  * Dirty region
  * Screen-to-screen moves
  * Mouse cursor information
* Application is provided access to frame and metadata.
* Application is responsible for processing each frame:
  * Application can choose to optimize based on dirty region.
  * Application can choose to use hardware acceleration to process move and mouse data.
  * Application can choose to use hardware acceleration for compression before streaming out.

For detailed documentation and samples, see [Desktop Duplication API](/windows/win32/direct3ddxgi/desktop-dup-api).
