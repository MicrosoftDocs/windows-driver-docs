---
title: Comment Token
description: Comment Token
ms.assetid: b1e5f8c8-4d7d-49ce-876d-4a6cbccc550d
ms.date: 01/05/2018
ms.localizationpriority: medium
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

 

 





