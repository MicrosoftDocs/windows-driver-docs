---
title: Container IDs for PCI Express Devices
description: Container IDs for PCI Express Devices
ms.assetid: ff86def3-a278-4f7b-a394-42f608f8993d
---

# Container IDs for PCI Express Devices


The PCI Express (PCIe) bus cannot express a container ID. The Windows operating system relies on the removable capability that the PCI bus driver returns when it determines the device container grouping for a PCIe device.

The PCI bus driver determines that a PCIe device is removable by reading the following PCIe register bits.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">PCIe register</th>
<th align="left">Byte offset</th>
<th align="left">Bit location</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>PCI Express Capabilities</p></td>
<td align="left"><p>0x02</p></td>
<td align="left"><p>8 - Slot Implemented</p></td>
<td align="left"><p>When set to 1, this bit value indicates that the PCIe link that is associated with this port is connected to a physical slot, instead of being connected to an integrated component.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Slot Capabilities</p></td>
<td align="left"><p>0x14</p></td>
<td align="left"><p>6 - Hot-Plug Capable</p></td>
<td align="left"><p>When set to 1, this bit value indicates that this slot can support hot-plug operations.</p></td>
</tr>
</tbody>
</table>

 

The PCI bus driver marks a PCIe device as removable if both of the following conditions are satisfied:

-   The Slot Implemented bit is set to 1.

-   The Hot-Plug-Capable bit is set to 1:

The mechanism that is used to set these register bits varies by PCIe chipset version and manufacturer. For example, some chipsets let the firmware program these bits, whereas other chipsets require physical pins to be strapped to the voltage charge connection (Vcc) or ground (GND).

Be aware that if the device implements an \_EJ0 method in the ACPI namespace, the ACPI driver marks the device as removable. This occurs regardless of the setting of the Slot Implemented or Hot-Plug Capable bits. For more information, see the [Hot-Plug PCI and Windows](http://go.microsoft.com/fwlink/p/?linkid=26278) white paper.

For more information about the PCIe interface, see the [PCIe Base](http://go.microsoft.com/fwlink/p/?linkid=69486) specification.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Container%20IDs%20for%20PCI%20Express%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




