---
title: Initializing and Unloading a SAN Proxy Driver
description: Initializing and Unloading a SAN Proxy Driver
ms.assetid: 1c602f7d-a1c2-429a-a297-4290a7cbfd9f
keywords:
- proxy drivers WDK SANs , initializing
- SAN proxy drivers WDK , initializing
- proxy drivers WDK SANs , unloading
- SAN proxy drivers WDK , unloading
- unloading drivers
- initializing SAN proxy drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initializing and Unloading a SAN Proxy Driver





In addition to creating and initializing a device object for the driver object, the proxy driver's **DriverEntry** routine can register to be notified when NICs under the driver's control are either added or removed. For more information, see [Registering for SAN NIC Notifications](registering-for-san-nic-notifications.md).

If the proxy driver's SAN service provider sends I/O control requests down to the proxy driver, then **DriverEntry** must specify an *entry point* that enables device control. The provider might request, for example, to retrieve the list of IP addresses assigned to the driver's NICs. An entry point for this request is an [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) dispatch routine that returns the list of IP addresses assigned to the driver's NICs. For more information, see [Implementing IOCTLs for a SAN Service Provider](implementing-ioctls-for-a-san-service-provider.md).

The **DriverEntry** routine must specify an entry point for a routine that unloads the proxy driver. This unload routine removes the device that was created in **DriverEntry**.

 

 





