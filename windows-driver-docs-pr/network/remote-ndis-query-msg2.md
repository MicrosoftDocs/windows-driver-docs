---
title: REMOTE\_NDIS\_QUERY\_MSG
description: REMOTE\_NDIS\_QUERY\_MSG
ms.assetid: 36da5e67-384b-4d3c-93e6-5c09a9bc7cf6
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# REMOTE\_NDIS\_QUERY\_MSG


## <a href="" id="ddk-remote-ndis-query-msg-ng"></a>


[**REMOTE\_NDIS\_QUERY\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570641) is sent to a Remote NDIS device from a host when it needs to query the device for its characteristics or statistics information or status. The parameter or statistics counter being queried for is identified by means of an NDIS Object Identifier (OID).

The host may send [**REMOTE\_NDIS\_QUERY\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570641) to the device through the control channel at any time that the device is in a state not initialized by Remote NDIS. A Remote NDIS device will respond to **REMOTE\_NDIS\_QUERY\_MSG** with information about the desired capabilities or status.

The host sends the following information in this message:

-   Remote NDIS message ID value. This value is used to match the messages sent by the host with device's responses.

-   NDIS OID.

-   Length of the input data, if any, for the query.

-   Byte offset from the beginning of the Remote NDIS message ID value where the input data, if any, for the query is located.

 

 





