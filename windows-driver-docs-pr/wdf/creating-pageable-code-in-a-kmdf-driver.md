---
title: Creating Pageable Code in a KMDF Driver
description: Creating Pageable Code in a KMDF Driver
ms.assetid: 5c694ae2-2a16-4c2f-84b0-62e26f4121bc
keywords:
- pageable drivers WDK KMDF
- KMDF WDK , pageable drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Pageable Code in a KMDF Driver


*Pageable code* is code that can be written to the computer's paging file when the code is not being used. You can make part of your driver pageable to reduce its load image and initial load time, and to reduce the amount of your driver's code that uses the computer's limited nonpaged memory pool.

To help you determine whether pageable code or data is appropriate for your driver, do the following:

1.  Identify pageable sections in your driver.

    Pageable sections are not loaded into memory until they are needed. For information about how to create pageable sections in a driver, see [Making Drivers Pageable](https://msdn.microsoft.com/library/windows/hardware/ff554346).

2.  Make sure that paged driver code does not impede a computer's ability to quickly awaken from a low-power state.

    All device object callback functions that drivers provide are called at IRQL = PASSIVE\_LEVEL, which enables you to make their code pageable (as described in [Making Drivers Pageable](https://msdn.microsoft.com/library/windows/hardware/ff554346)).

    However, you should not make a callback function's code pageable if the framework calls the callback function when the device leaves a low-power state and returns to its working (D0) state.

    If such code is pageable, the code might be written to the paging file before the computer enters a sleep state. Therefore, the computer will be slower to awaken because your code cannot be reloaded (and therefore your device cannot become fully operational) until the paging disk's power is restored.

    Therefore, the callback functions that are listed in the [A Device Returns to Its Working State](a-device-returns-to-its-working-state.md) topic should not be pageable.

3.  Determine whether your driver requires access to pageable data outside the driver, such as files, the registry, or paged pool, during power transitions.

    For information about how to enable and disable a driver's ability to access pageable data during power transitions, see [**WdfDeviceInitSetPowerPageable**](https://msdn.microsoft.com/library/windows/hardware/ff546766) and [**WdfDeviceInitSetPowerNotPageable**](https://msdn.microsoft.com/library/windows/hardware/ff546147).

    For information about how to determine when your driver is in a nonpageable state, see [**WdfDevStateIsNP**](https://msdn.microsoft.com/library/windows/hardware/ff546958).

 

 





