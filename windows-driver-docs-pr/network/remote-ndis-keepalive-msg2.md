---
title: REMOTE_NDIS_KEEPALIVE_MSG
description: REMOTE_NDIS_KEEPALIVE_MSG
ms.assetid: 2da0be7e-db6d-4bc6-ad7a-20c74ed4604d
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# REMOTE\_NDIS\_KEEPALIVE\_MSG


## <a href="" id="ddk-remote-ndis-keepalive-msg-ng"></a>


The host sends a [**REMOTE\_NDIS\_KEEPALIVE\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570629) message to the device through the control channel in order to check the health of the device. When the device is in a state initialized by Remote NDIS, the host sends this message periodically when there has been no other control or data traffic from the device to the host for the *KeepAliveTimeoutPeriod*. *KeepAliveTimeoutPeriod* is bus-dependent and is defined in the appropriate bus-mapping specifications.

Upon receiving this message, the remote device must send back a response whose *Status* field indicates whether the device solicits a [**REMOTE\_NDIS\_RESET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570648) message from the host.

The host will not send [**REMOTE\_NDIS\_KEEPALIVE\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570629) until the *KeepAliveTimeoutPeriod* has elapsed since the last message received from the remote device. This avoids unnecessary exchange of **REMOTE\_NDIS\_KEEPALIVE\_MSG** messages when the communication channel is active.

The device may optionally send this message to the host as well. For example, the device may use this message to trigger a response from the host for the purpose of computing round-trip delay time. If implemented, the device must send [**REMOTE\_NDIS\_KEEPALIVE\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570629) through the control channel and only when in a state initialized by Remote NDIS.

The device does not need to perform any specific action if it stops seeing [**REMOTE\_NDIS\_KEEPALIVE\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570629) messages from the host.

 

 





