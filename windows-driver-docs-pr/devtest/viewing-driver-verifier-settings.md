---
title: Viewing Driver Verifier Settings
description: Viewing Driver Verifier Settings
ms.assetid: 2dd5f1b4-5c78-459c-8b73-c8d511f8a22b
keywords:
- Driver Verifier WDK , viewing settings
- viewing Driver Verifier setting
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Viewing Driver Verifier Settings


## <span id="ddk_viewing_driver_verifier_settings_tools"></span><span id="DDK_VIEWING_DRIVER_VERIFIER_SETTINGS_TOOLS"></span>


The current Driver Verifier settings can be displayed by using Driver Verifier Manager. There are two versions of Driver Verifier Manager -- one for [Windows 2000](driver-verifier-manager--windows-2000-.md) and one for [Windows XP and later](driver-verifier-manager--windows-xp-and-later-.md). In Windows XP and later, these settings can also be displayed by using the [**Verifier Command Line**](verifier-command-line.md).

The following methods will display the settings that will take effect after the next boot. These will include a list of the Driver Verifier options that have been selected as well as a list of the drivers to be verified.

### <span id="verifier_command_line"></span><span id="VERIFIER_COMMAND_LINE"></span>Verifier Command Line

(Windows XP and later) To display the Driver Verifier settings, use the **verifier /querysettings** command.

### <span id="driver_verifier_manager__windows_2000_"></span><span id="DRIVER_VERIFIER_MANAGER__WINDOWS_2000_"></span>Driver Verifier Manager (Windows 2000)

To display the Driver Verifier settings, select the **Settings** tab.

Press **Exit** to stop viewing these settings.

### <span id="driver_verifier_manager__windows_xp_and_later_"></span><span id="DRIVER_VERIFIER_MANAGER__WINDOWS_XP_AND_LATER_"></span>Driver Verifier Manager (Windows XP and later)

To display the Driver Verifier settings, start Driver Verifier Manager and select the **Display Existing Settings** task. Then press **Next**.

Press **Finish** to stop viewing these settings.

### <span id="viewing_the_currently_active_features"></span><span id="VIEWING_THE_CURRENTLY_ACTIVE_FEATURES"></span>Viewing the Currently-Active Features

If you wish to view the Driver Verifier features that are currently active, rather than the settings that will take effect after the next boot, see [Using Volatile Settings](using-volatile-settings.md).

 

 





