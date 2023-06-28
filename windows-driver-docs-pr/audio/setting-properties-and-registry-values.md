---
title: Setting properties and registry values
description: Learn how a Port Class audio driver can set properties and registry values for a PnP device interface.
ms.date: 04/20/2017
---

# Setting properties and registry values

This guide explains how a Port Class audio driver can set properties and registry values for a PnP device interface. To properly register the device interface and set required values, the Portcls driver must follow these steps:

## 1. Register the device interface

Before calling `PcRegisterSubdevice` for the sub-device, the driver should call `IoRegisterDeviceInterface` to register the `KSCATEGORY_AUDIO` interface. This allows the driver to set interface properties and registry values before `PcRegisterSubdevice` registers and enables the interfaces.

When calling `IoRegisterDeviceInterface`, the audio driver sets the parameters as follows:

- The `PhysicalDeviceObject` parameter is the `PDEVICE_OBJECT` retrieved from the `PcGetPhysicalDeviceObject` function.
- The `InterfaceClassGuid` is set to the interface's class GUID.
- The `ReferenceString` is the same as the `Name` parameter passed to `PcRegisterSubdevice`.

After completing these tasks successfully, `IoRegisterDeviceInterface` returns a `SymbolicLinkName` for the registered interface.

## 2. Set registry values

The audio driver calls `IoOpenDeviceInterfaceRegistryKey` to obtain a handle to the device interface registry key. The parameters for `IoOpenDeviceInterfaceRegistryKey` are set as follows:

- The `SymbolicLinkName` is the string returned from `IoRegisterDeviceInterface` in the previous step.
- The `DesiredAccess` is set to `KEY_WRITE` (or other values if needed by the driver).

After completing these steps, `DeviceInterfaceKey` returns the opened registry key handle. The audio driver:

- Calls `ZwSetValueKey` to set registry values.
- Closes the registry key handle by calling `ZwClose`.

**Note:** If the driver needs to set values in a registry subkey, it should call `ZwCreateKey` to create the subkey. When preparing to call `ZwCreateKey`, the driver:

- Calls `InitializeObjectAttributes` and sets the `ObjectName` to the subkey path.
- Sets `Attributes` to `OBJ_CASE_INSENSITIVE | OBJ_KERNEL_HANDLE`.
- Sets `RootDirectory` to the handle returned by `IoOpenDeviceInterfaceRegistryKey`.
- Calls `ZwClose` to close any handle created by calling `ZwCreateKey`.

## 3. Set properties

The audio driver calls `IoSetDeviceInterfacePropertyData` to set properties. The parameters for `IoSetDeviceInterfacePropertyData` are set as follows:

- The `SymbolicLinkName` is the string returned from `IoRegisterDeviceInterface`.
- The remaining parameters depend on the specific property being set.

## See also

[Sample Audio Drivers](sample-audio-drivers.md)
