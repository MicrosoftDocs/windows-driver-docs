---
title: NDIS_STATUS_WWAN_SAR_TRANSMISSION_STATUS
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_SAR_TRANSMISSION_STATUS notification to inform the mobile broadband (MB) service about the completion of a previous OID_WWAN_SAR_TRANSMISSION_STATUS Query or Set request.
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_WWAN_SAR_TRANSMISSION_STATUS Network Drivers Starting with Windows Vista
---

# NDIS_STATUS_WWAN_SAR_TRANSMISSION_STATUS

Miniport drivers use the **NDIS_STATUS_WWAN_SAR_TRANSMISSION_STATUS** notification to inform the mobile broadband (MB) service about the completion of a previous [OID_WWAN_SAR_TRANSMISSION_STATUS](oid-wwan-sar-transmission-status.md) Query or Set request.

Unsolicited events are sent when there is a change to the active over-the-air (OTA) channels. For example, if a modem started uploading packet data, it would be required to set up uplink channels when it uses the network data channel so that it can upload payloads. This would trigger the notification to be provided to the operating system.

This notification uses the [**NDIS_WWAN_SAR_TRANSMISSION_STATUS_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_TRANSMISSION_STATUS_info) structure.

## Requirements

**Version**: Windows 10, version 1703
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB SAR Platform Support](./mb-sar-platform-support.md)

[OID_WWAN_SAR_TRANSMISSION_STATUS](oid-wwan-sar-transmission-status.md)

[**NDIS_WWAN_SAR_TRANSMISSION_STATUS_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_transmission_status_info)
