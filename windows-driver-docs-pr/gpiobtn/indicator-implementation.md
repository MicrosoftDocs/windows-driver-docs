---
title: Indicator implementation
author: windows-driver-content
description: This topic describes indicator implementation.
ms.assetid: 60BCE8C7-416E-4D5B-9B32-9B398CEA6A8A
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

![convertible implementation options](../images/implementationconvertibles.jpg)

**Figure 1 Convertible Implementation Options**

## <span id="Laptop_Slate_mode_-_implementation_for_laptops"></span><span id="laptop_slate_mode_-_implementation_for_laptops"></span><span id="LAPTOP_SLATE_MODE_-_IMPLEMENTATION_FOR_LAPTOPS"></span>Laptop/Slate mode - implementation for laptops


*Figure 2 Laptop Implementation Options* shows the options for implementing GPIO indicators on a laptop system.

![laptop implementation options](../images/implementationlaptops.jpg)

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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[gpiobtn\gpiobtn]:%20Indicator%20implementation%20%20RELEASE:%20%289/25/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


