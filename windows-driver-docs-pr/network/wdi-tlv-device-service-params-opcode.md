---
title: WDI_TLV_DEVICE_SERVICE_PARAMS_OPCODE
ms.topic: reference
description: WDI_TLV_DEVICE_SERVICE_PARAMS_OPCODE is a TLV that contains the opcode specific to the device service.
ms.date: 06/15/2018
keywords:
 - WDI_TLV_DEVICE_SERVICE_PARAMS_OPCODE Network Drivers Starting with Windows Vista
---

# WDI_TLV_DEVICE_SERVICE_PARAMS_OPCODE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

WDI_TLV_DEVICE_SERVICE_PARAMS_OPCODE is a TLV that contains the opcode specific to the device service. This TLV is used in the [NDIS_STATUS_WDI_INDICATION_DEVICE_SERVICE_EVENT](ndis-status-wdi-indication-device-service-event.md) status indication.

## TLV Type

0x13F

## Length

The size, in bytes, of a UINT8.

## Values

| Type | Description |
| --- | --- |
| TLV\<UINT8\> | The opcode specific to the device service. |

## Requirements

**Minimum supported client**: Windows 10, version 1809

**Minimum supported server**: Windows Server 2016

**Header**: Wditypes.hpp

