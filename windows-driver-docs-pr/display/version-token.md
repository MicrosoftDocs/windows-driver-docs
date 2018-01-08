---
title: Version Token
description: Version Token
ms.assetid: e38ae148-3bb8-41b4-acdd-55bd67c24d48
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Version%20Token%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




