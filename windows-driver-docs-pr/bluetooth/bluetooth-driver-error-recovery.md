---
title: Bluetooth Driver Error Recovery
description: Bluetooth driver automated error recovery mechanisms with diagnostic telemetry.
keywords: ["Bluetooth Driver Error Recovery", "Bluetooth PLDR"]
ms.date: 08/16/2019
ms.localizationpriority: medium
---

# Bluetooth Device-based Reset and Recovery

Bluetooth Device-based Reset and Recovery is a technology in Windows 10, version 1803 and later that introduces a robust reset recovery mechanism for Bluetooth devices and drivers. This mechanism enables Bluetooth devices to recover from failures that cause malfunction, loss of connectivity, or unresponsiveness to operational commands, making the user experience seamless and reducing the likelihood of requiring a system restart.

Device-based Reset and Recovery can be implemented with or without firmware dependencies. IHV or OEM partners can extend the software-based reset mechanisms available on all Windows PCs with supported device- or firmware-level reset mechanisms to increase the likelihood of successful recovery.

> [!IMPORTANT]
> **This topic is for developers.** If you are a customer experiencing bluetooth problems see [Fix Bluetooth problems in Windows 10](https://support.microsoft.com/help/14169/windows-10-fix-bluetooth-problems).

## Bluetooth Reset and Recovery Scenarios

There are three broad categories of issues where Bluetooth Reset and Recovery is initiated:

- **Bus enumeration failures:** The device fails enumeration or re-enumeration by the bus as indicated by a _visible failed state_ in Device Manager, which is typically symptomatic of hardware errors.

- **Client driver enumeration failures:** The device is in a failed state _after_ after successful enumeration during normal use. If the device has been successfully enumerated by the bus, then the next step involves the driver stack of the USB client e.g. filter or function driver installed on the Bluetooth device node (devnode). Failures could occur if the client driver encounters an error during one or more start operations and thus reporting PnP failure. An example of such an operation could be a firmware download to the device.

- **Non-enumeration failures:** The device is not in a failed state but is otherwise non-operational as seen by the driver stack. These are failures outside of the enumeration pathway and could be general critical USB transfer failures or device-specific failures such as a non-recoverable firmware error. The Bluetooth Reset and Recovery mechanisms described below is used in these cases.

## Reset and Recovery Mechanisms

[GUID_DEVICE_RESET_INTERFACE_STANDARD](https://docs.microsoft.com/windows-hardware/drivers/kernel/working-with-guid-device-reset-interface-standard) defines two levels of reset. Note that:

- The reset mechanisms work only for **internal devices** so externally-pluggable Bluetooth radios such as dongles are not supported.

- The reset mechanisms require support both in Windows (typically by the function driver stack) and the underlying firmware (typically in the ACPI BIOS) to actually perform the reset.

- The actual reset mechanism is system-specific.

| Reset Level | Implementation |
| --- | --- |
| Function-level device reset (FLDR) | The reset operation is restricted to a specific device and is not visible to other devices. There is no re-enumeration; function drivers must assume that the hardware has returned to its original state after the operation and intermediary state has not been preserved.|
| Platform-level device reset (PLDR) | The reset operation affects a specific device and all other devices that are connected to it via the same power rail or reset line. The reset operation causes the device to be reported as missing from the bus and re-enumerated. This type of reset has the most impact on the system since all devices that share the resource go back to their original state.|

- **To support FLDR** there must be an __RST method defined within the __ADR_ namespace as detailed in [ACPI firmware: Function-level reset](https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/resetting-and-recovering-a-device#acpi-firmware-function-level-reset).

- **To support PLDR** there must be an _RST or _PR3  method defined within the __ADR_ namespace as detailed in [ACPI firmware: Platform-level reset](https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/resetting-and-recovering-a-device#acpi-firmware-platform-level-reset). Note that if a __PR3_ method is used, ACPI uses the D3Cold power cycle mechanism to reset. This emulates removing power from the device and subsequently restoring it. If any other devices share the same power rail they will also be reset. If an __RST_ method is defined and referenced by a __PRR_ (PowerResource) then all devices that use that PowerResource will be affected.

  - Since PLDR works only for internal devices, it must be declared as such in ACPI. Specifically for USB devices, To specify a port that is internal (not user visible) and can be connected to an integrated device, the __UPC.PortIsConnectable_ byte must be set to 0xFF and the __PLD.UserVisible_ bit must be set to 0.

  - If the __PR3_ (D3Cold) mechanism is used for PLDR, care must be taken to ensure that scenarios like SystemWake and DeviceWake continue to work. Nominally, this means that there are appropriate power resources defined for D2 e.g. __PR2_. The following table is a useful guide:

### Related links

[Resetting and recovering a device](https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/resetting-and-recovering-a-device)
