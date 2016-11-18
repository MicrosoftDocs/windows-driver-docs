---
title: Devices Using WDF Tab
description: This topic discusses WDF Verifier's Devices using WDF page.
ms.assetid: 06144cf4-bb6f-4b5b-ac0d-f4fae89a04a9
keywords: ["WDF Verifier WDK , managing KMDF settings", "KMDF verifier settings WDK WDF"]
---

# Devices Using WDF Tab


This topic discusses WDF Verifier's **Devices using WDF** page. This page lists all devices that are using WDF drivers. When you highlight a device, you see the WDF driver stack for the highlighted device. You can also change verification settings from this screen.

At the top of this page, you'll find a summary of installed runtimes and drivers. Below is a list of device instances that are associated with WDF drivers.

![screen grab of devices using wdf tab](images/wdfverifier-tab2.png)

In the **Devices with WDF drivers** box, devices that have WDF-related settings are preceded by a +. To change settings, right-click the device ID or the individual settings within the node.

When you select a device or individual setting, the device's friendly name appears to the right of the box.

In addition, all of the WDF drivers for that device are shown in the **WDF Driver Stack For This Device** box, in stack order from top to bottom. For example, upper filters appear at the top, followed by the function driver and then lower filters.

If UMDF drivers are used, they are also shown in stack order at the correct location in the kernel device stack.

Similarly, you can click the + in the driver stack to open the node, and then right-click to change values for each driver.

If you make changes on the **Devices using WDF** page, you'll see those changes reflected on the **WDF Drivers** page.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Devices%20Using%20WDF%20Tab%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




