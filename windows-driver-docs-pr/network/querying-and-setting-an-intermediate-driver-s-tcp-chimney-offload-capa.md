---
title: Querying and setting TCP chimney offload for intermediate drivers
description: Querying and Setting an Intermediate Driver's TCP Chimney Offload Capabilities
ms.assetid: afa7fadf-81cf-4efb-8c66-5bd7af3c95b9
keywords:
- intermediate drivers WDK TCP chimney offload , capabilities
- capabilities WDK TCP chimney offload
- querying TCP chimney offload capabilities
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Querying and Setting an Intermediate Driver's TCP Chimney Offload Capabilities

\[The TCP chimney offload feature is deprecated and should not be used.\]

If an intermediate driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function returns NDIS\_STATUS\_SUCCESS, NDIS and the host stack query the operational characteristics of the offload target. In particular, the host stack queries the [OID\_TCP\_TASK\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569815) OID to determine an offload target's task offload and TCP chimney offload capabilities. For more information about task offload capabilities, see [**NDIS\_TASK\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff558995). For more information about TCP chimney offload capabilities, see [**NDIS\_TASK\_TCP\_CONNECTION\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567873).

If the intermediate driver allows either task offload or TCP chimney offload, it should propagate the query of OID\_TCP\_TASK\_OFFLOAD to the underlying driver. If the intermediate driver does not allow TCP chimney offload, it can still propagate up the underlying driver's advertisement of TCP chimney offload capabilities. In this situation, NDIS blocks TCP chimney offload for the intermediate driver and underlying drivers because the intermediate driver has not registered any *MiniportXxx* or *ProtocolXxx* TCP chimney functions.

If the intermediate driver allows neither task offload nor TCP chimney offload, its [*MiniportRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function should return NDIS\_STATUS\_NOT\_SUPPORTED in response to a query of OID\_TCP\_TASK\_OFFLOAD. This response blocks the underlying driver from receiving the query.After determining the underlying driver's task offload and TCP chimney offload capabilities, the host stack sets

OID\_TCP\_TASK\_OFFLOAD to enable the offload target's task offload and TCP chimney offload capabilities. An intermediate driver should always pass such a set request to the underlying driver.

 

 





