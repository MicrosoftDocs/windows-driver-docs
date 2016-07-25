---
title: Using ACPI to Configure USB Ports on a Computer
description: Using ACPI to Configure USB Ports on a Computer
ms.assetid: 999f9fef-512c-415a-abc6-d64560c5c2f8
---

# Using ACPI to Configure USB Ports on a Computer


If the system requires ACPI BIOS changes to accurately reflect the USB port configuration, you should consider the user's ability to connect a device to the port when you configure the port.

If you use ACPI to specify the configuration of a USB port, you must define the USB port capabilities (**\_UPC**) and physical location description (**\_PLD**) objects. Although the ACPI 3.0 specification does not specifically prohibit the use of only the **\_UPC** object, the use of both objects more precisely indicates the user's ability to connect devices to the port. Using only the **\_UPC** object might not set the device container grouping correctly or as expected.

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
<td align="left"><p>Set (OxFF)</p></td>
<td align="left"><p>Set (1)</p></td>
<td align="left"><p>Set</p></td>
</tr>
<tr class="even">
<td align="left"><p>Port is hidden or internal and user cannot freely connect and disconnect devices.</p></td>
<td align="left"><p>Port is directly hard-wired to an integrated device, such as a laptop webcam or an internal USB hub.</p></td>
<td align="left"><p>Set (OxFF)</p></td>
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

 

The following examples show correctly formed ACPI Source Language (ASL) that demonstrates the use of the **\_UPC** and **\_PLD** objects to describe a USB port:

-   To specify a port that is internal (not user visible) and can be connected to an integrated device, the **\_UPC.PortIsConnectable** byte must be set to 0xFF and the **\_PLD.UserVisible** bit must be set to 0.

    In the following example the device is grouped with the computer's device container.

    ```
    Name(_UPC, Package(){
        0xFF,         // Port is connectable
        0xFF,         // Connector type (N/A for non-visible ports)
        0x00000000,   // Reserved 0, must be zero
        0x00000000})  // Reserved 1, must be zero

    Name(_PLD, Buffer(0x10){
        0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x30, 0x1C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00})
    ```

-   To specify a port that is external (user visible) and can be connected to an external device, the **\_UPC.PortIsConnectable** byte must be set to 0xFF and the **\_PLD.UserVisible** bit must be set to 1. The \_**UPC**.**PortConnectorType** byte must be set to the appropriate USB connector type as specified in Section 9.14 of the ACPI 3.0 specification.

    In the following example the device is assigned a new device container and is displayed as a separate physical device.

    ```
    Name(_UPC, Package(){
        0xFF,         // Port is connectable
        0x00,         // Connector type, Type &#39;A&#39; in this case
        0x00000000,   // Reserved 0, must be zero
        0x00000000})  // Reserved 1, must be zero

    Name(_PLD, Buffer(0x10){
        0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x31, 0x1C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00})
    ```

For more information about the ACPI 3.0 interface, see [Advanced Configuration and Power Interface Specification Revision 3.0b](http://go.microsoft.com/fwlink/p/?linkid=145427).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20ACPI%20to%20Configure%20USB%20Ports%20on%20a%20Computer%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




