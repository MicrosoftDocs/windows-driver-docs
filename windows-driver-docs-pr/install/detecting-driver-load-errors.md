---
title: Detecting Driver Load Errors
description: Detecting Driver Load Errors
keywords:
- driver load errors WDK driver signing
- errors WDK driver signing
- detecting driver loaded
- load errors WDK driver signing
- status information WDK driver signing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Detecting Driver Load Errors


To detect whether a driver loaded, check the status of the device in Device Manager. If the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) blocks a driver from loading because the driver is not correctly signed, the device status message will indicate that Windows could not load the driver and that the driver might be corrupted or missing. If this occurs, you can use [Code Integrity diagnostic system log events](code-integrity-diagnostic-system-log-events.md) to further diagnose the problem. For more info on code 52, see [CM_PROB_UNSIGNED_DRIVER](cm-prob-unsigned-driver.md).

For a full list of errors reported by Device Manager, see [Device Manager Error Messages](device-manager-error-messages.md).

For additional information that may help with the problem code, see [**DEVPKEY_Device_ProblemStatus**](devpkey-device-problemstatus.md).

