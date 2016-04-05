---
title: NFP-facilitated peripheral wireless device pairing
description: NFP-facilitated peripheral wireless device pairing
ms.assetid: 7B57019F-C80A-4E74-BBC2-A26BEDEB20DD
---

# NFP-facilitated peripheral wireless device pairing


One of the scenarios NFP technologies can enable is the pairing with Windows of wireless devices such as Bluetooth keyboards, mice, and headphones. Only unidirectional pairing is supported. Bidirectional pairing required by smart devices like cell phones is not supported.

In order to accomplish this kind of pairing, the device needs to make its transport-specific pairing information available to the NFP technology. In the case of a Bluetooth mouse, the mouse will need to publish the standard Bluetooth Out-Of-Band (OOB) pairing information, as defined by the Bluetooth SIG. The NFP provider needs to read that OOB data from the device and hand it to the Windows service subscribed to pairing type messages.

The NFP provider must understand and handle Bluetooth pairing type messages. These are identified by the type component of the *messageType* parameter. An example might be “Pairing:Bluetooth”, which would correspond to a device that supports static Bluetooth OOB pairing. When the NFP provider receives one of these pairing messages, it must translate the message into just the standard OOB pairing data, removing any technology-specific protocol information (like NDEF headers).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFP-facilitated%20peripheral%20wireless%20device%20pairing%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




