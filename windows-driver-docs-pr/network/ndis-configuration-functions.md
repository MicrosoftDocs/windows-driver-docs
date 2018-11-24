---
title: NDIS Configuration Functions
description: NDIS Configuration Functions
ms.assetid: 248e08d0-6145-499a-b307-2a5ffbd3733f
keywords:
- configuration functions WDK NDIS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Configuration Functions





NDIS includes the following functions to simplify driver configuration:

[**NdisOpenConfigurationEx**](https://msdn.microsoft.com/library/windows/hardware/ff563717)

[**NdisMGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff563591)

[**NdisMSetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff563670)

To obtain configuration information for an adapter, an NDIS miniport driver calls **NdisOpenConfigurationEx** and [**NdisReadConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff564511). The driver can call **NdisMGetBusData** to obtain bus-specific information. The driver can call **NdisMSetBusData** to set bus-specific information.

A protocol driver uses a registry path to an adapter name to read configuration parameters that are specific to the binding between the driver and the underlying adapter. NDIS provides the registry path in the call to the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function. The driver can pass this registry path to the [**NdisOpenProtocolConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff553683) function or to direct registry calls. As an alternative, the driver can pass a *BindParameters* structure to the **NdisOpenConfigurationEx** function to read the same parameters.

 

 





