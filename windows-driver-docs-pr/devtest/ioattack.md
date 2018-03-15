---
title: IoAttack
description: The Penetration Tests (Device Fundamentals) test, Run I/O Attack, performs the fuzz tests
ms.assetid: ae0eda5c-534e-44c2-a997-66fe1337ca9f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IoAttack


The [Penetration Tests (Device Fundamentals)](penetration-tests--device-fundamentals-.md) test **Run I/O Attack** performs the fuzz tests. The **Run I/O Attack** test uses the [IoSpy data file](iospy.md) that was previously created through IoSpy on a test system.

Before running IoAttack on a test system, you must do the following:

-   Enable kernel-mode debugging on the test computer. This is done when you configure a computer for testing, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909), or [Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/hh698272).

-   Run the **Enable Driver Verifier test** to enable [Driver Verifier](driver-verifier.md) options on all of the drivers in the driver stack for the devices to be tested. In particular, you should enable the [Special Pool](special-pool.md) option. In the **Add or Remove Driver Tests** dialog box, the **Enable Driver Verifier test** is under All Tests\\Driver Verifier. See [How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime). For information about selecting and configuring tests and tool parameters, see [How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

-   Remove [IoSpy](iospy.md) from the test system. To do this, run the **Disable I/O Spy** test.

If any of these steps have been performed, you must reboot the test system before you run IoAttack.

For more information about how to run fuzz tests, see [How to Perform Fuzz tests with IoSpy and IoAttack](how-to-perform-fuzz-tests-with-iospy-and-ioattack.md).

 

 





