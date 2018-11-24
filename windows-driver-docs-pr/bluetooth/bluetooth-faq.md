---
title: Bluetooth FAQ
description: This FAQ section provides information about Bluetooth wireless technology support for the Windows family of operating systems.
ms.assetid: 529DD4A2-4E4B-47F4-BD65-BE89EA21E217
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bluetooth FAQ


This FAQ section provides information about Bluetooth wireless technology support for the Windows family of operating systems. It is intended primarily for independent hardware vendors (IHVs) who are new to the Bluetooth ecosystem on Windows and addresses topics of interest to both hardware and software developers.

Additional frequently asked questions are located in the following topics:

[Bluetooth Version and Profile Support in Windows 10](general-bluetooth-support-in-windows.md)
[Bluetooth Version and Profile Support in Previous Windows Versions](bluetooth-support-in-previous-windows-versions.md)
[Bluetooth Host Radio Support](bluetooth-host-radio-support.md)
[Bluetooth User Interface](bluetooth-user-interface.md)
[Bluetooth Certification](bluetooth-certification.md)
[Appendix A](bluetooth-faq--appendix-a.md)
[Appendix B](bluetooth-faq--appendix-b.md)
## <span id="How_many_Bluetooth_radios_can_Windows_support_"></span><span id="how_many_bluetooth_radios_can_windows_support_"></span><span id="HOW_MANY_BLUETOOTH_RADIOS_CAN_WINDOWS_SUPPORT_"></span>How many Bluetooth radios can Windows support?


The Bluetooth stack in Windows supports only one Bluetooth radio. This radio must comply with the Bluetooth specification and the latest Windows Hardware Certification Program requirements.

## <span id="How_can_Bluetooth_and_Wi-Fi_radios_coexist_effectively_"></span><span id="how_can_bluetooth_and_wi-fi_radios_coexist_effectively_"></span><span id="HOW_CAN_BLUETOOTH_AND_WI-FI_RADIOS_COEXIST_EFFECTIVELY_"></span>How can Bluetooth and Wi-Fi radios coexist effectively?


Both Bluetooth and Wi-Fi radios operate in the 2.4-GHz frequency range, so they could momentarily try to use the same frequency. The frequency hopping technique that Bluetooth wireless technology uses prevents such a conflict from causing a complete connectivity loss, but it could reduce the transfer rates for both radios.

Version 2.0 of the Bluetooth specification supports AFH. With AFH, a Bluetooth radio senses traffic from other types of radios, marks the busy channels as ”noisy,” and avoids those channels as it hops frequencies. Windows Vista and later improves AFH even further by treating the ”air” as a shareable spectrum. This feature lets wireless technologies such as Wi-Fi adapters report which channels they intend to use. When the Bluetooth stack becomes active, it is notified of the reported in use channels and marks them as noisy.

## <span id="How_do_I_enable_AFH_in_Windows_"></span><span id="how_do_i_enable_afh_in_windows_"></span><span id="HOW_DO_I_ENABLE_AFH_IN_WINDOWS_"></span>How do I enable AFH in Windows?


Windows Vista and later includes a shared-spectrum model to support AFH for Bluetooth radios that are based on version 2.0 and later versions of the Bluetooth specification. However, this feature is disabled by default. For a system to support the shared spectrum model, the OEM must explicitly enable the feature and specify the width of the frequency band that should be blocked around an active Wi Fi channel. To specify the width of the frequency band, create a value of type REG\_DWORD that is named ChannelAvoidanceRange under the following registry key:

**HKLM\\System\\CurrentControlSet\\Services\\BthServ\\Parameters**

The **ChannelAvoidanceRange** value enables or disables spectrum sharing and specifies the width of the blocked frequency band. To enable spectrum sharing, set **ChannelAvoidanceRange** to the full width of the frequency band that should be blocked around an active Wi-Fi channel. The units are in MHz and can range from 20 to 40 (0.02 to 0.04 GHz). OEMs must determine an appropriate bandwidth based on a selected set of radios, antenna characteristics, and radio manufacturer feedback.

A new **ChannelAvoidanceRange** value takes effect only after the system has been rebooted. Ideally, the OEM should set the **ChannelAvoidanceRange** value during the preinstallation process.

For the Windows shared-spectrum model to work effectively, Wi-Fi miniport drivers must report their channel usage to the networking connections manager. The networking stack then passes the channel-use information to the Bluetooth stack.

## <span id="How_do_I_enable_remote_wake_in_Windows_"></span><span id="how_do_i_enable_remote_wake_in_windows_"></span><span id="HOW_DO_I_ENABLE_REMOTE_WAKE_IN_WINDOWS_"></span>How do I enable remote wake in Windows?


Windows Vista with Service Pack 2 (SP2) and later provides software support that lets Bluetooth-enabled keyboards and mouse devices wake the computer from sleep (S3) or hibernate (S4) system power states. For such a wake to be successful, the Bluetooth module must be self-powered and must have enough power to wake the computer. Even if Windows enables wake from the S4 system power state, the computer will not wake if the Bluetooth module has no power when the computer is in S4.

To enable Remote Wake in software, verify that the Bluetooth module can support wake and set the following registry values:

-   HKLM\\System\\CurrentControlSet\\Services\\Bthport\\Parameters \\SystemRemoteWakeSupported : (DWORD) 1
-   HKLM\\System\\CurrentControlSet\\Enum\\USB\\&lt;vid\_pid&gt;\\&lt;Bluetooth Radio ID&gt; \\Device Parameters\\RemoteWakeEnabled : (DWORD) 1
-   HKLM\\System\\CurrentControlSet\\Enum\\USB\\&lt;vid\_pid&gt;\\&lt;Bluetooth Radio ID&gt; \\Device Parameters\\DeviceRemoteWakeSupported : (DWORD) 1

**Note**  If the Bluetooth radio’s property page in Device Manager has a **Power Management** tab, the radio can support wake. If no **Power Management** tab exists, the radio might support wake, but it is unlikely.

 

 

 





