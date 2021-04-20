---
title: Hardware ID
description: A hardware ID is a vendor-defined identification string that Windows uses to match a device to an INF file.
ms.date: 01/11/2021
ms.localizationpriority: High
ms.custom: contperf-fy21q3
---

# Hardware ID


A hardware ID is a vendor-defined identification string that Windows uses to match a device to an INF file. In most cases, a device has more than one hardware ID associated with it. Typically, a list of hardware IDs is sorted from most to least suitable for a device.

To find hardware ID for a given device, follow these steps:

1. Open Device Manager.
2. Find the device in the tree.
3. Right-click the device and select **Properties**.
4. Select the Details tab.
5. In the **Property** drop-down, select **Hardware Ids** or **Compatible Ids**.

## Creating a hardware ID for a device

Typically, when you create a new hardware ID for your device, you'll use one of the following generic formats:

`<enumerator>\<enumerator-specific-device-ID>`

This is the most common format for individual PnP devices reported to the Plug and Play (PnP) manager by a single enumerator.

`\*<generic-device-ID>`

The asterisk indicates that the device is supported by more than one enumerator, such as ISAPNP and the BIOS. 

`<device-class-specific-ID>`

For more information, see [Generic Identifiers](generic-identifiers.md).

## Selecting a hardware ID

Root enumerated devices sharing generic namespace such as `ROOT\SYSTEM` may conflict and result in an yellow-bang error icon in Device Manager when updating Windows.

You can prevent this by using a unique namespace for each driver that has a root enumerated device. For a USB or system device, instead of using `ROOT\USB` or `ROOT\SYSTEM”` use `ROOT\[COMPANYNAME]\[DEVICENAME]`.  Then, before installing, check to see if the devnode is already present.

An existing device class that has established its own naming convention might use a custom format. For information about their hardware ID formats, see the hardware specification for such buses.

The number of characters of a hardware ID, excluding a NULL terminator, must be less than `MAX_DEVICE_ID_LEN`. This constraint applies to the sum of the lengths of all the fields and any `\\` field separators in a hardware ID. For more information, see the **Operations** section of [**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md).

## Obtaining the list of hardware IDs for a device

To obtain the list of hardware IDs for a device, call [**IoGetDeviceProperty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty) with the *DeviceProperty* parameter set to **DevicePropertyHardwareID**. The list of hardware IDs that this routine retrieves is a [REG_MULTI_SZ](/windows/desktop/SysInfo/registry-value-types) value.

The maximum number of characters in a hardware list, including a NULL terminator after each hardware ID and a final NULL terminator, is `REGSTR_VAL_MAX_HCID_LEN`. The maximum possible number of IDs in a list of hardware IDs is 64.

## Examples of Hardware IDs

Here is an example of a [generic identifier](generic-identifiers.md) for a PnP device:

`root\*PNP0F08`

Here is an example of an [identifier for a PCI device](identifiers-for-pci-devices.md):

`PCI\VEN_1000&DEV_0001&SUBSYS_00000000&REV_02`


## See Also

[INF HardwareId Directive](./inf-hardwareid-directive.md)
