---
title: MB modem reset operations
description: MB modem reset operations
ms.assetid: E33073B5-53D5-4F6F-85EC-5B46FDE9EA4D
keywords:
- MB modem reset, Mobile Broadband modem reset, Mobile Broadband miniport driver modem reset
ms.author: windowsdriverdev
ms.date: 08/17/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MB modem reset operations

This section defines MBIM CID commands and data structures, as well as NDIS OID commands and data structures, for resetting the modem in a mobile broadband (MB) device. These commands and data structures are available in Windows 10, version 1709 and later.

## MBIM_CID_MS_DEVICE_RESET

The host sends MBIM_CID_MS_DEVICE_RESET to the MBIM function to reset the modem device.

| Service name | UUID | UUID value |
| --- | --- | --- |
| Microsoft Basic IP Connectivity Extensions | UUID_BASIC_CONNECT_EXTENSIONS | 3d01dcc5-fef5-4d05-9d3a-bef7058e9aaf |

| CID | Command code | Set | Query | Notify |
| --- | --- | --- | --- | --- |
| MBIM_CID_MS_DEVICE_RESET | 10 | Y | N | N |

### Parameters

|   | Set | Query | Notification |
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

The NDIS equivalent for MBIM_CID_MS_DEVICE_RESET is [OID_WWAN_DEVICE_RESET](oid-wwan-device-reset.md)

## Related topics

[MB UICC reset and modem reset operations](mb-uicc-reset-and-modem-reset-operations.md)

[MB UICC reset operations](mb-uicc-reset-operations.md)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")