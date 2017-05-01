---
title: REMOTE\_NDIS\_INITIALIZE\_CMPLT
description: REMOTE\_NDIS\_INITIALIZE\_CMPLT
ms.assetid: 1e8cf7f0-0c18-415f-bc2c-9758b9ea51d2
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# REMOTE\_NDIS\_INITIALIZE\_CMPLT


## <a href="" id="ddk-remote-ndis-initialize-cmplt-ng"></a>


[**REMOTE\_NDIS\_INITIALIZE\_CMPLT**](https://msdn.microsoft.com/library/windows/hardware/ff570621) is sent by the Remote NDIS device to the host in response to a [**REMOTE\_NDIS\_INITIALIZE\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570624) message.

In this message, the Remote NDIS device indicates the following:

-   Remote NDIS message ID value. This value is used to match the messages sent by the host with device responses.

-   Status value of RNDIS\_STATUS\_SUCCESS if the device initialized successfully, otherwise the status value is set to an error code indicating the failure.

-   Highest Remote NDIS protocol version number that the device can support. The combined version number should be less than or equal to the version number specified by the host in the [**REMOTE\_NDIS\_INITIALIZE\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570624) message. This allows the device to fall back to a compatibility mode when the host implements a Remote NDIS protocol version that is lower than that supported by the device.

-   Medium type supported by the device. Set to RNDIS\_MEDIUM\_802\_3 (0x00000000).

-   Maximum number of Remote NDIS data messages that the device can handle in a single transfer to it. This value should be at least one.

-   Maximum size, in bytes, of a single data transfer that the device expects to receive from the host. The device can specify the byte alignment it expects for each Remote NDIS message that is part of a multimessage transfer to it. This alignment value is specified in terms of powers of two. For example, this value is set to 3 to indicate 8-byte alignment.

 

 





