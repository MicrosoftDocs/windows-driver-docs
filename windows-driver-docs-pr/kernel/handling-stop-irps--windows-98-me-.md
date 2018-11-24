---
title: Handling Stop IRPs (Windows 98/Me)
description: Handling Stop IRPs (Windows 98/Me)
ms.assetid: 98eefb69-e321-4cc5-8b4d-79335cd8b06e
keywords: ["stop IRPs WDK PnP", "IRPs WDK PnP", "I/O request packets WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling Stop IRPs (Windows 98/Me)





On Windows 98/Me, the PnP manager can send stop IRPs for the following reasons:

-   To pause the device while rebalancing resources

-   To stop the device when Device Manager disables it

-   To stop the device after a failed [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request

A driver cannot determine from the IRP why it was sent. Consequently, WDM drivers that run on Windows 98/Me must handle all stop IRPs as if the device were being disabled. In short, this means that such drivers fail incoming I/O requests rather than queuing them (as on Windows 2000 and later).

The following topics provide step-by-step details on handling each of the stop IRPs:

[Handling an IRP\_MN\_QUERY\_STOP\_DEVICE Request (Windows 98/Me)](handling-an-irp-mn-query-stop-device-request--windows-98-me-.md)

[Handling an IRP\_MN\_STOP\_DEVICE Request (Windows 98/Me)](handling-an-irp-mn-stop-device-request--windows-98-me-.md)

[Handling an IRP\_MN\_CANCEL\_STOP\_DEVICE Request (Windows 98/Me)](handling-an-irp-mn-cancel-stop-device-request--windows-98-me-.md)

 

 




