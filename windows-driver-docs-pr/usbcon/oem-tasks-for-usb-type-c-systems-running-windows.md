---
Description: This table describes the use cases is supported by Windows 10, and the additional tasks OEMs must perform for those use case to work.
title: OEM tasks for USB Type-C systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# OEM tasks for USB Type-C systems


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

This table describes the use cases is supported by Windows 10, and the additional tasks OEMs must perform for those use case to work.




<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Use case</th>
<th>Windows support</th>
<th>OEM tasks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Power delivery</strong></p>
<p>Support for charging a USB Type-C system by using legacy chargers (&lt;7.5W), USB Type-C chargers (&lt;15W), Power Delivery chargers (100W+)</p></td>
<td><p>For Windows 10 Mobile systems,</p>
<ul>
<li>Charging from legacy chargers is handled by the <a href="usb-device-side-drivers-in-windows.md" data-raw-source="[USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md)">USB device-side drivers in Windows</a>.</li>
<li>Charging from USB Type-C chargers (including those that implement Power Delivery), is handled by the USB connector manager drivers: USB connector manager class extension (UcmCx) and its client driver for the connector. The client driver communicates with the hardware to determine the charging policy and forwards that UcmCx, which further sends it to the charging arbitration driver (CAD). CAD selects the charging source to use.</li>
</ul>
<p>For Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) systems,</p>
<ul>
<li>Charging from legacy chargers is not recommended, as they are not powerful enough to charge desktop systems.</li>
<li>Charging for USB Type-C chargers is handled by USB connector manager class extension (UcmCx) and its client driver for the connector. The system does not currently specify which power source to use and how much power to consume.</li>
</ul>
<p></p>
<div class="alert">
<strong>Note</strong>  The user is notified when a slower charger is detected.
</div>
<div>
 
