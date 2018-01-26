---
title: Load image using large pages if possible
description: Load image using large pages if possible
ms.assetid: 7f75b5bd-cc25-4f09-9d60-55b86969d16b
keywords: ["Load image using large pages if possible (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Load image using large pages if possible


## <span id="ddk_load_image_using_large_pages_if_possible_dtools"></span><span id="DDK_LOAD_IMAGE_USING_LARGE_PAGES_IF_POSSIBLE_DTOOLS"></span>


The **Load image using large pages if possible** setting directs the system to use large pages (4 MB) rather than the standard small pages (4 KB) when mapping binaries into the process address space.

This setting is most helpful for large executable files, because it significantly reduces the number of page table entries in physical memory.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>lpg</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>(none)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>Image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This setting is not technically a global flag, because its value is stored in a separate registry entry, not as a value of the GlobalFlag registry entry. As a result, you cannot set it by using a hexadecimal value, and when you select this setting for an image file, it appears in the **Other settings** field of the display.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Load%20image%20using%20large%20pages%20if%20possible%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




