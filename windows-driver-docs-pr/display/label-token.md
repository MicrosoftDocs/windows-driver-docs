---
title: Label Token
description: Label Token
ms.assetid: 29b2b4b1-c599-4bea-9d83-3a10eedac4a6
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Label%20Token%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




