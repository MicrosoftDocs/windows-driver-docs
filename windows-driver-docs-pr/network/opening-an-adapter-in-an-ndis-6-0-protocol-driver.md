---
title: Opening an Adapter in an NDIS 6.0 Protocol Driver
description: Opening an Adapter in an NDIS 6.0 Protocol Driver
ms.assetid: 15a0cdc2-388d-4122-a456-2aaec5812a2e
keywords:
- NdisOpenAdapterEx
- NdisOpenAdapter
- opening adapters
- adapters WDK networking
- opening
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening an Adapter in an NDIS 6.0 Protocol Driver





In NDIS 6.0, the [**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715) function replaces the [**NdisOpenAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff553673) function. A protocol driver calls **NdisOpenAdapterEx** from the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function. The driver passes protocol binding configuration parameters to **NdisOpenAdapterEx** in an [**NDIS\_OPEN\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566734) structure.

If a protocol driver returns NDIS\_STATUS\_PENDING from *ProtocolBindAdapterEx*, it must call the [**NdisCompleteBindAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561702) function (formerly [**NdisCompleteBindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff551036)) with the final status to complete the bind request.

If NDIS returns NDIS\_STATUS\_PENDING from **NdisOpenAdapterEx**, NDIS later calls the protocol driver's [*ProtocolOpenAdapterCompleteEx*](https://msdn.microsoft.com/library/windows/hardware/ff570265) function (formerly [**ProtocolOpenAdapterComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563238)) with the final status after the open request has been completed.

Before the driver calls **NdisOpenAdapterEx**, the driver can pass the pointer at the *BindParameters* parameter of *ProtocolBindAdapterEx* to the [**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/ff563717) function to read the configuration parameters that are associated with a binding. After a successful **NdisOpenAdapterEx** call, the driver can pass the handle at the *ProtocolBindingContext* parameter of **NdisOpenAdapterEx** to **NdisOpenConfigurationEx** to read the configuration parameters that are associated with a binding. For more information about **NdisOpenConfigurationEx**, see [Reading the Registry in NDIS 6.0 Protocol Drivers](reading-the-registry-in-an-ndis-6-0-protocol-driver.md).

 

 





