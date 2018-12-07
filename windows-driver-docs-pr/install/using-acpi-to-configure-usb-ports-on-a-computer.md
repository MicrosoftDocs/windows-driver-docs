---
title: Using ACPI to Configure USB Ports on a Computer
description: Using ACPI to Configure USB Ports on a Computer
ms.assetid: 999f9fef-512c-415a-abc6-d64560c5c2f8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using ACPI to Configure USB Ports on a Computer


If the system requires ACPI BIOS changes to accurately reflect the USB port configuration, you should consider the user's ability to connect a device to the port when you configure the port.

If you use ACPI to specify the configuration of a USB port, you must define the USB port capabilities (**_UPC**) and physical location description (**_PLD**) objects. Although the ACPI 6.0 specification does not specifically prohibit the use of only the **_UPC** object, the use of both objects more precisely indicates the user's ability to connect devices to the port. Using only the **_UPC** object might not set the device container grouping correctly or as expected.

Devices that are attached to the port are removable from the hub if the **DeviceRemovable** bit is set. The following table shows how the values of the ACPI objects for a given port affect the value of the USB hub descriptor **DeviceRemovable** bit that Windows reports for the device.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">USB Port Status</th>
<th align="left">Example</th>
<th align="left">_UPC.PortIsConnectable byte</th>
<th align="left">_PLD.UserVisible bit (bit 64)</th>
<th align="left">Resulting DeviceRemovable Bit Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Port is visible and the user can freely connect and disconnect devices.</p></td>
<td align="left"><p>Port is exposed on the face of a panel on the computer that is visible to the user.</p></td>
<td align="left"><p>Set (0xFF)</p></td>
<td align="left"><p>Set (1)</p></td>
<td align="left"><p>Set</p></td>
</tr>
<tr class="even">
<td align="left"><p>Port is hidden or internal and user cannot freely connect and disconnect devices.</p></td>
<td align="left"><p>Port is directly hard-wired to an integrated device, such as a laptop webcam or an internal USB hub.</p></td>
<td align="left"><p>Set (0xFF)</p></td>
<td align="left"><p>Cleared</p></td>
<td align="left"><p>Cleared</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Port is physically implemented by the USB host controller, but is not used.</p></td>
<td align="left"><p>Port is an excess port that is not connected to a port plug terminal or an integrated device.</p></td>
<td align="left"><p>Cleared (0x00)</p></td>
<td align="left"><p>Clear</p></td>
<td align="left"><p>Cleared</p></td>
</tr>
</tbody>
</table>

 

**Note**   It is an invalid configuration to define a port as not connectable but visible to the user.

 

The following examples show correctly formed ACPI Source Language (ASL) that demonstrates the use of the **_UPC** and **_PLD** objects to describe a USB port:

-   To specify a port that is internal (not user visible) and can be connected to an integrated device, the **_UPC.PortIsConnectable** byte must be set to 0xFF and the **_PLD.UserVisible** bit must be set to 0.

    In the following example the device is grouped with the computer's device container.

    ```cpp
    Name(_UPC, Package(){
        0xFF,         // Port is connectable
        0xFF,         // Connector type (N/A for non-visible ports)
        0x00000000,   // Reserved 0, must be zero
        0x00000000})  // Reserved 1, must be zero

    Name(_PLD, Buffer(0x10){
        0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x30, 0x1C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00})
    ```

-   To specify a port that is external (user visible) and can be connected to an external device, the **_UPC.PortIsConnectable** byte must be set to 0xFF and the **_PLD.UserVisible** bit must be set to 1. The _**UPC**.**PortConnectorType** byte must be set to the appropriate USB connector type as specified in Section 9.13 of the ACPI 3.0 specification.

    In the following example the device is assigned a new device container and is displayed as a separate physical device.

    ```cpp
    Name(_UPC, Package(){
        0xFF,         // Port is connectable
        0x00,         // Connector type, Type &#39;A&#39; in this case
        0x00000000,   // Reserved 0, must be zero
        0x00000000})  // Reserved 1, must be zero

    Name(_PLD, Buffer(0x10){
        0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x31, 0x1C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00})
    ```
    
A USB Type-C connector must be correctly described in ACPI in order to pass the [USB Type-C ACPI Validation](https://msdn.microsoft.com/library/windows/hardware/mt770585(v=vs.85).aspx) Hardware Lab Kit test.

Example _UPC for a USB Type-C connector:
```cpp
      Name(_UPC, Package(4){
        0x01,                       // Port is connectable
        0x09,                       // Connector type: Type C connector - USB2 and SS with Switch
        0x00000000,                 // Reserved0 – must be zero
        0x00000000})                // Reserved1 – must be zero
```

For more information about the ACPI 6.0 interface, see [Advanced Configuration and Power Interface Specification Revision 6.0](http://go.microsoft.com/fwlink/?LinkId=827852).

 

 





