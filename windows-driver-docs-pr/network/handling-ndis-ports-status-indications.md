---
title: Handling NDIS Ports Status Indications
description: Handling NDIS Ports Status Indications
keywords:
- ports WDK NDIS , status indications
- NDIS ports WDK , status indications
- status indications WDK networking , NDIS ports
- port states WDK NDIS
ms.date: 04/20/2017
---

# Handling NDIS Ports Status Indications





If an NDIS port is the source of a status indication, a miniport driver should use the **PortNumber** member in the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure to specify the source port. Miniport drivers never indicate status for inactive ports.

Miniport drivers should use the [**NDIS\_STATUS\_PORT\_STATE**](./ndis-status-port-state.md) status indication to indicate changes in the state of an NDIS port. For this status indication, miniport drivers must set the port number in the **PortNumber** member of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure. The **StatusBuffer** member of the NDIS\_STATUS\_INDICATION structure contains a pointer to an [**NDIS\_PORT\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_port_state) structure.

 

