---
ms.assetid: ACD6E5C3-5CE5-4C3F-BA44-1C87C39EF3C4
title: Driver convergence model for Windows 10
description: To make your device work on Windows and Windows Phone releases before Windows 10, you probably needed to write two separate drivers, for example one for Windows 8.1 and one for Windows Phone 8.1.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver convergence model for Windows 10

To make your device work on Windows and Windows Phone releases before Windows 10, you probably needed to write two separate drivers, for example one for Windows 8.1 and one for Windows Phone 8.1. In Windows 10, in most cases, you can write one driver that will run on any Windows 10 version. This topic describes convergence plans for device driver interfaces in Windows 10 and provides details when there are version-specific differences. It answers these questions:

-   For legacy drivers, will a Windows 8.1 driver work on Windows 10 for desktop editions (Home, Pro, and Enterprise) and/or Windows 10 Mobile?
-   For new drivers, can I build one driver with the Windows 10 kit that will work on Windows 10 for desktop editions and Windows 10 Mobile?

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Technology</th>
<th align="left">Windows 8.1 driver binary runs on Windows 10?</th>
<th align="left">Changes for Windows 10</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Audio</td>
<td align="left">Yes</td>
<td align="left"><p>Starting in Windows 10, you can write a Kernel-Mode Driver Framework (KMDF) audio driver that calls KMDF interfaces for PnP, power management, and idle management. For I/O handling, a KMDF audio driver should not use the I/O queue functionality in WDF, but should instead use the existing COM interfaces provided by PortClass. However, your driver can use the framework&#39;s support for timers, interrupts, DMA, and remote I/O targets. KMDF audio drivers work on both Windows 10 for desktop editions and Windows 10 Mobile.</p>
<p>Existing Windows 8.1 drivers that link to PortClass continue to work on Windows 10 for desktop editions and Windows 10 Mobile.</p></td>
</tr>
<tr class="even">
<td align="left">Biometric</td>
<td align="left">Yes</td>
<td align="left"><p>The Windows Biometric Framework (WBF) is available in both Windows 10 for desktop editions and Windows 10 Mobile.</p>
<p>If you are developing a new biometric driver for Windows 10 Mobile, you can use a Windows 8.1 WBF driver as a starting point.</p></td>
</tr>
<tr class="odd">
<td align="left">Bluetooth</td>
<td align="left">Yes</td>
<td align="left"><p>In Windows 10, the Bluetooth transport driver interface for all devices is converged and uses a universal Bluetooth driver model. You can write a single driver that runs on all Windows device platforms.</p>
<p>The Bluetooth audio driver surface area is diverged for Windows 10 and allows the following two options:</p>
<ul>
<li>You can write a new universal audio driver that works for both desktop and mobile devices.</li>
<li>An existing Windows Phone 8.1 Bluetooth audio driver will run on Windows 10 Mobile.</li>
</ul></td>
</tr>
<tr class="even">
<td align="left">Camera</td>
<td align="left">Yes</td>
<td align="left"><p>Features previously available in Windows Phone 8.1 (such as auto focus and HFR) will be available in both Windows 10 for desktop editions and Windows 10 Mobile. Legacy camera drivers from Windows 8.1 will require modifications to take advantage of these features.</p></td>
</tr>
<tr class="odd">
<td align="left">Cellular</td>
<td align="left">Yes</td>
<td align="left"><p>Windows 10 continues to support MBIM 1.0 (Mobile Broadband Interface Model) for data cards on PCs.</p>
<p>Equivalent cellular and wi-fi connection management using converged stack. Mobile operators can use Open Mobile Alliance Device Management (OMA DM) configuration of cellular settings in both Windows 10 for desktop editions and Windows 10 Mobile. Also, OEMs will have access to Multivariant provisioning in both Windows 10 for desktop editions and Windows 10 Mobile, while the Mobile Broadband Account Experience (MBAE) will still be available in Windows 10 for desktop editions.</p></td>
</tr>
<tr class="even">
<td align="left">Display</td>
<td align="left">Yes</td>
<td align="left"><p>Already converged. Windows Display Driver Model (WDDM) 1.3 runs on Windows 8.1 and Windows Phone 8.1. WDDM 1.3 continues to be supported in Windows 10. WDDM 2.0 is new for Windows 10. To use Direct3D (D3D) 12 runtime and features, must have a WDDM 2.0 driver.</p></td>
</tr>
<tr class="odd">
<td align="left">Location</td>
<td align="left">Yes</td>
<td align="left"><p>New GNSS (Global Navigation Satellite System) adapter DDI for Windows 10.</p>
<p>Windows 8.1 sensor will be supported using a GNSS legacy PE.</p></td>
</tr>
<tr class="even">
<td align="left">NFC</td>
<td align="left">Yes</td>
<td align="left"><p>New Windows 10 DDI for Smart card, Radio Manager, SE.</p>
<p>A Windows 8.1 NFC driver continues to work, but cannot take advantage of the new features.</p></td>
</tr>
<tr class="odd">
<td align="left">Sensor</td>
<td align="left">Yes</td>
<td align="left"><p>New drivers for Windows 10 can write a User-Mode Driver Framework (UMDF) 2.<em>x</em> driver that uses common sensor stack (similar to Windows Phone 8.1 model) and same driver package works on Windows 10 for desktop editions and Windows 10 Mobile.</p>
<p>Windows 8.1 sensor class extension uses UMDF 1. Windows Phone 8.1 sensor class extension uses UMDF 2. For Windows 10, new sensor class extension uses UMDF 2 like Windows Phone 8.1. To build using Windows 10 kit, must use latter. Driver binary from Windows 8.1 still runs on Windows 10. HID class driver still inbox for Windows 10, no vendor-supplied driver and no firmware changes required if you use the defined existing HID types from Windows 8.1.</p></td>
</tr>
<tr class="even">
<td align="left">Touch/Precision Touchpad (PTP)</td>
<td align="left">Yes</td>
<td align="left"><p>In Windows 10, both HID and touch miniport drivers will be supported. Vendors can update a legacy HID driver or implement a new touch miniport driver.</p>
<p>For Windows 10 Mobile, bus restrictions removed, no longer limited to USB, I2C. Current class drivers remain in place, any other bus requires HID miniport driver. Can provide a filter driver to support custom gestures.</p></td>
</tr>
<tr class="odd">
<td align="left">USB</td>
<td align="left">Yes</td>
<td align="left"><p>Windows 8.1 provides a host controller stack. Windows 10 adds a function stack that allows the device with a host controller (PC/tablet/phone) to work as a peripheral device.</p></td>
</tr>
<tr class="even">
<td align="left">Windows Driver Frameworks (WDF)</td>
<td align="left">Yes</td>
<td align="left"><p>Windows 10 ships with KMDF 1.15, UMDF 2.15, UMDF 1.11, and earlier framework versions. Windows 10 Mobile also ships with KMDF 1.15, UMDF 2.15, and earlier framework versions. Note that UMDF version 1 is not available in Windows 10 Mobile. Only KMDF and UMDF version 2 can be used to write <a href="getting-started-with-universal-drivers.md" data-raw-source="[Universal Windows drivers](getting-started-with-universal-drivers.md)">Universal Windows drivers</a>.</p></td>
</tr>
<tr class="odd">
<td align="left">WLAN</td>
<td align="left">Yes</td>
<td align="left"><p>WDI (WLAN Device Driver Interface) is the new universal WLAN driver model for Windows 10. WLAN device manufacturers can write a single WDI miniport driver that runs on all device platforms, and requires less code than the previous native WLAN driver model. All new WLAN features introduced in Windows 10 require WDI-based drivers.</p>
<p>Vendor-supplied native WLAN drivers continue to work in Windows 10, but functionality is limited to the version of Windows for which they were developed.</p></td>
</tr>
</tbody>
</table>

 

 

 





