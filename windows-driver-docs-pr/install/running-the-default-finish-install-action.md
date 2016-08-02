---
title: Running the Default Finish-Install Action
description: Running the Default Finish-Install Action
ms.assetid: a66d418e-9a66-4c11-854d-6e597ffa01f7
---

# Running the Default Finish-Install Action


In Windows 7, the default finish-install action is provided by the system-supplied [**SetupDiFinishInstallAction**](https://msdn.microsoft.com/library/windows/hardware/ff551022) function.

If a device does not have a class installer, or a class installer returns ERROR\_DI\_DO\_DEFAULT in response to a [**DIF\_FINISHINSTALL\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request, Windows calls **SetupDiFinishInstallAction** after all the installers for a device complete their finish-install actions.

In Windows 8 and later versions, there are no default finish-install actions.

 

 





