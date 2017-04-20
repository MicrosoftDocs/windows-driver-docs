---
title: GDI Support for Window Objects
description: GDI Support for Window Objects
ms.assetid: 288120e0-e43c-4733-8bba-0e310ed55aae
keywords:
- GDI WDK Windows 2000 display , window objects
- graphics drivers WDK Windows 2000 display , window objects
- drawing WDK GDI , window objects
- window objects WDK GDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left"><p>[<strong>EngCreateWnd</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564769)</p></td>
<td align="left"><p>Create a [<strong>WNDOBJ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570599) structure on a specified surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngDeleteWnd</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564830)</p></td>
<td align="left"><p>Deletes a [<strong>WNDOBJ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570599) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WNDOBJ_bEnum</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570602)</p></td>
<td align="left"><p>Gets a collection of rectangles from the visible region of a window.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>WNDOBJ_cEnumStart</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570603)</p></td>
<td align="left"><p>Sets parameters for enumeration of rectangles in the visible region of a window.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>WNDOBJ_vSetConsumer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570606)</p></td>
<td align="left"><p>Sets a driver-defined value in the <strong>pvConsumer</strong> member of the specified [<strong>WNDOBJ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570599) structure.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Support%20for%20Window%20Objects%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




