---
title: Desktop duplication
description: Windows 8 introduces a new Microsoft DirectX Graphics Infrastructure (DXGI)-based API to make it easier for independent software vendors (ISVs) to support desktop collaboration and remote desktop access scenarios.
ms.assetid: 5D4CBEA1-3C13-4B5C-A43D-7E6DBBB1A80F
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Desktop duplication


Windows 8 introduces a new Microsoft DirectX Graphics Infrastructure (DXGI)-based API to make it easier for independent software vendors (ISVs) to support desktop collaboration and remote desktop access scenarios.

Such applications are widely used in enterprise and educational scenarios. These applications share a common requirement: access to the contents of a desktop together with the ability to transport the contents to a remote location. The Windows 8 Desktop duplication APIs provide access to the desktop contents.

Currently, no Windows API allows an application to seamlessly implement this scenario. Therefore, applications use mirror drivers, screen scrapping, and other proprietary methods to access the contents of the desktop. However, these methods have the following set of limitations:

-   It can be challenging to optimize the performance.
-   These solutions might not support newer graphics-rendering APIs because the APIs are released after the product ships.
-   Windows does not always provide rich metadata to assist with the optimization.
-   Not all solutions are compatible with the desktop composition in Windows Vista and later versions of Windows.

Windows 8 introduces a DXGI-based API called *Desktop Duplication API*. This API provides access to the contents of the desktop by using bitmaps and associated metadata for optimizations. This API works with the Aero theme enabled, and is not dependent on the graphics API that applications use. If a user can view the application on the local console, then the content can be viewed remotely as well. This means that even full screen DirectX applications can be duplicated. Note that the API provides protection against accessing protected video content.

The API enables an application to request Windows to provide access to the contents of the desktop along monitor boundaries. The application can duplicate one or more of the active displays. When an application requests duplication, the following occurs:

-   Windows renders the desktop and provides a copy to the application.
-   Each rendered frame is placed in GPU memory.
-   Each rendered frame comes with the following metadata:
    -   Dirty region
    -   Screen-to-screen moves
    -   Mouse cursor information
-   Application is provided access to frame and metadata.
-   Application is responsible for processing each frame:
    -   Application can choose to optimize based on dirty region.
    -   Application can choose to use hardware acceleration to process move and mouse data.
    -   Application can choose to use hardware acceleration for compression before streaming out.

For detailed documentation and samples, see [Desktop Duplication API](https://msdn.microsoft.com/library/windows/desktop/hh404487).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Desktop%20duplication%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




