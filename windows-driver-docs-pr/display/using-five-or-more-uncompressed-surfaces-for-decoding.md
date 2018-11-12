---
title: Using Five or More Uncompressed Surfaces for Decoding
description: Using Five or More Uncompressed Surfaces for Decoding
ms.assetid: 7cd09d7a-6700-4079-97bd-0b0151705b82
keywords:
- video decoding WDK DirectX VA , sequence requirements
- decoding video WDK DirectX VA , sequence requirements
- picture decoding WDK DirectX VA , sequence requirements
- sequence requirements WDK DirectX VA
- succession requirements WDK DirectX VA
- multiple uncompressed surfaces for decoding WDK DirectX VA
- uncompressed surfaces example for decoding WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Five or More Uncompressed Surfaces for Decoding


## <span id="ddk_using_five_or_more_uncompressed_surfaces_for_decoding_gg"></span><span id="DDK_USING_FIVE_OR_MORE_UNCOMPRESSED_SURFACES_FOR_DECODING_GG"></span>


More than four uncompressed surfaces can be used for decoding, allowing the time lag between the start of the display of a buffer and new write operations to that buffer, to increase from a minimum of one display period to two or more. This technique can provide more of an allowance for jitter in the timing of the decoding process. This technique can also enable output processing on the decoded pictures to perform a three-field deinterlace operation as part of the display process. This is because not only is the current picture available for display, but the previous picture is also available, and can provide context and allow a one-field delay in the actual display process.

Although a minimum of four buffers is required for effective use of DirectX VA with B pictures, the use of five or more buffers is encouraged, particularly in scenarios that do not require keeping delay to a minimum. DirectX VA decoders for I, B, and P-structured video decoding are therefore expected to set their minimum and maximum requested uncompressed surface allocation counts to at least four and five, respectively, when allocating uncompressed surfaces. Using one or more extra uncompressed surfaces can achieve reliable, tear-free operation.

 

 





