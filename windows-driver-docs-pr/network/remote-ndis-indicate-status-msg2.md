---
title: REMOTE_NDIS_INDICATE_STATUS_MSG
description: REMOTE_NDIS_INDICATE_STATUS_MSG
ms.assetid: 1858ac41-30d2-4ae0-86ba-ebdf6dc90d5a
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# REMOTE\_NDIS\_INDICATE\_STATUS\_MSG


## <a href="" id="ddk-remote-ndis-indicate-status-msg-ng"></a>


The device may send [**REMOTE\_NDIS\_INDICATE\_STATUS\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570617) to the host through the control channel in an unsolicited fashion at any time that the device is in a state initialized by Remote NDIS. This message is used to indicate a change in the status of the device. A common use of this message is to notify the host of changes in link state (media connect status), using RNDIS\_STATUS\_MEDIA\_CONNECT and RNDIS\_STATUS\_MEDIA\_DISCONNECT status values. The device must send **REMOTE\_NDIS\_INDICATE\_STATUS\_MSG** with one of these status values whenever its link state changes. **REMOTE\_NDIS\_INDICATE\_STATUS\_MSG** can also be used to indicate an error event, such as an unrecognized message.

In the specific case where this message is sent in response to a host message that the device could not handle, the returned status value must be set to RNDIS\_STATUS\_INVALID\_DATA, and the status buffer is formatted to contain the following:

-   Additional status information about the error itself (for example, RNDIS\_STATUS\_NOT\_SUPPORTED).

-   Zero-based byte offset in the original message where the error was detected.

If the error condition was caused by an Remote NDIS message, for example the device can't recognize a particular Remote NDIS message, the device should append the original message at the end of the status message defined above.

[**REMOTE\_NDIS\_INDICATE\_STATUS\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570617) is used to report an error event only in circumstances where the device is not able to generate a response message with appropriate status. Examples of appropriate usage are:

-   On receiving a message with unsupported message type.

-   On receiving a [**REMOTE\_NDIS\_PACKET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570635) with unacceptable contents.

 

 





