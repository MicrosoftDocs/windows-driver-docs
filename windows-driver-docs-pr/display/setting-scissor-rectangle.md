---
title: Setting Scissor Rectangle
description: Setting Scissor Rectangle
keywords:
- scissor rectangle WDK DirectX 9.0
- rectangular clipping region WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Scissor Rectangle


## <span id="ddk_setting_scissor_rectangle_gg"></span><span id="DDK_SETTING_SCISSOR_RECTANGLE_GG"></span>


A DirectX 9.0 version driver must support setting a rectangular clipping region, that is, a scissor rectangle. After this scissor rectangle is set, rendering is restricted to just the portion of the render target that is specified by the scissor rectangle. To set a scissor rectangle, the driver must process the D3DDP2OP\_SETSCISSORRECT operation code in its [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) function. A RECT structure that specifies the rectangular clipping region follows the operation code in the [command stream](command-stream.md).

 

