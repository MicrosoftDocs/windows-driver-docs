---
title: NDIS_STATUS_TIMESTAMP_CAPABILITY
description: Miniport drivers use the NDIS_STATUS_TIMESTAMP_CAPABILITY status indication to report the NIC and miniport driver timestamping capabilities.
ms.date: 12/31/2020
keywords:
 - NDIS_STATUS_TIMESTAMP_CAPABILITY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_TIMESTAMP_CAPABILITY

Miniport drivers use the **NDIS_STATUS_TIMESTAMP_CAPABILITY** status indication to report the NIC's hardware timestamping capabilities and the miniport driver's software timestamping capabilities to NDIS and overlying drivers.

This status indication represents the timestamping capabilities of the hardware and miniport driver, not which capability is currently enabled or disabled. See [**NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG**](ndis-status-timestamp-current-config.md)(ADD LINK) for more information on reporting current timestamping capabilities.

## Remarks

During initialization, the miniport driver should indicate its hardware and software timestamp capabilities from within its [**MiniportInitializeEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function.

Miniport drivers generate **NDIS_STATUS_TIMESTAMP_CAPABILITY** status indications by calling the [**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex) function. The **StatusBuffer** field of the [**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication) structure should point to an [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure. For more information on how to set the members of the **NDIS_TIMESTAMP_CAPABILITIES** structure, see [**Reporting NDIS timestamping capabilities](ADD LINK)

The miniport driver must also generate the **NDIS_STATUS_TIMESTAMP_CAPABILITY** status indication whenever it detects a change in underlying hardware capabilities.

## Requirements

**Version**: NDIS 6.82 and later

**Header**: Ntddndis.h (include Ndis.h)

## See also

[**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities)

[**NDIS_STATUS_TIMESTAMP_CURRENT_CONFIG**](ndis-status-timestamp-current-config.md)

[**MiniportInitializeEx**](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize)

[**NdisMIndicateStatusEx**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismindicatestatusex)

[**NDIS\_STATUS\_INDICATION**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_status_indication)