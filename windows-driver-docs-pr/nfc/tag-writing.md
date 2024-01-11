---
title: Tag Writing
description: Tag writing
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# Tag writing

Tag writing is specified for the categories: General, NFC, and All. Within each category a driver will recognize only certain types of tags.

These are special publications that allow a message to be written to any NearFieldProximity tag. Any existing payload of the tag MUST be overwritten. Append semantics are only defined for NFC. If the client wants to append instead of overwrite, it must construct an NDEF payload that contains the original NDEF Message and place it into an "NDEF:WriteTag" publication. It is expected (but not enforced) that zero or one "\*:WriteTag" publication will be active at any given moment.

## General Tag Writing

Tag writing is an optional feature for NFP providers that are not NFC enabled. The driver MAY recognize the following tag types for publications only:

- "WindowsUri:WriteTag"
- "WindowsMime:WriteTag"
- "Windows:WriteTag"

## NFC Tag Writing

Tag writing support is required for NFC-enabled NFP providers. These requirements must be met.

If the proximity technology is advertised as NFC, then driver MUST recognize the following tag types for publications only:

- "WindowsUri:WriteTag"
- "WindowsMime:WriteTag"
- "Windows:WriteTag"
- "NDEF:WriteTag"

Strict NDEF encoding rules are used in accordance with NFC Forum specifications. For example, an NDEF Message fragment MUST NOT be written (even following a valid NDEF Message).

For NFC tags, if a tag is not NDEF formatted and a message is published for \*.WriteTag, the provider MUST format the tag to NDEF and then write the payload.

## All Tag Writing

If tag writing is supported at all by the NFP provider, the driver must meet all of the listed requirements.

### Required Actions

- The driver MUST NOT recognize any "\*:WriteTag" subscriptions.
- If one or more "\*:WriteTag" publications is enabled and the driver detects a writable tag with enough space available, the existing payload of the tag MUST NOT be read for the purposes of matching other subscriptions. This allows a tag-writing app to preempt other apps or services that might be subscribed to messages on tags.
- For NFC-enabled NFP providers, the driver MUST NOT transmit "\*:WriteTag" publications when connected to an NFC Forum Device (as opposed to an NFC Forum Tag).
- If one or more "\*:WriteTag" publications is enabled at the moment the driver detects a writable tag with sufficient space available for at least one of the payloads, the driver MUST write exactly one of the payloads to the tag. o In the event that more than one publications is active and small enough to be written to a tag, the most recently created or enabled "\*:WriteTag" publication MUST be the one written.
- If a "\*:WriteTag" publication is created or enabled while the driver is currently in communication with a writable tag with sufficient space available for the payload, the driver MUST write the payload to the tag even if the driver previously wrote to the tag.
- The driver MUST write to tags in such a way that the previous contents are overwritten.
- If a "\*:WriteTag" payload is successfully written to a tag, the driver MUST trigger the [**IOCTL_NFP_GET_NEXT_TRANSMITTED_MESSAGE**](/windows-hardware/drivers/ddi/nfpdev/ni-nfpdev-ioctl_nfp_get_next_transmitted_message) handling (as specified above) for that publication.

## Related topics

- [Near field communications (NFC) API reference](/windows-hardware/drivers/ddi/_nfpdrivers/)
