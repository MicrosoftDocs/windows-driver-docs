---
title: Windows protocol
description: Windows protocol
ms.assetid: 9D28589E-FA19-43F2-BE22-438795807657
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
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

## “Windows:WriteTag.” Publications


A “Windows:WriteTag.” publication is a means for an app to simply write a Windows-typed payload to a tag.

### Required Actions

-   The common “\*:WriteTag” requirements described elsewhere apply.
-   The “Windows.&lt;SomeSubType&gt;” publication requirements also apply to “Windows:WriteTag.&lt;SomeSubType&gt;” publications.

## “LaunchApp:WriteTag” Publications


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

 

 





