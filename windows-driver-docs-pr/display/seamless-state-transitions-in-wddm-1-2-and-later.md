---
title: Providing seamless state transitions in WDDM 1.2 and later
description: several features help to minimize screen flashes during the boot process, transitions from lower power states, and transitions back to operating system control.
ms.assetid: CD2208AA-62B6-4BAD-BE7C-0791B13D1E96
keywords:
- state transitions WDK display
- resume from hibernation WDK display
- firmware modes in display drivers WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Providing seamless state transitions in WDDM 1.2 and later


Starting in Windows 8, several features help to minimize or eliminate screen flashes and flickers during the boot process, during transitions from lower power states, and during transitions back to operating system control in driver upgrades or system bug checks. In addition, system firmware on Windows 8 and later computers must detect native resolution and timing of the integrated display panel at the time of power up and hand off this information to the operating system. Windows Display Driver Model (WDDM) 1.2 and later display miniport drivers must support this behavior.

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
<td align="left">Driver implementation—Full graphics and Display only</td>
<td align="left">Mandatory</td>
</tr>
<tr class="even">
<td align="left"><a href="https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit" data-raw-source="[WHCK](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit)">WHCK</a> requirements and tests</td>
<td align="left"><p><strong>System.Client.Firmware.UEFI.GOP.Display</strong></p>
<p><strong>Device.Graphics…PnpStopStartSupport</strong></p>
<p><strong>Device.Graphics…DisplayOutputControl</strong></p></td>
</tr>
</tbody>
</table>

 

## <span id="Transition_from_firmware_to_operating_system"></span><span id="transition_from_firmware_to_operating_system"></span><span id="TRANSITION_FROM_FIRMWARE_TO_OPERATING_SYSTEM"></span>Transition from firmware to operating system


All Windows 8 systems targeted for client SKUs must support the Unified Extensible Firmware Interface (UEFI) Graphics Output Protocol (GOP). During the boot phase, the GOP sets the native timing and native resolution on the integrated display panel of the system. When the operating system is ready to take over ownership of the display, the GOP hands off a frame buffer that can be used to scan out to the display. At this time the operating system doesn't attempt to reset the display timings or the resolution but simply uses the provided frame buffer, thereby eliminating one screen flash.

**Hardware certification requirements**

For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) on **System.Client.Firmware.UEFI.GOP.Display**.

## <span id="Transition_from_operating_system_to_driver"></span><span id="transition_from_operating_system_to_driver"></span><span id="TRANSITION_FROM_OPERATING_SYSTEM_TO_DRIVER"></span>Transition from operating system to driver


