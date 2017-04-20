---
title: REMOTE\_NDIS\_HALT\_MSG
description: REMOTE\_NDIS\_HALT\_MSG
ms.assetid: 2e3a15fb-457d-4e81-b5ed-8d77e8e77901
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# REMOTE\_NDIS\_HALT\_MSG


## <a href="" id="ddk-remote-ndis-halt-msg-ng"></a>


[**REMOTE\_NDIS\_HALT\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570613) is sent by either the host or the Remote NDIS device in order to terminate the network connection. Unlike the other host initiated control messages, there is no device response to **REMOTE\_NDIS\_HALT\_MSG**. The message may be sent at any time that the device is in a state not initialized by Remote NDIS. All outstanding requests and packets should be discarded on receipt of this message.

It is optional for the device to implement sending the message [**REMOTE\_NDIS\_HALT\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570613). If implemented, the device sends this message to the host through the control channel only when the device is in a state not yet initialized by Remote NDIS. The device must terminate all communication immediately after sending this message. Sending this message causes the device to enter a state not initialized by Remote NDIS.

 

 





