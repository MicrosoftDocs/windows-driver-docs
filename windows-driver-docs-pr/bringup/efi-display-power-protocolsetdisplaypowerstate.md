---
title: EFI_DISPLAY_POWER_PROTOCOL.SetDisplayPowerState
description: Provides information about EFI_DISPLAY_POWER_PROTOCOL.SetDisplayPowerState.
ms.date: 08/20/2021
---

# EFI_DISPLAY_POWER_PROTOCOL.SetDisplayPowerState

Modifies the power state of the display and backlight.

## Syntax

```cpp
typedef EFI_STATUS (EFIAPI * EFI_DISPLAY_POWER_SETDISPLAYPOWERSTATE) (
    IN EFI_DISPLAY_POWER_PROTOCOL *This,
    IN EFI_DISPLAY_POWER_STATE PowerState 
    );
```

## Parameters

*This*  
[in] A pointer to the [EFI_DISPLAY_POWER_PROTOCOL](efi-display-power-protocol.md) instance.

*PowerState*  
[in] An [EFI_DISPLAY_POWER_STATE](efi-display-power-state.md) value that specifies the new power state to set.

## Return value

Returns one of the following status codes.

| Status code | Description |
|--|--|
| EFI_SUCCESS | The function returned successfully after changing the power state of both the display and backlight. |
| EFI_INVALID_PARAMETER | A parameter was incorrect. |
| EFI_DEVICE_ERROR | The physical device reported an error. |

## Remarks

This function should have no impact on any hardware component other than the display or backlight.

This function must allow redundant calls without returning an error code. Multiple calls to this function with the same *PowerState* argument must return success. The implementation of this function should avoid unnecessary work when handling redundant calls.

## Requirements

**Header:** User generated

## Related topics

[EFI_DISPLAY_POWER_PROTOCOL](efi-display-power-protocol.md)  
