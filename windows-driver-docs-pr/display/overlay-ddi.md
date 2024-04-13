---
title: Overlay DDI
description: Overlay DDI
keywords:
- Overlay DDI WDK Windows 7 display
- Overlay DDI WDK Server 2008 R2 display
ms.date: 04/20/2017
---

# Overlay DDI


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The Overlay DDI is an extension to the [Direct3D version 9 DDI](/windows-hardware/drivers/ddi/d3dumddi/index) to verify overlay support. The Overlay DDI consists of the following entry points:

-   The D3DDDICAPS\_CHECKOVERLAYSUPPORT value from the [**D3DDDICAPS\_TYPE**](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-_d3dddicaps_type) enumeration is used by the Direct3D runtime to verify whether the display device supports a particular overlay. The runtime sets D3DDDICAPS\_CHECKOVERLAYSUPPORT in the **Type** member of the [**D3DDDIARG\_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps) structure that the *pData* parameter of the driver's [**GetCaps**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_getcaps) function points to when the runtime calls **GetCaps**. The runtime also sets the **pInfo** member of D3DDDIARG\_GETCAPS to a pointer to a [**DDICHECKOVERLAYSUPPORTINPUT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_ddicheckoverlaysupportinput) structure that describes the overlay. If the driver supports the overlay, the driver sets the members of a D3DOVERLAYCAPS structure and returns a pointer to this structure in the **pData** member of **D3DDDIARG\_GETCAPS**. Otherwise, if the driver does not support the overlay, the driver fails the call to its **GetCaps** function with either D3DDDIERR\_UNSUPPORTEDOVERLAYFORMAT or D3DDDIERR\_UNSUPPORTEDOVERLAY depending on whether the lack of support was based on the overlay format. D3DOVERLAYCAPS is described in the DirectX SDK documentation.

    The driver sets the **MaxOverlayDisplayWidth** and **MaxOverlayDisplayHeight** members of D3DOVERLAYCAPS to indicate any restrictions that the driver and hardware might have, which involve the final overlay size (after stretching the overlay data).

    The driver sets the D3DOVERLAYCAPS\_STRETCHX (0x00000040) and D3DOVERLAYCAPS\_STRETCHY (0x00000080) capability bits in the **Caps** member of D3DOVERLAYCAPS to indicate that the overlay hardware is capable of arbitrarily stretching and shrinking the overlay data. Drivers should not attempt to emulate overlay stretching through the GPU and should only set these caps if the overlay hardware supports stretching. Less overhead is typically required for the application to perform GPU stretching as a part of the video processing and composition phase than for the driver to perform a separate pass at the very end to emulate overlay stretching.

-   The driver should handle the following new bit-field flags from the [**D3DDDI\_OVERLAYINFOFLAGS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_overlayinfoflags) structure. A D3DDDI\_OVERLAYINFOFLAGS structure identifies the type of overlay operation to perform. A D3DDDI\_OVERLAYINFOFLAGS structure is specified in the **Flags** member of the [**D3DDDI\_OVERLAYINFO**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_overlayinfo) structure in a call to either the driver's [**CreateOverlay**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createoverlay) or [**UpdateOverlay**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_updateoverlay) function.

    <span id="LimitedRGB"></span><span id="limitedrgb"></span><span id="LIMITEDRGB"></span>**LimitedRGB**  
    The overlay is limited range RGB rather than full range RGB. In limited range RGB, the RGB range is compressed such that 16:16:16 is black and 235:235:235 is white.

    <span id="YCbCrBT709"></span><span id="ycbcrbt709"></span><span id="YCBCRBT709"></span>**YCbCrBT709**  
    The overlay is BT.709, which indicates high-definition TV (HDTV), rather than BT.601.

    <span id="YCbCrxvYCC"></span><span id="ycbcrxvycc"></span><span id="YCBCRXVYCC"></span>**YCbCrxvYCC**  
    The overlay is extended YCbCr (xvYCC) rather than conventional YCbCr.

-   When the display format is 64 bits rather than 32 bits (for example, when the Desktop Windows Manager (DWM) uses D3DFMT\_A16B16G16R16F for the display mode), the runtime places the lower 32 bits of the overlay colorkey in the **DstColorKeyLow** member of the [**D3DDDI\_OVERLAYINFO**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_overlayinfo) structure and the upper 32 bits in the **DstColorKeyHigh** member of D3DDDI\_OVERLAYINFO.

 

