---
title: WMI Property Sheets
author: windows-driver-content
description: WMI Property Sheets
ms.assetid: cc521aff-362a-4064-adea-f6f3cf8a1c10
keywords: ["WMI WDK kernel , property sheets", "property sheets WDK WMI", "device property sheets WDK WMI"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WMI Property Sheets


## <a href="" id="ddk-wmi-property-sheets-kg"></a>


A user-friendly driver allows users to control its settings through its **Device Manager** property sheet. See [Using Device Manager](https://msdn.microsoft.com/library/windows/hardware/ff553570) for a description of Device Manager.

Drivers can automatically expose any WMI classes they implement on their property sheet by using the [WMI generic property page provider](wmi-generic-property-page-provider.md).

Drivers can enable certain controls on the **Power Management** tab of the **Device Manager** property sheet by supporting certain particular WMI class GUIDs. See [WMI and the Power Management Tab](wmi-and-the-power-management-tab.md) for details.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20WMI%20Property%20Sheets%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


