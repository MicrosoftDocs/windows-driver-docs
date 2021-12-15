---
title: MB modem reset operations
description: MB modem reset operations
keywords:
- MB modem reset, Mobile Broadband modem reset, Mobile Broadband miniport driver modem reset
ms.date: 08/09/2018
---

# MB modem reset operations

This section defines MBIM CID commands and data structures, as well as NDIS OID commands and data structures, for resetting the modem in a mobile broadband (MB) device. These commands and data structures are available in Windows 10, version 1709 and later.

## MBIM_CID_MS_DEVICE_RESET

The host sends MBIM_CID_MS_DEVICE_RESET to the MBIM function to reset the modem device.

| Service name | UUID | UUID value |
| --- | --- | --- |
| Microsoft Basic IP Connectivity Extensions | UUID_BASIC_CONNECT_EXTENSIONS | 3d01dcc5-fef5-4d05-0d3a-bef7058e9aaf |

| CID | Command code | Set | Query | Notify |
| --- | --- | --- | --- | --- |
| MBIM_CID_MS_DEVICE_RESET | 10 | Y | N | N |

### Parameters

|  Type | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | Empty | Not applicable | Not applicable |
| Response | Empty | Not applicable | Not applicable |

### Query

Not applicable.

### Set

The InformationBuffer shall be NULL and *InformationBufferLength* shall be zero.

### Response

The InformationBuffer shall be NULL and *InformationBufferLength* shall be zero.

### Notification

Not applicable.

### Status codes

The following status codes are applicable. Status is returned as an asynchronous response to a set operation after reset is complete.

| Status code | Description |
| --- | --- |
| MBIM_STATUS_SUCCESS | The operation succeeded. |
| MBIM_STATUS_BUSY | The device is busy. |
| MBIM_STATUS_FAILURE | The operation failed. |
| MBIM_STATUS_NO_DEVICE_SUPPORT | The device does not support this operation. |

## OID_WWAN_DEVICE_RESET

The NDIS equivalent for MBIM_CID_MS_DEVICE_RESET is [OID_WWAN_DEVICE_RESET](oid-wwan-device-reset.md).
