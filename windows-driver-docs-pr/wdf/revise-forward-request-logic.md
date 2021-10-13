---
title: Revise Forward Request Logic
description: Revise Forward Request Logic
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Revise Forward Request Logic


If a driver cannot complete a request by itself, it passes the request down the stack to the next lower driver. For a WDF driver, the next lower driver is considered the default I/O target and is represented by a WDFIOTARGET object. To get a handle to this object, the driver calls [**WdfDeviceGetIoTarget**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetiotarget).

For information about how a WDF driver passes a request down to the next lower driver in the stack, see [Forwarding I/O Requests](forwarding-i-o-requests.md).

 

