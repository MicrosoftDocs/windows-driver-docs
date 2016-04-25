---
title: EFI\_BATTERY\_CHARGING\_PROTOCOL.ChargeBattery
description: EFI\_BATTERY\_CHARGING\_PROTOCOL.ChargeBattery
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 362b812f-b64b-4b6c-84a6-61c09a60f8a3
---

# EFI\_BATTERY\_CHARGING\_PROTOCOL.ChargeBattery


Charges the main battery to the specified target level with a maximum charge current.

## Syntax


``` syntax
typedef EFI_STATUS (EFIAPI * EFI_BATTERY_CHARGING_CHARGE_BATTERY) (
    IN EFI_BATTERY_CHARGING_PROTOCOL *This,
    IN UINT32 MaximumCurrent, 
    IN UINT32 TargetStateOfCharge,
    IN EFI_BATTERY_CHARGING_COMPLETION_TOKEN *CompletionToken );
```

## Parameters


<a href="" id="this"></a>*This*  
\[in\] A pointer to the EFI\_BATTERY\_CHARGING\_PROTOCOL instance.

<a href="" id="maximumcurrent"></a>*MaximumCurrent*  
\[in\] Optional. The maximum current in mA that can be used to charge the main battery. A NULL value prompts the driver implementing this protocol to handle such details on its own.

<a href="" id="targetstateofcharge"></a>*TargetStateOfCharge*  
\[in\] Target state of charge (SOC) of the main battery after which the function would return if *CompletionToken* is NULL. SOC is represented in percentage, 100% indicating full charge.

<a href="" id="completiontoken"></a>*CompletionToken*  
\[in\] Pointer to a [EFI\_BATTERY\_CHARGING\_COMPLETION\_TOKEN](efi-battery-charging-completion-token.md) that is associated with the requested charge operation.

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


This non-blocking function charges the main battery to the specified target level with a maximum charge current.

To detect errors, the event type contained in *CompletionToken* must be EVT\_NOTIFY\_SIGNAL, created using **CreateEventEx** and must associate a **NotifyFunction** with the *CompletionToken* as **NotifyContext**. The status error code will be available via the **Status** member of the *CompletionToken*.

## Requirements


**Header:** User generated

## Related topics


[EFI\_BATTERY\_CHARGING\_PROTOCOL](efi-battery-charging-protocol.md)

[EFI\_BATTERY\_CHARGING\_COMPLETION\_TOKEN](efi-battery-charging-completion-token.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_BATTERY_CHARGING_PROTOCOL.ChargeBattery%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





