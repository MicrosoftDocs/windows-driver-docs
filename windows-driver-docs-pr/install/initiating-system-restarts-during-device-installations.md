---
title: Initiating System Restarts During Device Installations
description: Initiating System Restarts During Device Installations
ms.assetid: 52db2894-e759-4382-97de-5db7f268ff59
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initiating System Restarts During Device Installations


In the rare cases in which it is necessary for the system to be restarted to complete a device installation, use the following rules:

-   During initial installations, a device's installer or co-installer can request a system restart by setting DI_NEEDRESTART in the [**SP_DEVINSTALL_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff552346) structure, which is received along with [device installation function codes](https://msdn.microsoft.com/library/windows/hardware/ff541307). (This should not be done unless absolutely necessary.)

-   During update installations, a device's installation application can call [**UpdateDriverForPlugAndPlayDevices**](https://msdn.microsoft.com/library/windows/hardware/ff553534), which determines whether a system restart is necessary.

 

 





