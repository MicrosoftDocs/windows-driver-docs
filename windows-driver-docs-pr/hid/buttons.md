---
title: HID button drivers
description: Use the Microsoft-provided button driver for GPIO buttons; otherwise, implement your driver that injects HID data to the operating system.
ms.assetid: FBA8141D-8DBA-4C68-8BB5-44B3EDB7D062
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HID button drivers


**Summary**

-   [Describe a GPIO button in ACPI and load Microsoft-provided driver](acpi-button-device.md)
-   [Write a HID source driver in kernel mode for non-GPIO button](virtual-hid-framework--vhf-.md)
-   [Write a UMDF HID Minidriver for a non-GPIO button](https://msdn.microsoft.com/library/windows/hardware/hh439579)

**Applies to**

-   Windows 10
-   Driver developers of HID button devices

**Important APIs**

-   [Virtual HID Framework Reference](https://msdn.microsoft.com/library/windows/hardware/dn925048)
-   [UMDF HID Minidriver IOCTLs](https://msdn.microsoft.com/library/windows/hardware/hh463977)

Use the Microsoft-provided button driver for GPIO buttons; otherwise, implement your driver that injects HID data to the operating system.

Buttons (Power, Windows, volume and rotation lock) are typically used for tasks that occur while the physical keyboard is not available to the user, on form factors such as convertibles or slates. Buttons declare themselves to the operating system as HID devices by supplying [HID button report descriptors](https://msdn.microsoft.com/library/windows/hardware/dn457881). This allows the system to interpret the purpose and events of those buttons in a standardized way. When a button state changes, that event is mapped to a [HID Usages](hid-usages.md). A HID transport minidriver reports those events to upper-level drivers that then send details to HID clients in user mode or kernel mode.

For physical general-purpose I/O (GPIO) buttons, the HID transport minidriver is a Microsoft-provided in-box driver that reports the events based on the interrupts that are received on the defined GPIO hardware resources.

The in-box driver cannot service a button that is not wired to an interrupt line. For such buttons, you need to write a driver that exposes the button as a HID button and reports state changes to the HID class driver (Microsoft-provided). Your driver could be a HID source driver or a HID transport driver.

## Guidance for supporting HID buttons


Here are some general pointers to help you decide which implementation you should follow if you are creating HID buttons.

![decision chart for implementing buttons](images/button.png)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Use the Microsoft-provided in-box button driver</strong></p>
<p><img src="images/hid-acpi.png" alt="ACPI description of a HID button" /></p></td>
<td><p>If you are implementing a GPIO button, describe the button in the system ACPI so that Windows can load the in-box driver, Hidinterrupt.sys, as the button driver that reports events to the operating system.</p>
<ul>
<li><a href="acpi-button-device.md" data-raw-source="[ACPI button device](acpi-button-device.md)">ACPI button device</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/dn457871(v=vs.85).aspx" data-raw-source="[Button Behavior](https://msdn.microsoft.com/library/windows/hardware/dn457871(v=vs.85).aspx)">Button Behavior</a></li>
<li><a href="acpi-button-device.md#acpi-button-phone" data-raw-source="[Sample buttons ACPI for phone/tablet](acpi-button-device.md#acpi-button-phone)">Sample buttons ACPI for phone/tablet</a></li>
<li><a href="acpi-button-device.md#acpi-button-desktop" data-raw-source="[Sample buttons ACPI for desktop](acpi-button-device.md#acpi-button-desktop)">Sample buttons ACPI for desktop</a></li>
</ul>
<p>Microsoft encourages you to use the in-box transport-minidrivers whenever possible.</p></td>
</tr>
<tr class="even">
<td><p><strong>Write a HID source driver in kernel mode</strong></p>
<p><img src="images/hid-vhf.png" alt="Buttons using Virtual HID Framework" /></p></td>
<td><p>If you are implementing a non-GPIO button such as a stream of data in the HID format that needs to be injected by another software component, you can choose to write a kernel-mode driver. Starting in Windows 10, you can write a HID source driver by calling programming interfaces that communicate with Virtual HID Framework (VHF) and gets and sets HID Reports to and from the HID class driver.</p>
<ul>
<li><a href="virtual-hid-framework--vhf-.md" data-raw-source="[How to write a HID source driver that interacts with Virtual HID Framework (VHF)](virtual-hid-framework--vhf-.md)">How to write a HID source driver that interacts with Virtual HID Framework (VHF)</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/dn925048" data-raw-source="[Virtual HID Framework Reference](https://msdn.microsoft.com/library/windows/hardware/dn925048)">Virtual HID Framework Reference</a></li>
</ul>
<p>Alternately, you can write a kernel-mode HID transport minidriver as supported by the earlier versions of Windows. However, we do not recommend this approach because poorly written KMDF HID transport minidrivers can crash the system.</p>
<ul>
<li><a href="transport-minidrivers.md" data-raw-source="[Transport Minidrivers](transport-minidrivers.md)">Transport Minidrivers</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff539926" data-raw-source="[HID Minidriver IOCTLs](https://msdn.microsoft.com/library/windows/hardware/ff539926)">HID Minidriver IOCTLs</a></li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>Write a UMDF HID Minidriver</strong></p>
<p><img src="images/hid-umdf.png" alt="HID Transport Minidriver" /></p></td>
<td><p>If you are implementing a non-GPIO button, instead of using preceding model of writing a HID source driver, you can write a HID transport minidriver in user mode. These drivers are easier to develop than kernel-mode drivers and errors in this driver do not bug check the whole system.</p>
<ul>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh439579" data-raw-source="[Creating UMDF HID Minidrivers](https://msdn.microsoft.com/library/windows/hardware/hh439579)">Creating UMDF HID Minidrivers</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh463977" data-raw-source="[UMDF HID Minidriver IOCTLs](https://msdn.microsoft.com/library/windows/hardware/hh463977)">UMDF HID Minidriver IOCTLs</a></li>
</ul></td>
</tr>
</tbody>
</table>

 

## Universal Windows drivers for HID buttons


Starting with Windows 10, the HID driver programming interfaces are part of OneCoreUAP-based editions of Windows. By using that common set of interfaces, you can write a button driver by using [Virtual HID Framework](https://msdn.microsoft.com/library/windows/hardware/dn925048) or [Transport Minidrivers](transport-minidrivers.md) interfaces. Those drivers will run on both Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows 10 Mobile, as well as other Windows 10 versions.

For step-by-step guidance, see [Getting Started with Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers).

## Related topics
[Human Interface Device](https://msdn.microsoft.com/library/windows/hardware/ff543301)  



