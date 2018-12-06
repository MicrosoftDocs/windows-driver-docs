---
title: Guidelines for Implementing Finish-Install Actions
description: Guidelines for Implementing Finish-Install Actions
ms.assetid: 455d520a-ccd7-470b-ab5f-5786ee90b91d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Guidelines for Implementing Finish-Install Actions


Finish-install actions can be run by an *installer* (a class installer, class co-installer, or device co-installer). In its finish-install actions, an installer can run an executable program, create a process, create a thread, or execute code in the device driver installation finish-install process.

Consider the following guidelines when you implement finish-install actions in an installer:

-   Finish-install actions cannot be used to apply any critical settings that are required for a device to work.

-   An installer should wait for the finish-install action to finish if the finish-install action must run to completion.

    For example, to avoid being interrupted by a system restart while a finish-install action is still running, an installer should wait for the finish-install action to finish before the installer returns from processing a [**DIF_FINISHINSTALL_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request.

-   A finish-install action should inform a user of progress.

    Windows does not inform a user that finish-install actions are running or that finish-install actions succeed or fail. Therefore, a finish-install action should inform the user that a finish-install action is in progress and then notify the user that the finish-install action succeeded or failed.

-   An installer must handle the situation where a system restart is required to complete the finish-install actions.

    If a finish-install action requires a system restart before the settings take effect on the device, the installer should set the DI_NEEDREBOOT flag before it returns from processing a [**DIF_FINISHINSTALL_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request. However, a device installation should not force a restart of a computer unless absolutely necessary.

    For more information about when a device installation should require a system restart, see [Device Installations and System Reboots](device-installations-and-system-restarts.md).

-   An installer should handle the situation where a finish-install action fails, but should be attempted again. For example, the installer can fail the finish-install action in this way if the device that is being installed has been removed from the system.

    Prior to Windows 8, if a finish-install action fails, but should be attempted again, an installer should notify the user of the temporary failure, perform any necessary cleanup, and return a Win32 error code for the DIF_FINISHINSTALL_ACTION request. If an installer returns a Win32 error code for a DIF_FINISHINSTALL_ACTION request, Windows does not clear the device as having been flagged to perform a finish install action for the device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)).

    However, starting with Windows 8, returning an error code will not prevent the flag being cleared. If the finish-install action has an error, it needs to provide the user with the ability to run it again in the future.

    While this flag remains set for the device, Windows runs a new finish-install process.

    For more information, see [Running Finish-Install Actions](running-finish-install-actions.md).

-   An installer should handle the situation where a finish-install action fails and should not be attempted again.

    If an error makes it impossible for a finish-install action ever to succeed, an installer should notify the user that the action cannot be completed, and then perform any necessary cleanup. In this situation, a co-installer should return NO_ERROR and a device or class installer should return ERROR_DI_DO_DEFAULT. Windows will subsequently clear the device as having been flagged to perform a finish install action for the devnode and call [**SetupDiFinishInstallAction**](https://msdn.microsoft.com/library/windows/hardware/ff551022) to perform the default finish-install operations.

-   When the installer processes a [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) DIF code, it should check to see if any finish-install actions are needed. The installer should only set the DI_FLAGSEX_FINISHINSTALL_ACTION flag if there are finish-install actions that must be performed. If this flag is set unnecessarily, users get an extra device installation prompt during reinstallation of the driver, and the DIF_FINISHINSTALL_ACTION request has no finish-install actions to perform.

    For example, consider a device co-installer where the finish-install action installs an application that is required for the device to work properly. For instance, the finish-install action for a Microsoft keyboard might install the IntelliType application. When such a co-installer processes the [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) DIF code, it should check to see whether the application is already installed. If the application is already installed, there is no finish-install action to perform, and therefore the DI_FLAGSEX_FINISHINSTALL_ACTION flag should not be set. In this situation, if the co-installer incorrectly sets the DI_FLAGSEX_FINISHINSTALL_ACTION flag, the user gets an undesired User Account Control (UAC) prompt for permission to proceed even though the finish-install action has no action to perform.

    **Note**  Starting with Windows 7, if UAC is set to the default setting ("Notify me only when programs try to make changes to my computer") or a lower setting, the operating system does not display the prompt for users with administrative privileges when it processes finish-install actions.

     

-   Before you register an installer that implements finish-install actions, you must include and install all the files that are needed to run the finish-install actions in the [**CopyFiles directive**](inf-copyfiles-directive.md) of the [INF file](inf-files.md) for the device. This is required so that the files get placed during the installation in a location that is accessible by the installer.

    For more information about the registration requirements of a device or class co-installer, see [Registering a Class Co-installer](registering-a-class-co-installer.md).

 

 





