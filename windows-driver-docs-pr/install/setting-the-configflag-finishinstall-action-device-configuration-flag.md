---
title: Marking a Device as having a Finish-Install Action to Perform
description: Marking a Device as having a Finish-Install Action to Perform
ms.assetid: 7f2560e6-94a7-4dd0-aa2a-e6cdd96c6d9b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Marking a Device as having a Finish-Install Action to Perform


An *installer* (a class installer, class co-installer, or device co-installer) indicates to Windows that it has finish-install actions to perform by setting the DI_FLAGSEX_FINISHINSTALL_ACTION flag when the installer processes a [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) request. This action will cause Windows to flag the device as needing to perform a finish install action. The steps are as follows:

1.  When an installer receives a [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) request, the installer sets the DI_FLAGSEX_FINISHINSTALL_ACTION flag if it has finish-install actions to perform.

    The installer then returns one of the following error codes:

    -   ERROR_DI_DO_DEFAULT if the installer is a class installer that has no finish-install wizard pages.
    -   NO_ERROR if the installer is a class installer that has finish-install wizard pages or a co-installer that either has or does not have finish-install wizard pages.

2.  If the DI_FLAGSEX_FINISHINSTALL_ACTION flag is set for a device after all installers have processed the [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) request for the device, Windows flags the device as needing to perform a finish install action.

 

 





