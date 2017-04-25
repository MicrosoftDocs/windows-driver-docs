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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Processing Texture Stages


## <span id="ddk_processing_texture_stages_gg"></span><span id="DDK_PROCESSING_TEXTURE_STAGES_GG"></span>


The driver uses the D3DDP2OP\_TEXTURESTAGESTATE operation code and [**D3DHAL\_DP2TEXTURESTAGESTATE**](https://msdn.microsoft.com/library/windows/hardware/ff545878) structures that follow in the command stream to process changes to texture-stage states. For information about how the driver processes operation codes, see [Command Stream](command-stream.md).

For example, when the operation code is D3DDP2OP\_TEXTURESTAGESTATE, and the value of the **wStateCount** member of the [**D3DHAL\_DP2COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff545454) structure is seven, then seven D3DHAL\_DP2TEXTURESTAGESTATE structures follow before the next D3DHAL\_DP2COMMAND instruction is reached. Each D3DHAL\_DP2TEXTURESTAGESTATE structure contains a **dwStage** member that specifies which stage of the texture blending pipeline needs to have a texture state change. The **TSState** member of the same structure specifies which state of the D3DTEXTURESTAGESTATETYPE enumerated type to set, and the **dwValue** member of the D3DHAL\_DP2TEXTURESTAGESTATE structure contains the value to which the specified state should be set.

The process is the same for all render states, or any other type of instruction. If the **bCommand** member of the [**D3DHAL\_DP2COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff545454) structure is D3DDP2OP\_RENDERSTATE, then the structure to follow is a [**D3DHAL\_DP2RENDERSTATE**](https://msdn.microsoft.com/library/windows/hardware/ff545705) structure and the information in that structure is used to set the render state accordingly.

Rather than using distinct Boolean-valued render states to control the coordinates, each render state value is a set of flags composed with the D3DWRAP\_U and D3DWRAP\_V flags (defined in *d3dtypes.h*). This change was made for compatibility with higher-dimensional textures.

Other useful information pertaining to multiple texture implementation can be found in the DirectX SDK documentation, in the sections covering blend equations, semantics of per-texture states, color operations, and alpha operations. For more information about the texture stage state types enabled for DirectX 6.0 and later versions, see the D3DTEXTUREOP and D3DTEXTUREFILTERTYPE enumerated types.

**Note**   DirectX 9.0 and later applications can use values in the D3DSAMPLERSTATETYPE enumeration to control the characteristics of sampler texture-related render states. In DirectX 8.0 and earlier, these sampler states were included in the D3DTEXTURESTAGESTATETYPE enumeration. The runtime maps user-mode sampler states (D3DSAMP\_*Xxx*) to kernel-mode D3DTSS\_*Xxx* values so that drivers are not required to process user-mode sampler states. For more information about D3DSAMPLERSTATETYPE, see the latest DirectX SDK documentation.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Processing%20Texture%20Stages%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




