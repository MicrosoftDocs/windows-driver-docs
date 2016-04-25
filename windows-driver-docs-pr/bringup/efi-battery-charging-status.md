---
title: EFI\_BATTERY\_CHARGING\_STATUS
description: EFI\_BATTERY\_CHARGING\_STATUS
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: dc267920-2c2f-447b-8772-35160886a24c
---

# EFI\_BATTERY\_CHARGING\_STATUS


This enumeration specifies the status of a charging battery.

## Syntax


``` syntax
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_BATTERY_CHARGING_STATUS%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


