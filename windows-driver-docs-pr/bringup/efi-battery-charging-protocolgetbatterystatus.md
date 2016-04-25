---
title: EFI\_BATTERY\_CHARGING\_PROTOCOL.GetBatteryStatus
description: EFI\_BATTERY\_CHARGING\_PROTOCOL.GetBatteryStatus
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: dc2b647b-b3b6-4d85-9faf-9e401fa67571
---

# EFI\_BATTERY\_CHARGING\_PROTOCOL.GetBatteryStatus


Returns information about the current state of the main battery.

## Syntax


``` syntax
typedef EFI_STATUS (EFIAPI * EFI_BATTERY_CHARGING_GET_BATTERY_STATUS) (
    IN EFI_BATTERY_CHARGING_PROTOCOL *This,
    OUT UINT32 *StateOfCharge,
    OUT UINT32 *RatedCapacity,
    OUT INT32 *ChargeCurrent );
```

## Parameters


<a href="" id="this"></a>*This*  
\[in\] A pointer to the EFI\_BATTERY\_CHARGING\_PROTOCOL instance.

<a href="" id="stateofcharge"></a>*StateOfCharge*  
\[out\] Returns the current state of charge (SOC) of the main battery. SOC is represented in percentage, 100% indicating full charge.

<a href="" id="ratedcapacity"></a>*RatedCapacity*  
\[out\] Returns the rated capacity of the main battery, in mAh.

<a href="" id="chargecurrent"></a>*ChargeCurrent*  
\[out\] If the battery is in the process of being charged, returns a positive number indicating the current delivered to the battery in mA. If the battery is in the process of being discharged, returns a negative number indicating the current being drawn from the battery in mA. If the battery is neither being charged, nor being discharged, it returns 0. If the hardware is unable to provide this information, it returns EFI\_BATTERY\_CHARGE\_CURRENT\_NOT\_SUPPORTED (0x80000000).

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


This function returns rated capacity and state of charge (SOC) for the main battery. This function is called periodically to aid additional processing by the driver implementing this protocol.

## Requirements


**Header:** User generated

## Related topics


[EFI\_BATTERY\_CHARGING\_PROTOCOL](efi-battery-charging-protocol.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_BATTERY_CHARGING_PROTOCOL.GetBatteryStatus%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





