---
title: EFI_BATTERY_CHARGING_STATUS
description: EFI_BATTERY_CHARGING_STATUS
ms.assetid: dc267920-2c2f-447b-8772-35160886a24c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_BATTERY\_CHARGING\_STATUS


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


<a href="" id="efibatterychargingstatusnone"></a>EfiBatteryChargingStatusNone  
Charging status is unavailable.

<a href="" id="efibatterychargingstatussuccess"></a>EfiBatteryChargingStatusSuccess  
The operation completed successfully.

<a href="" id="efibatterychargingstatusoverheat"></a>EfiBatteryChargingStatusOverheat  
The battery is getting too hot to charge.

<a href="" id="efibatterychargingstatusvoltageoutofrange"></a>EfiBatteryChargingStatusVoltageOutOfRange  
Charging logic detected the voltage to be out of the operational range.

<a href="" id="efibatterychargingstatuscurrentoutofrange"></a>EfiBatteryChargingStatusCurrentOutOfRange  
Charging logic detected the current to be out of the operational range.

<a href="" id="efibatterychargingstatustimeout"></a>EfiBatteryChargingStatusTimeout  
Charging logic detected that the battery is not getting charged within a reasonable time.

<a href="" id="efibatterychargingstatusaborted"></a>EfiBatteryChargingStatusAborted  
The operation was aborted.

<a href="" id="efibatterychargingstatusdeviceerror"></a>EfiBatteryChargingStatusDeviceError  
The physical device reported an error.

<a href="" id="efibatterychargingstatusextremecold"></a>EfiBatteryChargingStatusExtremeCold  
The battery is too cold to continue charging.

<a href="" id="efibatterychargingstatusbatterychargingnotsupported"></a>EfiBatteryChargingStatusBatteryChargingNotSupported  
The battery does not support the charging operation.

<a href="" id="efibatterychargingstatusbatterynotdetected"></a>EfiBatteryChargingStatusBatteryNotDetected  
The battery is not detected.

<a href="" id="efibatterychargingsourcenotdetected"></a>EfiBatteryChargingSourceNotDetected  
The device is not attached to a charging source and therefore cannot continue with the charging operation.

<a href="" id="eefibatterychargingsourcevoltageinvalid"></a>EEfiBatteryChargingSourceVoltageInvalid  
The charging source supplied an invalid voltage.

<a href="" id="efibatterychargingsourcecurrentinvalid"></a>EfiBatteryChargingSourceCurrentInvalid  
The charging source supplied an invalid current.

<a href="" id="efibatterychargingerrorrequestshutdown"></a>EfiBatteryChargingErrorRequestShutdown  
The driver requested a system shutdown.

<a href="" id="efibatterychargingerrorrequestreboot"></a>EfiBatteryChargingErrorRequestReboot  
The driver requested a system reboot.

## Remarks


EFI\_BATTERY\_CHARGING\_STATUS is returned in the **Status** member of the [EFI\_BATTERY\_CHARGING\_COMPLETION\_TOKEN](efi-battery-charging-completion-token.md) structure.

## Requirements


**Header:** User generated

## Related topics
[EFI\_BATTERY\_CHARGING\_COMPLETION\_TOKEN](efi-battery-charging-completion-token.md)  



