---
title: Allocator Properties
author: windows-driver-content
description: Allocator Properties
ms.assetid: 851bc3d8-46f6-46d0-87a8-81de2536492a
keywords: ["allocator properties WDK video capture", "PROPSETID_ALLOCATOR_CONTROL"]
---

# Allocator Properties


The [PROPSETID\_ALLOCATOR\_CONTROL](https://msdn.microsoft.com/library/windows/hardware/ff567792) property set contains properties related to controlling the allocation and operations of video port surfaces. User-mode filters, such as the Overlay Mixer, use PROPSETID\_ALLOCATOR\_CONTROL. The following table describes properties that are part of the PROPSETID\_ALLOCATOR\_CONTROL property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_ALLOCATOR_CONTROL KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_ALLOCATOR_CONTROL_HONOR_COUNT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564276)</p></td>
<td><p>Controls how a filter determines the number of video port overlay surfaces to allocate.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564278)</p></td>
<td><p>Controls the dimensions of the video port overlay surface.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564267)</p></td>
<td><p>Describes the capture capabilities of the video port.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_INTERLEAVE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564271)</p></td>
<td><p>Returns if the video port supports interleaved capture.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Allocator%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


