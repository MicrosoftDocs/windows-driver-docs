---
title: Keyboard and mouse HID client drivers
author: windows-driver-content
description: This topic discusses keyboard and mouse HID client drivers. Keyboards and mice represent the first set of HID clients that were standardized in the HID Usage tables and implemented in Windows operating systems.
ms.assetid: DAD50261-7619-4554-B864-9158A0FA1ACE
keywords:
- HID keyboard driver
- keyboard drivers, HID
- HID keyboard driver for Windows
- HID mouse driver
- mouse drivers, HID
- HID mouse driver for Windows
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Keyboard and mouse HID client drivers


This topic discusses keyboard and mouse HID client drivers. Keyboards and mice represent the first set of HID clients that were standardized in the HID Usage tables and implemented in Windows operating systems.

Keyboard and mouse HID client drivers are implemented in the form of HID Mapper Drivers. A HID mapper driver is a kernel-mode WDM filter driver that provides a bidirectional interface for I/O requests between a non-HID Class driver and the HID class driver. The mapper driver maps the I/O requests and data protocols of one to the other.

Windows provides system-supplied HID mapper drivers for HID keyboard, and HID mice devices.

## Architecture and overview


The following figure illustrates the system-supplied driver stacks for USB keyboard and mouse/touchpad devices.

![keyboard and mouse driver stack diagram, showing the hid class mapper drivers for keyboards and mice, along with the keyboard and mouse class drivers.](images/keyboard-driver-stack.png)

The figure above includes the following components:

-   KBDHID.sys – HID client mapper driver for keyboards. Converts HID usages into scancodes to interface with the existing keyboard class driver.
-   MOUHID.sys – HID client mapper driver for mice/touchpads. Converts HID usages into mouse commands (X/Y, buttons, wheel) to interface with the existing keyboard class driver.
-   KBDCLASS.sys – The keyboard class driver maintains functionality for all keyboards and keypads on the system in a secure manner.
-   MOUCLASS.sys – The mouse class driver maintains functionality for all mice / touchpads on the system. The driver does support both absolute and relative pointing devices. This is not the driver for touchscreens as that is managed by a different driver in Windows.

The system builds the driver stack as follows:

-   The transport stack creates a physical device object (PDO) for each HID device attached and loads the appropriate HID transport driver which in turn loads the HID Class Driver.
-   The HID class driver creates a PDO for each keyboard or mouse TLC. Complex HID devices (more than 1 TLC) are exposed as multiple PDOs created by HID class driver. For example, a keyboard with an integrated mouse might have one collection for the standard keyboard controls and a different collection for the mouse.
-   The keyboard or mouse hid client mapper drivers are loaded on the appropriate FDO.
-   The HID mapper drivers create FDOs for keyboard and mouse, and load the class drivers.

Important notes:

-   Vendor drivers are not required for keyboards and mice that are compliant with the supported HID Usages and top level collections.
-   Vendors may optionally provide filter drivers in the HID stack to alter/enhance the functionality of these specific TLC.
-   Vendors should create separate TLCs, that are vendor specific, to exchange vendor proprietary data between their hid client and the device. Avoid using filter drivers unless critical.
-   The system opens all keyboard and mouse collections for its exclusive use.
-   The system prevents disable/enabling a keyboard.
-   The system provides support for horizontal/vertical wheels with smooth scrolling capabilities.

## Driver Guidance


Microsoft provides the following guidance for IHVs writing drivers:

1.  Driver developers are allowed to add additional drivers in the form of a filter driver or a new HID Client driver. The criteria are described below:
    1.  Filters Drivers: Driver developers should ensure that their value-add driver is a filter driver and does not replace (or be used in place of) existing Windows HID drivers in the input stack.
        -   Filter drivers are allowed in the following scenarios:
            -   As an upper filter to kbdhid/mouhid
            -   As an upper filter to kbdclass/mouclass
        -   Filter drivers are NOT recommended in the following scenarios:
            -   As a lower filter to the HID transport (e.g. HIDI2C)
            -   As a filter between HIDCLASS and HID Transport minidriver

    2.  Function Drivers: Alternatively vendors can create a function driver (instead of a filter driver) but only for vendor specific HID PDOs (with a user mode service if necessary).

        Function drivers are allowed in the following scenarios:

        -   Only load on the specific vendor’s hardware

    3.  Transport Drivers: Windows team does not recommend creating additional HID Transport minidriver as they are complex drivers to write/maintain. If a partner is creating a new HID Transport minidriver, especially on SoC systems, we recommend a detailed architectural review to understand the reasoning and ensure that the driver is developed correctly.

2.  Driver developers should leverage driver Frameworks (KMDF or UMDF) and not rely on WDM for their filter drivers.
3.  Driver developers should reduce the number of kernel-user transitions between their service and the driver stack.
4.  Driver developers should ensure ability to wake the system via both keyboard and touchpad functionality (adjustable by the end user (device manager) or the PC manufacturer). In addition on SoC systems, these devices must be able to wake themselves from a lower powered state while the system is in a working S0 state.
5.  Driver developers should ensure that their hardware is power managed efficiently.
    -   Device can go into its lowest power state when the device is idle.
    -   Device is in the lowest power state when the system is in a low power state (for example, standby (S3) or connected standby).

## Keyboard layout


A *keyboard layout* fully describes a keyboard's input characteristics for Microsoft Windows 2000 and later versions. For example, a keyboard layout specifies the language, keyboard type and version, modifiers, scan codes, and so on.

See the following for information about keyboard layouts:

-   Keyboard header file, kdb.h, in the Windows Driver Development Kit (DDK), which documents general information about keyboard layouts.

