---
title: D3DTRANSFORMSTATE Changes
description: D3DTRANSFORMSTATE Changes
ms.assetid: 30d895d5-c9c3-4994-a77b-ee9eeec6d8d8
keywords:
- multimatrix vertex blending WDK Direct3D , D3DTRANSFORMSTATE
- D3DTRANSFORMSTATE
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20D3DTRANSFORMSTATE%20Changes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




