---
title: Shader Relative Addressing
description: Shader Relative Addressing
ms.assetid: 7f936b56-cd41-4df5-8fc0-b8a7332ca7fa
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Shader Relative Addressing


## <span id="ddk_shader_relative_addressing_gg"></span><span id="DDK_SHADER_RELATIVE_ADDRESSING_GG"></span>


Pixel and vertex shader versions that support relative addressing can specify that relative addressing is used in bit 13 of [destination](destination-parameter-token.md) and [source parameter tokens](source-parameter-token.md). When relative addressing is specified, an additional DWORD token follows the destination or source parameter token.

Note that this relative-addressing token is present only for vertex shader version 2\_0 and later and for pixel shader version 3\_0 and later. Relative addressing is not used for pixel shader versions earlier than 3\_0.

This relative-addressing token is formatted the same as the destination or source parameter token and the following rules apply:

-   Only D3DSPR\_ADDR or D3DSPR\_LOOP can be used as [register types](https://msdn.microsoft.com/library/windows/hardware/ff569707).

-   Swizzle bits in source parameter tokens are used to determine a register component.

-   Bit 31 is 0x1.

-   Register offset is used.

-   All other bits are not used.

Address registers and the aL register are used for relative addressing of constant registers.

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


Available in Windows Vista and later versions of the Windows operating systems.

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


Available in Windows Vista and later versions of the Windows operating systems.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Shader%20Relative%20Addressing%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




