---
title: Obtaining the Parent of a Device in the Device Tree
description: Obtaining the Parent of a Device in the Device Tree
ms.assetid: 0ac1ccbb-c926-4d14-975e-127159309361
keywords:
- SetupAPI functions WDK , determining parents
- parent device determining WDK SetupAPI
- device parents WDK
- SP_DEVINFO_DATA
- connected sequence of ancestors WDK
- ancestors WDK
- immediate parents in device tree WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Obtaining the Parent of a Device in the Device Tree





This topic describes how to obtain an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure for the parent of a device that has a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in the device tree.

**To obtain an SP_DEVINFO_DATA structure for the immediate parent of a device in the device tree**

1.  Verify that the device has a devnode in the [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194) by calling [**CM_Get_DevNode_Status**](https://msdn.microsoft.com/library/windows/hardware/ff538514) for the device:
    -   If the device has a devnode, the function returns CR_SUCCESS.
    -   If the device does not have a devnode, the function returns CR_NO_SUCH_DEVINST.

2.  If the device has a devnode, call [**CM_Get_Parent**](https://msdn.microsoft.com/library/windows/hardware/ff538610) to obtain a device instance handle for the parent of the device.

    (If a device does not have a devnode, **CM_Get_Parent** returns a device instance handle for the root device).

3.  Using the device instance handle for the parent device, call [**CM_Get_Device_ID**](https://msdn.microsoft.com/library/windows/hardware/ff538405) to obtain the device instance ID for the parent device.

4.  Using the device instance ID for the parent device, call [**SetupDiOpenDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff552071) to obtain an SP_DEVINFO_DATA structure for the parent device.

**To obtain the SP_DEVINFO_DATA structures for a connected sequence of ancestors of a device in the device tree**

-   Starting with the device's immediate parent and ending with a given ancestor, call **CM_Get_Parent** repeatedly until all the handles are obtained. For each call to **CM_Get_Parent**, supply the device instance handle obtained from the previous call.

-   For each device instance handle that you obtain, first call **CM_Get_Device_ID** to obtain a device instance ID and then call **SetupDiOpenDeviceInfo** to obtain the SP_DEVINFO_DATA structure for the device.

For information about how to work with nonpresent devices, see [Determining the Parent of a Nonpresent Device](determining-the-parent-of-a-nonpresent-device.md).

 

 





