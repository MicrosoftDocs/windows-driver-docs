---
title: PnPUtil Return Values
description: PnPUtil Return Values
ms.assetid: c26ecf54-b3d4-4559-9ec1-ff535cf03d77
ms.author: windowsdriverdev
ms.date: 02/08/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PnPUtil Return Values


The following table includes some of the more common values that the PnPUtil tool returns:

* `ERROR_SUCCESS` (0): The requested operation completed successfully.
* `ERROR_SUCCESS_REBOOT_REQUIRED` (3010): The requested operation completed successfully and a system reboot is required.  For example, if the  `/install /add-driver` options were specified, one or more devices were successfully installed and a system reboot is required to finalize installation.
* `ERROR_SUCCESS_REBOOT_INITIATED` (1641): The operation was successful and a system reboot is underway because the `/reboot` option was specified.

While you can still use PnPUtil to bulk install drivers, to get actionable return values we recommend specifying `/install /add-driver` with one INF at a time.
