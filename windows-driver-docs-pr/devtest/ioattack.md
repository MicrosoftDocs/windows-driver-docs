---
title: IoAttack
description: The Penetration Tests (Device Fundamentals) test, Run I/O Attack, performs the fuzz tests
ms.assetid: ae0eda5c-534e-44c2-a997-66fe1337ca9f
ms.date: 07/10/2018
ms.localizationpriority: medium
---

# IoAttack

> [!NOTE]
> IoSpy and IoAttack are no longer available in the WDK after Windows 10 Version 1703.
>
> As an alternative to these tools, consider using the fuzzing tests available in the HLK. Here are a few to consider.
> 
> [DF - Fuzz random IOCTL test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/236b8ad5-0ba1-4075-80a6-ae9dafb71c94)
>
> [DF - Fuzz sub-opens test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/92bf534e-aa48-4aeb-b3cd-e46fb7cc7d80)
>
> [DF - Fuzz zero length buffer FSCTL test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/5f5f6c7e-d5db-4ff1-8cee-da47203ab070)
>
> [DF - Fuzz random FSCTL test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/e529e34e-076a-4978-926f-7eca333e8f4d)
>
> [DF - Fuzz Misc API test (Reliability)](https://docs.microsoft.com/windows-hardware/test/hlk/testref/fb305d04-6e8c-4dfc-9984-9692df82fbd8)
>
> You can also use the [Kernel synchronization delay fuzzing](https://docs.microsoft.com/windows-hardware/drivers/devtest/kernel-synchronization-delay-fuzzing) that is included with Driver Verifier.
>


The [Penetration Tests (Device Fundamentals)](penetration-tests--device-fundamentals-.md) test **Run I/O Attack** performs the fuzz tests. The **Run I/O Attack** test uses the [IoSpy data file](iospy.md) that was previously created through IoSpy on a test system.

Before running IoAttack on a test system, you must do the following:

-   Enable kernel-mode debugging on the test computer. This is done when you configure a computer for testing, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909), or [Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/hh698272).

-   Run the **Enable Driver Verifier test** to enable [Driver Verifier](driver-verifier.md) options on all of the drivers in the driver stack for the devices to be tested. In particular, you should enable the [Special Pool](special-pool.md) option. In the **Add or Remove Driver Tests** dialog box, the **Enable Driver Verifier test** is under All Tests\\Driver Verifier. See [How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime). For information about selecting and configuring tests and tool parameters, see [How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

-   Remove [IoSpy](iospy.md) from the test system. To do this, run the **Disable I/O Spy** test.

If any of these steps have been performed, you must reboot the test system before you run IoAttack.

For more information about how to run fuzz tests, see [How to Perform Fuzz tests with IoSpy and IoAttack](how-to-perform-fuzz-tests-with-iospy-and-ioattack.md).

 

 





