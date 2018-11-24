---
title: Version Token
description: Version Token
ms.assetid: e38ae148-3bb8-41b4-acdd-55bd67c24d48
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# Version Token


## <span id="ddk_version_token_gg"></span><span id="DDK_VERSION_TOKEN_GG"></span>


A version token describes the version number of the shader code and informs the driver whether the shader code is for a pixel or vertex shader. The version token is composed of the following bits:

### <span id="bits"></span><span id="BITS"></span>Bits

<span id="_07_00_"></span>**\[07:00\]**
Bits 0 through 7 indicate the minor version number or the code.

<span id="_15_08_"></span>**\[15:08\]**
Bits 8 through 15 specify the major version number or the code.

<span id="_31_16_"></span>**\[31:16\]**
Bits 16 through 31 specify whether the code is for a pixel or vertex shader.
For a pixel shader, the value is 0xFFFF.
For a vertex shader, the value is 0xFFFE.
## <span id="Requirements"></span><span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements


Available in Windows Vista and later versions of the Windows operating systems.

 

 





