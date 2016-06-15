---
title: Use of Mapping Buffers in the Storport I/O Model
author: windows-driver-content
description: Use of Mapping Buffers in the Storport I/O Model
ms.assetid: cd22ec31-ff4d-42d4-a47d-7b8bd85804be
---

# Use of Mapping Buffers in the Storport I/O Model


## <span id="ddk_use_of_mapping_buffers_in_the_storport_i_o_model_kg"></span><span id="DDK_USE_OF_MAPPING_BUFFERS_IN_THE_STORPORT_I_O_MODEL_KG"></span>


In the SCSI Port I/O model, miniport drivers can require the port driver to allocate and map system virtual memory for SRB I/O buffers. Miniport drivers configure the port driver to map I/O buffers by setting the **MapBuffers** member of the [**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](https://msdn.microsoft.com/library/windows/hardware/ff563900) structure to **TRUE**.

If the port driver is configured with **MapBuffers** set to **TRUE**, the **DataBuffer** member of each SRB that the miniport driver receives will contain a system virtual address of an I/O buffer. This address is valid in the address space of all processes in the system. Also, the miniport driver will be free to directly access the I/O buffer.

On the other hand, if the miniport driver sets **MapBuffers** to **FALSE**, **DataBuffer** will contain a virtual address that belongs to a particular process that is not necessarily valid in the context in which the miniport driver runs. Therefore, the miniport driver will not be able to access the memory area to which **DataBuffer** points.

In the Storport I/O model, miniport drivers are required to support DMA-based I/O. When DMA is used, there should be no need for miniport drivers to access an SRB's I/O buffers indirectly through a system-wide virtual address. With this in view, the Storport I/O model defines a different set of values for the **MapBuffers** member of [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](https://msdn.microsoft.com/library/windows/hardware/ff563901).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>STOR_MAP_NO_BUFFERS</p></td>
<td align="left"><p>The Storport driver does not map data buffers for any type of SRB. Therefore, its miniport drivers must <em>not</em> directly access the data pointed to by the <strong>DataBuffer</strong> member in any of the SRBs it receives.</p></td>
</tr>
<tr class="even">
<td align="left"><p>STOR_MAP_ALL_BUFFERS</p></td>
<td align="left"><p>This feature is not currently implemented. If the <strong>MapBuffers</strong> member is assigned this value, the Storport driver interprets it as though it were STOR_MAP_NON_READ_WRITE_BUFFERS.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>STOR_MAP_NON_READ_WRITE_BUFFERS</p></td>
<td align="left"><p>The Storport driver maps the data buffers for the request, provided it is not a data transfer (read and write) request. Likewise, miniport drivers can access data in the SRB provided that the SRB does not belong to a read or a write request.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Use%20of%20Mapping%20Buffers%20in%20the%20Storport%20I/O%20Model%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


