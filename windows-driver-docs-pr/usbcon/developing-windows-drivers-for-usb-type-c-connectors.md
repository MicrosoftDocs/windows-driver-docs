---
Description: You need to write a driver for the connector if your USB Type-C system does not include an embedded controller, otherwise you can load the Microsoft-provided UCSI driver.
title: Developing Windows drivers for USB Type-C connectors
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Developing Windows drivers for USB Type-C connectors


**Intended audience**

-   Driver development guidance for a USB Type-C system does not include an embedded controller.

**Last Updated**

-   March 2016

**Windows version**

-   Windows 10 for desktop editions (Home, Pro, Enterprise, and Education)
-   Windows 10 Mobile

**Important APIs**

-   [UCmCx client driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188011)

You need to write a driver for the connector if your USB Type-C system does not include an embedded controller, otherwise you can load the Microsoft-provided [UCSI driver](ucsi.md).

![drivers](images/drivers-c.png)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Architecture: USB Type-C design for a Windows system](architecture--usb-type-c-in-a-windows-system.md)</p></td>
<td><p>Describes a typical hardware design of a USB Type-C system and the Microsoft-provided drivers that support the hardware components.</p></td>
</tr>
<tr class="even">
<td><p>[Bring up the function controller on a USB Type-C Windows system](function-controller-bringup-for-a-usb-type-c-system.md)</p></td>
<td><p>The driver for the function controller informs the operating system about the charging levels that its USB Type-C connector supports and notifies the battery subsystem when it can begin charging and the maximum amount of current the device can draw.</p></td>
</tr>
<tr class="odd">
<td><p>[Bring up the dual-role controller for a USB Type-C Windows system](dual-role-controller-bringup-for-a-usb-type-c-system.md)</p></td>
<td><p>The USB role-switch drivers (URS) are a set of WDF class extension and its client driver that handles the role-switching capability of a dual-role controller. If your system has a dual role controller, you can switch the role of the system depending on the device that is attached to the partner port of the USB Type-C connector of the system. This allows interesting scenarios such as wired docking.</p></td>
</tr>
<tr class="even">
<td><p>[Write a USB Type-C connector driver](bring-up-a-usb-type-c-connector-on-a-windows-system.md)</p></td>
<td><p>Describes the USB connector manager (UCM) that manages a USB Type-C connector and the expected behavior of a connector driver.</p></td>
</tr>
</tbody>
</table>

 

**Related sections**

<a href="" id="write-a-usb-role-switch--urs--client-driver"></a>Write a USB role-switch (URS) client driver  
[USB Dual Role Driver Stack Architecture](usb-dual-role-driver-stack-architecture.md)

[USB dual-role controller driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt628026)

<a href="" id="write-a-usb-function-client-driver"></a>Write a USB function client driver  
[Developing Windows drivers for USB function controllers](developing-windows-drivers-for-usb-function-controllers.md)

[USB function controller programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188013)

## Related topics
[Windows support for USB Type-C connectors](oem-tasks-for-bringing-up-a-usb-typec.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Developing%20Windows%20drivers%20for%20USB%20Type-C%20connectors%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


