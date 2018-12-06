---
title: Finish-Install Actions
description: Finish-Install Actions
ms.assetid: 52c7f166-ee74-46b6-815b-5d360d829b4c
keywords:
- finish-install actions WDK device installations
- installer finish-install actions WDK device installations
- finish-install wizard pages WDK device installations
- class installers WDK device installations , finish-install actions
- co-installers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Finish-Install Actions


**Note**  Features described in this section are not supported in universal or mobile driver packages. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

*Finish-install actions* allow the installer to complete installation operations.

Installers can specify finish-install actions to happen in a class installer, class co-installer, or device co-installer, starting with Windows Vista and later versions. Finish-install actions run in the context of an administrator *after* all other installation operations, including finish-install wizard pages, are completed.

In Windows 7, the default finish-install action is provided by the system-supplied [**SetupDiFinishInstallAction**](https://msdn.microsoft.com/library/windows/hardware/ff551022) function. This function processes, in the interactive context of an administrator, the [RunOnce registry entries](runonce-registry-key.md) that are set for a device. If a device does not have a class installer, or a class installer returns ERROR_DI_DO_DEFAULT in response to a [**DIF_FINISHINSTALL_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request, Windows calls **SetupDiFinishInstallAction** after all the installers for a device complete their finish-install actions.

In Windows 8 and later versions, finish-install actions are not automatically run as part of device installation, and the [**SetupDiFinishInstallAction**](https://msdn.microsoft.com/library/windows/hardware/ff551022) function has been removed. Instead, an administrator (or a limited user that can provide administrator credentials to a UAC prompt) must go to the Action Center and address the "Finish installing device software" maintenance item in order for the finish-install action to be run. Until then, the finish-install action will not run. For example, if a user plugs in a device that installs a driver that includes a finish-install action, the finish-install action will not automatically run at that time. Instead, the finish-install action will run at some later point when the user manually initiates it. Thereafter, when Windows runs the finish-install action, the action has that single opportunity to run. If the action fails then it must take appropriate steps to allow the user to try again and finish later. Similarly, installing supporting software that should accompany a driver can still be accomplished with a finish-install action, but it will also not be installed automatically.

Alternatively, depending on your scenario, in Windows 8 and later versions, you may be able to make use of the new device app model. More information about device apps can be found at [Design Great Hardware Experiences](http://go.microsoft.com/fwlink/p/?linkid=227833).

Finish-install actions are useful in the following situations:

-   To run a device-specific application installation program that is not designed to run as part of a finish-install wizard page. If such an installation program has its own user interface, using a finish-install action to install the application provides a better user experience.

    For example, assume that a device manufacturer wants to install a device-specific application in addition to a driver for a device, and the device-specific application has its own installation program with its own user interface. To provide the best user experience, the device manufacturer would run the installation program as a finish-install action. In this way, when Windows detects the device and finds the driver, Windows first installs the driver and then runs the installation program for the application.

-   To run an installation program that can only run in an interactive user context (a client-side installation). For example, such an installation program can be started by using an **InteractiveInstall** directive in the [**INF ControlFlags Section**](inf-controlflags-section.md) of a [driver package's](driver-packages.md) INF file.

    **Note**  Starting with Windows Vista, such an installation program cannot be run in the same way as on earlier versions of Windows. This is because Windows Vista and later versions of Windows do not support the installation of devices within a client-side installation. However, such an installation program can be run as a finish-install action if the driver package includes a class installer, class co-installer, or device co-installer that starts the installation program.

     

This section discusses finish-install actions in more detail and includes the following topics:

[Overview of Finish-Install Actions](overview-of-finish-install-actions.md)

[Implementing Finish-Install Actions](implementing-finish-install-actions.md)

[How Finish-Install Actions are Processed](how-finish-install-actions-are-processed.md)

 

 





