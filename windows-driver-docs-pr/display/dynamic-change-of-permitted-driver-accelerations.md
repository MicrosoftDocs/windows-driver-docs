---
title: Dynamic Change of Permitted Driver Accelerations
description: Dynamic Change of Permitted Driver Accelerations
ms.assetid: a80bb755-f4ff-4d5d-aff1-28f8262061ae
keywords:
- acceleration levels WDK Windows 2000 display
- driver accelerations WDK Windows 2000 display
- Control Panel slider control WDK Windows 2000 display
- GDI acceleration changes WDK Windows 2000 display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Dynamic Change of Permitted Driver Accelerations


## <span id="ddk_dynamic_change_of_permitted_driver_accelerations_gg"></span><span id="DDK_DYNAMIC_CHANGE_OF_PERMITTED_DRIVER_ACCELERATIONS_GG"></span>


The driver's acceleration level can be changed through the user interface by using the slider that is produced by clicking on the Display icon in Control Panel. Depending on the value set with this slider, GDI allows the following levels of driver accelerations listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>All display driver accelerations are permitted.</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>[<strong>DrvSetPointerShape</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556289) and [<strong>DrvCreateDeviceBitmap</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556185) are disabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>In addition to 1, more sophisticated display driver accelerations are disallowed, including [<strong>DrvStretchBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556302), [<strong>DrvFillPath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556220), [<strong>DrvGradientFill</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556236), [<strong>DrvLineTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556245), [<strong>DrvAlphaBlend</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556176), and [<strong>DrvTransparentBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557283).</p></td>
</tr>
<tr class="even">
<td align="left"><p>3</p></td>
<td align="left"><p>In addition to 2, all DirectDraw and Direct3D accelerations are disallowed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>4</p></td>
<td align="left"><p>In addition to 3, almost all display driver accelerations are disallowed, except for solid color fills, [<strong>DrvCopyBits</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556182), [<strong>DrvTextOut</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557277), and [<strong>DrvStrokePath</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556316). [<strong>DrvEscape</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556217) is disabled.</p></td>
</tr>
<tr class="even">
<td align="left"><p>5</p></td>
<td align="left"><p>No hardware accelerations are allowed. The driver will only be called to do bit-block transfers from a system memory surface to the screen.</p></td>
</tr>
</tbody>
</table>

 

A display driver can determine the current acceleration level by:

-   Receiving notification of a change to the acceleration level from GDI by implementing [**DrvNotify**](https://msdn.microsoft.com/library/windows/hardware/ff556252).

-   Calling [**EngQueryDeviceAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff564986) to query the current acceleration level.

 

 





