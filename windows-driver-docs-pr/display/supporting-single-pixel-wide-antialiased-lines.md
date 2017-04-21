---
title: Supporting Single-Pixel-Wide Antialiased Lines
description: Supporting Single-Pixel-Wide Antialiased Lines
ms.assetid: f1e0df18-25d8-4ebd-b920-5cfbe5acf096
keywords:
- single-pixel-wide lines WDK DirectX 9.0
- alias single-pixel-wide lines WDK DirectX 9.0
- antialias single-pixel-wide lines WDK DirectX 9.0
- line antialiasing WDK DirectX 9.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Single-Pixel-Wide Antialiased Lines


## <span id="ddk_supporting_single_pixel_wide_antialiased_lines_gg"></span><span id="DDK_SUPPORTING_SINGLE_PIXEL_WIDE_ANTIALIASED_LINES_GG"></span>


A DirectX 9.0 version driver can support single-pixel-wide lines that are either alias or antialias. The driver indicates antialias support by setting the D3DLINECAPS\_ANTIALIAS capability bit in the **LineCaps** member of the D3DCAPS9 structure. The driver returns a D3DCAPS9 structure in response to a **GetDriverInfo2** query similarly to how it returns a D3DCAPS8 structure as described in [Reporting DirectX 8.0 Style Direct3D Capabilities](reporting-directx-8-0-style-direct3d-capabilities.md). Support of this query is described in [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

To enable line antialiasing, the driver receives the D3DDP2OP\_RENDERSTATE operation code in the [command stream](command-stream.md) of its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function. The driver processes the D3DRS\_ANTIALIASEDLINEENABLE render state from the **RenderState** member of the [**D3DHAL\_DP2RENDERSTATE**](https://msdn.microsoft.com/library/windows/hardware/ff545705) structure that is associated with this operation code. The driver determines whether to enable or disable line antialiasing from the Boolean value in the **dwState** member of D3DHAL\_DP2RENDERSTATE. The value **TRUE** means to enable and **FALSE** means to disable. By default, this render-state value is set to **FALSE**.

The D3DRS\_ANTIALIASEDLINEENABLE render state applies to triangles drawn in wire-frame mode as well as line-drawing primitive types.

When rendering to a multiple-sample render target, the driver must ignore a request to enable line antialiasing and render all lines aliased.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Single-Pixel-Wide%20Antialiased%20Lines%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




