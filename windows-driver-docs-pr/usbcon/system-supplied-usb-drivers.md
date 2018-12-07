---
Description: This topics in this section describe the class drivers, generic client driver, and the parent composite driver that are provided by Microsoft.
title: Microsoft-provided USB drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Microsoft-provided USB drivers


This topics in this section describe the class drivers, generic client driver, and the parent composite driver that are provided by Microsoft.

## Microsoft-provided USB drivers for controllers and hubs


Microsoft provides these set of drivers:

-   For USB host controllers and hubs. For more information, see [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md). You can develop a custom host controller driver that communicates with the USB host controller extension (UCX) driver. For more information, see [Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md).
-   For handling common function logic for USB devices. For more information, see [USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md).
-   For supporting Type-C connectors. For more information, see [USB connector manager class extension (UcmCx)](https://msdn.microsoft.com/library/windows/hardware/mt188011).

## Other Microsoft-provided USB drivers


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
<td><p>Windows 8.1</p>
<p>Windows 8</p>
<p>Windows 7</p>
<p>Windows Vista</p>
<p>Windows XP</p></td>
<td>Usbccgp.sys is a parent driver for composite devices that supports multiple functions. For more information, see <a href="usb-common-class-generic-parent-driver.md" data-raw-source="[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)">USB Generic Parent Driver (Usbccgp.sys)</a>.</td>
</tr>
<tr class="even">
<td>Biometric</td>
<td><p>WudfUsbBID.dll</p>
<p>WudfUsbBIDAdvanced.inf</p></td>
<td><p>Windows 8.1</p>
<p>Windows 8</p></td>
<td><p>Microsoft supports USB biometric devices (fingerprint readers) by providing the Windows Biometric Framework. See the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536448" data-raw-source="[Windows Biometric Framework](https://msdn.microsoft.com/library/windows/hardware/ff536448)">Windows Biometric Framework</a>.</p></td>
</tr>
<tr class="odd">
<td>Media Transfer Protocol Devices</td>
<td>Wpdusb.sys (Obsolete)</td>
<td><p>Windows Server 2008</p>
<p>Windows Vista</p>
<p>Windows Server 2003</p>
<p>Windows XP</p></td>
<td><div class="alert">
<strong>Note</strong><br/><p>Starting in Windows 7, Microsoft has replaced the kernel mode component of the Windows Vista USB driver stack (Wpdusb.sys) for Windows Portable Devices (WPD) with the generic Winusb.sys.</p>
</div>
<div>

</div>
<p>Microsoft provides the Wpdusb.sys driver to manage portable devices that support the Media Transfer Protocol. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff597864" data-raw-source="[WPD Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff597864)">WPD Design Guide</a>.</p></td>
</tr>
<tr class="even">
<td>USBDevice</td>
<td><p>Winusb.sys</p>
<p>Winusb.inf</p></td>
<td><p>Windows 8.1</p>
<p>Windows 8</p>
<p>Windows 7</p>
<p>Windows Vista</p>
<p>Windows XP with Service Pack 2 (SP2)</p></td>
<td>Winusb.sys can be used as the USB device&#39;s function driver instead of implementing a driver. See <a href="how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md" data-raw-source="[WinUSB](how-to-write-a-windows-desktop-app-that-communicates-with-a-usb-device.md)">WinUSB</a>.</td>
</tr>
</tbody>
</table>



## Microsoft-provided USB device class drivers


Microsoft provides drivers for several USB device classes approved by USB-IF. These drivers and their installation files are included in Windows. They are available in the \\Windows\\System32\\DriverStore\\FileRepository folder.

See, [USB device class drivers included in Windows](supported-usb-classes.md).

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  
[USB Driver Development Guide](usb-driver-development-guide.md)  



