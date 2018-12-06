---
title: Handling Stop IRPs (Windows 2000 and Later)
description: Handling Stop IRPs (Windows 2000 and Later)
ms.assetid: 5148ca15-07f0-4a93-aa65-45b13184184b
keywords: ["stop IRPs WDK PnP", "IRPs WDK PnP", "I/O request packets WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling Stop IRPs (Windows 2000 and Later)





Drivers that run only on Windows 2000 and later versions of Windows (WDM versions 0x10 and greater) receive stop IRPs only when the PnP manager rebalances resources. The following sections describe techniques such drivers should use in handling stop IRPs:

[Handling an IRP\_MN\_QUERY\_STOP\_DEVICE Request (Windows 2000 and later)](handling-an-irp-mn-query-stop-device-request--windows-2000-and-later-.md)

[Handling an IRP\_MN\_STOP\_DEVICE Request (Windows 2000 and later)](handling-an-irp-mn-stop-device-request--windows-2000-and-later-.md)

[Handling an IRP\_MN\_CANCEL\_STOP\_DEVICE Request (Windows 2000 and later)](handling-an-irp-mn-cancel-stop-device-request--windows-2000-and-later-.md)

[Holding Incoming IRPs When A Device Is Paused](holding-incoming-irps-when-a-device-is-paused.md)

WDM drivers that also run on Windows 98/Me must handle these IRPs differently. See [Handling Stop IRPs (Windows 98/Me)](handling-stop-irps--windows-98-me-.md) for details.

 

 




