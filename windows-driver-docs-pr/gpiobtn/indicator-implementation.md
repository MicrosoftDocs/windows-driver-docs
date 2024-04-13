---
title: Indicator Implementation
description: This topic describes indicator implementation.
ms.date: 10/17/2018
---

# Indicator implementation

This topic describes indicator implementation.

Because sensor placement and related logic is system-specific, it is important to update the mode when the system is performing any related power transitions, such as the following:

- Coming out of connected standby
- Coming out of sleep or hibernate
- After boot

This enforces the correct state and ensures a refresh to the user interface layer.

## Laptop/Slate mode - implementation for convertibles

*Figure 1 Convertible Implementation Options* shows the options for implementing GPIO indicators on a convertible system.

![convertible implementation options.](images/implementationconvertibles.jpg)

Figure 1 Convertible Implementation Options

## Laptop/Slate mode - implementation for laptops

*Figure 2 Laptop Implementation Options* shows the options for implementing GPIO indicators on a laptop system.

![laptop implementation options.](images/implementationlaptops.jpg)

Figure 2 Laptop Implementation Options

The ConvertibleSlateMode [Unattended Windows Setup](/previous-versions/windows/it-pro/windows-8.1-and-8/ff699026(v=win.10)) setting allows OEMs to statically flag clamshells to laptop mode as an image customization without implementing the injection mechanism.

This feature targets touchscreen systems that have a permanently attached keyboard (which the user can use at any time). The example that is provided here is the touchscreen clamshell that has no GPIO indicators/ injection available.

This setting must be applied as part of the specialized configuration passes and can be applied to all Windows client operating systems. See [Identifying Unattend Setting Passes](https://sharepoint/sites/cba/Wiki Pages/Identifying Unattend Setting Passes.aspx) for more information.

See for code samples.

> [!NOTE]
>
> - Loading the GPIO button driver overrides the value that is introduced with the unattend setting.
> - The injection mechanism can be used with Windows 8.1 systems.
> - The ConvertibleSlateMode unattend setting does not affect Windows 8 to Windows 8.1 upgrade scenarios.
> - If the ConvertibleSlateMode unattend setting is not present and the GPIO indicators are not implemented, the system defaults to slate mode.
> - The ConvertibleSlateMode unattend setting is not available for Windows Server operating systems.
