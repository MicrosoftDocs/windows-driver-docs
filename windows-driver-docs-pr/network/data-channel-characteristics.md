---
title: Data Channel Characteristics
description: Data Channel Characteristics
ms.assetid: 3e178d82-32de-468c-8175-4b0c2684be76
keywords:
- bulk WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Data Channel Characteristics





The data channel for the device consists of the *Bulk* IN and OUT endpoints in the *Data Class* interface.

A single USB data transfer in either direction may consist of a single [REMOTE\_NDIS\_PACKET\_MSG](remote-ndis-packet-msg.md) or a longer multipacket message.

The USB transfer to send a data message from the host to the device is a standard USB bulk transfer to the Bulk OUT endpoint of the Data Class interface.

The USB transfer to send a data message from the device to the host is a standard USB bulk transfer from the Bulk IN endpoint of the Data Class interface. The host will read up to the number of bytes indicated by the *MaxTransferSize* field of [REMOTE\_NDIS\_INITIALIZE\_MSG](remote-ndis-initialize-msg.md), which will be no greater than 0x4000 bytes for a USB 1.1 device.

 

 





