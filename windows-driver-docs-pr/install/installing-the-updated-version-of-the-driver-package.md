---
title: Installing the Updated Version of the Driver Package
description: Installing the Updated Version of the Driver Package
ms.date: 04/20/2017
---

# Installing the Updated Version of the Driver Package


After you [configure Windows to rank driver signatures equally](configuring-windows-to-rank-driver-signatures-equally.md), you can install the private build of the inbox driver on the target system. To install the private build, complete the following steps:

1.  Add the [driver package](driver-packages.md) to the driver store by using the [PnPUtil](../devtest/pnputil.md) utility that is provided in Windows Vista and later versions of Windows. For example:

    ```cpp
    pnputil.exe -a  sample.inf
    ```

2.  Use the DevCon Remove command to remove the device or device class that is installed by the updated driver package. The device or device class is specified through all or part of a [hardware ID](hardware-ids.md), [compatible ID](compatible-ids.md), or device instance ID of a device. For example:

    ```cpp
    devcon remove "PCI\VEN_8086&DEV_7110"
    ```

    The new driver is automatically loaded when the device is reinstalled after the system is restarted. To have DevCon automatically restart the system, add the conditional reboot parameter (**/r**) to the remove command.

    **Note**  The [DevCon](../devtest/devcon.md) tool is provided in the WDK. For more information about its commands, see [DevCon Commands](../devtest/devcon-general-commands.md).

     

An alternative to the DevCon Remove command is to update the [driver package](driver-packages.md) by using one of the following:

-   Device Manager to perform an "update driver" operation on the device.

    From within Device Manager's window, right-click the device's name or icon and choose **Properties**. In the **Properties** window, click the Driver tab and then click the **Update Driver** button.

-   The DevCon Update command. For more information about this command, see [**DevCon Commands**](../devtest/devcon-general-commands.md).

 

