---
title: NDIS_STATUS_WWAN_SAR_TRANSMISSION_STATUS
description: Miniport drivers use the NDIS_STATUS_WWAN_SAR_TRANSMISSION_STATUS notification to inform the mobile broadband (MB) service about the completion of a previous OID_WWAN_SAR_TRANSMISSION_STATUS Query or Set request.
ms.assetid: 0F04AC31-A16F-4E6A-A5FF-A69574A300A1
ms.date: 08/20/2018
keywords: 
 -NDIS_STATUS_WWAN_SAR_TRANSMISSION_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_WWAN_SAR_TRANSMISSION_STATUS

Miniport drivers use the **NDIS_STATUS_WWAN_SAR_TRANSMISSION_STATUS** notification to inform the mobile broadband (MB) service about the completion of a previous [OID_WWAN_SAR_TRANSMISSION_STATUS](oid-wwan-sar-transmission-status.md) Query or Set request.

Unsolicited events are sent when there is a change to the active over-the-air (OTA) channels. For example, if a modem started uploading packet data, it would be required to set up uplink channels when it uses the network data channel so that it can upload payloads. This would trigger the notification to be provided to the operating system.

This notification uses the [**NDIS_WWAN_SAR_TRANSMISSION_STATUS_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_TRANSMISSION_STATUS_info) structure.

## Requirements

|   |   |
| --- | --- |
| Version | Windows 10, version 1703 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[MB SAR Platform Support](https://docs.microsoft.com/windows-hardware/drivers/network/mb-sar-platform-support)

[OID_WWAN_SAR_TRANSMISSION_STATUS](oid-wwan-sar-transmission-status.md)

[**NDIS_WWAN_SAR_TRANSMISSION_STATUS_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_transmission_status_info)
