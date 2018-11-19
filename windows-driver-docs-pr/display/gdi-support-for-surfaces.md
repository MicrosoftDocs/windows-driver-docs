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
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564183" data-raw-source="[&lt;strong&gt;EngAssociateSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564183)"><strong>EngAssociateSurface</strong></a></p></td>
<td align="left"><p>Associates a surface with a PDEV and defines the drawing operations the driver writer wants to hook out for that surface. It uses the PDEV&#39;s default palette and style steps. The driver must make this call for the primary surface during the execution of <a href="https://msdn.microsoft.com/library/windows/hardware/ff556214" data-raw-source="[&lt;strong&gt;DrvEnableSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556214)"><strong>DrvEnableSurface</strong></a>. The driver must also make this call when it enables a secondary surface before locking the surface to write on it.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564189" data-raw-source="[&lt;strong&gt;EngCheckAbort&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564189)"><strong>EngCheckAbort</strong></a></p></td>
<td align="left"><p>(Printers only) Enables a printer driver to determine whether its printer job has been terminated.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564199" data-raw-source="[&lt;strong&gt;EngCreateBitmap&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564199)"><strong>EngCreateBitmap</strong></a></p></td>
<td align="left"><p>Creates a standard format <a href="https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-" data-raw-source="[&lt;em&gt;DIB&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-)"><em>DIB</em></a> bitmap. GDI can perform all drawing operations on this type of surface.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564204" data-raw-source="[&lt;strong&gt;EngCreateDeviceBitmap&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564204)"><strong>EngCreateDeviceBitmap</strong></a></p></td>
<td align="left"><p>Creates a device-dependent bitmap which the driver is responsible for drawing on (although it can be created as a DIB, in which case the driver can call back to have GDI draw on it).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564206" data-raw-source="[&lt;strong&gt;EngCreateDeviceSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564206)"><strong>EngCreateDeviceSurface</strong></a></p></td>
<td align="left"><p>Creates a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface" data-raw-source="[&lt;em&gt;device-managed surface&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-managed-surface)"><em>device-managed surface</em></a>. The driver is responsible for managing certain drawing operations for this surface. The function returns a handle that the driver manages.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564769" data-raw-source="[&lt;strong&gt;EngCreateWnd&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564769)"><strong>EngCreateWnd</strong></a></p></td>
<td align="left"><p>Create a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570599" data-raw-source="[&lt;strong&gt;WNDOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570599)"><strong>WNDOBJ</strong></a> structure on a specified surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564827" data-raw-source="[&lt;strong&gt;EngDeleteSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564827)"><strong>EngDeleteSurface</strong></a></p></td>
<td align="left"><p>Deletes a surface (DIB, device-dependent bitmap, or device-managed surface).</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564830" data-raw-source="[&lt;strong&gt;EngDeleteWnd&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564830)"><strong>EngDeleteWnd</strong></a></p></td>
<td align="left"><p>Deletes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff570599" data-raw-source="[&lt;strong&gt;WNDOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570599)"><strong>WNDOBJ</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564857" data-raw-source="[&lt;strong&gt;EngEraseSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564857)"><strong>EngEraseSurface</strong></a></p></td>
<td align="left"><p>Fills a specified rectangle on a surface with a given color, effectively erasing it. This function should be called only to erase the surface of a GDI bitmap.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564966" data-raw-source="[&lt;strong&gt;EngLockDirectDrawSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564966)"><strong>EngLockDirectDrawSurface</strong></a></p></td>
<td align="left"><p>Locks the kernel-mode handle of a DirectDraw surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564968" data-raw-source="[&lt;strong&gt;EngLockSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564968)"><strong>EngLockSurface</strong></a></p></td>
<td align="left"><p>Gives the driver access to a created surface by creating a user object (<a href="https://msdn.microsoft.com/library/windows/hardware/ff569901" data-raw-source="[&lt;strong&gt;SURFOBJ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569901)"><strong>SURFOBJ</strong></a>) for that surface. (The <a href="surface-negotiation.md" data-raw-source="[primary surface](surface-negotiation.md)">primary surface</a> is not locked.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564975" data-raw-source="[&lt;strong&gt;EngMarkBandingSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564975)"><strong>EngMarkBandingSurface</strong></a></p></td>
<td align="left"><p>(Printers only) Marks a surface as a banding surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564976" data-raw-source="[&lt;strong&gt;EngModifySurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564976)"><strong>EngModifySurface</strong></a></p></td>
<td align="left"><p>Notifies GDI about the attributes of a surface that was created by the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565042" data-raw-source="[&lt;strong&gt;EngUnlockDirectDrawSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565042)"><strong>EngUnlockDirectDrawSurface</strong></a></p></td>
<td align="left"><p>Releases the lock on a given DirectDraw specified surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565422" data-raw-source="[&lt;strong&gt;EngUnlockSurface&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565422)"><strong>EngUnlockSurface</strong></a></p></td>
<td align="left"><p>Unlocks a surface when the driver has finished a drawing operation (to be called when disabling a <a href="surface-negotiation.md" data-raw-source="[secondary surface](surface-negotiation.md)">secondary surface</a>).</p></td>
</tr>
</tbody>
</table>

 

 

 





