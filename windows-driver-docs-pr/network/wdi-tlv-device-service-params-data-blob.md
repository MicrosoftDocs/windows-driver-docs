---
title: WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB
description: WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB is a TLV that contains information about a device service received from the IHV driver.
ms.assetid: D07CDC24-849F-447A-8447-FD2D37178C42
ms.date: 06/15/2018
keywords:
 - WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB Network Drivers Starting with Windows Vista
---

# WDI_TLV_DEVICE_SERVICE_PARAMS_DATA_BLOB

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

|   |   |
| --- | --- |
| Minimum supported client | Windows 10, version 1809 |
| Minimum supported server | Windows Server 2016 |
| Header | Wditypes.hpp |
