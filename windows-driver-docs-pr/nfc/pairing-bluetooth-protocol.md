---
title: Pairing Bluetooth protocol
author: windows-driver-content
description: Pairing Bluetooth protocol
ms.assetid: 6C95CA57-A226-4252-91E2-FAD8F1A0432B
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
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

------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Pairing:Bluetooth%20protocol%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
