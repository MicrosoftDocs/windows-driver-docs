---
title: Obtaining the Parent of a Device in the Device Tree
description: Obtaining the Parent of a Device in the Device Tree
ms.assetid: 0ac1ccbb-c926-4d14-975e-127159309361
keywords: ["SetupAPI functions WDK , determining parents", "parent device determining WDK SetupAPI", "device parents WDK", "SP_DEVINFO_DATA", "connected sequence of ancestors WDK", "ancestors WDK", "immediate parents in device tree WDK"]
---

# Obtaining the Parent of a Device in the Device Tree


## <a href="" id="ddk-obtaining-the-parent-of-a-device-in-the-device-tree-dg"></a>


This topic describes how to obtain an [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure for the parent of a device that has a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in the device tree.

**To obtain an SP\_DEVINFO\_DATA structure for the immediate parent of a device in the device tree**

1.  Verify that the device has a devnode in the [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194) by calling [**CM\_Get\_DevNode\_Status**](https://msdn.microsoft.com/library/windows/hardware/ff538514) for the device:
    -   If the device has a devnode, the function returns CR\_SUCCESS.
    -   If the device does not have a devnode, the function returns CR\_NO\_SUCH\_DEVINST.

2.  If the device has a devnode, call [**CM\_Get\_Parent**](https://msdn.microsoft.com/library/windows/hardware/ff538610) to obtain a device instance handle for the parent of the device.

    (If a device does not have a devnode, **CM\_Get\_Parent** returns a device instance handle for the root device).

3.  Using the device instance handle for the parent device, call [**CM\_Get\_Device\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff538405) to obtain the device instance ID for the parent device.

4.  Using the device instance ID for the parent device, call [**SetupDiOpenDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff552071) to obtain an SP\_DEVINFO\_DATA structure for the parent device.

**To obtain the SP\_DEVINFO\_DATA structures for a connected sequence of ancestors of a device in the device tree**

-   Starting with the device's immediate parent and ending with a given ancestor, call **CM\_Get\_Parent** repeatedly until all the handles are obtained. For each call to **CM\_Get\_Parent**, supply the device instance handle obtained from the previous call.

-   For each device instance handle that you obtain, first call **CM\_Get\_Device\_ID** to obtain a device instance ID and then call **SetupDiOpenDeviceInfo** to obtain the SP\_DEVINFO\_DATA structure for the device.

For information about how to work with nonpresent devices, see [Determining the Parent of a Nonpresent Device](determining-the-parent-of-a-nonpresent-device.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Obtaining%20the%20Parent%20of%20a%20Device%20in%20the%20Device%20Tree%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




