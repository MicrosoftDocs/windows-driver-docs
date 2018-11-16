---
title: Indicator implementation
description: This topic describes indicator implementation.
ms.assetid: 60BCE8C7-416E-4D5B-9B32-9B398CEA6A8A
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Indicator implementation


This topic describes indicator implementation.

Because sensor placement and related logic is system-specific, it is important to update the mode when the system is performing any related power transitions, such as the following:

-   Coming out of connected standby
-   Coming out of sleep or hibernate
-   After boot

This enforces the correct state and ensures a refresh to the user interface layer.

## <span id="Laptop_Slate_mode_-_implementation_for_convertibles"></span><span id="laptop_slate_mode_-_implementation_for_convertibles"></span><span id="LAPTOP_SLATE_MODE_-_IMPLEMENTATION_FOR_CONVERTIBLES"></span>Laptop/Slate mode - implementation for convertibles


*Figure 1 Convertible Implementation Options* shows the options for implementing GPIO indicators on a convertible system.

![convertible implementation options](images/implementationconvertibles.jpg)

**Figure 1 Convertible Implementation Options**

## <span id="Laptop_Slate_mode_-_implementation_for_laptops"></span><span id="laptop_slate_mode_-_implementation_for_laptops"></span><span id="LAPTOP_SLATE_MODE_-_IMPLEMENTATION_FOR_LAPTOPS"></span>Laptop/Slate mode - implementation for laptops


*Figure 2 Laptop Implementation Options* shows the options for implementing GPIO indicators on a laptop system.

![laptop implementation options](images/implementationlaptops.jpg)

**Figure 2 Laptop Implementation Options**

The ConvertibleSlateMode [Unattended Windows Setup](http://go.microsoft.com/fwlink/p/?linkid=276788) setting allows OEMs to statically flag clamshells to laptop mode as an image customization without implementing the injection mechanism.

This feature targets touchscreen systems that have a permanently attached keyboard (which the user can use at any time). The example that is provided here is the touchscreen clamshell that has no GPIO indicators/ injection available.

This setting must be applied as part of the specialized configuration passes and can be applied to all Windows client operating systems. See [Identifying Unattend Setting Passes](http://sharepoint/sites/cba/Wiki Pages/Identifying Unattend Setting Passes.aspx) for more information.

See for code samples.

**Note**  
-   Loading the GPIO button driver overrides the value that is introduced with the unattend setting.
-   The injection mechanism can be used with Windows 8.1 systems.
-   The ConvertibleSlateMode unattend setting does not affect Windows 8 to Windows 8.1 upgrade scenarios.
-   If the ConvertibleSlateMode unattend setting is not present and the GPIO indicators are not implemented, the system defaults to slate mode.
-   The ConvertibleSlateMode unattend setting is not available for Windows Server operating systems.

 

 

 




