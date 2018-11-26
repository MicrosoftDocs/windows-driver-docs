---
title: UEFI display power state protocol
description: UEFI display power state protocol
ms.assetid: ab16c548-1402-4819-9fbb-a1d6f55d934a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UEFI display power state protocol


**Note**  Some information in this section may apply only to Windows 10 Mobile and certain processor architectures.

 

The display power state protocol is used by the Microsoft UEFI battery charging application to communicate with the UEFI battery charging driver in order to perform the following tasks:

-   Turn off the screen and backlight during low battery charging mode after displaying the alternating low battery UI for 10 seconds without any user input.

-   Turn the screen and backlight back on during low battery charging mode when the power button is pressed.

**Important**  If the device uses a custom UEFI battery charging application instead of the Microsoft-provided application, the UEFI battery charging driver must not implement this protocol. The Windows Boot Manager will load the Microsoft UEFI battery charging application if the driver implements this protocol.

 

For more information about the Microsoft-provided UEFI battery charging application, see [Battery charging in the boot environment](battery-charging-in-the-boot-environment.md).

## Protocol Interface


-   [EFI\_DISPLAY\_POWER\_PROTOCOL](efi-display-power-protocol.md)

-   [EFI\_DISPLAY\_POWER\_PROTOCOL.SetDisplayPowerState](efi-display-power-protocolsetdisplaypowerstate.md)

-   [EFI\_DISPLAY\_POWER\_PROTOCOL.GetDisplayPowerState](efi-display-power-protocolgetdisplaypowerstate.md)

-   [EFI\_DISPLAY\_POWER\_STATE](efi-display-power-state.md)

## Related topics
[Architecture of the UEFI battery charging application](architecture-of-the-uefi-battery-charging-application.md)  



