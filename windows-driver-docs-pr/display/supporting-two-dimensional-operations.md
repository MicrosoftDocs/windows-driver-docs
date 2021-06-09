---
title: Supporting Two-Dimensional Operations
description: Supporting Two-Dimensional Operations
keywords:
- two-dimensional operations WDK DirectX 9.0
- 2D operations WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Two-Dimensional Operations


## <span id="ddk_supporting_two_dimensional_operations_gg"></span><span id="DDK_SUPPORTING_TWO_DIMENSIONAL_OPERATIONS_GG"></span>


The DirectX 9.0 runtime directs a driver to perform two-dimensional (2D) pixel-copy operations differently depending on the version of the driver that the runtime detects. For a DirectX 8.1 and earlier driver, the runtime calls the driver's [*DdBlt*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_blt) function and synchronizes this call with the [command stream](command-stream.md). For a DirectX 9.0 and later driver, the runtime passes the D3DDP2OP\_BLT, D3DDP2OP\_SURFACEBLT, or D3DDP2OP\_COLORFILL operation code along with the [**D3DHAL\_DP2BLT**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2blt), [**D3DHAL\_DP2SURFACEBLT**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2surfaceblt), or [**D3DHAL\_DP2COLORFILL**](/windows-hardware/drivers/ddi/d3dhal/ns-d3dhal-_d3dhal_dp2colorfill) structure respectively in the command stream. DirectX 9.0 and later drivers must support these 2D operation codes.

If the runtime specifies the DDBLT\_COLORFILL flag in a call to a DirectX 8.1 or earlier driver's *DdBlt* function, the runtime converts the D3DCOLOR fill-color type to an explicit pixel value as long as the runtime recognizes the target surface format (that is, the code for the format is one of the codes in the D3DFORMAT enumerated type). If the format is supplied by the vendor and not recognized by the runtime, the runtime passes the D3DCOLOR fill-color type directly to the driver for processing. However, the runtime converts, to explicit pixel values, the D3DCOLOR fill-color types of certain color formats that are used by DirectShow but are otherwise private to the driver.

 

