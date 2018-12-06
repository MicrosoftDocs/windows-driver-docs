---
title: Plug and Play (PnP) in WDDM 1.2 and later
description: All Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers must support the following behavior in response to start and stop requests.
ms.assetid: A95DCFEA-BC1B-4A13-9850-13814725D53E
keywords:
- Plug and Play in display drivers WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Plug and Play (PnP) in WDDM 1.2 and later


All Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers must support the following behavior in response to start and stop requests by the Plug and Play (PnP) infrastructure. Behavior can differ depending on whether the driver returns a success or failure code, or whether the system hardware is based on the basic input/output system (BIOS) or Unified Extensible Firmware Interface (UEFI).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Minimum WDDM version</td>
<td align="left">1.2</td>
</tr>
<tr class="even">
<td align="left">Minimum Windows version</td>
<td align="left">8</td>
</tr>
<tr class="odd">
<td align="left">Driver implementation-Full graphics and Display only</td>
<td align="left">Mandatory</td>
</tr>
<tr class="even">
<td align="left"><a href="https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit" data-raw-source="[WHCK](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit)">WHCK</a> requirements and tests</td>
<td align="left"><p><strong>Device.Graphics.WDDM12.Display.PnpStopStartSupport</strong></p></td>
</tr>
</tbody>
</table>

 

## <span id="Display_miniport_driver_PnP_DDI"></span><span id="display_miniport_driver_pnp_ddi"></span><span id="DISPLAY_MINIPORT_DRIVER_PNP_DDI"></span>Display miniport driver PnP DDI


Starting in Windows 8, the Microsoft DirectX graphics kernel subsystem provides this function that a driver can call if the display device is started or resumed from hibernation:

