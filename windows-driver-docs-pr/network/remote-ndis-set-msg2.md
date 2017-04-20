---
title: REMOTE\_NDIS\_SET\_MSG
description: REMOTE\_NDIS\_SET\_MSG
ms.assetid: 28672557-bf29-480f-8f33-535dd70d3631
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# REMOTE\_NDIS\_SET\_MSG


## <a href="" id="ddk-remote-ndis-set-msg-ng"></a>


[**REMOTE\_NDIS\_SET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570654) is sent to a Remote NDIS device from a host, when it needs to set the value of some operational parameter on the device. The specific parameter being set is identified by means of an Object Identifier (OID), and the value it is to be set to is contained in an information buffer sent along with the message. The host may send **REMOTE\_NDIS\_SET\_MSG** to the device through the control channel at any time that the device is in a state not yet initialized by Remote NDIS. A Remote NDIS device will respond to a **REMOTE\_NDIS\_SET\_MSG** message with a status.

 

 





