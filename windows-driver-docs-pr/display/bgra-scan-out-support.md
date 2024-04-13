---
title: BGRA Scan-Out Support
description: BGRA Scan-Out Support
keywords:
- Direct3D version 10.1 WDK Windows 7 display , BGRA scan-out support
- BGRA scan-out support WDK Windows 7 display
- scan-out support WDK Windows 7 display
ms.date: 04/20/2017
---

# BGRA Scan-Out Support


This section applies only to Windows 7 and later operating systems.

The scan-out bit is turned on for the DXGI\_FORMAT\_B8G8R8A8\_UNORM and DXGI\_FORMAT\_B8G8R8A8\_UNORM\_SRGB formats. Therefore, the user-mode display driver should be able to perform the following operations:

-   Handle requests for the primary surface that are in these formats.

-   Handle calls to its [**SetDisplayMode**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_setdisplaymode) function for resources that are created with these formats.

-   Handle calls to its [**PresentDXGI**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_base_functions) function to present these formats through both bit-block transfer (bitblt) and flip operations.

-   Handle calls to its [**BltDXGI**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi_ddi_base_functions) function to copy these formats through stretch, rotate, and resolve (in fact, all the bitblt operations that are expected for the RGBA variants).

 

