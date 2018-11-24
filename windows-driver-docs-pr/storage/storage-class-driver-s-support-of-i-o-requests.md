---
title: Storage Class Driver's Support of I/O Requests
description: Storage Class Driver's Support of I/O Requests
ms.assetid: 046b7978-49ee-4e3e-a85f-f6ad327b91bf
keywords:
- storage class drivers WDK , I/O request support
- class drivers WDK storage , I/O request support
- I/O requests WDK storage
- IRPs WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's Support of I/O Requests


## <span id="ddk_storage_class_drivers_support_of_i_o_requests_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_SUPPORT_OF_I_O_REQUESTS_KG"></span>


The designer of a class driver for an entirely new type of storage device must determine an appropriate set of I/O requests for the driver to support, depending on the nature of the device. The set of requests to be supported generally includes at least the following:

[**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729) and, for some device types or for symmetry, [**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff550720)

[**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744)

[**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794), [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819), or both

[**IRP\_MJ\_PNP**](https://msdn.microsoft.com/library/windows/hardware/ff550772)

[**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784)

[**IRP\_MJ\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550813)

 

 




