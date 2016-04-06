---
title: WindowsMime protocol
description: WindowsMime protocol
ms.assetid: 03C5A31F-269A-45B3-9359-B6FFF4823190
---

# WindowsMime protocol


## <a href="" id="-windowsmime--subscriptions"></a>“WindowsMime” Subscriptions


A “WindowsMime” subscription is a means of abstracting a subscription for all possible MIME-typed payloads. Windows subscribes to this type in order to register with the driver that Windows is interested in receiving MIME-typed data that the user may be interested in using. Because this is a subscription for all possible MIME-typed payloads, the driver MUST return the type as well as the payload.

### Required Actions

-   The driver MUST return the MIME-type of the payload as an ASCII-encoded and NULL-terminated string within the first 256 bytes of the output buffer.
-   The driver MUST return the message payload after the first 256 bytes of the output buffer.
-   The driver MUST set the Information field of the completed IRP to be 256+**sizeof**(payload).
-   If the proximity technology is advertised as NFC, then the driver MUST match subscriptions for “WindowsMime” with all NDEF messages that have a TNF field value of 0x02.
    -   The driver MUST return only the PAYLOAD of matched NDEF messages to subscribers of this type.
    -   The driver MUST NOT return the full encoded NDEF message to subscribers of this type.
-   The provider MAY support other compatible schemes as well.

## <a href="" id="-windowsmime---protocol"></a>“WindowsMime.” Protocol


A “WindowsMime.” publication is a means of simply publishing a MIME-typed payload to a peer device. A “WindowsMime.” subscription is a means of subscribing to payloads with a specific MIME-type. Windows will publish a simple MIME-typed message to a proximate device when directed by the user to do so.

Generic Example Type: “WindowsMime.&lt;SomeMimeType&gt;”

Concrete Example Type: “WindowsMime.image/jpeg”

### Required Actions

-   If the proximity technology is advertised as NFC, then the driver MUST match subscriptions for “WindowsMime.&lt;SomeMimeType&gt;” ONLY with received NDEF messages that have a TNF field value of 0x02 and that have a TYPE field that matches “&lt;SomeMimeType&gt;” based on the equivalence rules specified in \[NDEF\].

    The driver MUST return only the PAYLOAD of individual matched NDEF messages to subscribers of this type.

-   If the proximity technology is advertised as NFC, then the driver MUST encapsulate each “WindowsMime.&lt;SomeSubType&gt;” publication within NDEF messages with a TNF field value of 0x02.
    -   The NDEF TYPE field MUST contain the direct mapping of the &lt;SomeSubType&gt; string where each wide character is interpreted as a single byte.
    -   The NDEF PAYLOAD MUST contain the direct binary contents of the publication message payload.

## <a href="" id="-windowsmime-writetag---publications"></a>“WindowsMime:WriteTag.” Publications


A “WindowsMime:WriteTag.” publication is a means for an app to simply write a MIME-typed payload to a tag.

### Required Actions

-   The common “\*:WriteTag” requirements described elsewhere apply.
-   The “WindowsMime.&lt;SomeMimeType&gt;” publication requirements described elsewhere apply to “WindowsMime:WriteTag.&lt;SomeMimeType&gt;” publications.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20WindowsMime%20protocol%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




