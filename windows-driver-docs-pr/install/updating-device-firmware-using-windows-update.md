---
title: Update Device Firmware Using Windows Update
description: This article describes how to update your device's firmware using the Windows Update (WU) service.
ms.date: 04/16/2025
ms.topic: how-to
---

# Update device firmware using Windows Update

This article describes how to update a removable or in-chassis device's firmware using the Windows Update (WU) service. For information about updating system firmware, see [Windows UEFI firmware update platform](../bringup/windows-uefi-firmware-update-platform.md).

To update device firmware using Windows Update, provide a device driver that includes the firmware payload. If you provide a function driver for your device, you can add the firmware update logic and payload to the existing driver, or you can provide a separate firmware update driver package. If your device uses a Microsoft-supplied driver, you must provide a separate firmware update driver package. In both cases, the firmware update driver package must be Universal.

For more info about Universal drivers, see [Using a Universal INF File](../install/using-a-universal-inf-file.md). The driver binary can use [KMDF](../wdf/index.md), [UMDF 2](../wdf/getting-started-with-umdf-version-2.md), or the [Windows Driver Model](../kernel/writing-wdm-drivers.md).

Because WU can't execute software, the firmware update driver must hand the firmware to Plug and Play (PnP) for installation.

## Firmware update driver actions

Typically, the firmware update driver is a lightweight device driver that implements the following procedures:

- At device start or in the driver's [*EVT_WDF_DRIVER_DEVICE_ADD*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function:

    1. Identify the device to which the driver is attached.
    1. Determine whether the driver has a firmware version that is more recent than the version on the firmware currently flashed on device hardware.
    1. If a firmware update is necessary, set an event timer to schedule the update.
    1. Otherwise, do nothing until the driver is started again.

- During system runtime:

    1. If an update is queued, wait for a set of conditions to be met.
    1. When conditions are met, perform the firmware update on the device.

## Firmware update driver contents

Typically, the firmware update driver package contains the following items:

- [Universal Driver INF](using-a-universal-inf-file.md)
- Driver catalog
- Function driver (.sys or .dll)
- Firmware update payload binary

Submit your firmware update package as a separate driver submission.

## Add firmware update logic to a vendor-supplied driver

The existing function driver can implement the firmware update mechanism, as shown in the following diagram:

:::image type="content" source="images/single-devnode.png" alt-text="Using Windows Update to deliver firmware update via existing function driver.":::

Alternatively, if you want to update the function driver and the firmware update driver separately, create a second device node, on which you install the firmware update driver. The following diagram shows how one device can have two separate device nodes:

:::image type="content" source="images/two-devnodes.png" alt-text="Using Windows Update to deliver firmware update via separate device node.":::

The function and firmware device nodes must have different hardware IDs in order to be targeted independently.

There are a couple ways to create a second device node. Certain device types have the ability to expose a second device node on one physical device, such as USB. You can use this functionality to create a device node targetable by WU, and install a firmware update driver on it. Many device types, however, don't allow a single physical device to enumerate more than one device node.

In that case, use an extension INF that specifies the [AddComponent](../install/inf-addcomponent-directive.md) directive to create a device node targeted by Windows Update, and install the firmware update driver on it. The following snippet from an INF file shows how you can do this:

```inf
[Manufacturer]
%Contoso%=Standard,NTamd64
[Standard.NTamd64]
%DeviceName%=Device_Install, PCI\DEVICE_ID
[Device_Install.Components]
AddComponent=ComponentName,,AddComponentSection
[AddComponentSection]
ComponentIDs = ComponentDeviceId
```

In the INF sample, `ComponentIDs = ComponentDeviceId` indicates that the child device has a hardware ID of `SWC\ComponentDeviceId`. When installed, this INF creates the following device hierarchy:

:::image type="content" source="images/component-device-hierarchy.png" alt-text="Parent device, primary device, AddComponent device.":::

For future firmware updates, update the INF and binary file containing the firmware payload.

## Add firmware update logic to a Microsoft-supplied driver

To update firmware for devices that use a Microsoft-supplied driver, create a second device node, as shown.

## Best practices

- In your firmware update driver INF, specify [DIRID 13](using-dirids.md) to cause PnP to leave the files in the driver package in the DriverStore:

    ```inf
    [Firmware_AddReg]
    ; Store location of firmware payload
    HKR,,FirmwareFilename,,"%13%\firmware_payload.bin"
    ```

    PnP resolves this location when it installs the device. The driver can then open this registry key to determine the location of the payload.

- Firmware update drivers specify the following INF entries:

    ```inf
    Class=Firmware
    ClassGuid={f2e7dd72-6468-4e36-b6f1-6488f42c1b52}
    ```

- To locate another device node, the firmware driver should walk the device tree relative to itself, not by enumerating all device nodes for a match. A user might have plugged in multiple instances of the device, and the firmware driver should only update the device with which it's associated. Typically, the device node to be located is the parent or sibling of the device node on which the firmware driver is installed. For example, in the diagram with two device nodes, the firmware update driver can look for a sibling device to find the function driver. In the next diagram, the firmware driver can look for the parent device to find the primary device with which it needs to communicate.

- The driver should be robust to multiple instances of the device being on the system, possibly with multiple different firmware versions. For example, there might be one instance of the device that has been connected and updated several times. A brand new device might then be plugged in which is several firmware versions old. This means that state (such as current version) must be stored against the device, and not in a global location.

- If there's an existing method to update the firmware (EXE or co-installer, for example), you can largely reuse the update code within a UMDF driver.
