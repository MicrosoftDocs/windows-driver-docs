---
title: Obtaining the Parent of a Device in the Device Tree
description: Obtaining the Parent of a Device in the Device Tree
keywords:
- SetupAPI functions WDK , determining parents
- parent device determining WDK SetupAPI
- device parents WDK
- SP_DEVINFO_DATA
- connected sequence of ancestors WDK
- ancestors WDK
- immediate parents in device tree WDK
ms.date: 04/20/2017
---

# Obtaining the Parent of a Device in the Device Tree





This topic describes how to obtain an [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) structure for the parent of a device that has a device node (*devnode*) in the device tree.

**To obtain an SP_DEVINFO_DATA structure for the immediate parent of a device in the device tree**

1.  Verify that the device has a devnode in the [device tree](../kernel/device-tree.md) by calling [**CM_Get_DevNode_Status**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_status) for the device:
    -   If the device has a devnode, the function returns CR_SUCCESS.
    -   If the device does not have a devnode, the function returns CR_NO_SUCH_DEVINST.

2.  If the device has a devnode, call [**CM_Get_Parent**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_parent) to obtain a device instance handle for the parent of the device.

    (If a device does not have a devnode, **CM_Get_Parent** returns a device instance handle for the root device).

3.  Using the device instance handle for the parent device, call [**CM_Get_Device_ID**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_idw) to obtain the device instance ID for the parent device.

4.  Using the device instance ID for the parent device, call [**SetupDiOpenDeviceInfo**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendeviceinfoa) to obtain an SP_DEVINFO_DATA structure for the parent device.

**To obtain the SP_DEVINFO_DATA structures for a connected sequence of ancestors of a device in the device tree**

-   Starting with the device's immediate parent and ending with a given ancestor, call **CM_Get_Parent** repeatedly until all the handles are obtained. For each call to **CM_Get_Parent**, supply the device instance handle obtained from the previous call.

-   For each device instance handle that you obtain, first call **CM_Get_Device_ID** to obtain a device instance ID and then call **SetupDiOpenDeviceInfo** to obtain the SP_DEVINFO_DATA structure for the device.

For information about how to work with nonpresent devices, see [Determining the Parent of a Nonpresent Device](determining-the-parent-of-a-nonpresent-device.md).

 

