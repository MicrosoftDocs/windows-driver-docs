---
title: EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryStatus
description: Provides information about EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryStatus.
ms.date: 03/23/2023
ms.topic: reference
---

# EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryStatus

Returns information about the current state of the main battery.

## Syntax

```cpp
typedef EFI_STATUS (EFIAPI * EFI_BATTERY_CHARGING_GET_BATTERY_STATUS) (
    IN EFI_BATTERY_CHARGING_PROTOCOL *This,
    OUT UINT32 *StateOfCharge,
    OUT UINT32 *RatedCapacity,
    OUT INT32 *ChargeCurrent );
```

## Parameters

*This*  
[in] A pointer to the EFI_BATTERY_CHARGING_PROTOCOL instance.

*StateOfCharge*  
[out] Returns the current state of charge (SOC) of the main battery. SOC is represented in percentage, 100% indicating full charge.

*RatedCapacity*  
[out] Returns the rated capacity of the main battery, in mAh.

*ChargeCurrent*  
[out] If the battery is in the process of being charged, returns a positive number indicating the current delivered to the battery in mA. If the battery is in the process of being discharged, returns a negative number indicating the current being drawn from the battery in mA. If the battery is neither being charged, nor being discharged, it returns 0. If the hardware is unable to provide this information, it returns EFI_BATTERY_CHARGE_CURRENT_NOT_SUPPORTED (0x80000000).

## Return Value

Returns one of the following status codes.

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter was incorrect. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request. |

## Remarks

This function returns rated capacity and state of charge (SOC) for the main battery. This function is called periodically to aid additional processing by the driver implementing this protocol.

## Requirements

**Header:** User generated

## Related topics

[EFI_BATTERY_CHARGING_PROTOCOL](efi-battery-charging-protocol.md)  
