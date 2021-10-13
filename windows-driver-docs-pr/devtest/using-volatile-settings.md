---
title: Using Volatile Settings
description: Using Volatile Settings
keywords:
- Driver Verifier WDK , volatile settings
- volatile settings WDK Driver Verifier
ms.date: 06/29/2021
ms.localizationpriority: medium
---

# Using Volatile Settings


## <span id="ddk_using_volatile_settings_tools"></span><span id="DDK_USING_VOLATILE_SETTINGS_TOOLS"></span>

Most changes to Driver Verifier's status (activating, deactivating, changing options, or changing the list of drivers being verified) take effect only when you restart the computer ("reboot").

However, you can activate and deactivate some options without rebooting. These are referred to as *volatile settings.* Changes to these settings are effective immediately, and last until the next boot, or until they are changed again.

This section explains the volatile settings and how to use them on the versions of Driver Verifier included in different versions of Windows.

> [!NOTE]
> This option will be deprecated in a future release of Windows. A replacement option for Windows 11 is provided with the **/now** [Verifier Command](verifier-command-line.md).

### Changing Options Without Rebooting

As of Windows 11, only the following flags can be used with volatile:

```
0x00000004 (bit  2) - Randomized low resources simulation
0x00000020 (bit  5) - Deadlock detection
0x00000080 (bit  7) - DMA checking
0x00000200 (bit  9) - Force pending I/O requests
0x00000400 (bit 10) - IRP logging
```

> [!NOTE]
> A number of other flags in Windows 11 may be enabled without reboot using the **/now** command. The supported flags are described in [Verifier Command](verifier-command-line.md).

As of Windows 10, only the following flags can be used with volatile:

#### Standard Flags

```
0x00000001 (bit  0) - Special pool
0x00000002 (bit  1) - Force IRQL checking
0x00000008 (bit  3) - Pool tracking
0x00000010 (bit  4) - I/O verification
0x00000020 (bit  5) - Deadlock detection
0x00000080 (bit  7) - DMA checking
0x00000100 (bit  8) - Security checks
0x00000800 (bit 11) - Miscellaneous checks
```

#### Additional Flags

```
0x00000004 (bit  2) - Randomized low resources simulation
0x00000200 (bit  9) - Force pending I/O requests (*)
0x00000400 (bit 10) - IRP logging (*)
0x00002000 (bit 13) - Invariant MDL checking for stack (*)
0x00004000 (bit 14) - Invariant MDL checking for driver (*)
```


### Changing Drivers Without Rebooting

You can add and remove drivers (that is, start and stop the verification of a driver) without rebooting the computer, even when Driver Verifier is not already running.

You can also start a verification of a driver that is already loaded without rebooting, but you cannot stop the verification of a loaded driver without rebooting. After a driver is loaded and being verified, Driver Verifier monitors it until the next reboot, but you can turn off the Driver Verifier optional checks for the driver without rebooting, thereby minimizing the Driver Verifier overhead.

You can change the volatile settings by using the [Verifier Command Line](verifier-command-line.md), or [Driver Verifier Manager](driver-verifier-manager--windows-xp-and-later-.md).

### Volatile and Registry Settings

Being able to add and change drivers and set options without rebooting is a significant convenience and it allows you to run Driver Verifier in some test scenarios that would not otherwise be possible.

However, because there are some advantages to the traditional model of adding the Driver Verifier settings to the registry, you need to decide for each setting whether you want to use the volatile method, or set it in the registry, or both.

-   Volatile or "runtime" settings become effective immediately, but these settings are lost when you shut down or reboot Windows.

-   Registry settings require a reboot, but they remain in the registry until you change them and reboot again.

Settings that you use consistently or need to measure while the driver is loading should be added to the registry. Other settings can be enabled when you need them.

When using both registry settings and volatile settings, remember that volatile settings are used instead of the registry settings; they are not additions.

### Configuring Volatile Settings by Using the Verifier Command Line

To add or delete volatile options, use the **/volatile /flags** parameter.

To add or remove a driver from the volatile list, use the **/volatile /adddriver** or **/volatile /removedriver** parameters. See [**Driver Verifier Command Syntax**](verifier-command-line.md) for details.

-   To start or stop the verification of a driver without rebooting:

    ```
    verifier /volatile /adddriver DriverName.sys
    verifier /volatile /removedriver DriverName.sys
    ```

    You can use this command syntax to add (start the verification) of any driver, even a driver that is currently loaded. Commands to remove (stop the verification) of a driver that is currently loaded will fail. As always, the verification of a driver that is not loaded will begin as soon as the driver is loaded.

-   To activate or deactivate options without rebooting:

    ```
    verifier /volatile /flags <flags>
    ```

    For example, this command activates the [deadlock detection](deadlock-detection.md) option without rebooting.

    ```
    verifier /volatile /flags 0x20
    ```


-   To turn off all Driver Verifier options:

    You cannot stop the verification of a driver that is currently loaded without rebooting. However, you can use the following command syntax to deactivate all of the Driver Verifier options without rebooting, thereby minimizing the overhead until the next reboot.

    ```
    verifier /volatile /flags 0
    ```

    Driver Verifier continues to monitor the driver using the options in the [Automatic Checks](automatic-checks.md) feature, which cannot be turned off, but the overhead is reduced to approximately ten percent of the overhead of a typical verification.


### Configuring Volatile Settings by Using Driver Verifier Manager

**To view the Driver Verifier features that are currently active, or to change the volatile settings**

1.  Start Driver Verifier Manager and select the **Display information about the currently verified drivers** task.

2.  Click **Next**.

    This screen shows the Driver Verifier options currently in effect, including volatile settings, but not including changes to permanent settings that are scheduled to take effect after the next restart. Each driver will have its status listed.

3.  To change the active options, click **Change**. Select or clear the desired options, and then click **OK**.

4.  To verify a new driver, click **Add**. This opens a dialog box where you can browse the computer for the driver file that you want to verify. After locating the correct driver, click **Open** to add it to the list of verified drivers.

5.  To remove a driver from the list, select that driver's name and click **Remove**.

6.  When you are finished viewing the Driver Verifier options in effect or when you are finished making changes, click **Next** two times, and then click **Finish**.

### Driver Status Values

Driver Verifier Manager shows three possible status values for drivers shown on the **Current settings and verified drivers (run time information)** screen. The possible status values are as follows:

<span id="Loaded"></span><span id="loaded"></span><span id="LOADED"></span>**Loaded**
The driver is currently loaded and is being verified.

<span id="Unloaded"></span><span id="unloaded"></span><span id="UNLOADED"></span>**Unloaded**
The driver was loaded and verified at least once since the last boot, but is currently not loaded.

<span id="Never_Loaded"></span><span id="never_loaded"></span><span id="NEVER_LOADED"></span>**Never Loaded**
Driver Verifier was instructed to verify this driver, but the driver has not been loaded since this request. This can indicate that the driver is loaded on demand and has not yet been required in this session. It might also indicate that a nonexistent driver was requested for verification, or that a driver image file has been corrupted.

## Related topics


[Driver Verifier Command Syntax](verifier-command-line.md)

[Controlling Driver Verifier](controlling-driver-verifier.md)










