---
title: Installing the Updated Version of the Driver Package
description: Installing the Updated Version of the Driver Package
ms.assetid: c2138956-a036-410d-b34e-b7b6efbcbace
---

# Installing the Updated Version of the Driver Package


After you [configure Windows to rank driver signatures equally](configuring-windows-to-rank-driver-signatures-equally.md), you can install the private build of the inbox driver on the target system. To install the private build, complete the following steps:

1.  Add the [driver package](driver-packages.md) to the driver store by using the [PnPUtil](https://msdn.microsoft.com/library/windows/hardware/ff550419) utility that is provided in Windows Vista and later versions of Windows. For example:

    ```
    pnputil.exe -a  sample.inf
    ```

2.  Use the DevCon Remove command to remove the device or device class that is installed by the updated driver package. The device or device class is specified through all or part of a [hardware ID](hardware-ids.md), [compatible ID](compatible-ids.md), or device instance ID of a device. For example:

    ```
    devcon remove "PCI\VEN_8086&amp;DEV_7110"
    ```

    The new driver is automatically loaded when the device is reinstalled after the system is restarted. To have DevCon automatically restart the system, add the conditional reboot parameter (**/r**) to the remove command.

    **Note**  The [DevCon](https://msdn.microsoft.com/library/windows/hardware/ff544707) tool is provided in the WDK. For more information about its commands, see [DevCon Commands](https://msdn.microsoft.com/library/windows/hardware/ff544766).

     

An alternative to the DevCon Remove command is to update the [driver package](driver-packages.md) by using one of the following:

-   Device Manager to perform an "update driver" operation on the device.

    From within Device Manager's window, right-click the device's name or icon and choose **Properties**. In the **Properties** window, click the Driver tab and then click the **Update Driver** button.

-   The DevCon Update command. For more information about this command, see [**DevCon Commands**](https://msdn.microsoft.com/library/windows/hardware/ff544766).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20the%20Updated%20Version%20of%20the%20Driver%20Package%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




