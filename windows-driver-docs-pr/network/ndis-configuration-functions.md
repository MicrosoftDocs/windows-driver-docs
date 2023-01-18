---
title: NDIS Configuration Functions
description: NDIS Configuration Functions
keywords:
- configuration functions WDK NDIS
ms.date: 04/20/2017
---

# NDIS Configuration Functions





NDIS includes the following functions to simplify driver configuration:

[**NdisOpenConfigurationEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisopenconfigurationex)

[**NdisMGetBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismgetbusdata)

[**NdisMSetBusData**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetbusdata)

To obtain configuration information for an adapter, an NDIS miniport driver calls **NdisOpenConfigurationEx** and [**NdisReadConfiguration**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisreadconfiguration). The driver can call **NdisMGetBusData** to obtain bus-specific information. The driver can call **NdisMSetBusData** to set bus-specific information.

A protocol driver uses a registry path to an adapter name to read configuration parameters that are specific to the binding between the driver and the underlying adapter. NDIS provides the registry path in the call to the [*ProtocolBindAdapterEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-protocol_bind_adapter_ex) function. The driver can pass this registry path to the [**NdisOpenProtocolConfiguration**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisopenprotocolconfiguration) function or to direct registry calls. As an alternative, the driver can pass a *BindParameters* structure to the **NdisOpenConfigurationEx** function to read the same parameters.

 

