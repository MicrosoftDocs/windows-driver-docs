---
title: NDEF protocol
description: NDEF protocol
ms.assetid: 5AF082EC-70D6-4117-BFCE-B28A8DBAC210
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDEF protocol


The “NDEF” protocol is a means of interacting with NFC Forum devices directly as mapped through the NFP provider pub/sub model. Any client using this protocol will be required to understand how to encode and decode NDEF packets. For publishing messages, a client would merely specify the type as “NDEF”, because the rest of the type information is embedded within the NDEF message itself. Publishing “NDEF” types allows a client nearly direct pass-through access to send NDEF messages over NFC. To subscribe, a client would specify “NDEF” followed by a ‘:’ (colon).

Following the colon are one of six record types.

-   Empty
-   ext
-   MIME
-   URI
-   wkt
-   Unknown

A provider supports NDEF by following the basic provider requirements as well as the NDEF protocol–specific requirements listed in this section.

To listen for these NDEF messages, a client subscribes to one of the supported types, such as “NDEF:wkt.Sp”. Whenever the provider detects an NDEF message that matches the type, the entire NDEF message (still encoded in NDEF) is delivered to the subscribing client. As per convention in \[NDEF\], the ‘type’ to be matched for an NDEF message is the TYPE field specified in the first NDEF record of an NDEF message. Again, to transmit an NDEF message, a client publishes a complete NDEF message specifying a protocol of “NDEF”.

There is also a mechanism for subscribing to ALL NDEF messages; this is accomplished by subscribing to “NDEF”.

## Common NDEF Protocol Driver Requirements


There are several requirements common for NDEF support on the drivers of all NFC-enabled NFP providers.

### Required Actions

-   The driver MUST match received NDEF messages to subscriptions based on the TNF and TYPE fields of the first NDEF record in the NDEF message as specified in \[NDEF\].
-   If one or more “\*:WriteTag” publications is enabled and the driver detects a writable tag with enough space available, the existing payload of the tag MUST NOT be read for the purposes of matching other subscriptions. This allows a tag-writing app to preempt other apps or services that might be subscribed to messages on tags.
-   For NFC-enabled NFP providers, the driver MUST NOT transmit “\*:WriteTag” publications when connected to an NFC Forum Device (as opposed to an NFC Forum Tag).
-   If one or more “\*:WriteTag” publications is enabled at the moment the driver detects a writable tag with sufficient space available for at least one of the payloads, the driver MUST write exactly one of the payloads to the tag. o In the event that more than one publications is active and small enough to be written to a tag, the most recently created or enabled “\*:WriteTag” publication MUST be the one written.
-   If a “\*:WriteTag” publication is created or enabled while the driver is currently in communication with a writable tag with sufficient space available for the payload, the driver MUST write the payload to the tag even if the driver previously wrote to the tag.
-   The driver MUST write to tags in such a way that the previous contents is overwritten.
-   If a “\*:WriteTag” payload is successfully written to a tag, the driver MUST trigger the [**IOCTL\_NFP\_GET\_NEXT\_TRANSMITTED\_MESSAGE**](https://msdn.microsoft.com/library/windows/hardware/jj853320) handling (as specified above) for that publication.

## Publications for “NDEF:WriteTag”


This is a special type of publication that allows one or more NDEF messages to be written to an NFC Forum tag.

### Required Actions

-   The common “\*:WriteTag” requirements described elsewhere apply.
-   Because an NFC Forum tag can contain multiple NDEF messages, the driver MUST correctly accept “NDEF:WriteTag” publications that happen to have multiple concatenated NDEF messages as payload.

## Publications for “SetTagReadOnly”


This publication allows for the client to lock a tag to read only. The provider must convert an already formatted NDEF read/write tag to Read only.

### Required Actions

-   The driver must first check if the connected tag is NDEF compliant.
-   If one or more “\*:.WriteTag” publications is enabled and the driver detects a writable tag, the driver MUST write to the tag first, adhering to the common “\*:WriteTag” requirements described elsewhere, and then convert the NDEF read/write tag to read only.

## Empty NDEF Record: “NDEF:Empty”


There is no type, ID, or payload in this message. It seems that subscriptions with the “NDEF:Empty” type do not make any sense from the point of view of a Windows client.

### Required Actions

Subscriptions or publications with this type MUST be rejected by the proximity provider driver with STATUS\_INVALID\_PARAMETER.

## Subscriptions for all NDEF types: “NDEF”


Clients can subscribe to all received NDEF messages. Typically, if the application knows the type of message it’s interested in, it will subscribe to that type specifically. However, it is sometimes useful to subscribe to every NDEF message. For example, an application that can copy and write a duplicate NDEF Tag might find this useful.

### Required Actions

The driver MUST match subscriptions for “NDEF” with each NDEF Message it receives.

## Subscriptions for External NDEF RTD Types: “NDEF:ext.”


Vendors can use a custom extensible RTD namespace to define the contents of their proprietary messages. This allows a client to subscribe to RTD external types defined not by the NFC Forum, but by the app or a third-party.

Generic Example Type: “NDEF:ext.&lt;SomeExternalType&gt;”

Concrete Example Type: “NDEF:ext.contoso.com:mytype”

### Required Actions

The driver MUST match subscriptions for “NDEF:ext.&lt;SomeExternalType&gt;” ONLY with received NDEF messages that have a TNF field value of 0x04 and that have a TYPE field that matches “&lt;SomeExternalType&gt;” based on the equivalence rules specified in \[NFC RTD\].

## Subscriptions for “NDEF:MIME.”


Messages can use the MIME namespace to define the contents of the message.

Generic Example Type: “NDEF:MIME.&lt;SomeMimeType&gt;”

Concrete Example Type: “NDEF:MIME.image/jpeg”

### Required Actions

The driver MUST match subscriptions for “NDEF:MIME.&lt;SomeMimeType&gt;” ONLY with received NDEF messages that have a TNF field value of 0x02 and that have a TYPE field that matches “&lt;SomeMimeType&gt;” based on the equivalence rules specified in \[NDEF\].

## Subscriptions for “NDEF:wkt.”


Messages can use the NFC Forum Well Known Type namespace to define the contents of the message.

### Required Actions

-   The driver MUST match subscriptions for “NDEF:wkt.&lt;SomeWellKnownType&gt;” ONLY with received NDEF messages that have a TNF field value of 0x01 and that have a TYPE field that matches “&lt;SomeWellKnownType&gt;” based on the equivalence rules specified in \[NDEF\].
-   The driver MUST NOT validate well known types, so that future well known types can be defined by NFC Forum without requiring a driver update.

## Subscriptions for Unknown NDEF Type: “NDEF:Unknown”


This allows a client to subscribe to an un-typed payload of data.

### Required Actions

The driver MUST match subscriptions for “NDEF:Unknown” ONLY with NDEF messages that have a TNF field value of 0x05 as specified in \[NDEF\].

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

