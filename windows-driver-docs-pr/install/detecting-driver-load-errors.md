---
title: Detecting Driver Load Errors
description: Detecting Driver Load Errors
ms.assetid: 1233aa87-067e-4f58-add5-3737f8ddd358
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


To detect whether a driver loaded, check the status of the device in Device Manager. If the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) blocks a driver from loading because the driver is not correctly signed, the device status message will indicate that Windows could not load the driver and that the driver might be corrupted or missing. If this occurs, you can use [Code Integrity diagnostic system log events](code-integrity-diagnostic-system-log-events.md) to further diagnose the problem.

The following screen shot shows the type of device status message that indicates that Windows could not load a driver for a device and that the driver might be corrupted or missing.

![screen shot of an unsigned driver error message](images/signing-driver-load-error-message.png)

 

 





