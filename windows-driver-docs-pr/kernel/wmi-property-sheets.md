---
title: WMI Property Sheets
description: WMI Property Sheets
ms.assetid: cc521aff-362a-4064-adea-f6f3cf8a1c10
keywords: ["WMI WDK kernel , property sheets", "property sheets WDK WMI", "device property sheets WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# WMI Property Sheets





A user-friendly driver allows users to control its settings through its **Device Manager** property sheet. See [Using Device Manager](https://msdn.microsoft.com/library/windows/hardware/ff553570) for a description of Device Manager.

Drivers can automatically expose any WMI classes they implement on their property sheet by using the [WMI generic property page provider](wmi-generic-property-page-provider.md).

Drivers can enable certain controls on the **Power Management** tab of the **Device Manager** property sheet by supporting certain particular WMI class GUIDs. See [WMI and the Power Management Tab](wmi-and-the-power-management-tab.md) for details.

 

 




