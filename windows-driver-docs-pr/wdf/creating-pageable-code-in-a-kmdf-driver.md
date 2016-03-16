---
title: Creating Pageable Code in a KMDF Driver
description: Creating Pageable Code in a KMDF Driver
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 5c694ae2-2a16-4c2f-84b0-62e26f4121bc
keywords: ["pageable drivers WDK KMDF", "KMDF WDK pageable drivers"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20Pageable%20Code%20in%20a%20KMDF%20Driver%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




