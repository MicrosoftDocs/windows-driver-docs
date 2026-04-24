---
title: PCI Express Device Serial Number Conflicts Cause Device Enumeration Errors in Windows
description: Workaround for device enumeration issues caused by PCI Express devices that report duplicate serial numbers due to a hardware defect.
keywords:
- PCI Express
- PCI duplicate serial number error
- Device Serial Number Extended Capability
- ms.date: 04/24/2026
ms.topic: concept-article
---

# PCI Express device serial number conflicts cause device enumeration errors in Windows

This article provides a workaround for device enumeration problems caused by PCI Express devices that report duplicate serial numbers due to a hardware defect.

## Applies to

- Windows 10
- Windows 11
- Windows Server 2016 and later versions

## Symptoms

Consider the following scenario:

- A computer has multiple PCI Express devices installed.
- Two or more of these devices report the same PCI Express device serial number through the Device Serial Number Extended Capability.

In this scenario, some devices don't start correctly, some devices are assigned the wrong driver, and some devices exhibit unexpected behavior. You might see one or more of the following problems:

- Devices appear interchanged or misidentified in Device Manager.
- A device fails to start with an error code in Device Manager.
- Driver or firmware updates are applied to the wrong device.
- Device-specific settings or configurations are applied inconsistently across reboots.

## Cause

PCI Express devices can optionally implement the **Device Serial Number Extended Capability** (as defined in the PCI Express specification). This capability provides a unique 64-bit serial number that Windows uses to consistently identify and track individual devices, even when you move them to different slots or when the system reboots.

Windows relies on this serial number to maintain a stable association between a physical device and its software configuration (driver settings, device properties, and so on).

Some hardware implementations contain a defect where multiple devices of the same model report an **identical serial number**. This defect violates the PCI Express specification, which requires that each device serial number be unique. When Windows encounters duplicate serial numbers, it can't reliably distinguish between the affected devices, which leads to the symptoms described earlier.

## Workaround

> [!IMPORTANT]
> This article contains information about how to modify the registry. Make sure that you back up the registry before you modify it. Make sure that you know how to restore the registry if a problem occurs. For more information about how to back up, restore, and modify the registry, see [How to back up and restore the registry in Windows](https://support.microsoft.com/help/322756).
> [!WARNING]
> Serious problems might occur if you modify the registry incorrectly by using Registry Editor or by using another method. These problems might require that you reinstall the operating system. Microsoft can't guarantee that these problems can be solved. Modify the registry at your own risk.

To work around this issue, disable PCI Express Device Serial Number support system-wide by setting the `PCI_SYS_HACK_DISABLE_EXPRESS_SERIAL_NUMBER_SUPPORT` hackflag. This change causes the Windows PCI driver (pci.sys) to ignore the Express Serial Number capability for all devices.

When you set this hackflag, Windows no longer uses the PCI Express Device Serial Number to identify devices. Device identification falls back to other methods, such as bus location, which might reset device settings if you move devices to different slots.

To apply this workaround:

1. Select **Start**, type **regedit** in the search box, and then select **regedit** in the results list.

   If you're prompted for an administrator password or for confirmation, type the password, or select **Continue**.

1. Locate the following registry subkey, and then select it:

   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\PnP\Pci`

1. **If the `HackFlags` registry entry doesn't exist**, follow these steps:

   1. On the **Edit** menu, point to **New**, and then select **DWORD (32-bit) Value**.
   1. Type **HackFlags**, and then press ENTER.
   1. Right-click **HackFlags**, and then select **Modify**.
   1. In the **Value data** box, type **10000**, select **Hexadecimal** in the **Base** area, and then select **OK**.
   1. Exit Registry Editor.

1. **If the `HackFlags` registry entry already exists**, the value might contain other hackflags that are already in use. In this case, combine the new flag with the existing value using a bitwise OR operation, rather than replacing it. Follow these steps:

   1. Right-click **HackFlags**, and then select **Modify**.
   1. Select **Hexadecimal** in the **Base** area.
   1. Note the current **Value data** (for example, `600`).
   1. Calculate the new value by performing a bitwise OR of the existing value with `10000`. For example, if the current value is `600`, the new value is `10600`.
   1. Type the new value in the **Value data** box, and then select **OK**.
   1. Exit Registry Editor.

   > [!TIP]
   > You can use the Windows Calculator in **Programmer** mode to perform the bitwise OR. Enter the existing hex value, select **OR**, enter **10000**, and press **=** to get the combined result.

1. Restart the computer for the change to take effect.

## How to verify the workaround is applied

After restarting the computer, verify the hackflag is active by checking the registry value:

1. Open Registry Editor and go to:

   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\PnP\Pci`

1. Double-click **HackFlags** and confirm that the value, when viewed in hexadecimal, includes the `10000` bit. For example, a value of `10000`, `10200`, `10600`, or any value where bit 16 is set confirms the flag is active.

## More information

- The hackflag value `0x00010000` corresponds to `PCI_SYS_HACK_DISABLE_EXPRESS_SERIAL_NUMBER_SUPPORT` in the Windows PCI driver.
- This setting affects all PCI Express devices. You can't apply it to individual devices.
- Use this workaround only for systems that have hardware with a known duplicate serial number defect. Don't use it as a general-purpose configuration change.

## Data collection

If you need assistance from Microsoft support, collect the information by following the steps mentioned in [Gather information by using TSS for deployment-related issues](https://learn.microsoft.com/troubleshoot/windows-client/windows-troubleshooters/gather-information-using-tss-deployment).
