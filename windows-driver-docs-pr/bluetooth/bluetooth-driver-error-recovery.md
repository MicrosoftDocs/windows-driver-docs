---
title: Bluetooth Driver Error Recovery
description: Bluetooth driver automated error recovery mechanisms with diagnostic telemetry.
keywords: ["Bluetooth Driver Error Recovery", "Bluetooth PLDR"]
ms.date: 08/16/2019
ms.localizationpriority: medium
---

# Bluetooth Driver Error Recovery

Bluetooth Driver Error Recovery is a capability added to Windows 10 1803 to allow the Bluetooth stack to recover to a working state and provide developer diagnostic telemetry in the event of a failure. This article details the error scenarios where Bluetooth Driver Error Recovery is initiated.

> [!IMPORTANT]
> **This topic is for developers.** If you are a customer experiencing bluetooth problems see [Fix Bluetooth problems in Windows 10](https://support.microsoft.com/help/14169/windows-10-fix-bluetooth-problems).

## Bluetooth Driver Error Recovery Scenarios

There are three broad categories of issues where Bluetooth Driver Error Recovery is initiated:

- **Bus enumeration failures:** The device fails enumeration or re-enumeration by the bus as indicated by a _visible failed state_ in Device Manager. This is typically symptomatic of hardware errors.

- **Client driver enumeration failures:** The device ends up in a failed state _after_ after successful enumeration during the course of use. If the device has been successfully enumerated by the bus, then the next step involves the driver stack of the USB client e.g. filter or function driver that gets installed on the Bluetooth device node (devnode). Failures could happen if the client driver encounters an error during one or more start operations and thus reporting PnP failure. An example of such an operation could be a firmware download to the device.

- **Non-enumeration failures:** The device is not in a failed state but is otherwise non-operational as far as the driver stack is concerned. These are failures outside of the enumeration pathway and could be general critical USB transfer failures or device-specific failures like a non-recoverable firmware error. There could also be generic device unresponsive scenarios where in the device appears connected and functional but there is no expected activity e.g. Bluetooth mouse is not sending notifications even though the user is moving the mouse. The Bluetooth Error Recovery mechanisms described below is used in these cases. Currently, we trigger them for hardware errors that are reported by the firmware; with a view to expanding and applying heuristics to cover more scenarios e.g. repeated command timeout errors for critical/init HCI commands, repeated transactional errors over the transport.

The typical error recovery process is to perform the documented steps for USB recovery outlined in [How to recover from USB pipe errors](https://docs.microsoft.com/en-us/windows-hardware/drivers/usbcon/how-to-recover-from-usb-pipe-errors). Bluetooth Driver Error Recovery adds the following additional recovery mechanisms:

- If a USB Reset port fails the additional error recovery and diagnostics will be performed by the USB stack.

- If the USB port reset succeeds but there is still an error condition, the client driver can choose to do a Cycle Port, which will also cause the USB stack to perform the additional error recovery and diagnostics.

## Error Recovery Mechanisms

The [GUID_DEVICE_RESET_INTERFACE_STANDARD](https://docs.microsoft.com/windows-hardware/drivers/kernel/working-with-guid-device-reset-interface-standard) interface defines a standard mechanism for function drivers to attempt to reset and recover a malfunctioning device. However, there are unique aspects that deserve special note:  

- The reset mechanisms work only for **internal devices** so externally-pluggable Bluetooth radios such as dongles are not supported.

- The reset mechanisms require support both in Windows (typically by the function driver stack) and the underlying firmware (typically in the ACPI BIOS) to actually perform the reset.

- The actual reset mechanism is system-specific.

[GUID_DEVICE_RESET_INTERFACE_STANDARD](https://docs.microsoft.com/windows-hardware/drivers/kernel/working-with-guid-device-reset-interface-standard) defines two levels of reset:

- **Function-level device reset (FLDR)**: The reset operation is restricted to a specific device and is not visible to other devices. There is no re-enumeration; function drivers must assume that the hardware has returned to its original state after the operation and intermediary state has not been preserved.

- **Platform-level device reset (PLDR)**: The reset operation affects a specific device and all other devices that are connected to it via the same power rail or reset line. The reset operation causes the device to be reported as missing from the bus and re-enumerated. This type of reset has the most impact on the system since all devices that share the resource go back to their original state.

While the Bluetooth stack supports both these mechanisms, **PLDR** is usually the most effective approach.

## ACPI reset interface

Building on the process detailed in [Working with the GUID_DEVICE_RESET_INTERFACE_STANDARD](https://docs.microsoft.com/windows-hardware/drivers/kernel/working-with-guid-device-reset-interface-standard) specific steps must be taken:

- The ACPI namespace must properly describe the internal device within a __ADR_ namespace. The _Address_ property provided in Device Manager for each device is the address that the firmware must report in the device's __ADR_.

- To declare that a device supports **Function-Level Device Reset (FLDR)**, within the __ADR_ namespace a __RST_ method must exist.

- To declare that a device supports **Platform-Level Device Reset (PLDR)**, within the __ADR_ namespace a __PR3_ or a __RST_ method must exist.

    - If a __PR3_ method is used, ACPI uses the D3Cold power cycle mechanism to reset. This emulates removing power from the device and subsequently restoring it. If any other devices share the same power rail they will also be reset.

    - If a __RST_ method is defined and referenced by a __PRR_ (PowerResource) then all devices that use that PowerResource will be affected.

- Since PLDR works only for internal devices, it must be declared as such in ACPI. Specifically for USB devices, To specify a port that is internal (not user visible) and can be connected to an integrated device, the __UPC.PortIsConnectable_ byte must be set to 0xFF and the __PLD.UserVisible_ bit must be set to 0.

- If the __PR3_ (D3Cold) mechanism is used for PLDR, care must be taken to ensure that scenarios like SystemWake and DeviceWake continue to work. Nominally, this means that there are appropriate power resources defined for D2 e.g. __PR2_. The following table is a useful guide:

| Power state | ACPI resource | Behavior |  
| --- | --- | --- |  
| D2 | _PR2 | Any power or clocks required for the class-defined reduced-functionality of this state. |  
| D3 Hot (reqd.) | _PR2 | The same resources as the next higher state that is supported (D2, D1, or D0). |  
| D3cold | _PR3 | Only the power or clocks required for the device to appear on its bus and respond to a bus-specific command.|  

### Related links
[Device power management](https://docs.microsoft.com/en-us/windows-hardware/drivers/bringup/device-power-management)

[Supporting D3cold in a Driver](https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/supporting-d3cold-in-a-driver)
