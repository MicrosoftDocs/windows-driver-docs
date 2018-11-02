---
title: Container IDs for PCI Express Devices
description: Container IDs for PCI Express Devices
ms.assetid: ff86def3-a278-4f7b-a394-42f608f8993d
ms.date: 04/20/2017
ms.localizationpriority: medium
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

Be aware that if the device implements an _EJ0 method in the ACPI namespace, the ACPI driver marks the device as removable. This occurs regardless of the setting of the Slot Implemented or Hot-Plug Capable bits. For more information, see the [Hot-Plug PCI and Windows](http://go.microsoft.com/fwlink/p/?linkid=26278) white paper.

For more information about the PCIe interface, see the [PCIe Base](http://go.microsoft.com/fwlink/p/?linkid=69486) specification.

 

 





