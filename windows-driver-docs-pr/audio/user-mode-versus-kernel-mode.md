---
title: User Mode Versus Kernel Mode
description: User Mode Versus Kernel Mode
ms.assetid: ee506167-6b64-4e50-9988-102416bcb056
keywords:
- software synthesizers WDK audio
- custom synths WDK audio
- DirectMusic WDK audio , user mode vs. kernel mode
- user-mode synths WDK audio , vs. kernel-mode
- kernel-mode synths WDK audio , vs. user-mode
- latency WDK audio , DirectMusic
- hardware synthesizers WDK audio
- time stamps WDK audio
- DirectMusic kernel-mode WDK audio , vs. user mode
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# User Mode Versus Kernel Mode


## <span id="user_mode_versus_kernel_mode"></span><span id="USER_MODE_VERSUS_KERNEL_MODE"></span>


A custom synth can be written to run in either user mode or kernel mode. In general, software synths are easier to implement in user mode, but they frequently can achieve lower latency in kernel mode. Hardware components can be supported only in kernel mode. Good reasons exist, however, for beginning development in user mode even if the final implementation is to run in kernel mode.

Building software synthesizers (and wave sinks) is much simpler in user mode. The user-mode interfaces are easy to use, and debugging is simplified. Another benefit is that the resulting component is a Microsoft Windows executable file. Because this executable file is a COM object, installing it is simply a matter of self-registering from the command line with regsvr32.exe. (The RegSvr32 system application calls your DLL's [**DllRegisterServer**](https://msdn.microsoft.com/library/windows/desktop/ms682162) function. For more information, see the Microsoft Windows SDK documentation.)

If a user-mode implementation is all you need, you can deliver your product with an application program instead of a driver. The user avoids a complicated driver-installation process, and no reboot is needed after installing. Your user-mode component can then be enumerated as one of the available ports, depending on whether you want other applications to be able to use it. For more information, see [Registering Your Synthesizer](registering-your-synthesizer.md).

The advantage of a kernel-mode software implementation is lower latency. With the advent of time-stamped messages, however, this advantage is not as great as it used to be. Legacy MIDI APIs had no time stamping, so when you played a note, that was exactly when it was queued to play. Time stamping makes it possible to queue notes to play at specified times in the future. Using time stamping means that the note plays at the correct time unless the advance warning is less than the latency inherent in the system.

Latency is only an issue when sounds are queued to play with little or no advance warning. Thus, kernel-mode implementations are recommended only when there is an undesirable limitation to a user-mode software implementation or when supporting hardware acceleration.

If you decide to do a kernel-mode implementation, the best approach is still to begin development in user mode. The source code for Microsoft's user-mode synth is provided in the Microsoft Windows Driver Kit (WDK), so you do not have to write a new synth from scratch. You can use the existing code to understand how the downloadable sounds (DLS) downloads are parsed. Then, you can add any new functionality (such as parsing additional chunks) and debug this logic in user mode first, stubbing out the routines that access the hardware. (A stubbed-out routine can either do nothing or emulate the hardware function in software.) For more information about DLS, see the Windows SDK documentation.

When you have your implementation working in user mode, you can move it down to kernel mode and make it work there. After you have the software version working in kernel mode, your next step is to begin moving the functionality to your hardware. The user-mode and kernel-mode software synths serve as useful intermediate steps in the process of getting your hardware synth up and running.

To summarize the recommendations above:

-   For software-only components, implement the components first in user mode (in order to work out the design issues with easy interfaces, debugging, installation, and removal) and then convert to kernel mode if necessary because of latency or other considerations.

-   For hardware components, first implement a software version in user mode (in order to work out the design issues with easy interfaces, debugging, installation, and removal), then convert it to a kernel-mode software version. Finally, connect the kernel-mode component to hardware, one feature at a time, until everything works as desired.

 

 




