---
title: EFI_BATTERY_CHARGING_PROTOCOL.ChargeBattery
description: Charges the main battery to the specified target level with a maximum charge current.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_BATTERY_CHARGING_PROTOCOL.ChargeBattery

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

*This*  
[in] A pointer to the EFI_BATTERY_CHARGING_PROTOCOL instance.

*MaximumCurrent*  
[in] Optional. The maximum current in mA that can be used to charge the main battery. A NULL value prompts the driver implementing this protocol to handle such details on its own.

*TargetStateOfCharge*  
[in] Target state of charge (SOC) of the main battery after which the function would return if *CompletionToken* is NULL. SOC is represented in percentage, 100% indicating full charge.

*CompletionToken*  
[in] Pointer to a [EFI_BATTERY_CHARGING_COMPLETION_TOKEN](efi-battery-charging-completion-token.md) that is associated with the requested charge operation.

## Return Value

Returns one of the following status codes.

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter was incorrect. |
| EFI_DEVICE_ERROR | The physical device reported an error. |
| EFI_NOT_READY | The physical device is busy or not ready to process this request. |

## Remarks

This non-blocking function charges the main battery to the specified target level with a maximum charge current.

To detect errors, the event type contained in *CompletionToken* must be EVT_NOTIFY_SIGNAL, created using **CreateEventEx** and must associate a **NotifyFunction** with the *CompletionToken* as **NotifyContext**. The status error code will be available via the **Status** member of the *CompletionToken*.

## Requirements

**Header:** User generated

## Related topics

[EFI_BATTERY_CHARGING_PROTOCOL](efi-battery-charging-protocol.md)  

[EFI_BATTERY_CHARGING_COMPLETION_TOKEN](efi-battery-charging-completion-token.md)  