When the operating system hands ownership of the display to the WDDM driver after a boot, it initiates a Plug and Play (PnP) start of the device by calling the [*DxgkDdiStartDevice*](https://msdn.microsoft.com/library/windows/hardware/ff560775) function. Alternately, after resuming from hibernation the operating system starts the device by calling the [*DxgkDdiSetPowerState*](https://msdn.microsoft.com/library/windows/hardware/ff560764) function with the *DeviceUid* parameter set to **DISPLAY\_ADAPTER\_HW\_ID** (defined in Video.h). At this time typically the screen is blanked out (renders as black) while the WDDM graphics driver takes control.

The driver can call the [**DxgkCbAcquirePostDisplayOwnership**](https://msdn.microsoft.com/library/windows/hardware/hh451339) function (available starting in Windows 8) to query the operating system for the exact state of the current frame buffer and the display mode that was set by the firmware and boot loader. With the information in the [**DXGK\_DISPLAY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/hh464017) structure retrieved by this function, it's possible for the driver to keep the display controller active and not cause a re-synchronization of the monitor. Because the driver also has detailed information about the frame buffer, it's possible to perform a smoother transition.

More details on PnP start are given in [Plug and Play (PnP) in WDDM 1.2 and later](plug-and-play--pnp--start-and-stop-cases.md).

## <span id="Transition_from_driver_to_operating_system"></span><span id="transition_from_driver_to_operating_system"></span><span id="TRANSITION_FROM_DRIVER_TO_OPERATING_SYSTEM"></span>Transition from driver to operating system


The operating system can request a PnP stop of the display device by calling the [*DxgkDdiStopDevice*](https://msdn.microsoft.com/library/windows/hardware/ff560781) function. At this time typically the screen is blanked out (renders as black) while the operating system takes over the display control. The operating system can call the [*DxgkDdiStopDeviceAndReleasePostDisplayOwnership*](https://msdn.microsoft.com/library/windows/hardware/hh451415) function (available starting in Windows 8) that requires the WDDM driver to set up a frame buffer configured for scan out. The operating system can render into this frame buffer while it's in control of the display, making it possible to perform a smooth transition.

More details on PnP stop, including additional scenarios, are given in [Plug and Play (PnP) in WDDM 1.2 and later](plug-and-play--pnp--start-and-stop-cases.md).

**Hardware certification requirements**

For more info about this handoff, refer to the relevant [WHCK documentation](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics…PnpStopStartSupport**.

## <span id="Transition_to_operating_system_without_disabling_driver"></span><span id="transition_to_operating_system_without_disabling_driver"></span><span id="TRANSITION_TO_OPERATING_SYSTEM_WITHOUT_DISABLING_DRIVER"></span>Transition to operating system without disabling driver


Sometimes the operating system experiences an unrecoverable error and has to issue a system bug check. When this happens, there are certain cases where the operating system has to take control of the display but doesn't have the ability to stop the WDDM driver. WDDM 1.2 and later drivers are required to implement the [*DxgkDdiSystemDisplayEnable*](https://msdn.microsoft.com/library/windows/hardware/hh451426) and [*DxgkDdiSystemDisplayWrite*](https://msdn.microsoft.com/library/windows/hardware/hh451429) functions, which let the operating system seamlessly transition to a state where it can display the error screen while maintaining the graphical interface at a high resolution and color depth. This transition eliminates a jarring user experience.

**Hardware certification requirements**

For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics…DisplayOutputControl**.

## <span id="Windows_8_firmware_mode_changes"></span><span id="windows_8_firmware_mode_changes"></span><span id="WINDOWS_8_FIRMWARE_MODE_CHANGES"></span>Windows 8 firmware mode changes


These are changes to the firmware's display mode before the firmware hands off control to the operating system:

<span id="_1.2_and_later_drivers__dxgkddi_interface_version____dxgkddi_interface_version_win8_"></span><span id="_1.2_AND_LATER_DRIVERS__DXGKDDI_INTERFACE_VERSION____DXGKDDI_INTERFACE_VERSION_WIN8_"></span>WDDM 1.2 and later drivers (**DXGKDDI\_INTERFACE\_VERSION** &gt;= **DXGKDDI\_INTERFACE\_VERSION\_WIN8**)  
To further eliminate display flashes, starting with Windows 8, Int10 mode change requests are not called on the firmware for WDDM 1.2 and later drivers.

In addition, if a mode change occurs while the monitor is turned off, the operating system calls the [*DxgkDdiCommitVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559597) function only once, with the *pCommitVidPnArg* parameter set to the value it would have if the monitor were turned on, and the **PathPoweredOff** member of *pCommitVidPnArg*-&gt;**Flags** set to **TRUE**.

<span id="_1.0_and_1.1_drivers__DXGKDDI_INTERFACE_VERSION___DXGKDDI_INTERFACE_VERSION_WIN8_"></span><span id="_1.0_and_1.1_drivers__dxgkddi_interface_version___dxgkddi_interface_version_win8_"></span><span id="_1.0_AND_1.1_DRIVERS__DXGKDDI_INTERFACE_VERSION___DXGKDDI_INTERFACE_VERSION_WIN8_"></span>WDDM 1.0 and 1.1 drivers (**DXGKDDI\_INTERFACE\_VERSION** &lt; **DXGKDDI\_INTERFACE\_VERSION\_WIN8**)  
For WDDM versions 1.0 and 1.1 drivers running on Windows 8, during the boot process or when resuming from hibernation, calls into Int10 VGA mode 0x12 are made that set the display resolution to the monitor's native high resolution. Prior to Windows 8, an Int10 VGA mode 0x12 call set the display resolution to 640 x 480 pixels, at 16 bits per pixel, with no flashing cursor, to show the operating system splash screen image.

However, for WDDM versions 1.0 and 1.1 drivers that indicate they don't support high-resolution mode, starting in Windows 8 a boot into VGA mode 0x12 sets the display resolution to 640 x 480 pixels, at 16 bits per pixel, with no flashing cursor. When the system resumes from hibernation, the display resolution will still be set to the monitor's native high resolution.

In addition, if a mode change occurs while the monitor is turned off, the operating system calls the [*DxgkDdiCommitVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559597) function as described above for WDDM 1.2 drivers, plus it calls *DxgkDdiCommitVidPn* a *second* time with an empty video present network (VidPN) in *pCommitVidPnArg*-&gt;**hFunctionalVidPn** , and none of the flag values set in *pCommitVidPnArg*-&gt;**Flags**.

This two-part calling sequence also occurs when the system resumes after hibernation and monitor sync generation is to remain enabled. In this case the driver should take no action when it receives the second call to [*DxgkDdiCommitVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559597).

 

 





