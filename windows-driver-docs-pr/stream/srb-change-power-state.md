---
title: SRB_CHANGE_POWER_STATE
description: SRB_CHANGE_POWER_STATE
keywords: ["SRB_CHANGE_POWER_STATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_CHANGE_POWER_STATE
api_type:
- NA
ms.date: 08/25/2020
ms.localizationpriority: medium
---

# SRB_CHANGE_POWER_STATE

The class driver sends this request to signal to the minidriver that it should reset its power state. *pSrb*->**DeviceState** specifies the new power state.

See [**HW_STREAM_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/strmini/ns-strmini-_hw_stream_request_block).

## Return value

The minidriver should set one of the following as the status in the SRB:

| Value | Description |
|--|--|
| STATUS_SUCCESS | Indicates successful completion of the command. |
| STATUS_NOT_IMPLEMENTED | Indicates that the function is not supported by the minidriver. |
| STATUS_IO_DEVICE_ERROR | Indicates that a hardware failure occurred and low power cannot be invoked. |

## Remarks

If the minidriver needs to save or restore device-specific data it should do so when processing an SRB_CHANGE_POWER_STATE request.

For more information about power states, see [Power IRPs for Individual Devices](../kernel/power-irps-for-individual-devices.md).