-   [**DxgkCbAcquirePostDisplayOwnership**](https://msdn.microsoft.com/library/windows/hardware/hh451339)

These functions and structure are available for the display miniport driver to implement WDDM 1.2 and later PnP requirements:

-   [*DxgkDdiStopDeviceAndReleasePostDisplayOwnership*](https://msdn.microsoft.com/library/windows/hardware/hh451415)
-   [*DxgkDdiSystemDisplayEnable*](https://msdn.microsoft.com/library/windows/hardware/hh451426)
-   [*DxgkDdiSystemDisplayWrite*](https://msdn.microsoft.com/library/windows/hardware/hh451429)
-   [**DXGK\_DISPLAY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/hh464017)

## <span id="PnP_start_operation"></span><span id="pnp_start_operation"></span><span id="PNP_START_OPERATION"></span>PnP start operation


A Plug and Play (PnP) start process on the display device occurs either during boot or during an upgrade from one display driver to another. In this case the driver must call the [*DxgkCbAcquirePostDisplayOwnership*](https://msdn.microsoft.com/library/windows/hardware/hh451339) function to get information about the frame buffer and to maintain display synchronization. Frame buffer information is provided either from the firmware or from the previous WDDM 1.2 and later driver that was loaded on the system.

During calls the operating system makes to [*DxgkDdiSetPowerState*](https://msdn.microsoft.com/library/windows/hardware/ff560764) function to return to the D0 power state, and to the [*DxgkDdiStartDevice*](https://msdn.microsoft.com/library/windows/hardware/ff560775) function, the WDDM 1.2 and later driver must set source visibility to false ([**DXGKARG\_SETVIDPNSOURCEVISIBILITY**](https://msdn.microsoft.com/library/windows/hardware/ff559486).**Visible** = **FALSE**) for all active video present network (VidPN) targets. In this case the display pipeline hardware must maintain sync signals with the monitor, but the pipeline must continue to send black pixel data to the monitor no matter what pixel data is present in the surface that's currently being scanned out. This means that the pixel pipeline is guaranteed to be blanking the monitor with all black pixels. Later, when the first frame is rendered into the frame buffer, the operating system sets source visibility to true.

All of these procedures keep the monitor synchronized and ensure that the user doesn't see flashes or flickers on the screen.

These are the return codes that the driver should return after a PnP start process.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Driver return code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="Success"></span><span id="success"></span><span id="SUCCESS"></span>Success</p></td>
<td align="left"><p>Behavior is the same as in Windows 7.</p>
<p>For a BIOS-based system, if the driver starts successfully, the frame buffer is still active and the driver must be ready to set to a valid mode.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Failure"></span><span id="failure"></span><span id="FAILURE"></span>Failure</p></td>
<td align="left"><p>For a BIOS-based system, the driver must leave the system in a BIOS-compatible state.</p>
<p>For a UEFI-based system, the driver must leave the display in the same mode that was set by the UEFI Graphics Output Protocol (GOP) so that the basic display driver can use the display. The driver must return a valid error code. If the driver cannot leave the GOP in a state that can be used by the basic display driver, the driver must return the <strong>STATUS_GRAPHICS_STALE_MODESET</strong> error code from Ntstatus.h, and the operating system causes a system bugcheck to occur.</p></td>
</tr>
</tbody>
</table>

 

## <span id="PnP_stop_operation"></span><span id="pnp_stop_operation"></span><span id="PNP_STOP_OPERATION"></span>PnP stop operation


A Plug and Play (PnP) stop process on the display device typically occurs when a driver is being upgraded to a new version. In this case the operating system calls the driver's [*DxgkDdiStopDeviceAndReleasePostDisplayOwnership*](https://msdn.microsoft.com/library/windows/hardware/hh451415) function, which requires the driver to provide accurate frame buffer information.

In the [*DxgkDdiStopDeviceAndReleasePostDisplayOwnership*](https://msdn.microsoft.com/library/windows/hardware/hh451415) call the driver must ensure that the source visibility for the active VidPn targets is true ([**DXGKARG\_SETVIDPNSOURCEVISIBILITY**](https://msdn.microsoft.com/library/windows/hardware/ff559486).**Visible** = **TRUE**). In addition, starting in WDDM 1.2 the driver needs to ensure that the surface that the pixel pipeline is programmed to scan out from is filled with black pixels. The driver should complete filling the surface with black pixels before source visibility is set to true.

Be sure to also implement [*DxgkDdiStopDevice*](https://msdn.microsoft.com/library/windows/hardware/ff560781) in your driver. In some cases the operating system might call *DxgkDdiStopDevice* instead of [*DxgkDdiStopDeviceAndReleasePostDisplayOwnership*](https://msdn.microsoft.com/library/windows/hardware/hh451415), or after a call to *DxgkDdiStopDeviceAndReleasePostDisplayOwnership* fails.

These are the return codes that the driver should return after a PnP stop process.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Driver return code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="Success__and_driver_returns_mode_information"></span><span id="success__and_driver_returns_mode_information"></span><span id="SUCCESS__AND_DRIVER_RETURNS_MODE_INFORMATION"></span>Success, and driver returns mode information</p></td>
<td align="left"><p>Before the driver is stopped it must set up a frame buffer, using the current resolution, that the basic display driver can use, and the driver must return this information when the operating system calls the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451415" data-raw-source="[&lt;em&gt;DxgkDdiStopDeviceAndReleasePostDisplayOwnership&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451415)"><em>DxgkDdiStopDeviceAndReleasePostDisplayOwnership</em></a> function. The saved mode information doesn&#39;t have to be compatible with BIOS, and the basic display driver won&#39;t offer a BIOS mode until the system is rebooted.</p>
<p>The operating system guarantees that it won&#39;t call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560781" data-raw-source="[&lt;em&gt;DxgkDdiStopDevice&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560781)"><em>DxgkDdiStopDevice</em></a> if <a href="https://msdn.microsoft.com/library/windows/hardware/hh451415" data-raw-source="[&lt;em&gt;DxgkDdiStopDeviceAndReleasePostDisplayOwnership&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451415)"><em>DxgkDdiStopDeviceAndReleasePostDisplayOwnership</em></a> returns <strong>STATUS_SUCCESS</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Success__and_driver_sets_the_Width_and_Height_members_of_the_DXGK_DISPLAY_INFORMATION_structure_to_zero"></span><span id="success__and_driver_sets_the_width_and_height_members_of_the_dxgk_display_information_structure_to_zero"></span><span id="SUCCESS__AND_DRIVER_SETS_THE_WIDTH_AND_HEIGHT_MEMBERS_OF_THE_DXGK_DISPLAY_INFORMATION_STRUCTURE_TO_ZERO"></span>Success, and driver sets the <strong>Width</strong> and <strong>Height</strong> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh464017" data-raw-source="[&lt;strong&gt;DXGK_DISPLAY_INFORMATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh464017)"><strong>DXGK_DISPLAY_INFORMATION</strong></a> structure to zero</p></td>
<td align="left"><p>This scenario is possible only if the system has two graphics cards, no monitors are connected to the current power-on self-test (POST) device, and the operating system calls the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451415" data-raw-source="[&lt;em&gt;DxgkDdiStopDeviceAndReleasePostDisplayOwnership&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451415)"><em>DxgkDdiStopDeviceAndReleasePostDisplayOwnership</em></a> function to stop the POST device.</p>
<p>In this case the current display continues to run on the second graphics adapter, and the basic display driver runs in headless mode on the adapter that supports the POST device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Failure"></span><span id="failure"></span><span id="FAILURE"></span>Failure</p></td>
<td align="left"><p>The operating system calls the Windows 7-style PnP stop driver interface through the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560781" data-raw-source="[&lt;em&gt;DxgkDdiStopDevice&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff560781)"><em>DxgkDdiStopDevice</em></a> function.</p>
<p>For a BIOS-based system, the driver must set the display into a BIOS-compatible mode.</p>
<p>For a UEFI-based system, the basic display driver runs in headless mode on the graphics adapter.</p></td>
</tr>
</tbody>
</table>

 

For further requirements on PnP and other state transitions, see [Providing seamless state transitions in WDDM 1.2 and later](seamless-state-transitions-in-wddm-1-2-and-later.md).

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics.WDDM12.Display.PnpStopStartSupport**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 





