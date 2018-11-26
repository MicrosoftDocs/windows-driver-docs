---
title: Vendor-Extended Events
description: Vendor-Extended Events
ms.assetid: 00131b75-3b15-46f8-b4da-1e1593afb3c0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Vendor-Extended Events





Vendor-extended events are defined in the **DeviceData** and **Events** INF file sections (see the example in [Vendor-Extended Features](vendor-extended-features.md)). An **EventCode** entry lists all the event codes, separated by commas. For each event code, an entry of the form **EventCode***XXXX* should exist, where XXXX is the PTP event code in uppercase hexadecimal. The entry should list the WIA GUID code to send when the event code is received by the driver.

Display names of events should be declared in the **Events** section. For each event, there must be an **EventCode***XXXX* entry, containing the event name in quotes, the event GUID, and the application to be launched when the event occurs, all separated by commas. If an asterisk is used in place of the application name, the registered application name is used. See [INF Files for WIA Devices](inf-files-for-wia-devices.md) for more information. An application can use the **IWiaDevMgr::RegisterEventCallback***Xxx* methods (described in the Microsoft Windows SDK documentation) to receive the events. Currently, the parameters from the event cannot be passed to the application.

 

 