</div></td>
<td><p>You must determine the charging policy in your hardware, firmware, and client driver. Charging policy mainly includes:</p>
<ul>
<li>Is the system a power source (provider) or power sink (consumer)?</li>
<li>How much power should the system consume?​</li>
<li>Which power source (charger) should be used if there are multiple power sources available (such as chargers)?​</li>
</ul>
<p>For power delivery-compliant chargers, the hardware must negotiate a power contract, which includes the voltage and current.​ The negotiated power contract must be forwarded to the system through the USB connector manager class extension (UcmCx) or the USCI driver for appropriate action.</p>
<p>If a slow charger is connected to the system, the system must be notified through UcmCx or UCSI.</p>
<p>To support legacy proprietary high-voltage or high-current charging mechanisms, an additional filter driver must be written for Microsoft’s in-box USB Function driver that detects the proprietary charger and reports it to the in-box driver.</p>
<p><a href="bring-up-a-usb-type-c-connector-on-a-windows-system.md" data-raw-source="[Write a USB Type-C connector driver](bring-up-a-usb-type-c-connector-on-a-windows-system.md)">Write a USB Type-C connector driver</a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/mt188012" data-raw-source="[USB filter driver for supporting proprietary chargers](https://msdn.microsoft.com/library/windows/hardware/mt188012)">USB filter driver for supporting proprietary chargers</a></p>
<div class="alert">
<strong>Note</strong>  Windows does not support Power Delivery for legacy USB-A and USB-B/USB-microB connectors.
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td><p><strong>Connecting USB devices and peripherals</strong></p>
<p>Ability of a Windows system (desktop and mobile) to connect USB devices/peripherals</p></td>
<td><p>Windows 10 for desktop editions supports most device classes. The device drivers and their installation files are included in Windows</p>
<p>Devices that run Windows 10 Mobile can connect and interact with USB devices/peripherals​ through a set of in-box drivers. The operating system supports a subset of device classes.</p>
<p>See, <a href="supported-usb-classes.md" data-raw-source="[USB device class drivers included in Windows](supported-usb-classes.md)">USB device class drivers included in Windows</a>.</p></td>
<td><p>If your system wants to connect to a custom USB device for which Windows does not include a driver, you can choose to load the generic driver (Winusb.sys) or write a driver. For guidance, see <a href="winusb-considerations.md" data-raw-source="[Choosing a driver model for developing a USB client driver](winusb-considerations.md)">Choosing a driver model for developing a USB client driver</a>.</p>
<p>We recommend that you write a single driver that runs on Windows 10 for desktop editions and Windows 10 Mobile. For more information, see <a href="https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers" data-raw-source="[Getting Started with Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers)">Getting Started with Universal Windows drivers</a>.</p>
<p>To write an application that communicates the device, use Windows Runtime APIs. For more information, see <a href="talking-to-usb-devices-start-to-finish.md" data-raw-source="[Talking to USB devices, start to finish (UWP app)](talking-to-usb-devices-start-to-finish.md)">Talking to USB devices, start to finish (UWP app)</a>.</p></td>
</tr>
<tr class="odd">
<td><strong>Alternate modes</strong>
<p>Connect to a non-USB device (e.g. monitor) using a USB Type-C connector.</p>
 </td>
<td><p>Windows 10 is capable of detecting DisplayPort/DockPort devices if the hardware supports those alternate modes.</p>
<p>Windows 10 provides an in-box driver for a Billboard device and notifies the user if the Billboard device indicates that an error occurred.</p></td>
<td><p>In order for an alternate mode to work, your system and device must support the alternate mode in the hardware and firmware. Perform necessary tasks to negotiate the alternate mode and entering the mode. That is typically accomplished by muxing the wire on the USB Type-C connector to the alternate mode.</p></td>
</tr>
<tr class="even">
<td><strong>Billboard devices</strong>
<p>Display information about the error condition to help the user troubleshoot issues.</p></td>
<td><p>Windows 10 provides an in-box driver for Billboard devices and notifies the user if the Billboard device indicates an error.</p>
<p>The user might see an error notification, if:</p>
<ul>
<li>The alternate mode is not supported by the PC or phone running Windows 10.</li>
<li>The alternate mode is not supported by the cable (if used).</li>
</ul>
For the best results, make sure that the alternate mode device or adapter’s requirements are met by PC or phone or cable.
<p></p></td>
<td><p>Your Alternate Mode adapter or device must implement a Billboard device that indicates whether or not an Alternate Mode negotiation was successful.</p>
<p>If your alternate mode adapter or device implements other USB functionality, updating the contents of your Billboard descriptor will require you to disconnect and reconnect the device, possibly interrupting functionality (such as a file transfer, if your device is a USB mass storage device). To avoid that, the Billboard specification recommends that you use an integrated hub in your device, and have the Billboard device appear as a separate USB device on one of its ports.</p>
<p>For more information, see <a href="http://go.microsoft.com/fwlink/p/?linkid=620207" data-raw-source="[USB Device Class Definition for Billboard Devices specification](http://go.microsoft.com/fwlink/p/?linkid=620207)">USB Device Class Definition for Billboard Devices specification</a>.</p></td>
</tr>
<tr class="odd">
<td><strong>USB dual role</strong>
<p>Connect two Windows devices together​</p></td>
<td><p>When two Windows devices are connected together, the system determines the appropriate role that each of the devices should be in and performs role swap operations if needed.</p>
<p>To support this, Windows 10 can communicate with the dual role controller on the system through the USB role switch class extension framework. An inbox client driver for this framework is also provided for Synopsys dual role controllers.</p>
<p>For USB Type-C systems, the USB connector manager gets information about the roles initially assigned by the hardware port controllers.</p>
<p>The USB role switch stack and the USB connector manager stack communicate with the hardware to get the current role and swap the roles of the system’s port as needed.</p>
<p></p>
<div class="alert">
<strong>Note</strong>  Peer-to-peer USB Type-C connections such as a PC is connected to another PC, or mobile device is connected to another mobile device are not supported. For such connections, an error is displayed to the user.
</div>
<div>
 
</div></td>
<td><p>Dual role ports must work with the operating system to make sure the right software stack (either Host or Function) is loaded at the right time.</p>
<p>Systems can be designed such that the dual-role USB port needs Windows to configure it to either Host or Function mode. These designs will need to use the USB role switch stack. If the system does not use a Synopsys or ChipIdea dual role controller, you will need to write a USB role switch client driver for the system’s dual role controller.</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/mt628026" data-raw-source="[USB dual-role controller driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt628026)">USB dual-role controller driver programming reference</a></p>
<p>System can also be designed such that the firmware or the customer-supplied drivers configure the port as either a Host or Function port, depending on the device that is connected to the port. These designs will need to either implement this logic in the firmware, or will need to implement it in a USB connector manager client driver. In these systems, Windows will automatically load the correct software stack.</p>
<p><a href="bring-up-a-usb-type-c-connector-on-a-windows-system.md" data-raw-source="[Write a USB Type-C connector driver](bring-up-a-usb-type-c-connector-on-a-windows-system.md)">Write a USB Type-C connector driver</a></p></td>
</tr>
<tr class="even">
<td><strong>Audio Accessories​</strong>
<p>USB Type-C connector can be used as an audio jack.</p></td>
<td>Windows 10 is capable of detecting a USB Type-C analog input as 3.5 mm audio jack, if the hardware supports the feature.
<p>The USB Type-C specification connector allows a USB Type-C connector to be used similar to a 3.5&quot; analog audio jack by using the audio accessory mode. Windows 10 supports systems that implement USB Type-C support for audio accessories by detecting the accessory as a regular 3.5&quot; analog audio device.</p></td>
<td>To use this feature, your hardware or firmware must detect if audio accessory is connected and switch to that mode, as per the Audio Type-C specification. This is done by mapping the pins on the 3.5&quot; analog audio connector to pins on the USB Type-C connector.</td>
</tr>
</tbody>
</table>

 

USB Type-C connectors can be used for wired docking, which allows the system to connect to a dock that delivers power to the system and attaches other peripherals. If the system detects an alternate display, the system can project to that display. To enable wired docking, make sure you have completed OEM tasks listed for Power delivery, Connecting USB devices and peripherals, and Alternate modes use cases in the preceding table.

## Related topics
[Windows support for USB Type-C connectors](oem-tasks-for-bringing-up-a-usb-typec.md)  



