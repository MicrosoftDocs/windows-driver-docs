---
title: WMI and the Power Management Tab
author: windows-driver-content
description: WMI and the Power Management Tab
MS-HAID:
- 'WMI\_5132950f-fd47-4b38-8f9f-ff044088d200.xml'
- 'kernel.wmi\_and\_the\_power\_management\_tab'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ff270fc0-806b-4014-ba9c-9c321a10c893
keywords: ["WMI WDK kernel , property sheets", "property sheets WDK WMI", "device property sheets WDK WMI", "power management WDK WMI", "property pages WDK WMI"]
---

# WMI and the Power Management Tab


## <a href="" id="ddk-wmi-and-the-power-management-tab-kg"></a>


Drivers that support power management can automatically enable the **Power Management** tab for the device property sheet in Device Manager. If a driver handles the GUID\_POWER\_DEVICE\_ENABLE or GUID\_POWER\_DEVICE\_WAKE\_ENABLE WMI class GUIDs, Device Manager displays a **Power Management** tab on the device property sheet. Certain controls on the property page are enabled depending on which WMI class GUIDs the driver supports.

The GUID\_POWER\_DEVICE\_*XXX* class GUIDs enable controls on the property page as follows:

-   GUID\_POWER\_DEVICE\_ENABLE

    Enables a check box to activate or deactivate power management for the device. The data block for the WMI class consists of a single BOOLEAN value that indicates whether power management is enabled. The meaning of the value is device-dependent.

-   GUID\_POWER\_DEVICE\_WAKE\_ENABLE

    Enables a check box to activate or deactivate sending wait/wake IRPs. When selected, the driver should send an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) request to its physical device object. This enables the device to wake the system in response to an external event. For example, when enabled for the keyboard class driver, the keyboard device will wake the system when a key is pressed. When the check box is not selected, the driver should cancel the **IRP\_MN\_WAIT\_WAKE** request. The data block for the WMI class consists of a single BOOLEAN value that indicates the current state of the check box.

WMI query requests are sent for the GUID\_POWER\_DEVICE\_*XXX* WMI class GUIDs whenever the property sheet for the driver is opened in Device Manager. The WMI change requests are sent whenever one of the check box values on the **Power Management** tab changes. Users will expect the value they set to persist between driver loads and unloads, so drivers should store the current value of either property in the registry.

The mouse or keyboard class sample drivers both handle the GUID\_POWER\_DEVICE\_WAKE\_ENABLE WMI class GUID. See \\src\\input\\kbdclass and \\src\\input\\mouclass in the Windows Driver Kit (WDK).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20WMI%20and%20the%20Power%20Management%20Tab%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


