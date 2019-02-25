---
title: EFI_BATTERY_CHARGING_COMPLETION_TOKEN
description: EFI_BATTERY_CHARGING_COMPLETION_TOKEN
ms.assetid: 1151643e-8b22-4034-b043-ac4d44c01082
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_BATTERY\_CHARGING\_COMPLETION\_TOKEN


This structure defines the completion token used by [EFI\_BATTERY\_CHARGING\_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md).

## Syntax


```cpp
typedef struct _EFI_BATTERY_CHARGING_COMPLETION_TOKEN {
  EFI_EVENT Event;
  EFI_BATTERY_CHARGING_STATUS Status;
} EFI_BATTERY_CHARGING_COMPLETION_TOKEN;
```

## Members


<a href="" id="event"></a>**Event**  
The event to signal after charge request is finished. The type of event must be EVT\_NOTIFY\_SIGNAL.

<a href="" id="status"></a>**Status**  
The result of the completed operation.

## Remarks


EFI\_BATTERY\_CHARGING\_COMPLETION\_TOKEN is returned in the *CompletionToken* parameter of [EFI\_BATTERY\_CHARGING\_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md).

## Requirements


**Header:** User generated

## Related topics

[EFI\_BATTERY\_CHARGING\_PROTOCOL.ChargeBattery](efi-battery-charging-protocolchargebattery.md)  

[EFI\_BATTERY\_CHARGING\_STATUS](efi-battery-charging-status.md)  
