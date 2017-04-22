---
title: GDI Support for Surfaces
description: GDI Support for Surfaces
ms.assetid: 78c1e09d-8c3e-4c5d-b670-2e4adf77814f
keywords:
- DrvEnableSurface
- DrvDisableSurface
- GDI WDK Windows 2000 display , surfaces
- graphics drivers WDK Windows 2000 display , surfaces
- drawing WDK GDI , surfaces
- surface enabling and disabling WDK GDI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI Support for Surfaces


## <span id="ddk_gdi_support_for_surfaces_gg"></span><span id="DDK_GDI_SUPPORT_FOR_SURFACES_GG"></span>


For each [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev), a driver must support the [**DrvEnableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556214) function. *DrvEnableSurface* sets up the surface to be drawn on and associates it with the PDEV. The driver must also support the [**DrvDisableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556200) function to disable created surfaces. Because GDI creates and maintains the surface, the driver relies on several GDI service functions, listed in the following table, to implement the enabling and disabling of surfaces.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function Name</th>
<th align="left">Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>EngAssociateSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564183)</p></td>
<td align="left"><p>Associates a surface with a PDEV and defines the drawing operations the driver writer wants to hook out for that surface. It uses the PDEV's default palette and style steps. The driver must make this call for the primary surface during the execution of [<strong>DrvEnableSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556214). The driver must also make this call when it enables a secondary surface before locking the surface to write on it.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngCheckAbort</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564189)</p></td>
<td align="left"><p>(Printers only) Enables a printer driver to determine whether its printer job has been terminated.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngCreateBitmap</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564199)</p></td>
<td align="left"><p>Creates a standard format [<em>DIB</em>](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-) bitmap. GDI can perform all drawing operations on this type of surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngCreateDeviceBitmap</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564204)</p></td>
<td align="left"><p>Creates a device-dependent bitmap which the driver is responsible for drawing on (although it can be created as a DIB, in which case the driver can call back to have GDI draw on it).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngCreateDeviceSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564206)</p></td>
<td align="left"><p>Creates a [<em>device-managed surface</em>](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface). The driver is responsible for managing certain drawing operations for this surface. The function returns a handle that the driver manages.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngCreateWnd</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564769)</p></td>
<td align="left"><p>Create a [<strong>WNDOBJ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570599) structure on a specified surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngDeleteSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564827)</p></td>
<td align="left"><p>Deletes a surface (DIB, device-dependent bitmap, or device-managed surface).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngDeleteWnd</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564830)</p></td>
<td align="left"><p>Deletes a [<strong>WNDOBJ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff570599) structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngEraseSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564857)</p></td>
<td align="left"><p>Fills a specified rectangle on a surface with a given color, effectively erasing it. This function should be called only to erase the surface of a GDI bitmap.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngLockDirectDrawSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564966)</p></td>
<td align="left"><p>Locks the kernel-mode handle of a DirectDraw surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngLockSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564968)</p></td>
<td align="left"><p>Gives the driver access to a created surface by creating a user object ([<strong>SURFOBJ</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569901)) for that surface. (The [primary surface](surface-negotiation.md) is not locked.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngMarkBandingSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564975)</p></td>
<td align="left"><p>(Printers only) Marks a surface as a banding surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngModifySurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564976)</p></td>
<td align="left"><p>Notifies GDI about the attributes of a surface that was created by the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>EngUnlockDirectDrawSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565042)</p></td>
<td align="left"><p>Releases the lock on a given DirectDraw specified surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>EngUnlockSurface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565422)</p></td>
<td align="left"><p>Unlocks a surface when the driver has finished a drawing operation (to be called when disabling a [secondary surface](surface-negotiation.md)).</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Support%20for%20Surfaces%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




