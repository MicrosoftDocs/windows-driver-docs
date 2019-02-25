---
title: WMI and the Power Management Tab
description: WMI and the Power Management Tab
ms.assetid: ff270fc0-806b-4014-ba9c-9c321a10c893
keywords: ["WMI WDK kernel , property sheets", "property sheets WDK WMI", "device property sheets WDK WMI", "power management WDK WMI", "property pages WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# WMI and the Power Management Tab





Drivers that support power management can automatically enable the **Power Management** tab for the device property sheet in Device Manager. If a driver handles the GUID\_POWER\_DEVICE\_ENABLE or GUID\_POWER\_DEVICE\_WAKE\_ENABLE WMI class GUIDs, Device Manager displays a **Power Management** tab on the device property sheet. Certain controls on the property page are enabled depending on which WMI class GUIDs the driver supports.

The GUID\_POWER\_DEVICE\_*XXX* class GUIDs enable controls on the property page as follows:

-   GUID\_POWER\_DEVICE\_ENABLE

    Enables a check box to activate or deactivate power management for the device. The data block for the WMI class consists of a single BOOLEAN value that indicates whether power management is enabled. The meaning of the value is device-dependent.

-   GUID\_POWER\_DEVICE\_WAKE\_ENABLE

    Enables a check box to activate or deactivate sending wait/wake IRPs. When selected, the driver should send an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) request to its physical device object. This enables the device to wake the system in response to an external event. For example, when enabled for the keyboard class driver, the keyboard device will wake the system when a key is pressed. When the check box is not selected, the driver should cancel the **IRP\_MN\_WAIT\_WAKE** request. The data block for the WMI class consists of a single BOOLEAN value that indicates the current state of the check box.

WMI query requests are sent for the GUID\_POWER\_DEVICE\_*XXX* WMI class GUIDs whenever the property sheet for the driver is opened in Device Manager. The WMI change requests are sent whenever one of the check box values on the **Power Management** tab changes. Users will expect the value they set to persist between driver loads and unloads, so drivers should store the current value of either property in the registry.

The mouse or keyboard class sample drivers both handle the GUID\_POWER\_DEVICE\_WAKE\_ENABLE WMI class GUID. See \\src\\input\\kbdclass and \\src\\input\\mouclass in the Windows Driver Kit (WDK).

 

 




