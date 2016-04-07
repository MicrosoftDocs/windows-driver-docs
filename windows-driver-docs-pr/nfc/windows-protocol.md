---
title: Windows protocol
author: windows-driver-content
description: Windows protocol
ms.assetid: 9D28589E-FA19-43F2-BE22-438795807657
---

# Windows protocol


In order to ensure interoperability of NFC-enabled NFP providers, this section defines exactly how a Windows message should be encapsulated within an NDEF message. This section also maps the NFP pub/sub model to published NFC Forum protocols for exchanging NDEF messages. These requirements only apply if the proximity technology is advertised as NFC.

## Encapsulation


The following requirements must be met to ensure the proper encapsulation of Windows messages for NFC interoperability.

### Required Actions

-   If the proximity technology is advertised as NFC, then the driver MUST encapsulate each “Windows.&lt;SomeSubType&gt;” publications within NDEF messages with a TNF field value of 0x03.
    -   The NDEF TYPE field MUST contain the direct mapping of the &lt;SomeSubType&gt; string where each wide character is interpreted as a single byte.
    -   The NDEF PAYLOAD MUST contain the direct binary contents of the publication message payload.
-   If the proximity technology is advertised as NFC, then the driver MUST match subscriptions for “Windows.&lt;SomeSubType&gt;” ONLY with NDEF messages that have a TNF field value of 0x03 and a TYPE field that is equal to “&lt;SomeSubType&gt;” where each wide character is interpreted as a single byte

    The driver MUST return only the PAYLOAD of the matched NDEF messages to subscribers of this type.

## <a href="" id="-windows-writetag---publications"></a>“Windows:WriteTag.” Publications


A “Windows:WriteTag.” publication is a means for an app to simply write a Windows-typed payload to a tag.

### Required Actions

-   The common “\*:WriteTag” requirements described elsewhere apply.
-   The “Windows.&lt;SomeSubType&gt;” publication requirements also apply to “Windows:WriteTag.&lt;SomeSubType&gt;” publications.

## <a href="" id="-launchapp-writetag--publications"></a>“LaunchApp:WriteTag” Publications


An “LaunchApp:WriteTag” publication is a means for an app to simply write a “Windows.windows.com/LaunchApp” message to a tag.

The client will send a tab-delimited (or null-delimited) list of strings as the payload for this publication encoded in UTF-16LE. The first string is the arguments list for the app. Following the argument string will be pairs of strings. The first string in each pair defines the platform qualifier for an app ID, the next string is the actual app ID to launch on that platform. This mechanism supports interoperability across app platforms beyond Windows.

### Required Actions

-   The type of the message MUST be encoded as if the type were “Windows.windows.com/LaunchApp”.
-   If the buffer contains fewer than three strings the driver MUST complete the IOCTL with STATUS\_INVALID\_PARAMETER.
-   If the buffer is longer than 3,000 characters the driver MUST complete the IOCTL with STATUS\_INVALID\_PARAMETER.
-   If the buffer contains one or more zero-length strings (two consecutive tab characters) the driver MUST complete the IOCTL with STATUS\_INVALID\_PARAMETER.
-   If the buffer contains an even number of strings the driver MUST complete the IOCTL with STATUS\_INVALID\_PARAMETER.
-   The driver MUST parse the buffer into an argument string and a list of platform/AppID tuples.
-   If any platform or AppID string is longer than 255 characters the driver MUST complete the IOCTL with STATUS\_INVALID\_PARAMETER.
-   The first USHORT of the payload written to the tag MUST contain the number of platform/AppID tuples in big-endian encoding.
-   All strings MUST be converted from UTF-16LE to UTF-8.
-   String lengths written in the payload MUST be in bytes.
-   For each platform/AppID tuple the driver MUST add to the payload a byte with the length (in bytes) of the platform string followed by the platform string itself followed by a byte with the length (in bytes) of the AppID string followed by the AppID string itself.
-   The driver MUST add a USHORT containing the length of the argument string followed by the argument string itself.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Windows%20protocol%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




