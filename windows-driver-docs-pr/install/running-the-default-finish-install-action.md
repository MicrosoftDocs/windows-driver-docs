---
title: Running the Default Finish-Install Action
description: Running the Default Finish-Install Action
ms.date: 04/20/2017
---

# Running the Default Finish-Install Action


In Windows 7, the default finish-install action is provided by the system-supplied [**SetupDiFinishInstallAction**](/previous-versions/windows/hardware/previsioning-framework/ff551022(v=vs.85)) function.

If a device does not have a class installer, or a class installer returns ERROR_DI_DO_DEFAULT in response to a [**DIF_FINISHINSTALL_ACTION**](./dif-finishinstall-action.md) request, Windows calls **SetupDiFinishInstallAction** after all the installers for a device complete their finish-install actions.

In Windows 8 and later versions, there are no default finish-install actions.

 

