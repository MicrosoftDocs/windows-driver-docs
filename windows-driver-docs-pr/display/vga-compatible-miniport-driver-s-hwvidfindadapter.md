---
title: VGA-Compatible Miniport Driver's HwVidFindAdapter
description: VGA-Compatible Miniport Driver's HwVidFindAdapter
ms.assetid: 4538e95f-e84d-434c-a674-e1d1d4e9e5a0
keywords:
- video miniport drivers WDK Windows 2000 , VGA, HwVidFindAdapter
- VGA WDK video miniport , HwVidFindAdapter
- HwVidFindAdapter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# VGA-Compatible Miniport Driver's HwVidFindAdapter


## <span id="ddk_vga_compatible_miniport_driver_s_hwvidfindadapter_gg"></span><span id="DDK_VGA_COMPATIBLE_MINIPORT_DRIVER_S_HWVIDFINDADAPTER_GG"></span>


A VGA-compatible miniport driver's [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) function (or registry *HwVid..Callback*) must set up the following in the [**VIDEO\_PORT\_CONFIG\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff570531) buffer:

-   **NumEmulatorAccessEntries**, indicating the number of entries in the **EmulatorAccessEntries** array

-   **EmulatorAccessEntries**, pointing to a static array containing the given number of [**EMULATOR\_ACCESS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff564131)-type elements, each describing a range of I/O ports hooked from the V86 emulator and, by default, forwarded to an *SvgaHwIoPortXxx* function

    Each entry includes a starting I/O address, a range length, the size of access to be trapped (UCHAR, USHORT, or ULONG), whether the miniport driver supports input or output of string data through the I/O port(s), and the miniport driver-supplied *SvgaHwIoPortXxx* function that actually validates and, possibly, transfers the data. Each *SvgaHwIoPortXxx* function handles read (**IN** or **REP INSB/INSW/INSD**) and/or write (**OUT** or **REP OUTSB/OUTSW/OUTSD**) transfers of UCHAR-, USHORT-, or ULONG-sized data.

-   **EmulatorAccessEntriesContext**, a pointer to storage, such as an area in the miniport driver's device extension, in which the miniport driver's *SvgaHwIoPortXxx* functions can batch a sequence of application-issued instructions that require validation

-   **VdmPhysicalVideoMemoryAddress** and **VdmPhysicalVideoMemoryLength**, describing a range of video memory that must be mapped into the [*VDM*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-vdm) address space to support BIOS INT10 calls from full-screen MS-DOS applications

    The miniport driver can call the [**VideoPortInt10**](https://msdn.microsoft.com/library/windows/hardware/ff570321) function when such an application changes the video mode to one that the miniport driver's adapter can support.

-   **HardwareStateSize**, describing the minimum number of bytes required to store the hardware state for the adapter in response to an IOCTL\_VIDEO\_SAVE\_HARDWARE\_STATE request

    When the user switches a full-screen MS-DOS application to run in a window, the miniport driver must save the adapter state before the display driver regains control of the video adapter. Note that a VGA-compatible miniport driver also must support the reciprocal IOCTL\_VIDEO\_RESTORE\_HARDWARE\_STATE request because the user might switch the windowed application back to full-screen mode.

A VGA-compatible miniport driver's emulator access entries specify subsets of its access ranges array for the adapter. The emulator access entries can be and usually are all I/O ports in the mapped access ranges array set up by its [*HwVidFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff567332) function. The access ranges it passes in calls to [**VideoPortSetTrappedEmulatorPorts**](https://msdn.microsoft.com/library/windows/hardware/ff570366), defining the current IOPM and determining the I/O ports that are directly accessible by a full-screen MS-DOS application, specify subsets of the miniport driver's emulator access entries.

 

 





