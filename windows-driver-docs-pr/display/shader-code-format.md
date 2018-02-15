---
title: Shader Code Format
description: Shader Code Format
ms.assetid: 62377d19-8e45-4d0c-b974-0c0417d1a948
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Shader Code Format


## <span id="ddk_shader_code_format_gg"></span><span id="DDK_SHADER_CODE_FORMAT_GG"></span>


A command to create a pixel or vertex shader is composed of a group of shader codes. These codes instruct the driver on how to create the shader. The format of tokens within each shader code determines its uniqueness. A [shader code token](shader-code-tokens.md) is a DWORD with a specific format.

The DirectX3D runtime validates shader code before passing the code to a driver. When shader code arrives at the driver, the driver can interpret the code because the code's format is valid. The driver reads the shader code's tokens to interpret the code.

Each individual shader code is formatted with a general token layout. The first token must be a [version token](version-token.md). The version token provides the version number of the code and also determines whether the code is for a pixel or vertex shader. Shader content follows the version token and is composed of various [instruction tokens](instruction-token.md), perhaps intermingled with [comment tokens](comment-token.md) and white space. Depending on the precise operation that an instruction token specifies, [label](label-token.md), [destination parameter](destination-parameter-token.md), and [source parameter tokens](source-parameter-token.md) can also be part of the shader content and follow an instruction token. For example, if the instruction token specifies an [ADD instruction](https://msdn.microsoft.com/library/windows/hardware/ff538212), the driver determines that one destination and two source parameter tokens follow the instruction token. An [end token](end-token.md) completes the shader code.

Setup instructions (for example, D3DSIO\_DCL and D3DSIO\_DEF) contain uniquely formatted tokens.

Each shader instruction contains a specific token format. The [Shader Operation Codes](https://msdn.microsoft.com/library/windows/hardware/ff569706) section describes the token format of each shader instruction.

Shader instructions start with the primary instruction and end with a D3DSIO\_RET or D3DSIO\_END instruction. Subroutines follow the D3DSIO\_RET instruction.

See the Pixel Shader Reference and Vertex Shader Reference in the latest DirectX SDK documentation for more information about operations that can be specified in instruction tokens.

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


Available in Windows Vista and later versions of the Windows operating systems.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Shader%20Code%20Format%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




