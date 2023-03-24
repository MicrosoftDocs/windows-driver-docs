---
title: EFI_DISPLAY_POWER_PROTOCOL.GetDisplayPowerState
description: Provides information about EFI_DISPLAY_POWER_PROTOCOL.GetDisplayPowerState.
ms.date: 03/23/2023
ms.topic: reference
---

# EFI_DISPLAY_POWER_PROTOCOL.GetDisplayPowerState

Returns the current power state of the display and backlight.

## Syntax

```cpp
typedef EFI_STATUS (EFIAPI * EFI_DISPLAY_POWER_GETDISPLAYPOWERSTATE) (
    IN EFI_DISPLAY_POWER_PROTOCOL *This,
    OUT EFI_DISPLAY_POWER_STATE *PowerState 
    );
```

## Parameters

*This*  
[in] A pointer to the [EFI_DISPLAY_POWER_PROTOCOL](efi-display-power-protocol.md) instance.

*PowerState*  
[out] A pointer to an [EFI_DISPLAY_POWER_STATE](efi-display-power-state.md) value that receives the current power state.

## Return value

Returns one of the following status codes.

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully. |
| EFI_INVALID_PARAMETER | A parameter was invalid. |
| EFI_DEVICE_ERROR | The physical device reported an error. |

## Requirements

**Header:** User generated

## Related topics

[EFI_DISPLAY_POWER_PROTOCOL](efi-display-power-protocol.md)  
