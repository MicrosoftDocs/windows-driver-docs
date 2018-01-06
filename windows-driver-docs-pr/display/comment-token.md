---
title: Comment Token
description: Comment Token
ms.assetid: b1e5f8c8-4d7d-49ce-876d-4a6cbccc550d
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Comment Token


## <span id="ddk_comment_token_gg"></span><span id="DDK_COMMENT_TOKEN_GG"></span>


A comment token describes the length of the comment that follows and is composed of the following bits:

### <span id="bits"></span><span id="BITS"></span>Bits

<span id="_15_00_"></span>**\[15:00\]**
Bits 0 through 15 indicate that the token is a comment token. This value is 0xFFFE.

<span id="_30_16_"></span>**\[30:16\]**
Bits 16 through 30 specify the length in DWORDs of the comment that follows. A comment can be up to 2^15 DWORDs in length, which equals 128 KB of video memory or system memory.

<span id="_31_"></span>**\[31\]**
Bit 31 is zero (0x0).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Note that bit 31 of the DWORDs in the comment that follows is not required to be set to 0x1.

## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


Available in Windows Vista and later versions of the Windows operating systems.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Comment%20Token%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




