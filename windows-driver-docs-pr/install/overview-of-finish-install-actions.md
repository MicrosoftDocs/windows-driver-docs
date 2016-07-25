---
title: Overview of Finish-Install Actions
description: Overview of Finish-Install Actions
ms.assetid: 986ac884-2970-4eda-a800-88fd30b95562
---

# Overview of Finish-Install Actions


If an *installer* (a class installer, class co-installer, or device co-installer) provides finish-install actions for a device, Windows runs the finish-install actions *after* all other device installation operations for the device have completed, and the device has been started. On a new system, finish-install actions run the first time that the operating system is started after Windows is finished.

Device installation operations include the following:

-   The *core device installation* (also known as *server-side installation*), in which the driver for the device is installed in a trusted system context and without user interaction.

Windows processes *finish-install actions* in the same way regardless of whether the installation is initiated by connecting a Plug and Play device to a computer (a [*hardware-first installation*](hardware-first-installation.md)) or the installation is initiated by running an installation program such as the Found New Hardware Wizard, the Update Driver Software Wizard, or a vendor-supplied installation program (a *software-first installation*).

Windows runs finish-install actions only in the context of a user who has administrator privileges.

Starting with Windows Vista, User Account Control (UAC) enables users to run at lower privilege most of the time and elevate privilege only when necessary. Therefore, if the finish-install process is invoked, Windows prompts the user for the consent and the credentials that are required to run the finish-install actions. If the user does not supply consent or provide the necessary credentials, the finish-install actions are deferred until a user who does supply consent and the necessary credentials signs in.

**Note**   Starting with Windows 7, if UAC is set to the default setting (Notify me only when programs try to make changes to my computer) or a lower setting, the operating system does not display the prompt for users with administrative privileges when it processes finish-install actions.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Overview%20of%20Finish-Install%20Actions%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




