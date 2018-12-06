---
title: Full-Screen VDMs in x86-based Machines
description: Full-Screen VDMs in x86-based Machines
ms.assetid: 5be4919d-d46f-430f-9d4f-670134379268
keywords:
- video miniport drivers WDK Windows 2000 , VGA, full-screen VDMs in x86-based machines
- VGA WDK video miniport , full-screen VDMs in x86-based machines
- full-screen VDMs in x86-based machines WDK video miniport
- x86-based machines WDK VGA-compatible video miniport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Full-Screen VDMs in x86-based Machines


## <span id="ddk_full_screen_vdms_in_x86_based_machines_gg"></span><span id="DDK_FULL_SCREEN_VDMS_IN_X86_BASED_MACHINES_GG"></span>


For performance reasons, when the user switches an MS-DOS application to full-screen mode in an x86-based machine, the display driver yields control of the adapter. The system VGA or a VGA-compatible miniport driver then hooks out from the V86 emulator all I/O instructions, such as application-issued **IN**, **REP INSB/INSW/INSD**, **OUT**, and **REP OUTSB/OUTSW/OUTSD** instructions, to the video I/O ports. These hooked I/O operations are forwarded to the VGA-compatible miniport driver's *SvgaHwIoPortXxx* functions.

However, for faster performance, a miniport driver can call [**VideoPortSetTrappedEmulatorPorts**](https://msdn.microsoft.com/library/windows/hardware/ff570366) to allow some I/O ports to be accessed directly by the application. The miniport driver continues to hook other I/O ports with its *SvgaHwIoPortXxx* to validate the application-issued instruction stream to those ports.

To prevent a full-screen application from issuing a sequence of instructions that might hang the machine, the *SvgaHwIoPortXxx* functions monitor the application instruction stream to a driver-determined set of adapter registers. A miniport driver must enable direct access only to I/O ports that are completely safe. For example, ports for the sequencer and miscellaneous output registers should always be hooked by the V86 emulator and trapped to the miniport driver-supplied *SvgaHwIoPortXxx* functions for validation.

Direct access to I/O ports for the application is determined by the IOPM (named for the x86 I/O permission map) that the VGA-compatible miniport driver sets by calling **VideoPortSetTrappedEmulatorPorts**. Note that the miniport driver can adjust the IOPM by calling this function to have access ranges, describing I/O ports, released for direct access by the application or retrapped to an *SvgaHwIoPortXxx* function. The current IOPM determines which ports can be accessed directly by the application and which remain hooked by the V86 emulator and trapped to an *SvgaHwIoPortXxx* function for validation.

By default, all I/O ports set up in such a miniport driver's emulator access ranges array are trapped to the corresponding *SvgaHwIoPortXxx* function. However, VGA-compatible miniport drivers usually call **VideoPortSetTrappedEmulatorPorts** on receipt of an IOCTL\_VIDEO\_ENABLE\_VDM request to reset the IOPM for the [*VDM*](https://msdn.microsoft.com/library/windows/hardware/ff556344#wdkgloss-vdm) to allow direct access to some of these I/O ports. Usually, such a driver allows direct access to all video adapter registers except the VGA sequencer registers and the miscellaneous output register, plus any SVGA adapter-specific registers that the driver writer has determined should always be validated by an *SvgaHwIoPortXxx* function.

 

 





