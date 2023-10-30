---
title: EFI_BATTERY_CHARGING_STATUS
description: Provides information about the EFI_BATTERY_CHARGING_STATUS enumeration.
ms.date: 03/23/2023
ms.topic: reference
---

# EFI_BATTERY_CHARGING_STATUS

This enumeration specifies the status of a charging battery.

## Syntax

```cpp
typedef enum _EFI_BATTERY_CHARGING_STATUS {      
    EfiBatteryChargingStatusNone = 0,
    EfiBatteryChargingStatusSuccess,
    EfiBatteryChargingStatusOverheat,
    EfiBatteryChargingStatusVoltageOutOfRange,
    EfiBatteryChargingStatusCurrentOutOfRange,
    EfiBatteryChargingStatusTimeout,
    EfiBatteryChargingStatusAborted,
    EfiBatteryChargingStatusDeviceError,
    EfiBatteryChargingStatusExtremeCold,
    EfiBatteryChargingStatusBatteryChargingNotSupported,
    EfiBatteryChargingStatusBatteryNotDetected,
    EfiBatteryChargingSourceNotDetected,
    EfiBatteryChargingSourceVoltageInvalid,
    EfiBatteryChargingSourceCurrentInvalid,
    EfiBatteryChargingErrorRequestShutdown,
    EfiBatteryChargingErrorRequestReboot
} EFI_BATTERY_CHARGING_STATUS;
```

## Elements

**EfiBatteryChargingStatusNone**  
Charging status is unavailable.

**EfiBatteryChargingStatusSuccess**  
The operation completed successfully.

**EfiBatteryChargingStatusOverheat**  
The battery is getting too hot to charge.

**EfiBatteryChargingStatusVoltageOutOfRange**  
Charging logic detected the voltage to be out of the operational range.

**EfiBatteryChargingStatusCurrentOutOfRange**  
Charging logic detected the current to be out of the operational range.

**EfiBatteryChargingStatusTimeout**  
Charging logic detected that the battery is not getting charged within a reasonable time.

**EfiBatteryChargingStatusAborted**  
The operation was aborted.

**EfiBatteryChargingStatusDeviceError**  
The physical device reported an error.

**EfiBatteryChargingStatusExtremeCold**  
The battery is too cold to continue charging.

**EfiBatteryChargingStatusBatteryChargingNotSupported**  
The battery does not support the charging operation.

**EfiBatteryChargingStatusBatteryNotDetected**  
The battery is not detected.

**EfiBatteryChargingSourceNotDetected**  
The device is not attached to a charging source and therefore cannot continue with the charging operation.

**EfiBatteryChargingSourceVoltageInvalid**  
The charging source supplied an invalid voltage.

**EfiBatteryChargingSourceCurrentInvalid**  
The charging source supplied an invalid current.

**EfiBatteryChargingErrorRequestShutdown**  
The driver requested a system shutdown.

**EfiBatteryChargingErrorRequestReboot**  
The driver requested a system reboot.

## Remarks

EFI_BATTERY_CHARGING_STATUS is returned in the **Status** member of the [EFI_BATTERY_CHARGING_COMPLETION_TOKEN](efi-battery-charging-completion-token.md) structure.

## Requirements

**Header:** User generated

## Related topics

[EFI_BATTERY_CHARGING_COMPLETION_TOKEN](efi-battery-charging-completion-token.md)  
