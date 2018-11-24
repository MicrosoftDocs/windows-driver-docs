---
title: USB Short Packets
description: USB Short Packets
ms.assetid: e59476cf-754e-4550-849f-3aa645defe09
keywords:
- USB short packets WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Short Packets





USB passes data over the wire in the form of USB packets, which should not be confused with NDIS or networking packets. The maximum length of a USB packet to or from a USB endpoint is limited to the value of the **wMaxPacketSize** field of the endpoint's descriptor. For bulk pipes the maximum packet size is 64 bytes. Due to constraints of certain USB host controllers, there is a penalty associated with using short USB packets (for example, those of less then 64 bytes, when streaming data).

To work around this limitation, Remote NDIS USB devices may append zero-byte padding to data messages so that a short packet will not occur (within the constraints of the **MaxTransferSize** field of [REMOTE\_NDIS\_INITIALIZE\_MSG](remote-ndis-initialize-msg.md)). The **MessageLength** field of the final [REMOTE\_NDIS\_PACKET\_MSG](remote-ndis-packet-msg.md) does not include these appended padding bytes.

If the device has transmitted its last available REMOTE\_NDIS\_PACKET\_MSG (so no more are left in the device's queue), then it is acceptable to send a short USB packet.

If the last REMOTE\_NDIS\_PACKET\_MSG of a device-send Remote NDIS data message (without any zero-byte padding) ends with a USB packet whose length is exactly the **wMaxPacketSize** for that endpoint, then the device may send an additional one-byte zero packet as an appended part of the transfer. Some device implementations are simplified by this allowance.

Similarly, some device-side USB chipsets do not detect the end of a received USB transfer that ends with a USB packet whose length is the **wMaxPacketSize** for that endpoint. For this reason, the host must append a one-byte zero packet to a data transfer that otherwise would have a length that is a multiple of the **wMaxPacketSize** of the receiving endpoint. USB Remote NDIS devices must tolerate the appended byte. The **MessageLength** field of the final REMOTE\_NDIS\_PACKET\_MSG does not include this appended byte.

 

 





