---
title: EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryInformation
description: Provides information about EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryInformation.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryInformation

Returns information about the current state of the main battery including the state of charge, the amount of current being delivered to or drawn out of the battery, the voltage across the battery's terminals, the battery temperature, the voltage over the USB cable, and the current through the USB cable.

## Syntax

```cpp
typedef EFI_STATUS (EFIAPI * EFI_BATTERY_CHARGING_GET_BATTERY_INFORMATION) (
    IN EFI_BATTERY_CHARGING_PROTOCOL *This,
    OUT UINT32 *StateOfCharge,
    OUT INT32 *CurrentIntoBattery,
    OUT UINT32 *BatteryTerminalVoltage, 
    OUT INT32 *BatteryTemperature,
    OUT UINT32 *USBCableVoltage,
    OUT UINT32 *USBCableCurrent );
```

## Parameters

*This*  
[in] A pointer to the EFI_BATTERY_CHARGING_PROTOCOL instance.

*StateOfCharge*  
[out] Returns the current state of charge (SOC) of the main battery. SOC is represented in percentage, where 100% indicates a full charge.

*CurrentIntoBattery*  
[out] Returns one of the values listed in the following table.

| Value | Description |
|--|--|
| Positive number | The battery is in the process of being charged. The value indicates the current delivered to the battery in mA. |
| Negative number | The battery is in the process of being discharged. The value indicates the current being drawn from the battery in mA. |
| 0 | The battery is not being charged or discharged. |
| EFI_BATTERY_CHARGE_CURRENT_NOT_SUPPORTED (0x80000000) | The hardware is unable to provide this information. |

*BatteryTerminalVoltage*  
[out] The voltage across the battery terminals in mV.

*BatteryTemperature*  
[out] The temperature of the battery in 10ths of a degree Kelvin.

*USBCableVoltage*  
[out] The voltage over the USB cable in mV.

*USBCableCurrent*  
[out] The current through the USB cable in mA.

## Return Value

Returns one of the following status codes.

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter was incorrect. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request. |

## Remarks

This function is called periodically by the UEFI battery charging application to retrieve information about the battery. The application uses this information to help monitor the state of the battery and diagnose errors.

> [!NOTE]
> This function is available starting in revision 0x00010002 of the EFI_BATTERY_CHARGING_PROTOCOL. If the UEFI battery charging application detects that only revision 0x00010001 of the protocol is available, it will call [EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryStatus](efi-battery-charging-protocolgetbatterystatus.md) instead.

## Requirements

**Header:** User generated

## Related topics

[EFI_BATTERY_CHARGING_PROTOCOL](efi-battery-charging-protocol.md)  
