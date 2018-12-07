---
title: EFI_BATTERY_CHARGING_PROTOCOL.ChargeBattery
description: EFI_BATTERY_CHARGING_PROTOCOL.ChargeBattery
ms.assetid: 362b812f-b64b-4b6c-84a6-61c09a60f8a3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_BATTERY\_CHARGING\_PROTOCOL.ChargeBattery


Charges the main battery to the specified target level with a maximum charge current.

## Syntax


```cpp
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
