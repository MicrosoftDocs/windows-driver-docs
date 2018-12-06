---
title: Selecting Drivers to be Verified
description: Selecting Drivers to be Verified
ms.assetid: a752dea1-f49c-4e58-9e56-6b54701c760e
keywords:
- Driver Verifier WDK , driver selections
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Selecting Drivers to be Verified


## <span id="ddk_selecting_drivers_to_be_verified_tools"></span><span id="DDK_SELECTING_DRIVERS_TO_BE_VERIFIED_TOOLS"></span>


Drivers can be selected for verification by using the [**Verifier Command Line**](verifier-command-line.md), or by using Driver Verifier Manager. There are two versions of Driver Verifier Manager -- one for [Windows 2000](driver-verifier-manager--windows-2000-.md) and one for [Windows XP and later](driver-verifier-manager--windows-xp-and-later-.md).

### <span id="verifier_command_line"></span><span id="VERIFIER_COMMAND_LINE"></span>Verifier Command Line

To verify all drivers, use the **/all** parameter.

To verify a list of drivers, use the **/driver** parameter.

See [**Verifier Command Line**](verifier-command-line.md) for details.

### <span id="driver_verifier_manager__windows_2000_"></span><span id="DRIVER_VERIFIER_MANAGER__WINDOWS_2000_"></span>Driver Verifier Manager (Windows 2000)

To verify all drivers, select the **Settings** tab. Select **Verify all drivers**. Then press **Apply**.

To verify a list of drivers, select the **Settings** tab. Select **Verify selected drivers**. You will see a list of all drivers that were loaded in the system during the most recent boot.

The **Verification Status** column gives the current status for each driver. Possible **Verification Status** values are:

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled**  
The driver is currently being verified and will continue to be verified after reboot.

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled**  
The driver is not currently being verified, and will not be verified after reboot.

<span id="Enabled__Reboot_Needed_"></span><span id="enabled__reboot_needed_"></span><span id="ENABLED__REBOOT_NEEDED_"></span>**Enabled (Reboot Needed)**  
The driver is not currently being verified, but the user has requested verification of this driver. This driver will be verified after reboot.

<span id="Disabled__Reboot_Needed_"></span><span id="disabled__reboot_needed_"></span><span id="DISABLED__REBOOT_NEEDED_"></span>**Disabled (Reboot Needed)**  
The driver is currently being verified, but the user has requested an end to this verification. After reboot, this driver will no longer be verified.

You can select one or more drivers from this list and click the **Verify** or **Don't Verify** button. You can also right-click the driver's name and control verification from the menu.

The **Verify These Additional Drivers After Next Reboot** text box allows you to enter the names of drivers not currently loaded on the system. Multiple names must be separated with spaces.

Once you have selected the drivers to verify, press **Apply**.

To deactivate all options and clear the verified driver list, select the **Settings** tab. Press the **Reset All** button. Then press **Apply**.

### <span id="driver_verifier_manager__windows_xp_and_later_"></span><span id="DRIVER_VERIFIER_MANAGER__WINDOWS_XP_AND_LATER_"></span>Driver Verifier Manager (Windows XP and later)

In the Windows XP and later Driver Verifier Manager, selection of drivers must be done after selection of options. See [Selecting Driver Verifier Options](selecting-driver-verifier-options.md) for a description of this first step.

Once the first step has been completed, you will see the **Select what drivers to verify** panel. You can choose drivers in a variety of ways:

-   To verify all drivers, select **Automatically select all drivers installed on this computer**.

-   To verify a list of drivers, select **Select driver names from a list** and then press **Next**. You will see a list of all drivers that are currently loaded. (In Windows XP and later, the current verification status of each driver will not be indicated.) Check the box next to each driver that you wish to verify. To select drivers that are not on the list, press **Add currently not loaded driver(s) to the list**. This allows you to browse the system for the desired driver's file. Press **Open** to add that driver to the top of the list. You must then check the box next to this driver to select it for verification.

    Starting with Windows 8, you can use buttons in Driver Verifier Manager to select all drivers (**Select all**), clear your selection (**Deselect all**), and invert your selection (**Invert selection**).

-   To verify unsigned drivers, select **Automatically select unsigned drivers**. A list of these drivers will be displayed. (If no such drivers exist, an error message will appear.)

-   To verify drivers built for earlier versions of Windows, select **Automatically select drivers built for older versions of Windows**. A list of these drivers will be displayed. (If no such drivers exist, an error message will appear.)

After you have selected the drivers to be verified, press either **Next** or **Finish**.

If you enabled Disk Integrity Checking, you will see a list of all physical disks attached to your computer. Check the box next to each disk that you wish to verify, and then press **Finish**.

To deactivate all options and clear the verified driver list, start Driver Verifier Manager and select **Delete existing settings** from the first screen. Then press **Finish**.

### <span id="reboot_required"></span><span id="REBOOT_REQUIRED"></span>Reboot Required

On Windows XP and Windows Server 2003, you can start and stop the verification of a driver without restarting ("rebooting") the computer, but only if the driver is not loaded. For details, see [Using Volatile Settings](using-volatile-settings.md).

Beginning in Windows Vista, you can start and stop the verification of drivers that are not loaded without rebooting the computer. You can also start the verification of a driver that is already loaded without rebooting. However, you cannot stop the verification of a driver that is already loaded until you reboot the system. For details, see [Using Volatile Settings](using-volatile-settings.md).

 

 





