---
title: D3DRENDERSTATETYPE Changes
description: D3DRENDERSTATETYPE Changes
ms.assetid: b62bc1f9-b9f1-40f1-aed1-752285adb3c4
keywords:
- multimatrix vertex blending WDK Direct3D , D3DRENDERSTATETYPE
- D3DRENDERSTATETYPE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# D3DRENDERSTATETYPE Changes


## <span id="ddk_d3drenderstatetype_changes_gg"></span><span id="DDK_D3DRENDERSTATETYPE_CHANGES_GG"></span>


A new render state has been defined to enable and control multimatrix vertex blending operations: D3DRENDERSTATE\_VERTEXBLEND, which is described in the DirectX SDK documentation. The value of this render state can be one of the following D3DVERTEXBLENDFLAGS enumerators:

-   D3DVBLEND\_DISABLE (use only the world matrix specified by the D3DTRANSFORMSTATE\_WORLD transformation state)

-   D3DVBLEND\_1WEIGHT (blend between the two world matrices specified by the D3DTRANSFORMSTATE\_WORLD and D3DTRANSFORMSTATE\_WORLD1 transformation states)

-   D3DVBLEND\_2WEIGHTS (blend between the three world matrices specified by the D3DTRANSFORMSTATE\_WORLD, D3DTRANSFORMSTATE\_WORLD1, and D3DTRANSFORMSTATE\_WORLD2 transformation states)

-   D3DVBLEND\_3WEIGHTS (blend between four world matrices specified by the D3DTRANSFORMSTATE\_WORLD, D3DTRANSFORMSTATE\_WORLD1, D3DTRANSFORMSTATE\_WORLD2, and D3DTRANSFORMSTATE\_WORLD3 transformation states)

For a description of the D3DTRANSFORMSTATE\_WORLD *n* transformation states, see D3DTRANSFORMSTATETYPE in the DirectX SDK documentation.

Even though additional blending world matrices have been defined with the **IDirect3DDevice7::SetTransform** method (described in the Direct3D SDK documentation), the contributions (that is, weights) of any matrices beyond the number specified in this render state are set to zero.

 

 





