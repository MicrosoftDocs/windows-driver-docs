---
title: OID_WWAN_SAR_CONFIG
description: OID_WWAN_SAR_CONFIG gets or sets information about a mobile broadband (MB) device's Specific Absorption Rate (SAR) back off mode and level.
ms.assetid: 78B049E0-A80E-42AA-9D81-D45BBCF84FCB
ms.date: 08/17/2018
keywords: 
 -OID_WWAN_SAR_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_WWAN_SAR_CONFIG

OID_WWAN_SAR_CONFIG gets or sets information about a mobile broadband (MB) device's Specific Absorption Rate (SAR) back off mode and level. 

Miniport drivers must process Query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_SAR_CONFIG](ndis-status-wwan-sar-config.md) status notification containing an [**NDIS_WWAN_SAR_CONFIG_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_config_info) structure that describes the current SAR configuration.

For Set requests, this OID's payload contains an [**NDIS_WWAN_SET_SAR_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_set_sar_config) structure that specifies the new SAR configuration for the modem.

## Remarks

After each Query or Set request, the miniport driver should return an [**NDIS_WWAN_SAR_CONFIG_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_config_info) structure that contains information for all antennas on the device associated with Mobile Broadband.

For more information about usage of this OID, see [MBIM_CID_MS_SAR_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/network/mb-sar-platform-support#mbimcidmssarconfig).

## Requirements

|   |   |
| --- | --- |
| Version | Windows 10, version 1703 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[MB SAR Platform Support](https://docs.microsoft.com/windows-hardware/drivers/network/mb-sar-platform-support)

[NDIS_STATUS_WWAN_SAR_CONFIG](ndis-status-wwan-sar-config.md)

[**NDIS_WWAN_SAR_CONFIG_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_config_info)

[**NDIS_WWAN_SET_SAR_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_set_sar_config)
