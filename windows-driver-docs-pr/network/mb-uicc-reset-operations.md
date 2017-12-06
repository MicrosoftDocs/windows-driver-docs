---
title: MB UICC reset operations
description: MB UICC reset operations
ms.assetid: E33073B5-53D5-4F6F-85EC-5B46FDE9EA4D
keywords:
- MB UICC reset, Mobile Broadband UICC reset, Mobile Broadband miniport driver UICC reset
ms.author: windowsdriverdev
ms.date: 08/17/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MB UICC reset operations

This section defines MBIM CID commands and data structures, as well as NDIS OID commands and data structures, for resetting a UICC in a mobile broadband (MB) device. These commands and data structures are available in Windows 10, version 1709 and later.

## MBIM_CID_MS_UICC_RESET

The host sends MBIM_CID_MS_UICC_RESET to the MBIM function to reset the UICC or to query the passthrough state of the function.

When the host requests that the function reset the UICC, it specifies a passthrough action.

- If the host specifies the *MBIMMsUICCPassThroughEnable* passthrough action, the function resets the UICC and, upon UICC power up, treats the UICC as if it were in a passthrough mode that enables communication between the host and UICC (even if the UICC has no Telecom UICC file system). The function does not send any APDUs to the card and does not interfere at any time with the communication between the host and the UICC.
- If the host specifies the *MBIMMsUICCPassThroughDisable* passthrough action, the function resets the UICC and, upon UICC power up, treats the UICC as a regular Telecom UICC and expects a Telecom UICC file system to be present on the UICC.

When the host queries the function to determine the passthrough status, if the function responds with the *MBIMMsUICCPassThroughEnabled* status, it means that passthrough mode is enabled. If the function responds with the *MBIMMsUICCPassThroughDisabled* status, it means that passthrough mode is disabled.

### Parameters

|   | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | MBIM_MS_SET_UICC_RESET | Empty | Not applicable |
| Response | MBIM_MS_UICC_RESET_INFO | MBIM_MS_UICC_RESET_INFO | Not applicable |

### Query

The InformationBuffer shall be null and *InformationBufferLength* shall be zero.

### Set

#### MBIM_SET_MS_UICC_RESET

The MBIM_SET_MS_UICC_RESET structure contains the passthrough action specified by the host.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | PassThroughAction | MBIM_MS_UICC_PASSTHROUGH_ACTION | For more info, see [MBIM_MS_UICC_PASSTHROUGH_ACTION](#mbimmsuiccpassthroughaction). |

#### MBIM_MS_UICC_PASSTHROUGH_ACTION

The MBIM_MS_UICC_PASSTHROUGH_ACTION enumeration defines the types of passthrough actions the host can specify to the MBIM function.

| Types | Value |
| --- | --- |
| MBIMMsUiccPassThroughDisable | 0 |
| MBIMMsUiccPassThroughEnable | 1 |

### Response

#### MBIM_MS_UICC_RESET_INFO

The MBIM_MS_UICC_RESET_INFO structure contains the passthrough status of the MBIM function.

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |
| 0 | 4 | PassThroughStatus | MBIM_MS_UICC_PASSTHROUGH_STATUS | For more info, see [MBIM_MS_UICC_PASSTHROUGH_STATUS](#mbimmsuiccpassthroughstatus). |

#### MBIM_MS_UICC_PASSTHROUGH_STATUS

The MBIM_MS_UICC_PASSTHROUGH_STATUS enumeration defines the types of passthrough status the MBIM function specifies to the host.

| Types | Value |
| --- | --- |
| MBIMMsUiccPassThroughDisabled | 0 |
| MBIMMsUiccPassThroughEnabled | 1 |

### Unsolicited events

Not applicable.

### Status codes

| Status code | Description |
| --- | --- |
| MBIM_STATUS_SUCCESS | Basic MBIM status as defined for all commands. |
| MBIM_STATUS_BUSY | The device is busy. |
| MBIM_STATUS_FAILURE | The operation failed. |
| MBIM_STATUS_NO_DEVICE_SUPPORT | The device does not support this operation. |

## OID_WWAN_UICC_RESET

The NDIS equivalent for MBIM_CID_MS_UICC_RESET is [OID_WWAN_UICC_RESET](oid-wwan-uicc-reset.md). 

## Related topics

[MB low level UICC access](mb-low-level-uicc-access.md)

[MB modem reset operations](mb-modem-reset-operations.md)

[OID_WWAN_UICC_RESET](oid-wwan-uicc-reset.md)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")