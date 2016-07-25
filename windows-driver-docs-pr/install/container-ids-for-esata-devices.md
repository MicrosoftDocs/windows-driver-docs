---
title: Container IDs for eSATA Devices
description: Container IDs for eSATA Devices
ms.assetid: 991836f1-936c-4051-ac3b-ad491a4ca221
---

# Container IDs for eSATA Devices


The External Serial Advanced Technology Attachment (eSATA) bus cannot report a container ID. When the Windows operating system determines the device container grouping for an eSATA device, it relies on the removable capability that the ATA bus driver returns.

The ATA bus driver determines that the eSATA device is removable by reading the following Advanced Host Controller Interface (AHCI) register bits.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">AHCI register</th>
<th align="left">Byte offset</th>
<th align="left">Bit location</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>HBA Capabilities (CAP))</p></td>
<td align="left"><p>0x000</p></td>
<td align="left"><p>5 - Supports External SATA (SXS)</p></td>
<td align="left"><p>When set to 1, this bit value indicates that the host bus adapter (HBA) has one or more SATA ports with a signal-only connector that is externally available (such as an eSATA connector).</p>
<p>If this bit is set to 1, software can reference the PxCMD.ESP bit to determine whether a specific port has its signal connector externally available as a signal-only connector (that is, power is not part of that connector).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Port x Command and Status (PxCMD)</p></td>
<td align="left"><p>0x18</p></td>
<td align="left"><p>18 - Hot-Plug Capable Port (HPCP)</p></td>
<td align="left"><p>When set to 1, this bit value indicates that the signal and power connectors for the port are externally available through a joint signal and power connector.</p>
<p></p>
<div class="alert">
<strong>Note</strong>  This only applies to blindmate connectors that support hot-plug capabilities.
</div>
<div>
 
</div>
.</td>
</tr>
<tr class="odd">
<td align="left"><p>Port x Command and Status (PxCMD)</p></td>
<td align="left"><p>0x18</p></td>
<td align="left"><p>21 - External SATA Port (ESP)</p></td>
<td align="left"><p>When set to 1, this bit value indicates that the signal connector for the port is externally available on a signal-only connector (such as an eSATA connector). Because of this, the port may experience hot-plug events.</p>
<p>If ESP is set to 1, the PxCMD.HPCP bit must be cleared to 0 and the CAP.SXS bit must be set to 1.</p></td>
</tr>
</tbody>
</table>

 

The ATA bus driver marks any device that is attached to the eSATA port as removable if one of the following is true:

-   The HPCP bit is set to 1, which indicates that the eSATA port is an external port that supports hot-plug operations.

-   The SXS and ESP bits are both set to 1, which indicates that the SATA port is an external signal-only port.

**Note**   These conditions are mutually exclusive. An eSATA port may declare itself to be either an external hot-plug-capable port or an external signal-only port, but not both.

 

For more information about the SATA and eSATA interface, refer to the [Serial ATA Advanced Host Controller Interface (AHCI) 1.3 specification](http://go.microsoft.com/fwlink/p/?linkid=148284).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Container%20IDs%20for%20eSATA%20Devices%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




