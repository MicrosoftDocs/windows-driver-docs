---
title: EFI_BATTERY_CHARGING_COMPLETION_TOKEN
description: This structure defines the completion token used by EFI_BATTERY_CHARGING_PROTOCOL.ChargeBattery.
ms.date: 02/24/2023
ms.topic: reference
---

# EFI_BATTERY_CHARGING_COMPLETION_TOKEN

This structure defines the completion token used by [EFI_BATTERY_CHARGING_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md).

## Syntax

```cpp
typedef struct _EFI_BATTERY_CHARGING_COMPLETION_TOKEN {
  EFI_EVENT Event;
  EFI_BATTERY_CHARGING_STATUS Status;
} EFI_BATTERY_CHARGING_COMPLETION_TOKEN;
```

## Members

**Event**  
The event to signal after charge request is finished. The type of event must be EVT_NOTIFY_SIGNAL.

**Status**  
The result of the completed operation.

## Remarks

EFI_BATTERY_CHARGING_COMPLETION_TOKEN is returned in the *CompletionToken* parameter of [EFI_BATTERY_CHARGING_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md).

## Requirements

**Header:** User generated

## Related topics

[EFI_BATTERY_CHARGING_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md)  

[EFI_BATTERY_CHARGING_STATUS](efi-battery-charging-status.md)  
