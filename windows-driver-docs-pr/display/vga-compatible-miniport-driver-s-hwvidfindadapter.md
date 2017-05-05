---
title: VGA-Compatible Miniport Driver's HwVidFindAdapter
description: VGA-Compatible Miniport Driver's HwVidFindAdapter
ms.assetid: 4538e95f-e84d-434c-a674-e1d1d4e9e5a0
keywords:
- video miniport drivers WDK Windows 2000 , VGA, HwVidFindAdapter
- VGA WDK video miniport , HwVidFindAdapter
- HwVidFindAdapter
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20VGA-Compatible%20Miniport%20Driver's%20HwVidFindAdapter%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




