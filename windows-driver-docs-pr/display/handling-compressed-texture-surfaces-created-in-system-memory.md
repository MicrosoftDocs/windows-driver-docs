---
title: Handling Compressed Texture Surfaces Created In SysMem
description: Handling Compressed Texture Surfaces Created In System Memory
keywords:
- drawing compressed textures WDK DirectDraw , system memory considerations
- DirectDraw compressed textures WDK Windows 2000 display , system memory considerations
- compressed texture surfaces WDK DirectDraw , system memory considerations
- surfaces WDK DirectDraw , compressed textures
- textures WDK DirectDraw , compressed
- drawing compressed textures WDK DirectDraw , width
- DirectDraw compressed textures WDK Windows 2000 display , width
- compressed texture surfaces WDK DirectDraw , width
- drawing compressed textures WDK DirectDraw , height
- DirectDraw compressed textures WDK Windows 2000 display , height
- compressed texture surfaces WDK DirectDraw , height
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# Handling Compressed Texture Surfaces Created In System Memory

**This topic applies only to Windows NT-based operating systems.**

The width and height of a compressed-texture surface created in system memory are altered by the user-mode runtime to force the kernel-mode runtime to allocate the appropriate amount of memory. The display driver must reverse this alteration to prevent subsequent operations that are performed on this surface from failing. Whenever the DirectDraw runtime calls the driver's [**D3dCreateSurfaceEx**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_createsurfaceex) function to create a compressed-texture surface, the driver must restore the width and height of the surface to their unaltered states.

The driver's *D3dCreateSurfaceEx* function receives the surface's width, pitch, and height altered as follows:

-   Width and pitch contain the number of 4x4 blocks in a row multiplied by the block size.

-   Height contains the number of 4x4 blocks in the column.

The following code snippet shows the calculations that the driver must perform to restore the width and height of the surface:

```cpp
RealWidth = (Width / Block size) * 4;
RealHeight = Height * 4;
```

The driver should assign the restored width and height values to members in the kernel's [**DD\_SURFACE\_GLOBAL**](/windows/win32/api/ddrawint/ns-ddrawint-dd_surface_global) surface structure. Doing so prevents the DirectDraw kernel-mode runtime from rejecting DXT texture download blts because the width and height values do not match. That is, if the driver leaves the altered sizes in the **wWidth** and **wHeight** members of DD\_SURFACE\_GLOBAL, the DirectDraw kernel-mode runtime rejects a blt from the altered system-memory surface to the video-memory surface because the width and height of the source, which is in unaltered coordinates, seems to be "outside" the altered DD\_SURFACE\_GLOBAL size.

 

