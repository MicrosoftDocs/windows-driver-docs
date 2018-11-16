---
title: NFP-facilitated peripheral wireless device pairing
description: NFP-facilitated peripheral wireless device pairing
ms.assetid: 7B57019F-C80A-4E74-BBC2-A26BEDEB20DD
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NFP-facilitated peripheral wireless device pairing


One of the scenarios NFP technologies can enable is the pairing with Windows of wireless devices such as Bluetooth keyboards, mice, and headphones. Only unidirectional pairing is supported. Bidirectional pairing required by smart devices like cell phones is not supported.

In order to accomplish this kind of pairing, the device needs to make its transport-specific pairing information available to the NFP technology. In the case of a Bluetooth mouse, the mouse will need to publish the standard Bluetooth Out-Of-Band (OOB) pairing information, as defined by the Bluetooth SIG. The NFP provider needs to read that OOB data from the device and hand it to the Windows service subscribed to pairing type messages.

The NFP provider must understand and handle Bluetooth pairing type messages. These are identified by the type component of the *messageType* parameter. An example might be “Pairing:Bluetooth”, which would correspond to a device that supports static Bluetooth OOB pairing. When the NFP provider receives one of these pairing messages, it must translate the message into just the standard OOB pairing data, removing any technology-specific protocol information (like NDEF headers).

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

