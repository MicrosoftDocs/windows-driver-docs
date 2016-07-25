---
title: Container IDs for 1394 Devices
description: Container IDs for 1394 Devices
ms.assetid: 667df2c6-bbbd-41da-b626-da493e316016
---

# Container IDs for 1394 Devices


The 1394 bus specification does not specify an internal hardware mechanism to indicate whether a device function is or is not removable from the 1394 host controller. The 1394 bus driver that is included with Windows marks every device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) as removable from the parent host controller.

If a single 1394 device exposes multiple device functions, each devnode that the bus driver enumerates is marked as removable. However, the 1394 bus driver that is included with Windows recognizes that each devnode originated from a single device and assigns the same container ID to each devnode. Therefore, each 1394 device receives a single device container object and is displayed as a single device in the Devices and Printers user interface (UI).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Container%20IDs%20for%201394%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




