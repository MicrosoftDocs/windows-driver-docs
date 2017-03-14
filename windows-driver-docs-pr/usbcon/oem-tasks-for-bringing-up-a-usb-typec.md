---
Description: 'Describes Windows support for USB Type-C connector and tasks for OEMs who are building USB Type-C systems, including how to write drivers that manage different features of the connector.'
MS-HAID:
- 'buses.oem\_tasks\_for\_bringing\_up\_a\_usb\_type-c'
- 'buses.oem\_tasks\_for\_bringing\_up\_a\_usb\_typec'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: 'Windows support for USB Type-C connectors'
---

# Windows support for USB Type-C connectors


**Last Updated**

-   December 2016

**Official specifications**

-   [USB 3.1 and USB Type-C specifications](http://go.microsoft.com/fwlink/p/?LinkId=699515)
-   [USB Power Delivery](http://go.microsoft.com/fwlink/p/?LinkID=623310)
-   [Billboard Devices specification](http://go.microsoft.com/fwlink/p/?linkid=620207)
-   [UCSI Specification](http://go.microsoft.com/fwlink/p/?LinkId=703713)

**Windows support**

-   USB Type-C feature support in Windows
-   [FAQ: USB Type-C connector on a Windows system](faq--usb-type-c-connector-on-a-windows-system.md)
-   [Troubleshoot messages in UI](introduction-to-usb-type-c-connectors.md)

Describes Windows support for USB Type-C connector and tasks for OEMs who are building USB Type-C systems, including how to write drivers that manage different features of the connector.

A traditional USB connection uses a cable with a USB A and USB B connector on each end. The USB A connector always plugs in to the host side and the USB B connector connects the function side, which is a device (phone) or peripheral (mouse, keyboard). By using those connectors, you can only connect a host to a function; never a host to another host or a function to another function. The host is the power source provider and the function consumes power from the host.

The traditional configuration limits some scenarios. For example, if a mobile device wants to connect to a peripheral, the device must act as the host and deliver power to the connected device.

The USB Type-C connector, introduced by the USB-IF, defined in the USB 3.1 specification, addresses those limitations. Windows 10 introduces native support for those features.

![usb connector comparison](images/typecccomp.jpg)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><img src="images/roadmap.png" alt="Windows 10 USB Type-C " /></p></td>
<td><p><img src="images/usb-type-c.png" alt="USB Type-C symmetric cable" /></p>
<p></p>
<p>USB Type-C connector is reversible and symmetric.</p>
<p>Allows for faster charging up to 100W with Power Delivery over USB Type-C.</p>
<p>Single connector for both USB Hosts and USB Devices</p>
<p>Can switch USB roles to support a USB host or device.</p>
<p>Can switch power roles between sourcing and sinking power</p>
<p>Supports other protocols like DisplayPort and Thunderbolt over USB Type-C.</p>
<p>Introduces USB Billboard device class to provide error notifications for Alternate Modes.</p></td>
</tr>
<tr class="even">
<td><img src="images/design.png" alt="Design" /></td>
<td><p>The main component are: the USB Type-C connector and its port or PD controller that manages the CC pin logic for the connector. Such systems typically have a dual-role controller that can swap the USB role from host to function. It has Display-Out module that allows video signal to be transmitted over USB. Optionally it can support BC1.2 charger detection.</p>
<p>[Hardware design of a USB Type-C system](architecture--usb-type-c-in-a-windows-system.md)</p>
<p>[Hardware design for a USB Type-C system with an embedded controller](ucsi.md)</p>
<p>Consider recommendations for the design and development of USB components, including minimum hardware requirements, Windows Hardware Compatibility Program requirements, and other recommendations that build on those requirements.</p>
<p>[Hardware component guidelines USB](https://msdn.microsoft.com/library/windows/hardware/dn915125)</p></td>
</tr>
<tr class="odd">
<td><img src="images/drivers-c.png" alt="Drivers" /></td>
<td><ul>
<li><p>For a system that has an embedded controller, implement the USB Type-C Connector System Software Interface (UCSI) in the EC and BIOS, and load the Microsoft provided in-box driver, UcmUcsi.sys, that implements UCSI Specification.</p>
<p>[UCSI driver](ucsi.md)</p></li>
<li><p>Otherwise, implement a driver that communicates with the connector and keeps the operating system informed about USB Type-C events on the connector.</p>
<p>[Developing Windows drivers for USB Type-C connectors](developing-windows-drivers-for-usb-type-c-connectors.md)</p>
<p>[Write a USB Type-C connector driver](bring-up-a-usb-type-c-connector-on-a-windows-system.md)</p>
<p>[UCmCx client driver programming reference](https://msdn.microsoft.com/library/windows/hardware/mt188011)</p></li>
</ul></td>
</tr>
<tr class="even">
<td><img src="images/bringup-c3.png" alt="Bringup" /></td>
<td><ol>
<li>If you are building is a mobile device (such as a phone) modify system ACPI to indicate to the Microsoft in-box function controller driver that the connector is a USB Type-C connector.</li>
<li>If you are building a dual-role mobile device, modify system ACPI to enable the Microsoft in-box USB role-switch driver.</li>
<li>Bringing up the connector driver depends on the driver that you choose for the connector, Microsoft in-box driver, UCSI (UcmUcsi.sys) or a custom driver.
<ul>
<li>If you are using UCSI, follow the instructions given in [Intel BIOS Implementation of UCSI](http://go.microsoft.com/fwlink/p/?LinkId=760658) to load the driver.</li>
<li>If you are using a custom driver, load the driver by using the connector driver installation package.</li>
</ul></li>
</ol></td>
</tr>
<tr class="odd">
<td><img src="images/test-c1.png" alt="Test" /></td>
<td><ul>
<li><p>Perform various functional and stress tests on systems and devices that expose a USB Type-C connector.</p>
<p>[Test USB Type-C systems with MUTT ConnEx-C](test-usb-type-c-systems-with-mutt-connex-c.md)</p></li>
<li>Run USB tests included in the Windows Hardware Lab Kit (HLK) for Windows 10.
<div class="alert">
<strong>Note</strong>  Run USB function HLK tests with a C-to-A cable (searc for <strong>&quot;Windows USB Device&quot;</strong> in the HLK search box.
</div>
<div>
 
</div></li>
<li><p>Certification/Compliance</p>
<p>Attend Power Delivery and USB-C compliance workshops hosted by the standards bodies,</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Windows%20support%20for%20USB%20Type-C%20connectors%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")



