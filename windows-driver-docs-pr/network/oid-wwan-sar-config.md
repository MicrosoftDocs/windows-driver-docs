---
title: OID_WWAN_SAR_CONFIG
author: windows-driver-content
description: OID_WWAN_SAR_CONFIG gets or sets information about a mobile broadband (MB) device's Specific Absorption Rate (SAR) back off mode and level.
ms.assetid: 78B049E0-A80E-42AA-9D81-D45BBCF84FCB
ms.author: windowsdriverdev
ms.date: 08/17/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_SAR_CONFIG Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_WWAN_SAR_CONFIG

OID_WWAN_SAR_CONFIG gets or sets information about a mobile broadband (MB) device's Specific Absorption Rate (SAR) back off mode and level. 

Miniport drivers must process Query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_SAR_CONFIG](ndis-status-wwan-sar-config.md) status notification containing an [**NDIS_WWAN_SAR_CONFIG_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_config_info) structure that describes the current SAR configuration.

For Set requests, this OID's payload contains an [**NDIS_WWAN_SET_SAR_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_set_sar_config) structure that specifies the new SAR configuration for the modem. After complpeting the Set request, the miniport driver should return an [NDIS_STATUS_WWAN_SAR_CONFIG](ndis-status-wwan-sar-config.md) status notification containing an [**NDIS_WWAN_SAR_CONFIG_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_config_info) structure that describes the updated SAR configuration.

## Remarks

For Set requests, the MB device must act on the SAR back off command immediately by overwriting the current Transmit power limits and applying them to the transmitting antennas. If an antenna’s SAR configuration was not changed by the operating system, it should maintain its current setting. For example, if the operating system sets antenna 1 to be SAR back off index 1, then antenna 2’s configuration should be kept the same without any changes.

It is expected for devices that support this command to handle Query requests to provide device information to the OS and its clients. For a Set request, it is between the IHV and the OEM to define which value of each field is acceptable. The typical expectation is that the SAR back off index is configurable for all antennas as a minimum baseline. If a Set request is sent with fields that are not supported by the device, then NDIS_STATUS_INVALID_PARAMETER must be returned as the status code.

After each Query or Set response, the modem should return a MBIM_MS_SAR_CONFIG structure that contains information for all antennas on the device associated with Mobile Broadband.

## Requirements

|   |   |
| --- | --- |
| Version | Windows 10, version 1703 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[NDIS_STATUS_WWAN_SAR_CONFIG](ndis-status-wwan-sar-config.md)

[**NDIS_WWAN_SAR_CONFIG_INFO**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_config_info)

[**NDIS_WWAN_SET_SAR_CONFIG**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndiswwan/ns-ndiswwan-_ndis_wwan_set_sar_config)