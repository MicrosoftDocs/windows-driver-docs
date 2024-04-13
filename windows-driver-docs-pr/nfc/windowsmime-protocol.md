---
title: WindowsMime Protocol
description: WindowsMime protocol
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# WindowsMime protocol

## "WindowsMime" Subscriptions

A "WindowsMime" subscription is a means of abstracting a subscription for all possible MIME-typed payloads. Windows subscribes to this type in order to register with the driver that Windows is interested in receiving MIME-typed data that the user may be interested in using. Because this is a subscription for all possible MIME-typed payloads, the driver MUST return the type as well as the payload.

### Required Actions

- The driver MUST return the MIME-type of the payload as an ASCII-encoded and NULL-terminated string within the first 256 bytes of the output buffer.
- The driver MUST return the message payload after the first 256 bytes of the output buffer.
- The driver MUST set the Information field of the completed IRP to be 256+**sizeof**(payload).
- If the proximity technology is advertised as NFC, then the driver MUST match subscriptions for "WindowsMime" with all NDEF messages that have a TNF field value of 0x02.
  - The driver MUST return only the PAYLOAD of matched NDEF messages to subscribers of this type.
  - The driver MUST NOT return the full encoded NDEF message to subscribers of this type.
- The provider MAY support other compatible schemes as well.

## "WindowsMime." Protocol

A "WindowsMime." publication is a means of simply publishing a MIME-typed payload to a peer device. A "WindowsMime." subscription is a means of subscribing to payloads with a specific MIME-type. Windows will publish a simple MIME-typed message to a proximate device when directed by the user to do so.

Generic Example Type: "WindowsMime.\<SomeMimeType>"

Concrete Example Type: "WindowsMime.image/jpeg"

### Required Actions

- If the proximity technology is advertised as NFC, then the driver MUST match subscriptions for "WindowsMime.\<SomeMimeType>" ONLY with received NDEF messages that have a TNF field value of 0x02 and that have a TYPE field that matches "\<SomeMimeType>" based on the equivalence rules specified in \[NDEF\].

    The driver MUST return only the PAYLOAD of individual matched NDEF messages to subscribers of this type.

- If the proximity technology is advertised as NFC, then the driver MUST encapsulate each "WindowsMime.\<SomeSubType>" publication within NDEF messages with a TNF field value of 0x02.
  - The NDEF TYPE field MUST contain the direct mapping of the \<SomeSubType> string where each wide character is interpreted as a single byte.
  - The NDEF PAYLOAD MUST contain the direct binary contents of the publication message payload.

## "WindowsMime:WriteTag." Publications

A "WindowsMime:WriteTag." publication is a means for an app to simply write a MIME-typed payload to a tag.

### Required Actions

- The common "\*:WriteTag" requirements described elsewhere apply.
- The "WindowsMime.\<SomeMimeType>" publication requirements described elsewhere apply to "WindowsMime:WriteTag.\<SomeMimeType>" publications.

## Related topics

- [Near field communications (NFC) API reference](/windows-hardware/drivers/ddi/_nfpdrivers/)
