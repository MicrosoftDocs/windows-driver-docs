---
title: Remote NDIS Data Message
author: windows-driver-content
Description: Remote NDIS Data Message
ms.assetid: 99ba2f83-9e2c-4681-a4ff-d61fedb20884
ms.author: windowsdriverdev
ms.date: 07/31/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Remote NDIS Data Message


## <a href="" id="ddk-remote-ndis-data-message-nr"></a>


A Remote NDIS device encapsulates NDIS packets to transfer them across the data channel. Data messages are used to do this because they can contain out-of-band (OOB) data or per-packet information.

The data message that is used to encapsulate data for transfer across the data channel is described in the following topic:

[**REMOTE\_NDIS\_PACKET\_MSG**](remote-ndis-packet-msg.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20Remote%20NDIS%20Data%20Message%20%20RELEASE:%20%287/31/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


