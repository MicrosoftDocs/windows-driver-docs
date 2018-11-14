---
title: Processing Texture Stages
description: Processing Texture Stages
ms.assetid: e22f5e2f-f17c-4a84-941b-c38e14b28550
keywords:
- multiple textures WDK Direct3D , texture stages
- texture stages WDK Direct3D
- D3DDP2OP_TEXTURESTAGESTATE
- D3DHAL_DP2TEXTURESTAGESTATE
- texture management WDK Direct3D , stages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing Texture Stages


## <span id="ddk_processing_texture_stages_gg"></span><span id="DDK_PROCESSING_TEXTURE_STAGES_GG"></span>


The driver uses the D3DDP2OP\_TEXTURESTAGESTATE operation code and [**D3DHAL\_DP2TEXTURESTAGESTATE**](https://msdn.microsoft.com/library/windows/hardware/ff545878) structures that follow in the command stream to process changes to texture-stage states. For information about how the driver processes operation codes, see [Command Stream](command-stream.md).

For example, when the operation code is D3DDP2OP\_TEXTURESTAGESTATE, and the value of the **wStateCount** member of the [**D3DHAL\_DP2COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff545454) structure is seven, then seven D3DHAL\_DP2TEXTURESTAGESTATE structures follow before the next D3DHAL\_DP2COMMAND instruction is reached. Each D3DHAL\_DP2TEXTURESTAGESTATE structure contains a **dwStage** member that specifies which stage of the texture blending pipeline needs to have a texture state change. The **TSState** member of the same structure specifies which state of the D3DTEXTURESTAGESTATETYPE enumerated type to set, and the **dwValue** member of the D3DHAL\_DP2TEXTURESTAGESTATE structure contains the value to which the specified state should be set.

The process is the same for all render states, or any other type of instruction. If the **bCommand** member of the [**D3DHAL\_DP2COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff545454) structure is D3DDP2OP\_RENDERSTATE, then the structure to follow is a [**D3DHAL\_DP2RENDERSTATE**](https://msdn.microsoft.com/library/windows/hardware/ff545705) structure and the information in that structure is used to set the render state accordingly.

Rather than using distinct Boolean-valued render states to control the coordinates, each render state value is a set of flags composed with the D3DWRAP\_U and D3DWRAP\_V flags (defined in *d3dtypes.h*). This change was made for compatibility with higher-dimensional textures.

Other useful information pertaining to multiple texture implementation can be found in the DirectX SDK documentation, in the sections covering blend equations, semantics of per-texture states, color operations, and alpha operations. For more information about the texture stage state types enabled for DirectX 6.0 and later versions, see the D3DTEXTUREOP and D3DTEXTUREFILTERTYPE enumerated types.

**Note**   DirectX 9.0 and later applications can use values in the D3DSAMPLERSTATETYPE enumeration to control the characteristics of sampler texture-related render states. In DirectX 8.0 and earlier, these sampler states were included in the D3DTEXTURESTAGESTATETYPE enumeration. The runtime maps user-mode sampler states (D3DSAMP\_*Xxx*) to kernel-mode D3DTSS\_*Xxx* values so that drivers are not required to process user-mode sampler states. For more information about D3DSAMPLERSTATETYPE, see the latest DirectX SDK documentation.

 

 

 





