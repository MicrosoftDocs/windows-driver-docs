---
title: Implementing IOCTLs for a SAN Service Provider
description: Implementing IOCTLs for a SAN Service Provider
ms.assetid: 7d4c7039-6b42-4620-aee5-9189b4acd030
keywords:
- proxy drivers WDK SANs , IOCTLs
- SAN proxy drivers WDK , IOCTLs
- IOCTLs WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implementing IOCTLs for a SAN Service Provider





If a SAN service provider sends I/O control (IOCTL) requests to the proxy driver, the driver should implement an [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) dispatch routine to process these requests. An IOCTL request can be a request to retrieve the list of IP addresses assigned to the driver's NICs, for example, or a request to allocate or release memory. The **DriverEntry** routine must specify an entry point for the dispatch routine.

The proxy driver's device control routine calls the [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) function, in which the device control routine passes a pointer to the IRP that was passed to the routine. The device control routine then determines which IOCTL request was received and processes the request accordingly.

After the current IOCTL request completes, the device control routine calls the [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) function and passes the status of the operation. This status is returned to the SAN service provider.

 

 





