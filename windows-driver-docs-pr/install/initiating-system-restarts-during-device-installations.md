---
title: Initiating System Restarts During Device Installations
description: Initiating System Restarts During Device Installations
ms.assetid: 52db2894-e759-4382-97de-5db7f268ff59
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Initiating System Restarts During Device Installations


In the rare cases in which it is necessary for the system to be restarted to complete a device installation, use the following rules:

-   During initial installations, a device's installer or co-installer can request a system restart by setting DI_NEEDRESTART in the [**SP_DEVINSTALL_PARAMS**](/windows/win32/api/setupapi/ns-setupapi-sp_devinstall_params_a) structure, which is received along with [device installation function codes](/previous-versions/ff541307(v=vs.85)). (This should not be done unless absolutely necessary.)

-   During update installations, a device's installation application can call [**UpdateDriverForPlugAndPlayDevices**](/windows/desktop/api/newdev/nf-newdev-updatedriverforplugandplaydevicesa), which determines whether a system restart is necessary.

 

