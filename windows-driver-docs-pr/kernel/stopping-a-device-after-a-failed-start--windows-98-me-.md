---
title: Stopping a Device after a Failed Start (Windows 98/Me)
description: Stopping a Device after a Failed Start (Windows 98/Me)
ms.assetid: 373a1797-6479-4b99-b577-c74494f1774c
keywords: ["failed starts WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Stopping a Device after a Failed Start (Windows 98/Me)





On Windows 98/Me, the PnP manager issues an [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) request without a preceding query when the drivers for a device fail an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request. (On Windows 2000 and later, the PnP manager sends remove IRPs in this situation. See [Understanding When Remove IRPs Are Issued](understanding-when-remove-irps-are-issued.md).)

In response to the stop IRP, drivers release the device's hardware resources (such as its I/O ports), disable and deregister any user-mode interfaces, and fail any incoming I/O requests that require access to the device.

 

 




