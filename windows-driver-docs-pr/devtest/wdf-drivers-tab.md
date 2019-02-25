---
title: WDF Drivers Tab
description: This topic provides detailed information about WDF Verifier's WDF Drivers page.
ms.assetid: e1e1d92e-1173-48ef-b985-688ebfb08bdc
keywords:
- WDF Verifier control application WDK
- WDF Verifier WDK
- tools WDK , verifying
- testing drivers WDK WDF
- debugging drivers WDK WDF
- verifying drivers WDK WDF
- KMDF verifier tools WDK WDF
- UMDF verifier tools WDK WDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDF Drivers Tab


This topic provides detailed information about WDF Verifier's **WDF Drivers** page. This page lists all WDF drivers on the computer, and you can change their verification settings and the settings of devices that use them. Start here if you're interested in a specific driver.

When you start up the application, you'll see a list of the WDF drivers and runtime versions currently on the system. Each line includes the name of the driver binary, its service display name, framework version, and, for KMDF drivers, start type.

When you highlight a driver, you'll see any devices currently using that driver, as well as related UMDF host processes. The host process control is only visible when a running UMDF driver is selected.

![screen grab of wdf drivers tab](images/wdfverifier-tab1.png)

## <span id="Color_Scheme"></span><span id="color_scheme"></span><span id="COLOR_SCHEME"></span>Color Scheme


For each driver, a color-coded icon indicates if it uses KMDF, UMDF 1 or UMDF 2.

The color code indicates the driver's status and what you need to do so that changes to the driver's verification settings take effect.

-   Blue indicates that the driver is in use and is associated with one or more PnP devices. For changes to take effect, you need to disable and reenable these devices. You can choose if WDF Verifier does this for you on the **My Preferences** tab. For these drivers, you get a list of associated devices.
-   Red indicates that a driver is in use, but it is not associated with a PnP device. For changes to take effect:
    -   For KMDF, you must reboot.
    -   For UMDF, you must stop and restart all UMDF host processes.
-   Green indicates that the driver is not currently in use. If you change settings, the changes take effect the next time the driver is loaded.

## <span id="Preset_Options"></span><span id="preset_options"></span><span id="PRESET_OPTIONS"></span>Preset Options


For drivers that have driver-specific settings (KMDF and UMDF 2), right-click the driver name for the following quick option menu:

-   Set to default settings.
-   Enable WDF breakpoints and VERIFY macros in the driver code.
-   Enable all recommended test settings (verifier on, verbose and larger IFR buffer, downlevel verification).

If you change the driver’s settings but haven't committed the changes, (\*) appears after the driver name, and the menu includes an additional option to undo changes.

## <span id="Changing_Individual_Verification_Settings_for_a_Driver"></span><span id="changing_individual_verification_settings_for_a_driver"></span><span id="CHANGING_INDIVIDUAL_VERIFICATION_SETTINGS_FOR_A_DRIVER"></span>Changing Individual Verification Settings for a Driver


Click the + to the left of the color icon to see a driver's current verification settings. You can right-click on individual options to change them.

Right-clicking a Boolean setting toggles it. Some settings present a list of valid options, while others present an edit control where you can type a value. The app beeps if you enter an invalid value. Press **Enter** to use your new value or click outside the control to cancel the change.

You must enter a hexadecimal value in **AllocateFailCount**, and a decimal value for **HostTimeoutSeconds**.

If you enable a feature that requires KMDF Verifier on, and the **VerifierOn** option is currently off, the app turns it on. You can still disable it manually. In this case, the text describing the feature indicates what it would do if Verifier were on. Similar changes in text describing a setting’s state can be seen whenever a setting depends on other settings, or the usage of App Verifier or Driver Verifier.

If you start and stop devices or install new drivers, you must restart WDF Verifier to update the inventory.

If you make changes on the **WDF Drivers** page, you'll see those changes reflected on the **Devices using WDF** page.

 

 





