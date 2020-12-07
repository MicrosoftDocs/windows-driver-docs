---
title: Display Samples
description: Display Samples
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Display Samples


### <span id="display_samples"></span><span id="DISPLAY_SAMPLES"></span>

Starting with Windows 8, [samples are available for download](https://go.microsoft.com/fwlink/p/?LinkId=618052) from the Hardware Dev Center. For Windows 7 and earlier, samples and documentation were included in the Windows Driver Kit (WDK) or Driver Development Kit (DDK).

<table>
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Sample name</th>
<th align="left">Build environment</th>
<th align="left">Target operating system</th>
<th align="left">PnP driver</th>
<th align="left">In-box driver</th>
<th align="left">Sample description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://go.microsoft.com/fwlink/p/?LinkId=618052" data-raw-source="[Kernel mode display-only miniport driver](https://go.microsoft.com/fwlink/p/?LinkId=618052)">Kernel mode display-only miniport driver</a></p>
<p>Available in the Hardware Dev Center.</p></td>
<td align="left"><p></p>
Windows 8</td>
<td align="left"><p></p>
Windows 8</td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Implements most of the device driver interfaces (DDIs) that a display-only miniport driver should provide to the Windows Display Driver Model (WDDM).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://go.microsoft.com/fwlink/p/?LinkId=618052" data-raw-source="[PixLib](https://go.microsoft.com/fwlink/p/?LinkId=618052)">PixLib</a></p>
<p>Available in the Hardware Dev Center.</p></td>
<td align="left"><p></p>
Windows 8
Windows 7
Windows Server 2008
Windows Vista
Windows Server 2003
Windows XP</td>
<td align="left"><p></p>
Windows 8
Windows 7
Windows Server 2008
Windows Vista
Windows Server 2003
Windows XP</td>
<td align="left"><p>No</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Demonstrates how to implement the <a href="/windows-hardware/drivers/display/cpixel-support-methods-for-lightweight-mip-maps" data-raw-source="[CPixel](./cpixel-support-methods-for-lightweight-mip-maps.md)">CPixel</a> class.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Mirror - Mirror driver for mirroring GDI content</p></td>
<td align="left"><p></p>
Windows 7
Windows Server 2008
Windows Vista
Windows Server 2003
Windows XP
Windows 2000</td>
<td align="left"><p></p>
Windows 7
Windows Server 2008
Windows Vista
Windows Server 2003
Windows XP
Windows 2000</td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Demonstrates a driver that performs <a href="mirror-drivers.md" data-raw-source="[video mirroring](mirror-drivers.md)">video mirroring</a>.</p>
<div class="alert">
<strong>Note</strong>  Starting with Windows 8, mirror drivers will not install on the system.
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td align="left"><p>MonINF</p></td>
<td align="left"><p></p>
Windows 7
Windows Server 2008
Windows Vista</td>
<td align="left"><p></p>
Windows 7
Windows Server 2008
Windows Vista</td>
<td align="left"><p>No</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Demonstrates how monitor manufacturers can avoid reflashing the monitor's EEPROM by implementing a monitor INF that overrides part of, or the entire, EDID information in software.</p></td>
</tr>
</tbody>
</table>

 

