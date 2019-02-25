---
title: How Finish-Install Actions are Processed
description: How Finish-Install Actions are Processed
ms.assetid: 028cce46-018d-496e-bc99-c8bf6158c898
keywords:
- finish-install actions WDK device installations
- default finish-install actions
- server-side installations WDK
- CONFIG_FINISHINSTALL
- actions WDK finish-install
- DI_FLAGSEX_FINISHINSTALL_ACTION
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How Finish-Install Actions are Processed


Finish-install actions for a device are processed in the same way by an *installer* (a class installer, class co-installer, or device co-installer), regardless of whether the installation was a [*hardware-first installation*](hardware-first-installation.md) or the installation is initiated by running an installation program such as the Found New Hardware Wizard, the Update Driver Software Wizard, or a vendor-supplied installation program (a [*software-first installation*](software-first-installation.md)).

**Note**  In Windows 8, Windows 8.1, and Windows 10, finish-install actions must be completed in the Action Center by an administrator (or a limited user that can provide administrator credentials to a UAC prompt). Users must click on "Finish installing device software".

 

Windows processes finish-install actions after all other installation operations have completed and the device has been started, including:

-   Core device installation (also known as *server-side installation*), in which the driver for the device is installed and loaded by the system's Plug and Play (PnP) manager components.

Windows completes the following steps to process an installer's finish-install actions:

1.  At the end of core device installation, Windows calls [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) to send a [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) request to the installers for the device.

    DIF_NEWDEVICEWIZARD_FINISHINSTALL is the only DIF code that is sent in both the context of core device installation and in the client context. Therefore, a class installer, class co-installer, or device co-installer must indicate that it has finish-install actions during DIF_NEWDEVICEWIZARD_FINISHINSTALL processing, instead of during DIF_INSTALLDEVICE processing.

2.  If an installer provides finish-install actions, it sets the DIF_FLAGSEX_FINISHINSTALL_ACTION flag in response to a [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) request. If the DIF_FLAGSEX_FINISHINSTALL_ACTION flag is set after all the installers have processed a DIF_NEWDEVICEWIZARD_FINISHINSTALL request, the device is flagged to perform a finish install action.

    For more information about this operation, see [Marking a Device as having a Finish-Install Action to Perform](setting-the-configflag-finishinstall-action-device-configuration-flag.md).

3.  After core device installation is complete for a device, Windows checks whether the device has been flagged to perform a finish-install action. If it has, Windows queues a finish-install process that performs the finish-install actions specific to the device. The process executes in the user's context.

    In Windows 8 and later versions, finish-install actions are not automatically run as part of device installation. Instead, an administrator (or a limited user that can provide administrator credentials to a UAC prompt) must go to the Action Center and address the "Finish installing device software" maintenance item for the finish-install action to run. Until then, the finish-install action will not run. For example, if a user plugs in a device that installs a driver that includes a finish-install action, the finish-install action will not automatically run at that time. The finish-install action runs at a later point when the user manually initiates it. When Windows runs the finish-install action, the action has that single opportunity to run. If the action fails then it must take appropriate steps to allow the user to try again and finish later. Installing supporting software that should accompany a driver can still be accomplished with a finish-install action, but it will also not be installed automatically.

    In Windows 7, the finish-install process runs only in the context of a user with administrator credentials at one of the following times:

    -   The next time that a user who has administrator credentials logs on while the device is attached.
    -   When the device is reattached.
    -   When the user selects **Scan for hardware changes** in Device Manager.

    If a user is signed in without administrative privileges, Windows prompts the user for consent and credentials to run the finish-install actions in an administrator context.

4.  When finish-install operations run, the finish-install process starts and completes any finish-install wizard pages for the device, and then calls [**SetupDiCallClassInstaller**](https://msdn.microsoft.com/library/windows/hardware/ff550922) to send a [**DIF_FINISHINSTALL_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request to all installers for the device, as described in [Running Finish-Install Actions](running-finish-install-actions.md).

5.  After the installers have completed their finish-install actions, Windows runs the default finish-install action, as described in [Running the Default Finish-Install Action](running-the-default-finish-install-action.md).

 

 





