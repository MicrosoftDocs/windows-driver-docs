---
title: Bluetooth user interface
description: Describes working with the Bluetooth user interface in Windows for software developers and vendors
ms.assetid: 7E342615-217A-4252-AAC4-7F7EE013840D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bluetooth User Interface


## <span id="What_is_the_Bluetooth_File_Transfer_Wizard_"></span><span id="what_is_the_bluetooth_file_transfer_wizard_"></span><span id="WHAT_IS_THE_BLUETOOTH_FILE_TRANSFER_WIZARD_"></span>What is the Bluetooth File Transfer Wizard?


The Bluetooth File Transfer Wizard enables users to transfer files between a computer and a Bluetooth device. For example, users can transfer files between a computer and a mobile phone or a personal digital assistant (PDA). The Bluetooth File Transfer Wizard can also transfer files between two computers that support Bluetooth.

**Note**  The default GUI that the Bluetooth File Transfer Wizard uses is implemented in the Fsquirt.exe file. This file can be unhooked from the underlying transfer wizard mechanism to enable replacement of the default Bluetooth File Transfer Wizard GUI. For more information, see the following question.

 

## <span id="how_do_i_unhook_fsquirt.exe_"></span><span id="HOW_DO_I_UNHOOK_FSQUIRT.EXE_"></span>How do I unhook Fsquirt.exe?


Software developers that desire to replace the in-box Bluetooth File Transfer Wizard with a proprietary application can unhook Fsquirt.exe from the underlying transfer wizard mechanism by performing the following steps:

1.  Create a DWORD value that is named **DisableFsquirt** under the HKLM\\System\\CurrentControlSet\\Services\\Bthport\\Parameters key in the registry.
2.  Set the value of **DisableFsquirt** to 0x1
3.  Either reboot or run the following command in a command prompt window: **fsquirt.exe -UnRegister**

To re-enable Fsquirt.exe, perform the following steps:

1.  Delete the **DisableFsquirt** value from the registry.
2.  Reboot or run the following command in a command prompt window: **fsquirt.exe -Register**

## <span id="In_Windows_Vista__why_does_the_Bluetooth_notification_area_icon_sometimes_disappear_"></span><span id="in_windows_vista__why_does_the_bluetooth_notification_area_icon_sometimes_disappear_"></span><span id="IN_WINDOWS_VISTA__WHY_DOES_THE_BLUETOOTH_NOTIFICATION_AREA_ICON_SOMETIMES_DISAPPEAR_"></span>In Windows Vista, why does the Bluetooth notification area icon sometimes disappear?


In Windows Vista RTM and Windows Vista with SP1, the Bluetooth notification area icon appears when the Bluetooth radio is connected to the computer. The icon is configured to stay active for up to 10 minutes, but after that period the icon disappears from the notification area.

If users want a persistent Bluetooth notification area icon, they can select the **Show the Bluetooth icon in the notification area** check box on the **Options** tab of the Control Panel Bluetooth Settings application.

![bluetooth notification settings](images/bluetoothnotificationsettings.jpg)

**Note**  Even if no Bluetooth icon is in the notification area, you can still use the Control Panel Bluetooth Settings application to perform related tasks such as adding new Bluetooth devices, making the computer discoverable, and so on.

 

## <span id="Can_vendors_add_tabs_to_the_Control_Panel_Bluetooth_Settings_application_"></span><span id="can_vendors_add_tabs_to_the_control_panel_bluetooth_settings_application_"></span><span id="CAN_VENDORS_ADD_TABS_TO_THE_CONTROL_PANEL_BLUETOOTH_SETTINGS_APPLICATION_"></span>Can vendors add tabs to the Control Panel Bluetooth Settings application?


Yes, vendors can add tabs by implementing a shell property sheet handler for the application. For example, IHVs that implement extensions to the in-box Bluetooth stack can implement a property sheet handler that adds tabs for profiles such as file transfer, enhancements added to version 2.1 of the Bluetooth specification, and so on. For more information about how to implement property sheet handlers, see [Property Sheet Handlers](https://msdn.microsoft.com/library/windows/desktop/cc144106).

## <span id="Why_does_Windows_7_and_Windows_Vista_display_a_dialog_box_when_a_Bluetooth_audio_device_is_initially_connected_"></span><span id="why_does_windows_7_and_windows_vista_display_a_dialog_box_when_a_bluetooth_audio_device_is_initially_connected_"></span><span id="WHY_DOES_WINDOWS_7_AND_WINDOWS_VISTA_DISPLAY_A_DIALOG_BOX_WHEN_A_BLUETOOTH_AUDIO_DEVICE_IS_INITIALLY_CONNECTED_"></span>Why does Windows 7 and Windows Vista display a dialog box when a Bluetooth audio device is initially connected?


Windows might not provide default support for headset (HSP), hands-free (HFP), or advanced audio distribution (A2DP) audio profiles. If a Bluetooth audio device is paired with a system that does not have the necessary drivers, Windows typically displays the **Found New Hardware** dialog box. However, the dialog box does not appear if one of the following is true:

-   The computer’s OEM provided a profile pack that supports Bluetooth audio.
-   The end user previously installed a Bluetooth headset and downloaded the audio drivers from media that the IHV or Windows Update provided.

## <span id="How_do_I_enhance_the_functionality_and_better_represent_my_Bluetooth_device_in_Devices_and_Printers_"></span><span id="how_do_i_enhance_the_functionality_and_better_represent_my_bluetooth_device_in_devices_and_printers_"></span><span id="HOW_DO_I_ENHANCE_THE_FUNCTIONALITY_AND_BETTER_REPRESENT_MY_BLUETOOTH_DEVICE_IN_DEVICES_AND_PRINTERS_"></span>How do I enhance the functionality and better represent my Bluetooth device in Devices and Printers?


You can create a device metadata package for your Bluetooth device so that Devices and Printers displays device-specific information about your device, such as photorealistic icons and custom descriptions. This can significantly improve a user’s experience with your Bluetooth device. For example, you might want to more effectively expose all the features that your device supports. Certain device classes can also take advantage of Device Stage, which enables IHVs to further enhance the device experience by providing a customized and branded device-specific user interface.

For more information about how to create a device metadata package for your device, see [How to Create a Device Metadata Package for Devices and Printers](https://docs.microsoft.com/previous-versions/windows/hardware/metadata/).

For more information about Device Stage, see **“Device Stage General Development Kit” on the MSDN Web site**.

**Note**  To take advantage of Device Stage, the Device ID Profile must be implemented, which includes the Hardware ID, Vendor ID, and PID.

 

 

 





