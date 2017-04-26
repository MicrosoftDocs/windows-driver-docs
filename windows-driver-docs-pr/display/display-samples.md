---
title: Display Samples
description: Display Samples
ms.assetid: 4595369c-20fa-4c8d-ad1d-aada97ab9fc2
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Display Samples


### <span id="display_samples"></span><span id="DISPLAY_SAMPLES"></span>

Starting with Windows 8, samples are published in the [MSDN Developer Samples code gallery](http://go.microsoft.com/fwlink/p/?LinkId=618052), along with documentation. For Windows 7 and earlier, samples and documentation were included in the Windows Driver Kit (WDK) or Driver Development Kit (DDK).

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
<td align="left"><p>[Kernel mode display-only miniport driver](http://go.microsoft.com/fwlink/p/?LinkId=618052)</p>
<p>Available in the MSDN Developer Samples code gallery.</p></td>
<td align="left"><p></p>
Windows 8</td>
<td align="left"><p></p>
Windows 8</td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Implements most of the device driver interfaces (DDIs) that a display-only miniport driver should provide to the Windows Display Driver Model (WDDM).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[PixLib](http://go.microsoft.com/fwlink/p/?LinkId=618052)</p>
<p>Available in the MSDN Developer Samples code gallery.</p></td>
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
<td align="left"><p>Demonstrates how to implement the [CPixel](https://msdn.microsoft.com/library/windows/hardware/ff540585) class.</p></td>
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
<td align="left"><p>Demonstrates a driver that performs [video mirroring](mirror-drivers.md).</p>
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Display%20Samples%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




