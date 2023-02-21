---
title: WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB
ms.topic: reference
description: WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB is a TLV that contains information about a device service received from the IHV driver.
ms.date: 06/15/2018
keywords:
 - WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB Network Drivers Starting with Windows Vista
---

# WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB is a TLV that contains information about a device service received from the IHV driver. This TLV is used in the [NDIS_STATUS_WDI_INDICATION_DEVICE_SERVICE_EVENT](ndis-status-wdi-indication-device-service-event.md) status indication.

## TLV Type

0x141

## Length

The size, in bytes, of a `(UINT8 * (the number of elements in the list))`.

## Values

| Type | Description |
| --- | --- |
| TLV\<List\<UINT8\>\> | [Optional] The information received from the IHV driver. |

## Requirements

**Minimum supported client**: Windows 10, version 1809

**Minimum supported server**: Windows Server 2016

**Header**: Wditypes.hpp

