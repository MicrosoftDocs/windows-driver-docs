---
title: Storage Class Driver's Support of I/O Requests
description: Storage Class Driver's Support of I/O Requests
keywords:
- storage class drivers WDK , I/O request support
- class drivers WDK storage , I/O request support
- I/O requests WDK storage
- IRPs WDK storage
ms.date: 04/20/2017
---

# Storage Class Driver's Support of I/O Requests


## <span id="ddk_storage_class_drivers_support_of_i_o_requests_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_SUPPORT_OF_I_O_REQUESTS_KG"></span>


The designer of a class driver for an entirely new type of storage device must determine an appropriate set of I/O requests for the driver to support, depending on the nature of the device. The set of requests to be supported generally includes at least the following:

[**IRP\_MJ\_CREATE**](../kernel/irp-mj-create.md) and, for some device types or for symmetry, [**IRP\_MJ\_CLOSE**](../kernel/irp-mj-close.md)

[**IRP\_MJ\_DEVICE\_CONTROL**](../kernel/irp-mj-device-control.md)

[**IRP\_MJ\_READ**](../kernel/irp-mj-read.md), [**IRP\_MJ\_WRITE**](../kernel/irp-mj-write.md), or both

[**IRP\_MJ\_PNP**](../kernel/irp-mj-pnp.md)

[**IRP\_MJ\_POWER**](../kernel/irp-mj-power.md)

[**IRP\_MJ\_SYSTEM\_CONTROL**](../kernel/irp-mj-system-control.md)

 

