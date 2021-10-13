---
title: DeviceID command
description: The DeviceID command returns the function discovery key.
keywords:
- WSDMON port monitors WDK , DeviceID command
- DeviceID
ms.date: 09/07/2021
ms.localizationpriority: medium
---

# DeviceID command

The **DeviceID** command returns the device identifier (ID) in the form of the function discovery key, **PKEY_PNPX_GlobalIdentity**.

This key returns the universally unique ID (UUID) of the root device. The output buffer contains a NULL-terminated string that represents the UUID.
