---
title: Supporting Brightness Controls For External Display Connectors
description: Supporting Brightness Controls For External Display Connectors
keywords: ["brightness WDK display", "ACPI-based brightness hot-keys WDK display", "notifying brightness hot keys WDK display", "BIOS brightness control WDK display", "automatic brightness WDK display"]
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Supporting Brightness Controls For External Display Connectors

Some OEM systems have internal displays that are connected using external connectors such as HDMI. For those configurations, Windows has the ability to designate exactly one display panel to support the system software brightness control.
This feature does not support the ability to control the individual panel brightness on multiple display panels.


### General Requirements

A new DWORD registry value will be added: “BrightnessControl”.
Registry Path: HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E96E-E325-11CE-BFC1-08002BE10318}\XXXX
Where XXXX is for the targeted individual display.  


*	The first bit in this registry value defines the non-internal monitor brightness control support.
*	The second bit defines an ACPI override that forces ACPI brightness to be used.
*	The remaining 30bits are reserved and must be zero.  

OEMs that would like to enable brightness control on a non-internal panel must ship their own monitor.inf (see sample inf below) and set this registry value appropriately. 

OEMs should only define the “BrightnessControl” registry value when it is required. 

The brightness support control override (the first bit) should only be used on a system which does not have an internal display on an internal connector type on any display adapter. If a system does have an internal display on an internal connector type, then the first enumerated display will receive the brightness control.


### ACPI Brightness Override

The ACPI brightness override is not the preferred mechanism to use for brightness control, but is included for completeness, in situations where there is no other option for brightness control.

The ACPI override (the second bit) is valid on both internal and external displays but must only be applied to exactly one display on the system.

The ACPI override is intended to be used in conjunction with the brightness target override, and only when the display driver does not already provide brightness support.  This allows OEMs to implement their own display backlight control via ACPI. 

A secondary use for the ACPI override is during OS/driver development when brightness support fails on mobile systems, which can happen for several common reasons. In this case, the ACPI override is intended only as an interim solution; the driver brightness control should be used for the finished product.

In the case where this registry value is set for external connectors, the OS will limit the system to one exposed brightness control.


### SAMPLE MONITOR.INF FILE FRAGMENT
The following is an incomplete sample INF that outlines the above:


[Manufacturer]
%MONOEM%=MONOEM,NTx86,NTAMD64 
 
[MONOEM]  
%AIOHDMI_1%  = AIO_HDMI_1, Monitor\OEM1001
%AIOHDMI_2%  = AIO_HDMI_2, Monitor\OEM1002
%Laptop%  = Laptop_1, Monitor\OEM2001
 
[MONOEM.NTx86]
%AIOHDMI_1%  = AIO_HDMI_1, Monitor\OEM1001
%AIOHDMI_2%  = AIO_HDMI_2, Monitor\OEM1002
%Laptop%  = Laptop_1, Monitor\OEM2001
 
[MONOEM.NTAMD64]  
%AIOHDMI_1%  = AIO_HDMI_1, Monitor\OEM1001
%AIOHDMI_2%  = AIO_HDMI_2, Monitor\OEM1002
%Laptop%  = Laptop_1, Monitor\OEM2001
 
[ControlFlags]
ExcludeFromSelect = *
 
[AIO_HDMI_1]
AddReg= AIO_HDMI_1_Driver_Brightness
 
[AIO_HDMI_2]
AddReg= AIO_HDMI_2_ACPI_Brightness
 
[Laptop_1]
AddReg=Laptop_ACPI_Driver_Brightness
                                                                                     
 
; Override brightness to control the HDMI built into the all-in-one system under graphics driver control
[AIO_HDMI_1_Driver_Brightness]
HKR,,BrightnessControl,%REG_DWORD%,%OVERRIDE_BRIGHTNESS_TARGET%
 
; Override brightness to control the HDMI built into the all-in-one system under ACPI firmware control
[AIO_HDMI_2_ACPI_Brightness]
HKR,,BrightnessControl,%REG_DWORD%,%OVERRIDE_BRIGHTNESS_TARGET_AND_CONTROL_TO_ACPI%
 
; Override brightness to control the internal panel under ACPI firmware control instead of the driver
[Laptop_ACPI_Driver_Brightness]
HKR,,BrightnessControl,%REG_DWORD%,%OVERRIDE_BRIGHTNESS_CONTROL_TO_ACPI%
 
[Strings]
; Non-localizable
REG_DWORD = 0x00010001
OVERRIDE_BRIGHTNESS_TARGET = 1
OVERRIDE_BRIGHTNESS_CONTROL_TO_ACPI = 2
OVERRIDE_BRIGHTNESS_TARGET_AND_CONTROL_TO_ACPI = 3
 
; Localizable
MONOEM = “Manufacturer name” 
AIOHDMI_1  = “AIO monitor name one”
AIOHDMI_2  = “AIO monitor name two”
Laptop  = “Laptop monitor name”



**NOTE** OEMs need to provide a monitor.inf that has the proper hardware ID in order to ensure that the generic Microsoft monitor.inf is not used. 
