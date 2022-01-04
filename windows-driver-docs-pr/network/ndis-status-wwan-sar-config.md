---
title: NDIS_STATUS_WWAN_SAR_CONFIG
description: Miniport drivers use the NDIS_STATUS_WWAN_SAR_CONFIG notification to inform the mobile broadband (MB) service about the completion of a previous OID_WWAN_SAR_CONFIG Query or Set request.
ms.date: 08/17/2018
keywords: 
 -NDIS_STATUS_WWAN_SAR_CONFIG Network Drivers Starting with Windows Vista
---

# NDIS_STATUS_WWAN_SAR_CONFIG

Miniport drivers use the **NDIS_STATUS_WWAN_SAR_CONFIG** notification to inform the mobile broadband (MB) service about the completion of a previous [OID_WWAN_SAR_CONFIG](oid-wwan-sar-config.md) Query or Set request.

Unsolicited events are not applicable.

This notification uses the [**NDIS_WWAN_SAR_CONFIG_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_config_info) structure.

## Requirements

**Version**: Windows 10, version 1703
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB SAR Platform Support](./mb-sar-platform-support.md)

[OID_WWAN_SAR_CONFIG](oid-wwan-sar-config.md)

[**NDIS_WWAN_SAR_CONFIG_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_sar_config_info)
