---
title: How to Perform Fuzz Tests with IoSpy and IoAttack
description: How to Perform Fuzz Tests with IoSpy and IoAttack
ms.assetid: f800e962-2a0f-4039-a479-395a62428b06
---

# How to Perform Fuzz Tests with IoSpy and IoAttack


To perform fuzz tests by using [IoSpy](iospy.md) and [IoAttack](ioattack.md), do the following:

1.  Install [IoSpy](iospy.md):

    To install IoSpy and enable fuzz tests on specific device(s), run the **Enable I/O Spy** test. The *DQ* parameter controls which devices the IoSpy filter driver is installed on.

2.  Run IOCTL and WMI tests on the specified devices:

    After you restart the test system, [IoSpy](iospy.md) is ready to filter IOCTL and WMI requests to the devices that were enabled for fuzz tests. You must now exercise the IOCTL and WMI code paths in drivers for these devices by using whatever tests are appropriate. This allows IoSpy to record as many details as possible based on these IOCTL and WMI requests. IoSpy saves these details in the [IoSpy Data File](iospy.md#iospy_data_file).

3.  Uninstall IoSpy:

    After you have fully exercised the IOCTL and WMI code paths, you must first uninstall IoSpy before you can run IoAttack to perform the fuzz tests. To uninstall [IoSpy](iospy.md), run the **Disable I/O Spy** test.

    This command removes the [IoSpy](iospy.md) filter driver from all devices that were enabled for fuzz tests. After the command is run, reboot the test system in order to unload the IoSpy filter driver from memory.

    **Note**  When you uninstall IoSpy, it will not delete the IoSpy data file. The location of this file is set by the *DFD* parameter to the **Enable I/O Spy** test. The default location is %SystemDrive%\\DriverTest\\IoSpy. For more information, see [IoSpy Data File](iospy.md#iospy_data_file).

     

4.  Run [IoAttack](ioattack.md):

    The test system is now ready to run the fuzz tests by running the **Run I/O Attack** test. For more information about how to run IoAttack, see [IoAttack](ioattack.md).

    **Note**   In order to verify the access privileges of your driver's IOCTL and WMI interfaces, you should run [IoAttack](ioattack.md) accounts with different privileges, such as a guest account and an administrator account.

     

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20to%20Perform%20Fuzz%20Tests%20with%20IoSpy%20and%20IoAttack%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




