---
title: Handling Vertex Elements
description: Handling Vertex Elements
ms.assetid: b931b674-f8c4-4852-a66a-97d545059287
keywords:
- vertex shader declarations WDK DirectX 9.0 , handling vertex elements
- shader declarations WDK DirectX 9.0 , handling vertex elements
- vertex elements WDK DirectX 9.0
- vertex elements WDK DirectX 9.0 , vertex shader declarations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Vertex Elements


## <span id="ddk_handling_vertex_elements_gg"></span><span id="DDK_HANDLING_VERTEX_ELEMENTS_GG"></span>


The number of vertex elements in a shader declaration that a DirectX 9.0 version driver can handle depends on whether the driver's device supports fixed-function or programmable vertex processing. For more information about vertex elements in a shader declaration, see [Separating Declarations and Code for Vertex Shaders](separating-declarations-and-code-for-vertex-shaders.md).

If the device supports fixed-function vertex processing, the driver must handle up to 17 vertex elements (FVF codes).

If the device supports programmable vertex processing, the driver must handle up to 64 vertex elements and skip over those elements that it does not use. Because each channel (4 maximum) of an input register (16 maximum) for a device that supports vertex shader 3\_0 and later can be declared separately, up to 64 (16 \* 4) vertex elements are possible. This maximum number of 64 does not include the end element, which is formed from the D3DDECL\_END macro.

 

 





