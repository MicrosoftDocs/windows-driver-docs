---
title: Pairing Bluetooth protocol
description: Pairing Bluetooth protocol
ms.assetid: 6C95CA57-A226-4252-91E2-FAD8F1A0432B
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pairing:Bluetooth protocol


The “Pairing:Bluetooth” protocol is a means of abstracting a subscription for a Bluetooth OOB pairing structure. Windows subscribes to this type in order to register with the provider that Windows is interested in receiving Bluetooth OOB pairing structures in order to complete proximity-triggered Bluetooth simple OOB pairing.

**Note**  The behavior for publications of Pairing:Bluetooth is undefined

 

**Note**  For NFC-enabled NFP providers, both defined formats (Static Connection Handover Single Bluetooth Carrier and Simplified Tag Format) must be supported. Negotiated Connection Handover must NOT be supported.

 

### Required Actions

-   If the proximity technology is advertised as NFC, then the driver MUST match subscriptions for the “Pairing:Bluetooth” protocol with NDEF messages that have a TNF field value of 0x02 and a TYPE field that is equal to “application/vnd.bluetooth.ep.oob”.

    The driver MUST return ONLY the NDEF record’s PAYLOAD to subscribers of this type.

-   If the proximity technology is advertised as NFC, then the driver MUST also match subscriptions for the “Pairing:Bluetooth” protocol with NDEF messages where the first record has a TNF field value of 0x01, a TYPE field that is equal to “Hs”, and a single alternative carrier record that points to a Bluetooth Carrier Configuration Record (mime-type “application/vnd.bluetooth.ep.oob”).
    -   The driver MUST return ONLY the PAYLOAD of the “application/vnd.bluetooth.ep.oob” NDEF record to subscribers of this type.
    -   The driver MUST only support Static Connection Handover. The driver MUST NOT support other mechanisms within Connection Handover such as Negotiated Connection Handover.
    -   See \[NFC BTSSP\] for more information.
-   The driver MAY support publication of the “Pairing:Bluetooth” type. This publication format is undefined for NFC.
-   The driver MAY support other compatible schemes as well.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

