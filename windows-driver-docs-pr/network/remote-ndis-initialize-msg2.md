---
title: REMOTE_NDIS_INITIALIZE_MSG
description: REMOTE_NDIS_INITIALIZE_MSG
ms.assetid: bc63390a-85b3-4df2-953d-7dc9fb01a787
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# REMOTE\_NDIS\_INITIALIZE\_MSG


## <a href="" id="ddk-remote-ndis-initialize-msg-ng"></a>


[**REMOTE\_NDIS\_INITIALIZE\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570624) is sent by the host to a Remote NDIS device to initialize the network connection. It is sent through the control channel and only when the device is in a state not yet initialized by Remote NDIS. The message indicates the following:

-   Maximum size, in bytes, of any single bus data transfer that the host expects to receive from the device. Typically, each bus data transfer accommodates a single Remote NDIS message. However, as described in Remote NDIS Data Message, the device may bundle several Remote NDIS messages containing data packets into a single transfer.

-   Major and minor Remote NDIS protocol version implemented by the host. This value is the highest Remote NDIS protocol version supported by the host.

 

 





