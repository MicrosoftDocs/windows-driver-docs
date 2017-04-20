---
title: D3DRENDERSTATETYPE Changes
description: D3DRENDERSTATETYPE Changes
ms.assetid: b62bc1f9-b9f1-40f1-aed1-752285adb3c4
keywords:
- multimatrix vertex blending WDK Direct3D , D3DRENDERSTATETYPE
- D3DRENDERSTATETYPE
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3DRENDERSTATETYPE%20Changes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




