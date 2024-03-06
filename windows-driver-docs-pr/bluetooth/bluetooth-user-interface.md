---
title: Bluetooth User Interface
description: Describes working with the Bluetooth user interface in Windows for software developers and vendors
ms.date: 01/10/2024
---

# Bluetooth user interface

This article describes working with the Bluetooth user interface in Windows for software developers and vendors.

## What is the Bluetooth File Transfer Wizard?

The Bluetooth File Transfer Wizard enables users to transfer files between a computer and a Bluetooth device. For example, users can transfer files between a computer and a mobile phone or a personal digital assistant (PDA). The Bluetooth File Transfer Wizard can also transfer files between two computers that support Bluetooth.

> [!NOTE]
> The default GUI that the Bluetooth File Transfer Wizard uses is implemented in the Fsquirt.exe file. This file can be unhooked from the underlying transfer wizard mechanism to enable replacement of the default Bluetooth File Transfer Wizard GUI. For more information, see the following question.

## How do I unhook Fsquirt.exe?

Software developers that desire to replace the in-box Bluetooth File Transfer Wizard with a proprietary application can unhook Fsquirt.exe from the underlying transfer wizard mechanism by performing the following steps:

1. Create a DWORD value that is named **DisableFsquirt** under the HKLM\\System\\CurrentControlSet\\Services\\Bthport\\Parameters key in the registry.
1. Set the value of **DisableFsquirt** to 0x1
1. Either reboot or run the following command in a command prompt window: **fsquirt.exe -UnRegister**

To re-enable Fsquirt.exe, perform the following steps:

1. Delete the **DisableFsquirt** value from the registry.
1. Reboot or run the following command in a command prompt window: **fsquirt.exe -Register**

## Why does the Bluetooth notification area icon sometimes disappear?

The Bluetooth notification area icon appears when the Bluetooth radio is connected to the computer. The icon is configured to stay active for up to 10 minutes, but after that period the icon disappears from the notification area.

If users want a persistent Bluetooth notification area icon, they can select the **Show the Bluetooth icon in the notification area** check box on the **Options** tab of the Control Panel Bluetooth Settings application.

:::image type="content" source="images/bluetoothnotificationsettings.jpg" alt-text="Screenshot of the Options tab in the Bluetooth Settings dialog box, showing the 'Show the Bluetooth icon in the notification area' checkbox.":::

> [!NOTE]
> Even if no Bluetooth icon is in the notification area, you can still use the Control Panel Bluetooth Settings application to perform related tasks such as adding new Bluetooth devices, making the computer discoverable, and so on.

## Can vendors add tabs to the Control Panel Bluetooth Settings application?

Yes, vendors can add tabs by implementing a shell property sheet handler for the application. For example, IHVs that implement extensions to the in-box Bluetooth stack can implement a property sheet handler that adds tabs for profiles such as file transfer, enhancements added to version 2.1 of the Bluetooth specification, and so on. For more information about how to implement property sheet handlers, see [Property Sheet Handlers](/previous-versions/windows/desktop/legacy/cc144106(v=vs.85)).

## Why does Windows 7 and Windows Vista display a dialog box when a Bluetooth audio device is initially connected?

Windows might not provide default support for headset (HSP), hands-free (HFP), or advanced audio distribution (A2DP) audio profiles. If a Bluetooth audio device is paired with a system that does not have the necessary drivers, Windows typically displays the **Found New Hardware** dialog box. However, the dialog box does not appear if one of the following is true:

- The computer's OEM provided a profile pack that supports Bluetooth audio.
- The end user previously installed a Bluetooth headset and downloaded the audio drivers from media that the IHV or Windows Update provided.

## How do I enhance the functionality and better represent my Bluetooth device in Devices and Printers?

You can create a device metadata package for your Bluetooth device so that Devices and Printers displays device-specific information about your device, such as photorealistic icons and custom descriptions. This can significantly improve a user's experience with your Bluetooth device. For example, you might want to more effectively expose all the features that your device supports. Certain device classes can also take advantage of Device Stage, which enables IHVs to further enhance the device experience by providing a customized and branded device-specific user interface.

For more information about how to create a device metadata package for your device, see [How to Create a Device Metadata Package for Devices and Printers](/previous-versions/windows/hardware/metadata/).

For more information about Device Stage, see **"Device Stage General Development Kit" on the MSDN Web site**.

> [!NOTE]
> To take advantage of Device Stage, the Device ID Profile must be implemented, which includes the Hardware ID, Vendor ID, and PID.
