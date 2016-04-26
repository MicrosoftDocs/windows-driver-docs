---
title: EFI\_BATTERY\_CHARGING\_PROTOCOL.GetBatteryInformation
author: windows-driver-content
description: EFI\_BATTERY\_CHARGING\_PROTOCOL.GetBatteryInformation
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 497cd001-5180-4dee-a070-ccf8c987bd71
---

# EFI\_BATTERY\_CHARGING\_PROTOCOL.GetBatteryInformation


Returns information about the current state of the main battery including the state of charge, the amount of current being delivered to or drawn out of the battery, the voltage across the battery’s terminals, the battery temperature, the voltage over the USB cable, and the current through the USB cable.

## Syntax


``` syntax
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


<a href="" id="this"></a>*This*  
\[in\] A pointer to the EFI\_BATTERY\_CHARGING\_PROTOCOL instance.

<a href="" id="stateofcharge"></a>*StateOfCharge*  
\[out\] Returns the current state of charge (SOC) of the main battery. SOC is represented in percentage, where 100% indicates a full charge.

<a href="" id="currentintobattery"></a>*CurrentIntoBattery*  
\[out\] Returns one of the values listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Positive number</p></td>
<td><p>The battery is in the process of being charged. The value indicates the current delivered to the battery in mA.</p></td>
</tr>
<tr class="even">
<td><p>Negative number</p></td>
<td><p>The battery is in the process of being discharged. The value indicates the current being drawn from the battery in mA.</p></td>
</tr>
<tr class="odd">
<td><p>0</p></td>
<td><p>The battery is not being charged or discharged.</p></td>
</tr>
<tr class="even">
<td><p>EFI_BATTERY_CHARGE_CURRENT_NOT_SUPPORTED (0x80000000)</p></td>
<td><p>The hardware is unable to provide this information.</p></td>
</tr>
</tbody>
</table>

 

<a href="" id="batteryterminalvoltage"></a>*BatteryTerminalVoltage*  
\[out\] The voltage across the battery terminals in mV.

<a href="" id="batterytemperature"></a>*BatteryTemperature*  
\[out\] The temperature of the battery in 10ths of a degree Kelvin.

<a href="" id="usbcablevoltage"></a>*USBCableVoltage*  
\[out\] The voltage over the USB cable in mV.

<a href="" id="usbcablecurrent"></a>*USBCableCurrent*  
\[out\] The current through the USB cable in mA.

## Return Value


Returns one of the following status codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>EFI_SUCCESS</p></td>
<td><p>The function returned successfully.</p></td>
</tr>
<tr class="even">
<td><p>EFI_INVALID_PARAMETER</p></td>
<td><p>A parameter was incorrect.</p></td>
</tr>
<tr class="odd">
<td><p>EFI_DEVICE_ERROR</p></td>
<td><p>The physical device reported an error.</p></td>
</tr>
<tr class="even">
<td><p>EFI_NOT_READY</p></td>
<td><p>The physical device is busy or not ready to process this request.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


This function is called periodically by the UEFI battery charging application to retrieve information about the battery. The application uses this information to help monitor the state of the battery and diagnose errors.

**Note**  
This function is available starting in revision 0x00010002 of the EFI\_BATTERY\_CHARGING\_PROTOCOL. If the UEFI battery charging application detects that only revision 0x00010001 of the protocol is available, it will call [EFI\_BATTERY\_CHARGING\_PROTOCOL.GetBatteryStatus](efi-battery-charging-protocolgetbatterystatus.md) instead.

 

## Requirements


**Header:** User generated

## Related topics
[EFI\_BATTERY\_CHARGING\_PROTOCOL](efi-battery-charging-protocol.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryInformation%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