-   Sample keyboard [layouts](http://go.microsoft.com/fwlink/p/?linkid=256128) in the MSDN Code Gallery.

To visualize the layout of a specific keyboard, please review to the “Windows Keyboard Layout” article in MSDN.

For additional details around the keyboard layout, visit Control Panel\\Clock, Language, and Region\\Language.

## Supported buttons and wheels on mice


The following table identifies the features supported across different client versions of the Windows operating system.

| Feature                                               | Windows XP             | Windows Vista          | Windows 7              | Windows 8 and later    |
|-------------------------------------------------------|------------------------|------------------------|------------------------|------------------------|
| Buttons 1-5                                           | Supported (P/2 & HID)  | Supported (PS/2 & HID) | Supported (PS/2 & HID) | Supported (PS/2 & HID) |
| Vertical Scroll Wheel                                 | Supported (PS/2 & HID) | Supported (PS/2 & HID) | Supported (PS/2 & HID) | Supported (PS/2 & HID) |
| Horizontal Scroll Wheel                               | Not Supported          | Supported(HID only)    | Supported(HID only)    | Supported(HID only)    |
| Smooth Scroll Wheel Support (Horizontal and Vertical) | Not Supported          | Partly Supported       | Supported (HID only)   | Supported (HID only)   |

 

### Activating buttons 4-5 and wheel on PS/2 mice

The method used by Windows to activate the new 4&5-button + wheel mode is an extension of the method used to activate the third button and the wheel in IntelliMouse-compatible mice:

-   First, the mouse is set to the 3-button wheel mode, which is accomplished by setting the report rate consecutively to 200 reports/second, then to 100 reports/second, then to 80 reports/second, and then reading the ID from the mouse. The mouse should report an ID of 3 when this sequence is completed.
-   Next, the mouse is set to the 5-button wheel mode, which is accomplished by setting the report rate consecutively to 200 reports/second, then to 200 reports/second again, then to 80 reports/second, and then reading the ID from the mouse. Once this sequence is completed, a 5-button wheel mouse should report an ID of 4 (whereas an IntelliMouse-compatible 3-button wheel mouse would still report an ID of 3).

Note that this is applicable to PS/2 mice only and is not applicable to HID mice (HID mice must report accurate usages in their report descriptor).

*Standard PS/2-compatible mouse data packet format (2 Buttons)*

| Byte | D7    | D6    | D5    | D4    | D3  | D2  | D1  | D0  | Comment                          |
|------|-------|-------|-------|-------|-----|-----|-----|-----|----------------------------------|
| 1    | Yover | Xover | Ysign | Xsign | Tag | M   | R   | L   | X/Y overvlows and signs, buttons |
| 2    | X7    | X6    | X5    | X4    | X3  | X2  | X1  | X0  | X data byte                      |
| 3    | Y7    | Y6    | Y5    | Y4    | Y3  | Y2  | Y1  | Y0  | Y data bytes                     |

 

**Note**  Windows mouse drivers do not check the overflow bits. In case of overflow, the mouse should simply send the maximal signed displacement value.

 

*Standard PS/2-compatible mouse data packet format (3 Buttons + VerticalWheel)*

| Byte | D7  | D6  | D5    | D4    | D3  | D2  | D1  | D0  | Comment                     |
|------|-----|-----|-------|-------|-----|-----|-----|-----|-----------------------------|
| 1    | 0   | 0   | Ysign | Xsign | 1   | M   | R   | L   | X/Y signs and R/L/M buttons |
| 2    | X7  | X6  | X5    | X4    | X3  | X2  | X1  | X0  | X data byte                 |
| 3    | Y7  | Y6  | Y5    | Y4    | Y3  | Y2  | Y1  | Y0  | Y data bytes                |
| 4    | Z7  | Z6  | Z5    | Z4    | Z3  | Z2  | Z1  | Z0  | Z/wheel data byte           |

 

*Standard PS/2-compatible mouse data packet format (5 Buttons + VerticalWheel)*

| Byte | D7  | D6  | D5    | D4    | D3  | D2  | D1  | D0  | Comment                               |
|------|-----|-----|-------|-------|-----|-----|-----|-----|---------------------------------------|
| 1    | 0   | 0   | Ysign | Xsign | 1   | M   | R   | L   | X/Y signs and R/L/M buttons           |
| 2    | X7  | X6  | X5    | X4    | X3  | X2  | X1  | X0  | X data byte                           |
| 3    | Y7  | Y6  | Y5    | Y4    | Y3  | Y2  | Y1  | Y0  | Y data bytes                          |
| 4    | 0   | 0   | B5    | B4    | Z3  | Z2  | Z1  | Z0  | Z/wheel data data and buttons 4 and 5 |

 

Important note:

-   Notice that the Z/wheel data for a 5-button wheel mouse has been reduced to four bits instead of the 8 bits used in the IntelliMouse-compatible 3-button wheel mode. This reduction is made possible by the fact that the wheel typically cannot generate values beyond the range +7/-8 during any given interrupt period. Windows mouse drivers will sign extend the four Z/wheel data bits when the mouse is in the 5-button wheel mode, and the full Z/wheel data byte when the mouse operates in the 3-button wheel mode.
-   Buttons 4 & 5 on are mapped to WM\_APPCOMMAND messages and correspond to App\_Back and App\_Forward.

### Devices not requiring vendor drivers

Vendor drivers are not required for the following devices:

-   Devices that comply with the HID Standard.
-   Keyboard, mouse, or game port devices operated by the system-supplied non-HIDClass drivers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Keyboard%20and%20mouse%20HID%20client%20drivers%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


