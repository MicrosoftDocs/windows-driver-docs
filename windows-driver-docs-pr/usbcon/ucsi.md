---
Description: Microsoft provides a USB Type-C Connector System Software Interface (UCSI) Specification-compliant driver.
title: USB Type-C Connector System Software Interface (UCSI) driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB Type-C Connector System Software Interface (UCSI) driver


**Summary**

-   Microsoft-provided in-box UCSI driver for a USB Type-C system with an embedded controller.

**Last Updated**

-   October 2018

**Windows version**

-   Windows 10 for desktop editions (Home, Pro, Enterprise, and Education)
-   Windows 10 Mobile

**Official specifications**

-   [Intel BIOS Implementation of UCSI](http://go.microsoft.com/fwlink/p/?LinkId=760658)
-   [USB Type-C Connector System Software Interface Specification](http://go.microsoft.com/fwlink/p/?LinkId=703713)
-   [Hardware design: USB Type-C components for systems with embedded controllers](hardware-design-of-a-usb-type-c-system.md#emb)


Microsoft provides a USB Type-C Connector System Software Interface (UCSI) Specification-compliant driver for ACPI transport. If your design includes an embedded controller with ACPI transport, implement UCSI in your system's BIOS/EC and load the in-box UCSI driver (UcmUcsiCx.sys and UcmUcsiAcpiClient.sys).

If your UCSI-compliant hardware uses a transport other than ACPI, you need to [write a UCSI client driver](write-a-ucsi-driver.md).

## Drivers for supporting USB Type-C components for systems with embedded controllers

Here is an example of a system with an embedded controller.

![usb type-c software components](images/ucsiarch.png)

In the preceding example, USB role switching is handled in the firmware of the system and USB Role Switch driver stack is not loaded. In another system, the driver stack may not get loaded because dual role is not supported.

In the preceding image,

-   **USB device-side drivers**

    The [USB device-side drivers](usb-device-side-drivers-in-windows.md) service the function/device/peripheral. The USB function controller class extension supports MTP (Media Transfer Protocol) and charging using BC 1.2 chargers. Microsoft provides in-box client drivers for Synopsys USB 3.0 and ChipIdea USB 2.0 controllers. You can write a custom client driver for your function controller by using [USB function controller client driver programming interfaces](https://msdn.microsoft.com/library/windows/hardware/mt188010). For more information, see [Developing Windows drivers for USB function controllers](developing-windows-drivers-for-usb-function-controllers.md).

    The SoC vendor might provide you with the USB function lower filter driver for charger detection. You can implement your own filter driver if you are using the in-box Synopsys USB 3.0 or ChipIdea USB 2.0 client driver.

-   **USB host-side drivers**

    The USB host-side drivers are a set of drivers that work with EHCI or XHCI compliant USB host controllers. The drivers are loaded if the role-switch driver enumerates the host role. If your host controller is not specification-compliant, then you can write a custom driver by using [USB host controller extension (UCX) programming interface](https://msdn.microsoft.com/library/windows/hardware/mt188009). For information, see [Developing Windows drivers for USB host controllers](developing-windows-drivers-for-usb-host-controllers.md).

    **Note**  Not [all USB devices classes](supported-usb-classes.md) are supported on Windows 10 Mobile.

     

-   **USB connector manager**

    Microsoft provides a UCSI in-box driver with Windows (UcmUcsiCx.sys) that implements the features defined by the UCSI specification available [here](http://go.microsoft.com/fwlink/p/?LinkId=703713). The specification describes the capabilities of UCSI and explains the registers and data structures, for hardware component designers, system builders, and device driver developers.

    This driver is intended for systems with embedded controllers. This driver is a client to the Microsoft-provided USB connector manager class extension driver (Ucmcx.sys). The driver handles tasks such as initiating a request to the firmware to change the data or power roles and getting information needed to provide troubleshooting messages to the user.

## UCSI commands required by Windows


See the UCSI specification for commands that are "Required" in all UCSI implementations.

In addition to the commands marked as "Required", Windows requires these commands:

-   GET\_ALTERNATE\_MODES
-   GET\_CAM\_SUPPORTED
-   GET\_PDOS
-   SET\_NOTIFICATION\_ENABLE: The system or controller must support the following notifications within SET\_NOTIFICATION\_ENABLE:
    -   Supported Provider Capabilities Change
    -   Negotiated Power Level Change
-   GET\_CONNECTOR\_STATUS: The system or controller must support these connector status changes within GET\_CONNECTOR\_STATUS:
    -   Supported Provider Capabilities Change
    -   Negotiated Power Level Change

For information about the tasks required to implement UCSI in the BIOS, see [Intel BIOS Implementation of UCSI](http://go.microsoft.com/fwlink/p/?LinkId=760658).

## Example flow for UCSI


The examples given in this section describe interaction between the USB Type-C hardware/firmware, UCSI driver, and the operating system.

### DRP role detection

1.  USB Type-C hardware/firmware detects a device-attach event and the Windows 10 system DRP system initially becomes the UFP role.
    1.  The firmware sends a notification indicating a change in the connector.
    2.  The UCSI driver sends a ​ GET\_CONNECTOR\_STATUS request.
    3.  The firmware responds that its Connect Status = 1​ and Connector Partner Type = DFP. ​
2.  The drivers in the USB function stack responds to the enumeration.
3.  The USB connector manager class extension recognizes that the USB function stack has loaded and hence the system is in the wrong state. It tells the UCSI driver to send Set USB Operation Role and Set Power Direction Role requests to the firmware.
4.  USB Type-C hardware/firmware initiates the role-swap operation with the DFP​.

### <a name="detecting-a-charger-mismatch-error--condition"></a>Detecting a charger mismatch error​ condition

1.  USB Type-C hardware/firmware detects that a charger is connected and negotiates a default power contract. It also observes that the charger is not providing sufficient power to the system.
2.  USB Type-C hardware/firmware sets the slow charging bit.
    1.  The firmware sends a notification indicating a change in the connector.
    2.  The UCSI driver sends a ​ GET\_CONNECTOR\_STATUS request.
    3.  The firmware responds with Connect Status = 1​, Connector Partner Type=DFP, and Battery Charging Status = Slow/Trickle.
    
3.  The USB connector manager class extension sends notification to the UI to display the charger mismatch troubleshoot message.

## How to test UCSI


There are a number of ways to test your UCSI implementation. To test individual commands in your UCSI BIOS/EC implementation, use UCSIControl.exe, which is provided in the [MUTT Software Pack](mutt-software-package.md). To test your complete UCSI implementation, use both the UCSI tests that can be found in the Windows Hardware Lab Kit (HLK) and the steps in the [Type-C Manual Interop Procedures](https://msdn.microsoft.com/library/windows/hardware/mt422725).

**UCSIControl.exe**

You can test individual commands in your UCSI BIOS/EC implementation by using UCSIControl.exe. This tool enables you to send UCSI commands to the firmware through the UCSI driver. It requires the driver to be loaded and running, and also have the test interface to the driver enabled. By default, this interface is not enabled so as to prevent it from being accessible to unauthorized users on a retail system.

1.  Locate the device node in Device Manager (devmgmt.msc) named **UCSI USB Connector Manager**. The node is under the **Universal Serial Bus controllers** category.
2.  Right-click on the device, and select **Properties** and open the **Details** tab.
3.  Select **Device Instance Path** from the drop-down and note the property value.
4.  Open Registry Editor (regedit.exe).
5.  Navigate to the device instance path under this key.

    HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Enum\\&lt;device-instance-path&gt;\\Device Parameters

6.  Create a DWORD value named **TestInterfaceEnabled** and set the value to 0x1.
7.  Restart the device by selecting the **Disable** option on the device node in Device Manager, and then selecting **Enable**. Alternatively, you can simply restart the PC.

You can view the help by running **UcsiControl.exe /?**.

Here are the common commands:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>UCSI command</th>
<th>UcsiControl.exe command</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PPM Reset</td>
<td><strong>UcsiControl.exe Send 0 1</strong></td>
</tr>
<tr class="even">
<td>Connector Reset</td>
<td><p>Soft reset: <strong>UcsiControl.exe Send 0 10003</strong></p>
<p>Hard reset: <strong>UcsiControl.exe Send 0 810003</strong></p></td>
</tr>
<tr class="odd">
<td>Set Notification Enable</td>
<td><p>All notifications: <strong>UcsiControl.exe Send 0 ffff0005</strong></p>
<p>Only command completion: <strong>UcsiControl.exe Send 0 00010005</strong></p>
<p>No notification: <strong>UcsiControl.exe Send 0 00000005</strong></p></td>
</tr>
<tr class="even">
<td>Get Capability</td>
<td><strong>UcsiControl.exe Send 0 6</strong></td>
</tr>
<tr class="odd">
<td>Get Connector Capability</td>
<td><strong>UcsiControl.exe Send 0 10007</strong></td>
</tr>
<tr class="even">
<td>Set UOM</td>
<td><p><strong>DFP: UcsiControl.exe Send 0 810008</strong></p>
<p><strong>UFP: UcsiControl.exe Send 0 1010008</strong></p>
<p><strong>DRP: UcsiControl.exe Send 0 2010008</strong></p></td>
</tr>
<tr class="odd">
<td>Set UOR</td>
<td><p><strong>DFP: UcsiControl.exe Send 0 810009</strong></p>
<p><strong>UFP: UcsiControl.exe Send 0 1010009</strong></p>
<p><strong>Accept: UcsiControl.exe Send 0 2010009</strong></p></td>
</tr>
<tr class="even">
<td>Set PDR</td>
<td><p><strong>Provider: UcsiControl.exe Send 0 81000B</strong></p>
<p><strong>Consumer: UcsiControl.exe Send 0 101000B</strong></p>
<p><strong>Accept: UcsiControl.exe Send 0 201000B</strong></p></td>
</tr>
<tr class="odd">
<td>Get PDOs</td>
<td><p><strong>Local Source: UcsiControl.exe Send 7 00010010</strong></p>
<p><strong>Local Sink: UcsiControl.exe Send 3 00010010</strong></p>
<p><strong>Remote Source: UcsiControl.exe Send 7 00810010</strong></p>
<p><strong>Remote Sink: UcsiControl.exe Send 3 00810010</strong></p></td>
</tr>
<tr class="even">
<td>Get Connector Status</td>
<td><strong>UcsiControl.exe Send 0 010012</strong></td>
</tr>
<tr class="odd">
<td>Get Error Status</td>
<td><strong>UcsiControl.exe Send 0 13</strong></td>
</tr>
</tbody>
</table>

 

## Related topics
[Architecture: USB Type-C design for a Windows system](architecture--usb-type-c-in-a-windows-system.md)  



