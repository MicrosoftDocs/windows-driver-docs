---
title: OID_WWAN_MODEM_LOGGING_CONFIG
ms.topic: reference
description: OID_WWAN_MODEM_LOGGING_CONFIG is used to configure logs that are collected by the modem and how often they will be sent from the modem to the host over Data Service Stream (DSS).
ms.date: 04/11/2019
keywords: 
- OID_WWAN_MODEM_LOGGING_CONFIG Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID_WWAN_MODEM_LOGGING_CONFIG

OID_WWAN_MODEM_LOGGING_CONFIG is used to configure logs that are collected by the modem and how often they will be sent from the modem to the host over Data Service Stream (DSS).

Miniport drivers must process Query requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_MODEM_LOGGING_CONFIG](ndis-status-wwan-modem-logging-config.md) status notification containing an [**NDIS_WWAN_MODEM_LOGGING_CONFIG**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_modem_logging_config) structure that describes the current modem logging configuration.

Set payloads contain an [**NDIS_WWAN_SET_MODEM_LOGGING_CONFIG**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_modem_logging_config) structure specifying how to configure modem logging. Miniport drivers must process Set requests asynchronously, initially returning NDIS_STATUS_INDICATION_REQUIRED to the original request before later sending an [NDIS_STATUS_WWAN_MODEM_LOGGING_CONFIG](ndis-status-wwan-modem-logging-config.md) status notification containing an [**NDIS_WWAN_MODEM_LOGGING_CONFIG**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_modem_logging_config) structure that describes the modem logging configuration after the Set request.

## Remarks

Logging must be configured before a logging session is started. This is an optional OID for miniport drivers to support. However, if the miniport driver supports modem logging via the DSS channel, it must specify that it supports this OID. 

For more information about usage of this OID, see [MB modem logging with DSS](mb-modem-logging-with-dss.md).

## Requirements

**Version**: Windows 10, version 1903
**Header**: Ntddndis.h (include Ndis.h)

## See also

[MB modem logging with DSS](mb-modem-logging-with-dss.md)

[NDIS_STATUS_WWAN_MODEM_LOGGING_CONFIG](ndis-status-wwan-modem-logging-config.md)

[**NDIS_WWAN_SET_MODEM_LOGGING_CONFIG**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_set_modem_logging_config)

[**NDIS_WWAN_MODEM_LOGGING_CONFIG**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_modem_logging_config)
