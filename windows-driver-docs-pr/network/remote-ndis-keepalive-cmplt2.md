---
title: REMOTE\_NDIS\_KEEPALIVE\_CMPLT
description: REMOTE\_NDIS\_KEEPALIVE\_CMPLT
ms.assetid: 07267e90-a0e5-41ac-8c0b-fca27f617e23
---

# REMOTE\_NDIS\_KEEPALIVE\_CMPLT


## <a href="" id="ddk-remote-ndis-keepalive-cmplt-ng"></a>


A Remote NDIS device will respond to a [**REMOTE\_NDIS\_KEEPALIVE\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570629) message from the host by sending back a [**REMOTE\_NDIS\_KEEPALIVE\_CMPLT**](https://msdn.microsoft.com/library/windows/hardware/ff570626) response message. If the returned Status is not RNDIS\_STATUS\_SUCCESS, then the host will send [**REMOTE\_NDIS\_RESET\_MSG**](https://msdn.microsoft.com/library/windows/hardware/ff570648) to reset the device.

 

 





