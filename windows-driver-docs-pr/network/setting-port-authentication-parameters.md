---
title: Setting Port Authentication Parameters
description: Setting Port Authentication Parameters
ms.assetid: 88ac8229-d1d5-4287-8b5d-3a7b9b1f2e89
keywords:
- ports WDK NDIS , OID requests
- NDIS ports WDK , OID requests
- OID requests WDK NDIS ports
- authentication parameters WDK NDIS ports
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Port Authentication Parameters





NDIS and overlying drivers use an [OID\_GEN\_PORT\_AUTHENTICATION\_PARAMETERS](https://docs.microsoft.com/windows-hardware/drivers/network/oid-gen-port-authentication-parameters) OID set request to set the current state of an NDIS port. Miniport drivers that support NDIS ports must support this OID.

If the set request is successful, the miniport driver uses the receive port direction, port control state, and authenticate state from an [**NDIS\_PORT\_AUTHENTICATION\_PARAMETERS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_authentication_parameters) structure.

The miniport should generate an [**NDIS\_STATUS\_PORT\_STATE**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-port-state) status indication to notify overlying drivers of any state changes.

 

 





