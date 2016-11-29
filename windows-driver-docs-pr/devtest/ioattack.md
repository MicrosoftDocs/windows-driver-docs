---
title: IoAttack
description: IoAttack
ms.assetid: ae0eda5c-534e-44c2-a997-66fe1337ca9f
---

# IoAttack


The [Penetration Tests (Device Fundamentals)](penetration-tests--device-fundamentals-.md) test **Run I/O Attack** performs the fuzz tests. The **Run I/O Attack** test uses the [IoSpy data file](iospy.md#iospy_data_file) that was previously created through IoSpy on a test system.

Before running IoAttack on a test system, you must do the following:

-   Enable kernel-mode debugging on the test computer. This is done when you configure a computer for testing, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909), or [Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/hh698272).

-   Run the **Enable Driver Verifier test** to enable [Driver Verifier](driver-verifier.md) options on all of the drivers in the driver stack for the devices to be tested. In particular, you should enable the [Special Pool](special-pool.md) option. In the **Add or Remove Driver Tests** dialog box, the **Enable Driver Verifier test** is under All Tests\\Driver Verifier. See [How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime). For information about selecting and configuring tests and tool parameters, see [How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

-   Remove [IoSpy](iospy.md) from the test system. To do this, run the **Disable I/O Spy** test.

If any of these steps have been performed, you must reboot the test system before you run IoAttack.

For more information about how to run fuzz tests, see [How to Perform Fuzz tests with IoSpy and IoAttack](how-to-perform-fuzz-tests-with-iospy-and-ioattack.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20IoAttack%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




