---
title: Using Five or More Uncompressed Surfaces for Decoding
description: Using Five or More Uncompressed Surfaces for Decoding
ms.assetid: 7cd09d7a-6700-4079-97bd-0b0151705b82
keywords: ["video decoding WDK DirectX VA , sequence requirements", "decoding video WDK DirectX VA , sequence requirements", "picture decoding WDK DirectX VA , sequence requirements", "sequence requirements WDK DirectX VA", "succession requirements WDK DirectX VA", "multiple uncompressed surfaces for decoding WDK DirectX VA", "uncompressed surfaces example for decoding WDK DirectX VA"]
---

# Using Five or More Uncompressed Surfaces for Decoding


## <span id="ddk_using_five_or_more_uncompressed_surfaces_for_decoding_gg"></span><span id="DDK_USING_FIVE_OR_MORE_UNCOMPRESSED_SURFACES_FOR_DECODING_GG"></span>


More than four uncompressed surfaces can be used for decoding, allowing the time lag between the start of the display of a buffer and new write operations to that buffer, to increase from a minimum of one display period to two or more. This technique can provide more of an allowance for jitter in the timing of the decoding process. This technique can also enable output processing on the decoded pictures to perform a three-field deinterlace operation as part of the display process. This is because not only is the current picture available for display, but the previous picture is also available, and can provide context and allow a one-field delay in the actual display process.

Although a minimum of four buffers is required for effective use of DirectX VA with B pictures, the use of five or more buffers is encouraged, particularly in scenarios that do not require keeping delay to a minimum. DirectX VA decoders for I, B, and P-structured video decoding are therefore expected to set their minimum and maximum requested uncompressed surface allocation counts to at least four and five, respectively, when allocating uncompressed surfaces. Using one or more extra uncompressed surfaces can achieve reliable, tear-free operation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Using%20Five%20or%20More%20Uncompressed%20Surfaces%20for%20Decoding%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




