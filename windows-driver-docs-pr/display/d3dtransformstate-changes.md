---
title: D3DTRANSFORMSTATE Changes
description: D3DTRANSFORMSTATE Changes
keywords:
- multimatrix vertex blending WDK Direct3D , D3DTRANSFORMSTATE
- D3DTRANSFORMSTATE
ms.date: 04/20/2017
---

# D3DTRANSFORMSTATE Changes


## <span id="ddk_d3dtransformstate_changes_gg"></span><span id="DDK_D3DTRANSFORMSTATE_CHANGES_GG"></span>


Multimatrix blending also requires the specification of three additional world transform matrices.

In addition to the original world transform matrices, D3DTRANSFORMSTATE\_WORLD (which might be thought of as "D3DTRANSFORMSTATE\_WORLD0"), D3DTRANSFORMSTATE\_VIEW, and D3DTRANSFORMSTATE\_PROJECTION, there are now the following world transform matrices, which are described in the DirectX SDK documentation:

-   D3DTRANSFORMSTATE\_WORLD1, the second matrix to blend

-   D3DTRANSFORMSTATE\_WORLD2, the third matrix to blend

-   D3DTRANSFORMSTATE\_WORLD3, the fourth matrix to blend

Note that these are not consecutively enumerated after the original D3DTRANSFORMSTATE\_WORLD.

Matrices that are not defined by this call, but are enabled for blending, are assumed to default to identity matrices.

 

 





