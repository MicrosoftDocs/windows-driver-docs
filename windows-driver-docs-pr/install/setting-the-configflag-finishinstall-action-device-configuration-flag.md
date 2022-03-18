---
title: Marking a Device as having a Finish-Install Action to Perform
description: Marking a Device as having a Finish-Install Action to Perform
ms.date: 04/20/2017
---

# Marking a Device as having a Finish-Install Action to Perform

> [!NOTE]
> Features described in this section are not supported in universal or mobile driver packages. See [Using a Universal INF File](using-a-universal-inf-file.md).

An *installer* (a class installer, class co-installer, or device co-installer) indicates to Windows that it has finish-install actions to perform by setting the DI_FLAGSEX_FINISHINSTALL_ACTION flag when the installer processes a [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](./dif-newdevicewizard-finishinstall.md) request. This action will cause Windows to flag the device as needing to perform a finish install action. The steps are as follows:

1.  When an installer receives a [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](./dif-newdevicewizard-finishinstall.md) request, the installer sets the DI_FLAGSEX_FINISHINSTALL_ACTION flag if it has finish-install actions to perform.

    The installer then returns one of the following error codes:

    -   ERROR_DI_DO_DEFAULT if the installer is a class installer that has no finish-install wizard pages.
    -   NO_ERROR if the installer is a class installer that has finish-install wizard pages or a co-installer that either has or does not have finish-install wizard pages.

2.  If the DI_FLAGSEX_FINISHINSTALL_ACTION flag is set for a device after all installers have processed the [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](./dif-newdevicewizard-finishinstall.md) request for the device, Windows flags the device as needing to perform a finish install action.

 

