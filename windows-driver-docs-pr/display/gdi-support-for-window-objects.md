---
title: GDI Support for Window Objects
description: GDI Support for Window Objects
ms.assetid: 288120e0-e43c-4733-8bba-0e310ed55aae
keywords:
- GDI WDK Windows 2000 display , window objects
- graphics drivers WDK Windows 2000 display , window objects
- drawing WDK GDI , window objects
- window objects WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Support for Window Objects


## <span id="ddk_gdi_support_for_window_objects_gg"></span><span id="DDK_GDI_SUPPORT_FOR_WINDOW_OBJECTS_GG"></span>


GDI provides support for window creation and deletion, and for the enumeration of rectangles in a window.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564769" data-raw-source="[&lt;strong&gt;EngCreateWnd&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564769)"><strong>EngCreateWnd</strong></a></p></td>
<td align="left"><p>Create a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570599" data-raw-source="[&lt;strong&gt;WNDOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570599)"><strong>WNDOBJ</strong></a> structure on a specified surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564830" data-raw-source="[&lt;strong&gt;EngDeleteWnd&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564830)"><strong>EngDeleteWnd</strong></a></p></td>
<td align="left"><p>Deletes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570599" data-raw-source="[&lt;strong&gt;WNDOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570599)"><strong>WNDOBJ</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570602" data-raw-source="[&lt;strong&gt;WNDOBJ_bEnum&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570602)"><strong>WNDOBJ_bEnum</strong></a></p></td>
<td align="left"><p>Gets a collection of rectangles from the visible region of a window.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570603" data-raw-source="[&lt;strong&gt;WNDOBJ_cEnumStart&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570603)"><strong>WNDOBJ_cEnumStart</strong></a></p></td>
<td align="left"><p>Sets parameters for enumeration of rectangles in the visible region of a window.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff570606" data-raw-source="[&lt;strong&gt;WNDOBJ_vSetConsumer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570606)"><strong>WNDOBJ_vSetConsumer</strong></a></p></td>
<td align="left"><p>Sets a driver-defined value in the <strong>pvConsumer</strong> member of the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff570599" data-raw-source="[&lt;strong&gt;WNDOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570599)"><strong>WNDOBJ</strong></a> structure.</p></td>
</tr>
</tbody>
</table>

 

 

 





