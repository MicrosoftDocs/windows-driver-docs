---
title: Security Issues for Network Drivers
description: Security Issues for Network Drivers
ms.assetid: 04400213-9bd4-4dbe-b302-24917450829f
keywords:
- network drivers WDK , security
- security WDK networking
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Security Issues for Network Drivers


## <a href="" id="ddk-security-issues-for-network-drivers-ng"></a>


For a general discussion on writing secure drivers, see [Creating Reliable Kernel-Mode Drivers](https://msdn.microsoft.com/library/windows/hardware/ff542904).

In particular, network drivers should do the following to enhance security:

-   All drivers should validate values that they read from the registry. Specifically, the caller of [**NdisReadConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564511) or [**NdisReadNetworkAddress**](https://msdn.microsoft.com/library/windows/hardware/ff564512) must not make any assumptions about values read from the registry and must validate each registry value that it reads. If the caller of **NdisReadConfiguration** determines that a value is out of bounds, it should use a default value instead. If the caller of **NdisReadNetworkAddress** determines that a value is out of bounds, it should use the permanent medium access control (MAC) address or a default address instead.

-   A miniport driver, in its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) or [**MiniportCoOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559362) functions, should validate any object identifier (OID) value that the driver is requested to set. If the driver determines that the value to be set is out of bounds, it should fail the set request. For more information about object identifiers, see [Obtaining and Setting Miniport Driver Information and NDIS Support for WMI](obtaining-and-setting-miniport-driver-information-and-ndis-support-for.md).

-   If an intermediate driver's *MiniportOidRequest* function does not pass a set operation to an underlying miniport driver, the function should validate the OID value. For more information, see [Intermediate Driver Query and Set Operations](intermediate-driver-query-and-set-operations.md).

 

 





