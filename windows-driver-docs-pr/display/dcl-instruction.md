---
title: DCL Instruction Format
description: DCL Instruction Format
ms.assetid: 2833fe6a-f430-4a34-936f-04e997063671
ms.date: 01/05/2018
ms.localizationpriority: medium
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

```registry
       DCL   o10.xy
       DCL   o10.zw
```

The output DCL instructions must declare all registers that are written by a vertex shader 3\_0 and later.

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


Available in Windows Vista and later versions of the Windows operating systems.

 

 





