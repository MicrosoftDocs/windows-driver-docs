---
title: Framework I/O Request Object
description: Framework I/O Request Object
ms.assetid: e48437ee-597d-45b1-9093-8d5921356af5
keywords:
- UMDF objects WDK , I/O request objects
- framework objects WDK UMDF , I/O request objects
- I/O request objects WDK UMDF
- IWDFIoRequest
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework I/O Request Object


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The framework I/O request object is exposed to drivers by the [IWDFIoRequest](https://msdn.microsoft.com/library/windows/hardware/ff558985) interface. It encapsulates the details of an I/O operation. All I/O requests are represented as framework I/O request objects. The reflector notifies the driver host process when the reflector receives an I/O request packet (IRP) as the result of an application I/O operation, such as, a call to the Microsoft Win32 [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) or **ReadFile** function. The framework, in response to the reflector notification, constructs a new request object and puts it in the appropriate I/O queue. The queue configuration and the locking model chosen by the user-mode driver determine when the request is presented to the driver. For more information, see [Configuring Dispatch Mode for an I/O Queue](configuring-dispatch-mode-for-an-i-o-queue.md) and [Specifying a Callback Synchronization Mode](specifying-a-callback-synchronization-mode.md).

 

 





