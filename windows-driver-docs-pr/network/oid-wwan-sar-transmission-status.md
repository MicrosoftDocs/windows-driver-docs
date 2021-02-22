---
title: OID_WWAN_SAR_TRANSMISSION_STATUS
description: OID_WWAN_SAR_TRANSMISSION_STATUS enables or disables notifications from a mobile broadband (MB) modem on Specific Absorption Rate (SAR) transmission state.
ms.date: 08/20/2018
keywords: 
 -OID_WWAN_SAR_TRANSMISSION_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_WWAN_SAR_TRANSMISSION_STATUS

OID_WWAN_SAR_TRANSMISSION_STATUS enables or disables notifications from a mobile broadband (MB) modem on Specific Absorption Rate (SAR) transmission state.

Miniport drivers must process Query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_SAR_TRANSMISSION_STATUS](ndis-status-wwan-sar-transmission-status.md) status notification containing an [**NDIS_WWAN_SAR_TRANSMISSION_STATUS_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_transmission_status_info) structure that describes whether notifications on SAR transmit state are enabled in the modem.

For Set requests, this OID's payload contains an [**NDIS_WWAN_SET_SAR_TRANSMISSION_STATUS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_sar_transmission_status) structure that specifies if SAR transmission status notifications should be enabled or disabled.

## Remarks

After each Query or Set request, the miniport driver should return an [**NDIS_WWAN_SAR_TRANSMISSION_STATUS_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_transmission_status_info) structure that describes whether SAR notifications on transmit state are enabled in the modem.

For more information about usage of this OID, see [MBIM_CID_MS_TRANSMISSION_STATUS](./mb-sar-platform-support.md#mbim_cid_ms_transmission_status).

## Requirements

**Version**: Windows 10, version 1703
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB SAR Platform Support](./mb-sar-platform-support.md)

[NDIS_STATUS_WWAN_SAR_TRANSMISSION_STATUS](ndis-status-wwan-sar-transmission-status.md)

[**NDIS_WWAN_SAR_TRANSMISSION_STATUS_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_transmission_status_info)

[**NDIS_WWAN_SET_SAR_TRANSMISSION_STATUS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_sar_transmission_status)
