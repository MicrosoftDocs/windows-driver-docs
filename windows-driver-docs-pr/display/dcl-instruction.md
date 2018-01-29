---
title: DCL Instruction Format
description: DCL Instruction Format
ms.assetid: 2833fe6a-f430-4a34-936f-04e997063671
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DCL Instruction Format


## <span id="ddk_dcl_instruction_gg"></span><span id="DDK_DCL_INSTRUCTION_GG"></span>


The DCL instruction declares registers.

### <span id="format"></span><span id="FORMAT"></span>Format

**Pixel shader 2\_0 and later only.**

**Sampler state register only.**

[instruction token](instruction-token.md)

Contains D3DSIO\_DCL.
DWORD token

Has the following bit format:

**\[26:0\]** Reserved. Set to 0x0.

**\[30:27\]** Set to D3DSAMPLER\_TEXTURE\_TYPE for 2D, cube, and so on.

**\[31\]** Set to 0x1.

[destination parameter token](destination-parameter-token.md)

Indicates the register number and the [register type](https://msdn.microsoft.com/library/windows/hardware/ff569707) as D3DSPR\_SAMPLER. These are the only fields that are used in this token.

**Input or texture register only.**

[instruction token](instruction-token.md)

Contains D3DSIO\_DCL.
DWORD token

Has the following bit format:

**\[30:0\]** Reserved. Set to 0x0.

**\[31\]** Set to 0x1.

[destination parameter token](destination-parameter-token.md)

Indicates input or texture register number. The write-mask field indicates declared components.

**Vertex shader 2\_0 and later only.**

**Input register only.**

[instruction token](instruction-token.md)

Contains D3DSIO\_DCL.
DWORD token

Has the following bit format:

**\[4:0\]** D3DDECLUSAGE value (that is, D3DDECLUSAGE\_TEXCOORD, D3DDECLUSAGE\_NORMAL, and so on).

**\[15:5\]** Reserved. Set to 0x0.

**\[19:16\]** Usage index value.

**\[30:20\]** Reserved. Set to 0x0.

**\[31\]** Set to 0x1.

[destination parameter token](destination-parameter-token.md)

Indicates the register number and the [register type](https://msdn.microsoft.com/library/windows/hardware/ff569707) as D3DSPR\_INPUT. The write-mask field indicates declared components.

**Pixel shader 3\_0 and later only.**

**Texture register only.**

[instruction token](instruction-token.md)

Contains D3DSIO\_DCL.
DWORD token

Has the following bit format:

**\[4:0\]** D3DDECLUSAGE value (must be D3DDECLUSAGE\_TEXCOORD or D3DDECLUSAGE\_COLOR).

**\[15:5\]** Reserved. Set to 0x0.

**\[19:16\]** Usage index value. For D3DDECLUSAGE\_TEXCOORD, must be 0-7. For D3DDECLUSAGE\_COLOR, must be 0.

**\[30:20\]** Reserved. Set to 0x0.

**\[31\]** Set to 0x1.

[destination parameter token](destination-parameter-token.md)

Indicates the register number and the [register type](https://msdn.microsoft.com/library/windows/hardware/ff569707) as D3DSPR\_TEXTURE. The write-mask field indicates declared components.

**Face register only.**

[instruction token](instruction-token.md)

Contains D3DSIO\_DCL.
DWORD token

Has the following bit format:

**\[30:0\]** Reserved. Set to 0x0.

**\[31\]** Set to 0x1.

[destination parameter token](destination-parameter-token.md)

Indicates the face register. The write-mask field must be full although it is unused. The result-modifier and shift-scale fields must be 0 (also unused).

**Position register only.**

[instruction token](instruction-token.md)

Contains D3DSIO\_DCL.
DWORD token

Has the following bit format:

**\[30:0\]** Reserved. Set to 0x0.

**\[31\]** Set to 0x1.

[destination parameter token](destination-parameter-token.md)

Indicates position register. The write-mask field indicates declared components.

**Vertex shader 3\_0 and later only.**

**Output register only.**

[instruction token](instruction-token.md)

Contains D3DSIO\_DCL.
DWORD token

Has the following bit format:

**\[4:0\]** D3DDECLUSAGE value (that is, D3DDECLUSAGE\_TEXCOORD, D3DDECLUSAGE\_NORMAL, and so on).

**\[15:5\]** Reserved. Set to 0x0.

**\[19:16\]** Usage index value.

**\[30:20\]** Reserved. Set to 0x0.

**\[31\]** Set to 0x1.

[destination parameter token](destination-parameter-token.md)

Indicates the register number and the [register type](https://msdn.microsoft.com/library/windows/hardware/ff569707) as D3DSPR\_OUTPUT. The write-mask field defines which components are written.

Note that several DCL instructions, which describe the output, can use the same register offset. However, the write mask components for each DCL instruction must be different. For example, the following is valid in a vertex shader 3\_0 and later:

```
       DCL   o10.xy
       DCL   o10.zw
```

The output DCL instructions must declare all registers that are written by a vertex shader 3\_0 and later.

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


Available in Windows Vista and later versions of the Windows operating systems.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DCL%20Instruction%20Format%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




