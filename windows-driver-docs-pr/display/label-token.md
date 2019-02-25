---
title: Label Token
description: Label Token
ms.assetid: 29b2b4b1-c599-4bea-9d83-3a10eedac4a6
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# Label Token


## <span id="ddk_label_token_gg"></span><span id="DDK_LABEL_TOKEN_GG"></span>


A label token is only used for certain operations (for example, D3DSIO\_CALLNZ) and is composed of the following bits:

### <span id="bits"></span><span id="BITS"></span>Bits

<span id="_10_00_"></span>**\[10:00\]**
Bits 0 through 10 indicate the register number (offset in register file).

<span id="_12_11_"></span>**\[12:11\]**
Bits 11 and 12 are the fourth and fifth bits \[3,4\] for indicating the [register type](https://msdn.microsoft.com/library/windows/hardware/ff569707).

<span id="_27_13_"></span>**\[27:13\]**
Reserved for all versions of pixel shader (PS) and vertex shader (VS). This value is set to 0x0.

<span id="_30_28_"></span>**\[30:28\]**
Bits 28 through 30 are the first three bits \[0,1,2\] for indicating the [register type](https://msdn.microsoft.com/library/windows/hardware/ff569707).

<span id="_31_"></span>**\[31\]**
Bit 31 is 0x1.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The format of the label token is the same as the [source parameter token](source-parameter-token.md) except that only the register number and type fields are used.

Bits 28, 29, 30, 11, and 12 form a 5-bit value that indicates the register type. For information about register types, see [Shader Register Types](https://msdn.microsoft.com/library/windows/hardware/ff569707). The register type for a label token must be specified as D3DSPR\_LABEL.

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


Available in Windows Vista and later versions of the Windows operating systems.

 

 





