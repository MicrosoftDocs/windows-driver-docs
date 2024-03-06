---
title: UEFI Display Power State Protocol
description: Provides information about the UEFI display power state protocol.
ms.date: 03/23/2023
---

# UEFI display power state protocol

> [!IMPORTANT]
> Some information in this section may apply only to Windows 10 Mobile and certain processor architectures.

The display power state protocol is used by the Microsoft UEFI battery charging application to communicate with the UEFI battery charging driver in order to perform the following tasks:

- Turn off the screen and backlight during low battery charging mode after displaying the alternating low battery UI for 10 seconds without any user input.

- Turn the screen and backlight back on during low battery charging mode when the power button is pressed.

> [!IMPORTANT]
> If the device uses a custom UEFI battery charging application instead of the Microsoft-provided application, the UEFI battery charging driver must not implement this protocol. The Windows Boot Manager will load the Microsoft UEFI battery charging application if the driver implements this protocol.

For more information about the Microsoft-provided UEFI battery charging application, see [Battery charging in the boot environment](battery-charging-in-the-boot-environment.md).

## Protocol Interface

- [EFI_DISPLAY_POWER_PROTOCOL](efi-display-power-protocol.md)

- [EFI_DISPLAY_POWER_PROTOCOL.SetDisplayPowerState](efi-display-power-protocolsetdisplaypowerstate.md)

- [EFI_DISPLAY_POWER_PROTOCOL.GetDisplayPowerState](efi-display-power-protocolgetdisplaypowerstate.md)

- [EFI_DISPLAY_POWER_STATE](efi-display-power-state.md)

## Related topics

[Architecture of the UEFI battery charging application](architecture-of-the-uefi-battery-charging-application.md)  
