---
title: Overview of Finish-Install Actions
description: Overview of Finish-Install Actions
ms.assetid: 986ac884-2970-4eda-a800-88fd30b95562
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Finish-Install Actions


If an *installer* (a class installer, class co-installer, or device co-installer) provides finish-install actions for a device, Windows runs the finish-install actions *after* all other device installation operations for the device have completed, and the device has been started. On a new system, finish-install actions run the first time that the operating system is started after Windows is finished.

Device installation operations include the following:

-   The *core device installation* (also known as *server-side installation*), in which the driver for the device is installed in a trusted system context and without user interaction.

Windows processes *finish-install actions* in the same way regardless of whether the installation is initiated by connecting a Plug and Play device to a computer (a [*hardware-first installation*](hardware-first-installation.md)) or the installation is initiated by running an installation program such as the Found New Hardware Wizard, the Update Driver Software Wizard, or a vendor-supplied installation program (a *software-first installation*).

Windows runs finish-install actions only in the context of a user who has administrator privileges.

Starting with Windows Vista, User Account Control (UAC) enables users to run at lower privilege most of the time and elevate privilege only when necessary. Therefore, if the finish-install process is invoked, Windows prompts the user for the consent and the credentials that are required to run the finish-install actions. If the user does not supply consent or provide the necessary credentials, the finish-install actions are deferred until a user who does supply consent and the necessary credentials signs in.

**Note**   Starting with Windows 7, if UAC is set to the default setting (Notify me only when programs try to make changes to my computer) or a lower setting, the operating system does not display the prompt for users with administrative privileges when it processes finish-install actions.

 

 

 





