---
Description: This topics in this section describe the class drivers, generic client driver, and the parent composite driver that are provided by Microsoft.
title: Microsoft-provided USB drivers
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Microsoft-provided USB drivers


This topics in this section describe the class drivers, generic client driver, and the parent composite driver that are provided by Microsoft.

## Microsoft-provided USB drivers for controllers and hubs


Microsoft provides these set of drivers:

-   For USB host controllers and hubs. For more information, see [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md). You can develop a custom host controller driver that communicates with the USB host controller extension (UCX) driver. For more information, see [Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md).
-   For handling common function logic for USB devices. For more information, see [USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md).
-   For supporting Type-C connectors. For more information, see [USB connector manager class extension (UcmCx)](https://msdn.microsoft.com/library/windows/hardware/mt188011).

## <a href="" id="other-microsoft-provided-usb-drivers-"></a>Other Microsoft-provided USB drivers


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Device setup class</th>
<th>Microsoft-provided driver and INF</th>
<th>Windows support</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>USB</td>
<td><p>Usbccgp.sys</p>
<p>Usb.inf</p></td>
<td><p>Windows 8.1</p>
<p>Windows 8</p>
<p>Windows 7</p>
<p>Windows Vista</p>
<p>Windows XP</p></td>
<td>Usbccgp.sys is a parent driver for composite devices that supports multiple functions. For more information, see [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md).</td>
</tr>
<tr class="even">
<td>Biometric</td>
<td><p>WudfUsbBID.dll</p>
<p>WudfUsbBIDAdvanced.inf</p></td>
<td><p>Windows 8.1</p>
<p>Windows 8</p></td>
<td><p>Microsoft supports USB biometric devices (fingerprint readers) by providing the Windows Biometric Framework. See the [Windows Biometric Framework](https://msdn.microsoft.com/library/windows/hardware/ff536448).</p></td>
</tr>
<tr class="odd">
<td>Media Transfer Protocol Devices</td>
<td>Wpdusb.sys (Obsolete)</td>
<td><p>Windows Server 2008</p>
<p>Windows Vista</p>
<p>Windows Server 2003</p>
<p>Windows XP</p></td>
<td><div class="alert">
<strong>Note</strong>  
<p>Starting in Windows 7, Microsoft has replaced the kernel mode component of the Windows Vista USB driver stack (Wpdusb.sys) for Windows Portable Devices (WPD) with the generic Winusb.sys.</p>
</div>
<div>
 
</div>
<p>Microsoft provides the Wpdusb.sys driver to manage portable devices that support the Media Transfer Protocol. See [WPD Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff597864).</p></td>
</tr>
<tr class="even">
<td>USBDevice</td>
<td><p>Winusb.sys</p>
<p>Winusb.inf</p></td>
<td><p>Windows 8.1</p>
<p>Windows 8</p>
<p>Windows 7</p>
<p>Windows Vista</p>
<p>Windows XP with Service Pack 2 (SP2)</p></td>
<td>Winusb.sys can be used as the USB device's function driver instead of implementing a driver. See [WinUSB](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md).</td>
</tr>
</tbody>
</table>

 

## Microsoft-provided USB device class drivers


Microsoft provides drivers for several USB device classes approved by USB-IF. These drivers and their installation files are included in Windows. They are available in the \\Windows\\System32\\DriverStore\\FileRepository folder.

See, [USB device class drivers included in Windows](supported-usb-classes.md).

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  
[USB Driver Development Guide](usb-driver-development-guide.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Microsoft-provided%20USB%20drivers%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


