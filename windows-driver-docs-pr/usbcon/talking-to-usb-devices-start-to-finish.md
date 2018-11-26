---
Description: Use the Windows Runtime APIs, introduced in Windows 8.1, to write UWP apps that gives users access to their peripheral USB device.
title: Talking to USB devices, start to finish (UWP app)
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Talking to USB devices, start to finish (UWP app)


**Summary**

-   End-to-end walkthrough for creating a UWP app that talks to a USB device
-   **Companion sample**: [Custom USB device access sample](http://go.microsoft.com/fwlink/p/?linkid=309716)

**Important APIs**

-   [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466)
-   [**Windows.Devices.Enumeration**](https://msdn.microsoft.com/library/windows/apps/br225459)
-   [**Windows.Devices.Background**](https://msdn.microsoft.com/library/windows/apps/dn263409)

Use the Windows Runtime APIs, introduced in Windows 8.1, to write UWP apps that gives users access to their peripheral USB device. Such apps can connect to a device based on user-specified criteria, get information about the device, send data to the device and conversely get data streams from the device, and poll the device for interrupt data.

Here we describe, how your UWP app using C++, C#, or Visual Basic app can implement those tasks, and link to examples that demonstrate the use of classes included in [**Windows.Devices.Usb**](https://msdn.microsoft.com/library/windows/apps/dn278466). We'll go over the device capabilities required in the app manifest and how to launching the app when the device is connected. And we'll show how to run a data transfer task in the background even when the app is suspended to conserve battery life.

Follow the steps in this section or, skip directly to the [Custom USB device access sample](http://go.microsoft.com/fwlink/p/?linkid=309716). The companion sample implements all the steps here, but to keep things moving we won't walk through the code. Certain steps have a **Find it in the sample** section to help you find the code quickly. The structure of the sample's source files is simple and flat so you can easily find code without having to drill down through multiple layers of source files. But you may prefer to break up and organize your own project differently.

## In this section


-   [**Step 1**—Install the Microsoft-provided WinUSB driver as function driver for your device.](#step1)
-   [**Step 2**—Get the device interface GUID, hardware ID, and device class information about your device.](#step2)
-   [**Step 3**—Determine whether the device class, subclass, and protocol allowed by the Windows Runtime USB API set.](#step3)
-   [**Step 4**—Create a basic Microsoft Visual Studio 2013 project that you can extend in this tutorial.](#step4)
-   [**Step 5**—Add USB device capabilities to the app manifest.](#step5)
-   [**Step 6**—Extend the app to open the device for communication.](#step6)
-   [**Step 7**—Study your USB device layout. (Recommended)](#step7)
-   [**Step 8**—Extend the app to get and show USB descriptors in the UI.](#step8)
-   [**Step 9**—Extend the app to send vendor-defined USB control transfers.](#step9)
-   [**Step 10**—Extend the app to read or write bulk data.](#step10)
-   [**Step 11**—Extend the app to get hardware interrupt data.](#step11)
-   [**Step 12**—Extend the app to select an interface setting that is not currently active.](#step12)
-   [**Step 13**—Close the device.](#step13)
-   [**Step 14**—Create a device metadata package for the app.](#step14)
-   [**Step 15**—Extend the app to implement AutoPlay activation so that the app is launched when the device is connected to the system.](#step15)
-   [**Step 16**—Extend the app to implement a background task that can perform lengthy USB transfers to the device, such as firmware update without the app getting suspended.](#step16)
-   [**Step 17**—Run Windows App Certification Kit.](#step17)

## Walkthrough—Writing UWP app for USB devices


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Step</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="" id="step1"></a>
<p><strong>Step 1</strong>—Install the Microsoft-provided WinUSB driver as function driver for your device.</p></td>
<td><p><strong>QuickStart:</strong> <a href="winusb-installation.md" data-raw-source="[WinUSB (Winusb.sys) Installation](winusb-installation.md)">WinUSB (Winusb.sys) Installation</a></p>
<p>You can install Winusb.sys in these ways:</p>
<ul>
<li>When you connect your device, you might notice that Windows loads Winusb.sys automatically because the device is a <a href="automatic-installation-of-winusb.md" data-raw-source="[WinUSB Device](automatic-installation-of-winusb.md)">WinUSB Device</a>.</li>
<li>Install the driver by specifying the system-provided device class in Device Manager.</li>
<li>Install the driver by using a custom INF. You can get the INF in either of these two ways:
<ul>
<li>Get the INF from the hardware vendor.</li>
<li>Write a custom INF that references the Microsoft-provided Winusb.inf file. For more information, see <a href="winusb-installation.md" data-raw-source="[WinUSB (Winusb.sys) Installation](winusb-installation.md)">WinUSB (Winusb.sys) Installation</a>.</li>
</ul></li>
</ul></td>
</tr>
<tr class="even">
<td><a href="" id="step2"></a>
<p><strong>Step 2</strong>—Get the device interface GUID, hardware ID, and device class information about your device.</p></td>
<td><p>You can obtain that information from the device manufacturer.</p>
<ul>
<li><p><strong>Vendor and product identifiers</strong></p>
<p>In Device Manager, view the device properties. On the <strong>Details</strong> tab, view the <strong>Hardware Id</strong> property value. That value is a combination of those two identifiers. For example, for the SuperMUTT device, the <strong>Hardware Id</strong> is &quot;USB\VID_045E&amp;PID_F001&quot;; vendor ID is &quot;0x045E&quot; and product ID is &quot;0xF001&quot;.</p></li>
<li><strong>Device class, subclass, and protocol codes</strong></li>
<li><strong>Device interface GUID</strong></li>
</ul>
Alternatively, you can view information the registry. For more information, see <a href="usb-device-specific-registry-settings.md" data-raw-source="[USB Device Registry Entries](usb-device-specific-registry-settings.md)">USB Device Registry Entries</a>.</td>
</tr>
<tr class="odd">
<td><a href="" id="step3"></a>
<p><strong>Step 3</strong>—Determine whether the device class, subclass, and protocol allowed by the Windows Runtime USB API set.</p></td>
<td><p>You can write a UWP app, if device class, subclass, and protocol code of the device is one of the following:</p>
<ul>
<li><code>name:cdcControl,           classId:02 * *</code></li>
<li><code>name:physical, classId:05 * *</code></li>
<li><code>name:personalHealthcare,   classId:0f 00 00</code></li>
<li><code>name:activeSync,           classId:ef 01 01</code></li>
<li><code>name:palmSync,             classId:ef 01 02</code></li>
<li><code>name:deviceFirmwareUpdate, classId:fe 01 01</code></li>
<li><code>name:irda,                 classId:fe 02 00     </code></li>
<li><code>name:measurement,          classId:fe 03 *</code></li>
<li><code>name:vendorSpecific,       classId:ff * *</code></li>
</ul></td>
</tr>
<tr class="even">
<td><a href="" id="step4"></a>
<p><strong>Step 4</strong>—Create a basic Visual Studio 2013 project that you can extend in this tutorial.</p></td>
<td>For more information, see <a href="http://go.microsoft.com/fwlink/p/?linkid=617681" data-raw-source="[Getting started with UWP apps](http://go.microsoft.com/fwlink/p/?linkid=617681)">Getting started with UWP apps</a>.</td>
</tr>
<tr class="odd">
<td><a href="" id="step5"></a>
<p><strong>Step 5</strong>—Add USB device capabilities to the app manifest.</p></td>
<td><p><strong>QuickStart:</strong> <a href="updating-the-app-manifest-with-usb-device-capabilities.md" data-raw-source="[How to add USB device capabilities to the app manifest](updating-the-app-manifest-with-usb-device-capabilities.md)">How to add USB device capabilities to the app manifest</a></p>
<p>Open your Package.appxmanifest file in a text editor and add the <a href="https://msdn.microsoft.com/library/windows/apps/br211430" data-raw-source="[&lt;strong&gt;DeviceCapability&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br211430)"><strong>DeviceCapability</strong></a> element with <strong>Name</strong> attribute set to &quot;usb&quot; as shown in this example.</p>
<div class="alert">
<strong>Note</strong>  You cannot modify the USB device capability in Visual Studio 2013. You must right-click the Package.appxmanifest file in <strong>Solution Explorer</strong> and select <strong>Open With...</strong>, and then <strong>XML (Text) Editor</strong>. The file opens in plain XML.
</div>
<div>
 
</div>
<pre class="syntax" space="preserve"><code>&lt;Capabilities&gt;
      &lt;!--When the device&#39;s classId is FF * *, there is a predefined name for the class. 
          You can use the name instead of the class id. 
          There are also other predefined names that correspond to a classId.--&gt;
      &lt;m2:DeviceCapability Name=&quot;usb&quot;&gt;
          &lt;!--SuperMutt Device--&gt;
          &lt;m2:Device Id=&quot;vidpid:045E 0611&quot;&gt;
              &lt;!--&lt;wb:Function Type=&quot;classId:ff * *&quot;/&gt;--&gt;
              &lt;m2:Function Type=&quot;name:vendorSpecific&quot;/&gt;
          &lt;/m2:Device&gt;
      &lt;/m2:DeviceCapability&gt;
  &lt;/Capabilities&gt;</code></pre>
<div class="code">

</div>
<p><strong>Find it in the sample:</strong> The USB device capabilities are added in the Package.appxmanifest file.</p></td>
</tr>
<tr class="even">
<td><a href="" id="step6"></a>
<p><strong>Step 6</strong>— Extend the app to open the device for communication.</p></td>
<td><p><strong>Quickstart:</strong> <a href="how-to-connect-to-a-usb-device--uwp-app-.md" data-raw-source="[How to connect to a USB device (UWP app)](how-to-connect-to-a-usb-device--uwp-app-.md)">How to connect to a USB device (UWP app)</a></p>
<ol>
<li>Find the device by building an Advanced Query Syntax (AQS) string that contains search criteria for finding the device in the enumerated device collection.</li>
<li>Open the device in one of two ways:
<ul>
<li><p>Passing the AQS to <a href="https://msdn.microsoft.com/library/windows/apps/br225432" data-raw-source="[&lt;strong&gt;FindAllAsync&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225432)"><strong>FindAllAsync</strong></a> and get the <a href="https://msdn.microsoft.com/library/windows/apps/br225393" data-raw-source="[&lt;strong&gt;DeviceInformation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225393)"><strong>DeviceInformation</strong></a> object for the device.</p>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/apps/xaml/hh872189" data-raw-source="[Quickstart: enumerating commonly used devices](https://msdn.microsoft.com/library/windows/apps/xaml/hh872189)">Quickstart: enumerating commonly used devices</a>.</p></li>
<li>By using a <a href="https://msdn.microsoft.com/library/windows/apps/br225446" data-raw-source="[&lt;strong&gt;DeviceWatcher&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225446)"><strong>DeviceWatcher</strong></a> object to detect when the device is added to or removed from the system.
<ol>
<li>Pass the AQS to <a href="https://msdn.microsoft.com/library/windows/apps/br225427" data-raw-source="[&lt;strong&gt;CreateWatcher&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225427)"><strong>CreateWatcher</strong></a> and get a <a href="https://msdn.microsoft.com/library/windows/apps/br225446" data-raw-source="[&lt;strong&gt;DeviceWatcher&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225446)"><strong>DeviceWatcher</strong></a> object.</li>
<li>Register event handlers on the <a href="https://msdn.microsoft.com/library/windows/apps/br225446" data-raw-source="[&lt;strong&gt;DeviceWatcher&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225446)"><strong>DeviceWatcher</strong></a> object.</li>
<li>Get the <a href="https://msdn.microsoft.com/library/windows/apps/br225393" data-raw-source="[&lt;strong&gt;DeviceInformation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225393)"><strong>DeviceInformation</strong></a> object for the device in your <a href="https://msdn.microsoft.com/library/windows/apps/br225450" data-raw-source="[&lt;strong&gt;Added&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225450)"><strong>Added</strong></a> event handler.</li>
<li>Start and stop the <a href="https://msdn.microsoft.com/library/windows/apps/br225446" data-raw-source="[&lt;strong&gt;DeviceWatcher&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225446)"><strong>DeviceWatcher</strong></a> object.</li>
</ol>
For more information, see <a href="https://msdn.microsoft.com/library/windows/apps/xaml/hh967756" data-raw-source="[How to get notifications if devices are added, removed, or changed](https://msdn.microsoft.com/library/windows/apps/xaml/hh967756)">How to get notifications if devices are added, removed, or changed</a>.</li>
</ul></li>
<li>Get the device instance from the <a href="https://msdn.microsoft.com/library/windows/apps/br225437" data-raw-source="[&lt;strong&gt;DeviceInformation.Id&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225437)"><strong>DeviceInformation.Id</strong></a> property.</li>
<li>Call <a href="https://msdn.microsoft.com/library/windows/apps/dn264010" data-raw-source="[&lt;strong&gt;FromIdAsync&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264010)"><strong>FromIdAsync</strong></a> by passing the device instance string and get the <a href="https://msdn.microsoft.com/library/windows/apps/dn263883" data-raw-source="[&lt;strong&gt;UsbDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn263883)"><strong>UsbDevice</strong></a> object.</li>
</ol>
<p><strong>Find it in the sample:</strong> See files named Scenario1_DeviceConnect.</p></td>
</tr>
<tr class="odd">
<td><a href="" id="step7"></a>
<p><strong>Step 7</strong>(Recommended)—Study your <a href="usb-device-layout.md" data-raw-source="[USB device layout](usb-device-layout.md)">USB device layout</a>.</p></td>
<td><p>Review basic USB concepts about configuring the device and performing data transfers: <a href="usb-concepts-for-all-developers.md" data-raw-source="[Concepts for all USB developers](usb-concepts-for-all-developers.md)">Concepts for all USB developers</a>.</p>
<p>View the device configuration descriptor, interface descriptors for each supported alternate settings, and their endpoint descriptors. By using <a href="http://go.microsoft.com/fwlink/p/?linkid=617721" data-raw-source="[USBView](http://go.microsoft.com/fwlink/p/?linkid=617721)">USBView</a>, you can browse all USB controllers and the USB devices connected to them, and also inspect the device configuration.</p></td>
</tr>
<tr class="even">
<td><a href="" id="step8"></a>
<p><strong>Step 8</strong>— Extend the app to get and show USB descriptors in the UI.</p></td>
<td><p><strong>Quickstart:</strong> <a href="how-to-get-usb-descriptors--uwp-app-.md" data-raw-source="[How to get USB descriptors (UWP app)](how-to-get-usb-descriptors--uwp-app-.md)">How to get USB descriptors (UWP app)</a></p>
<p></p>
<ul>
<li>Get the device descriptor by getting the <a href="https://msdn.microsoft.com/library/windows/apps/dn264002" data-raw-source="[&lt;strong&gt;UsbDevice.DeviceDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264002)"><strong>UsbDevice.DeviceDescriptor</strong></a> value.</li>
<li>Get the configuration descriptor by getting the <a href="https://msdn.microsoft.com/library/windows/apps/dn263799" data-raw-source="[&lt;strong&gt;UsbConfiguration.ConfigurationDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn263799)"><strong>UsbConfiguration.ConfigurationDescriptor</strong></a> value.
<ul>
<li>Get the full configuration descriptor set by getting the <a href="https://msdn.microsoft.com/library/windows/apps/dn263802" data-raw-source="[&lt;strong&gt;UsbConfiguration.Descriptors&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn263802)"><strong>UsbConfiguration.Descriptors</strong></a> property.</li>
</ul></li>
<li>Get the array of interfaces within the configuration by getting the <a href="https://msdn.microsoft.com/library/windows/apps/dn263808" data-raw-source="[&lt;strong&gt;UsbConfiguration.UsbInterfaces&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn263808)"><strong>UsbConfiguration.UsbInterfaces</strong></a> property.</li>
<li>Get the array of alternate settings by getting <a href="https://msdn.microsoft.com/library/windows/apps/dn264291" data-raw-source="[&lt;strong&gt;UsbInterface.InterfaceSettings&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264291)"><strong>UsbInterface.InterfaceSettings</strong></a>.</li>
<li><p>Within the active alternate setting enumerate pipes and get the associated endpoints.</p>
<p>Endpoint descriptors are represented by these objects:</p>
<ul>
<li><a href="https://msdn.microsoft.com/library/windows/apps/dn297543" data-raw-source="[&lt;strong&gt;UsbBulkInEndpointDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn297543)"><strong>UsbBulkInEndpointDescriptor</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/apps/dn297619" data-raw-source="[&lt;strong&gt;UsbBulkOutEndpointDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn297619)"><strong>UsbBulkOutEndpointDescriptor</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/apps/dn264294" data-raw-source="[&lt;strong&gt;UsbInterruptInEndpointDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264294)"><strong>UsbInterruptInEndpointDescriptor</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/apps/dn278420" data-raw-source="[&lt;strong&gt;UsbInterruptOutEndpointDescriptor&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn278420)"><strong>UsbInterruptOutEndpointDescriptor</strong></a></li>
</ul></li>
</ul>
<p><strong>Find it in the sample:</strong> See files named Scenario5_UsbDescriptors.</p></td>
</tr>
<tr class="odd">
<td><a href="" id="step9"></a>
<p><strong>Step 9</strong>— Extend the app to send vendor-defined USB control transfers.</p></td>
<td><p><strong>Quickstart:</strong> <a href="how-to-send-a-usb-control-transfer--uwp-app-.md" data-raw-source="[How to send a USB control transfer request (UWP app)](how-to-send-a-usb-control-transfer--uwp-app-.md)">How to send a USB control transfer request (UWP app)</a></p>
<p></p>
<ol>
<li>Get the vendor command from the hardware specification of the device.</li>
<li>Create a <a href="https://msdn.microsoft.com/library/windows/apps/dn278431" data-raw-source="[&lt;strong&gt;UsbSetupPacket&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn278431)"><strong>UsbSetupPacket</strong></a> object and populate the setup packet by setting various properties.</li>
<li>Start an asynchronous operation to send the control transfer by these methods depending on the direction of the transfer:
<ul>
<li><a href="https://msdn.microsoft.com/library/windows/apps/dn264027" data-raw-source="[&lt;strong&gt;SendControlInTransferAsync&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264027)"><strong>SendControlInTransferAsync</strong></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/apps/dn264044" data-raw-source="[&lt;strong&gt;SendControlOutTransferAsync&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264044)"><strong>SendControlOutTransferAsync</strong></a></li>
</ul></li>
</ol>
<p><strong>Find it in the sample:</strong> See files named Scenario2_ControlTransfer.</p></td>
</tr>
<tr class="even">
<td><a href="" id="step10"></a>
<p><strong>Step 10</strong>— Extend the app to read or write bulk data.</p></td>
<td><p><strong>Quickstart:</strong> <a href="how-to-send-a-usb-bulk-transfer--uwp-app-.md" data-raw-source="[How to send a USB bulk transfer request (UWP app)](how-to-send-a-usb-bulk-transfer--uwp-app-.md)">How to send a USB bulk transfer request (UWP app)</a></p>
<p></p>
<ol>
<li>Get the bulk pipe object (<a href="https://msdn.microsoft.com/library/windows/apps/dn297647" data-raw-source="[&lt;strong&gt;UsbBulkOutPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn297647)"><strong>UsbBulkOutPipe</strong></a> or <a href="https://msdn.microsoft.com/library/windows/apps/dn297573" data-raw-source="[&lt;strong&gt;UsbBulkInPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn297573)"><strong>UsbBulkInPipe</strong></a>).</li>
<li>Configure the bulk pipe to set policy parameters.</li>
<li>Set up the data stream by using the <a href="https://msdn.microsoft.com/library/windows/apps/br208119" data-raw-source="[&lt;strong&gt;DataReader&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br208119)"><strong>DataReader</strong></a> or <a href="https://msdn.microsoft.com/library/windows/apps/br208154" data-raw-source="[&lt;strong&gt;DataWriter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br208154)"><strong>DataWriter</strong></a> object.</li>
<li>Start an asynchronous transfer operation by calling <a href="https://msdn.microsoft.com/library/windows/apps/br208135" data-raw-source="[&lt;strong&gt;DataReader.LoadAsync&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br208135)"><strong>DataReader.LoadAsync</strong></a> or <a href="https://msdn.microsoft.com/library/windows/apps/br208171" data-raw-source="[&lt;strong&gt;DataWriter.StoreAsync&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br208171)"><strong>DataWriter.StoreAsync</strong></a>.</li>
<li>Get results of the transfer operation.</li>
</ol>
<p><strong>Find it in the sample:</strong> See files named Scenario4_BulkPipes.</p></td>
</tr>
<tr class="odd">
<td><a href="" id="step11"></a>
<p><strong>Step 11</strong>— Extend the app to get hardware interrupt data.</p></td>
<td><p><strong>Quickstart:</strong> <a href="how-to-send-a-usb-interrupt-transfer--uwp-app-.md" data-raw-source="[How to send a USB interrupt transfer request (UWP app)](how-to-send-a-usb-interrupt-transfer--uwp-app-.md)">How to send a USB interrupt transfer request (UWP app)</a></p>
<p></p>
<ol>
<li>Get the interrupt pipe object (<a href="https://msdn.microsoft.com/library/windows/apps/dn278416" data-raw-source="[&lt;strong&gt;UsbInterruptInPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn278416)"><strong>UsbInterruptInPipe</strong></a> or <a href="https://msdn.microsoft.com/library/windows/apps/dn278425" data-raw-source="[&lt;strong&gt;UsbInterruptOutPipe&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn278425)"><strong>UsbInterruptOutPipe</strong></a>).</li>
<li>Implement the interrupt handler for the <a href="https://msdn.microsoft.com/library/windows/apps/dn278418" data-raw-source="[&lt;strong&gt;DataReceived&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn278418)"><strong>DataReceived</strong></a> event.</li>
<li>Register the event handler to start receiving data.</li>
<li>Unregister the event handler to stop receiving data.</li>
</ol>
<p><strong>Find it in the sample:</strong> See files named Scenario3_InterruptPipes.</p></td>
</tr>
<tr class="even">
<td><a href="" id="step12"></a>
<p><strong>Step 12</strong>— Extend the app to select an interface setting that is not currently active.</p></td>
<td><p><strong>Quickstart:</strong> <a href="how-to-select-a-usb-interface-setting--uwp-app-.md" data-raw-source="[How to select a USB interface setting (UWP app)](how-to-select-a-usb-interface-setting--uwp-app-.md)">How to select a USB interface setting (UWP app)</a></p>
<p>When the device is opened for communication, the default interface and its first setting is selected. If you want to change that setting, follow these steps:</p>
<ol>
<li>Get the active setting of a USB interface by using the <a href="https://msdn.microsoft.com/library/windows/apps/dn264285" data-raw-source="[&lt;strong&gt;UsbInterfaceSetting.Selected&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264285)"><strong>UsbInterfaceSetting.Selected</strong></a> value.</li>
<li>Set a USB interface setting by starting an asynchronous operation by calling <a href="https://msdn.microsoft.com/library/windows/apps/dn264286" data-raw-source="[&lt;strong&gt;UsbInterfaceSetting.SelectSettingAsync&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264286)"><strong>UsbInterfaceSetting.SelectSettingAsync</strong></a>.</li>
</ol></td>
</tr>
<tr class="odd">
<td><a href="" id="step13"></a>
<p><strong>Step 13</strong>— Close the device.</p></td>
<td><p><strong>Quickstart:</strong> <a href="how-to-connect-to-a-usb-device--uwp-app-.md" data-raw-source="[How to connect to a USB device (UWP app)](how-to-connect-to-a-usb-device--uwp-app-.md)">How to connect to a USB device (UWP app)</a></p>
<p>After you are finished using the UsbDevice object, close the device.</p>
<p>C++ apps must release the reference by using the <strong>delete</strong> keyword. C#/VB apps must call the <a href="https://msdn.microsoft.com/library/windows/apps/dn264007" data-raw-source="[&lt;strong&gt;UsbDevice.Dispose&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn264007)"><strong>UsbDevice.Dispose</strong></a> method. JavaScript apps must call <a href="https://msdn.microsoft.com/library/windows/apps/dn263990" data-raw-source="[&lt;strong&gt;UsbDevice.Close&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/dn263990)"><strong>UsbDevice.Close</strong></a>.</p>
<p><strong>Find it in the sample:</strong> See files named Scenario1_DeviceConnect.</p></td>
</tr>
<tr class="even">
<td><a href="" id="step14"></a>
<p><strong>Step 14</strong>—Create a device metadata package for the app.</p></td>
<td><strong>Tool:</strong> <a href="https://msdn.microsoft.com/library/windows/hardware/hh454213" data-raw-source="[Device Metadata Authoring Wizard](https://msdn.microsoft.com/library/windows/hardware/hh454213)">Device Metadata Authoring Wizard</a>
<ul>
<li>If you have the Windows Driver Kit (WDK) installed, open <strong>Driver</strong> &gt; <strong>Device Metadata</strong> &gt; <strong>Authoring</strong>.</li>
<li>If you have the Standalone SDK installed, the tool is located at <em>&lt;install_path&gt;</em>\bin\x86\DeviceMetadataWizardexe.</li>
</ul>
<p>Associate your app with the device by following the steps in the wizard. Enter this information about your device:</p>
<p></p>
<ul>
<li>On the <strong>Device Info</strong> page, enter <strong>Model Name</strong>, <strong>Manufacturer</strong>, and <strong>Description</strong>.</li>
<li>On the <strong>Hardware Info</strong> page, enter the hardware ID of your device.</li>
</ul>
<p><strong>To declare the app as a privileged app for your device, follow these instructions:</strong></p>
<ol>
<li><p>On the <strong>App Info</strong> page, in the <strong>Privileged application</strong> group, enter the <strong>Package name</strong>, <strong>Publisher name</strong>, and <strong>UWP app ID</strong>.</p>
<p><img src="images/privileged-app.png" alt="device metatdata for privileged apps" /></p>
<div class="alert">
<strong>Note</strong>  Do not check the <strong>Access custom driver</strong> option.
</div>
<div>
 
</div></li>
<li>Open the <strong>Finish</strong> tab. Select the <strong>Copy packages to your system&#39;s local metadata store</strong> check box.</li>
<li>Connect the device, in Control Panel, open <strong>View devices and printers</strong> and verify that the icon of the device is correct.</li>
</ol>
<p><strong>Find it in the sample:</strong> See the DeviceMetadata folder.</p></td>
</tr>
<tr class="odd">
<td><a href="" id="step15"></a>
<p><strong>Step 15</strong>—Extend the app to implement AutoPlay activation so that the app is launched when the device is connected to the system.</p></td>
<td><p><strong>Quickstart:</strong> <a href="https://msdn.microsoft.com/library/windows/apps/xaml/jj161017" data-raw-source="[Register an app for an AutoPlay device](https://msdn.microsoft.com/library/windows/apps/xaml/jj161017)">Register an app for an AutoPlay device</a></p>
<p>You can add AutoPlay capabilities so that app is launched when the device is connected to the system. You can enable Autoplay for all UWP apps (privileged or otherwise).</p>
<p></p>
<ol>
<li>In your device metadata package, you must specify how the device should respond to an AutoPlay notification. On the <strong>Windows Info</strong> tab, select the <strong>UWP device app</strong> option and enter app information as shown here:</li>
<li><p>In the app manifest, add <strong>AutoPlay Device</strong> declaration and launch information as shown here:</p>
<p><img src="images/autoplay.png" alt="AutoPlay" /></p></li>
<li>In the OnActivated method of the App class, check if the app is activated by the device. If it is, then the method receives a DeviceEventArgs parameter value that contains the <a href="https://msdn.microsoft.com/library/windows/apps/br225437" data-raw-source="[&lt;strong&gt;DeviceInformation.Id&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br225437)"><strong>DeviceInformation.Id</strong></a> property value. This is the same value described in <a href="#step6" data-raw-source="[&lt;strong&gt;Step 6&lt;/strong&gt;—Extend the app to open the device for communication](#step6)"><strong>Step 6</strong>—Extend the app to open the device for communication</a>.</li>
</ol>
<p><strong>Find it in the sample:</strong> See files named Autoplay. For JavaScript, see default.js.</p></td>
</tr>
<tr class="even">
<td><a href="" id="step16"></a>
<p><strong>Step 16</strong>—Extend the app to implement a background task that can perform length transfers to the device, such as firmware update without the app getting suspended.</p></td>
<td><p>To implement background task, you need two classes.</p>
<p>The background task class implements the <a href="https://msdn.microsoft.com/library/windows/apps/br224794" data-raw-source="[&lt;strong&gt;IBackgroundTask&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br224794)"><strong>IBackgroundTask</strong></a> interface and contains the actual code you create to either sync or update your peripheral device. The background task class is executed when the background task is triggered and from the entry point provided in your app’s application manifest.</p>
<div class="alert">
<strong>Note</strong>  The device background tasks infrastructure provided by Windows 8.1. For more information about Windows background tasks see <a href="https://msdn.microsoft.com/library/windows/apps/xaml/hh977056" data-raw-source="[Supporting your app with background tasks](https://msdn.microsoft.com/library/windows/apps/xaml/hh977056)">Supporting your app with background tasks</a>.
</div>
<div>
 
</div>
<p><strong>Background task class</strong></p>
<ol>
<li>Implements the <a href="https://msdn.microsoft.com/library/windows/apps/br224794" data-raw-source="[&lt;strong&gt;IBackgroundTask&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/apps/br224794)"><strong>IBackgroundTask</strong></a> interface required by the Windows background task infrastructure.</li>
<li>Obtains the DeviceUseDetails instance passed to the class in the <strong>Run</strong> method and uses this instance to report progress back to the Microsoft Store app and to register for cancellation events.</li>
<li>The <strong>Run</strong> method also calls the private OpenDevice and WriteToDeviceAsync methods that implement the background device sync code.</li>
</ol>
<p>The UWP app registers and triggers a DeviceUseTrigger background task. The app register, trigger, and handle progress on a background task.</p>
<div class="alert">
<strong>Note</strong>  The example code that follows can be applied to the DeviceServicingTrigger background task by use the corresponding objects. The only difference between the two trigger objects and their corresponding APIs are the policy checks made by Windows.
</div>
<div>
 
</div>
<ol>
<li>Creates DeviceUseTrigger and BackgroundTaskRegistration objects.</li>
<li>Checks to see if any background tasks were previously registered by this sample application and cancels them by calling the Unregister method on the task.</li>
<li>Registers the background task that will sync with the device. The SetupBackgroundTask method is called from the SyncWithDeviceAsync method in the next step.
<ol>
<li>Initializes the DeviceUseTrigger and saves it for later use.</li>
<li>Creates a BackgroundTaskBuilder object and uses its Name, TaskEntryPoint and SetTrigger properties and method to register the app’s DeviceUseTrigger object and background task name. The BackgroundTaskBuilder object’s TaskEntryPoint property is set to the full name of the background task class that will be run when the background task is triggered.</li>
<li>Registers for completion and progress events from the background task so the Microsoft Store app can provide completion and progress updates to the user.</li>
</ol></li>
<li>The private SyncWithDeviceAsync method registers the background task that will sync with the device and starts the background sync.
<ol>
<li>Calls the SetupBackgroundTask method from the previous step and registers the background task that will sync with the device.</li>
<li>Calls the private StartSyncBackgroundTaskAsync method which starts the background task.</li>
<li>Closes the app’s handle to the device to ensure that the background task is able to open the device when it starts.
<div class="alert">
<strong>Note</strong>  The background task will need to open the device to perform the update so the Microsoft Store app must close its connections to the device before calling RequestAsync
</div>
<div>
 
</div></li>
<li>Calls the DeviceUseTrigger object’s RequestAsync method which starts triggers the background task and returns the DeviceTriggerResults object from RequestAsync used to determine if the background task started successfully.
<div class="alert">
<strong>Note</strong>  Windows checks to ensure that all necessary task initiation policy checks have been completed. If all policy checks are completed the update operation is now running as a background task outside of the Microsoft Store app, allowing the app to be safely suspended while the operation is in progress. Windows will also enforce any runtime requirements and cancel the background task if those requirements are no longer met.
</div>
<div>
 
</div></li>
<li>Uses the DeviceTriggerResults object returned from StartSyncBackgroundTaskAsync to determine if the background task started successfully. A switch statement is used to inspect the result from DeviceTriggerResults.</li>
</ol></li>
<li>Implements a private OnSyncWithDeviceProgress event handler that will update the app UI with progress from the background task.</li>
<li>Implements a private OnSyncWithDeviceCompleted event handler to handle the transition from background tasks to foreground app when the background task has completed.
<ol>
<li>Uses the CheckResults method of the BackgroundTaskCompletedEventArgs object to determine if any exceptions were thrown by the background task.</li>
<li>The app reopens the device for use by the foreground app now that the background task is complete and updates the UI to notify the user.</li>
</ol></li>
<li>Implements private button click event handlers from the UI to start and cancel the background task.
<ol>
<li>The private Sync_Click event handler calls the SyncWithDeviceAsync method described in the previous steps.</li>
<li>The private CancelSync_Click event handler calls the private CancelSyncWithDevice method to cancel the background task.</li>
</ol></li>
<li>The private CancelSyncWithDevice method unregisters and cancels any active device syncs so the device can be reopened by using the Unregister method on the BackgroundTaskRegistration object.</li>
</ol>
<p><strong>Find it in the sample:</strong> See files named Scenario7_Sync files. Background class is implemented in IoSyncBackgroundTask.</p></td>
</tr>
<tr class="odd">
<td><a href="" id="step17"></a>
<p><strong>Step 17</strong>—Run Windows App Certification Kit.</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/apps/hh694081" data-raw-source="[Using the Windows App Certification Kit](https://msdn.microsoft.com/library/windows/apps/hh694081)">Using the Windows App Certification Kit</a></p>
<p>Recommended. Running Windows App Certification Kit helps you make sure your app fulfills Microsoft Store requirements, so you should do this when you&#39;ve added major functionality to your app.</p></td>
</tr>
</tbody>
</table>

 

## Want to know more?


Learn more from related samples.

**Related Samples**

-   [USB CDC Control sample](http://go.microsoft.com/fwlink/p/?linkid=309716)
-   [Firmware Update USB Device sample](http://go.microsoft.com/fwlink/p/?linkid=309716)

[UWP app UI, start to finish (XAML)](https://msdn.microsoft.com/library/windows/apps/xaml/dn263191)

Learn more about designing UWP app UI.

[Roadmap for UWP apps using C# and Visual Basic](https://msdn.microsoft.com/library/windows/apps/br229583) and [Roadmap for UWP apps using C++](https://msdn.microsoft.com/library/windows/apps/hh700360)

Learn more about creating UWP apps using C++, C#, or Visual Basic in general.

[Asynchronous programming (UWP apps)](https://msdn.microsoft.com/library/windows/apps/hh464924)

Learn about how to make your apps stay responsive when they do work that might take an extended amount of time.

 

 




