---
title: Hardware ID
description: A hardware ID is a vendor-defined identification string that Windows uses to match a device to an INF file.
ms.date: 04/08/2022
ms.custom: contperf-fy21q3
---

# Hardware ID

A hardware ID is a vendor-defined identification string that Windows uses to match a device to a [driver package](driver-packages.md). A hardware ID identifies what a device is to some level of specificity and is indicating that any driver package that declares it can work with a device that has that ID can work with this device for some degree of functionality. In most cases, a device has more than one hardware ID associated with it. Typically, a list of hardware IDs is sorted from most to least suitable for a device. For example, the list of conceptual hardware IDs for a device might look like:

```syntax
<Product X made by company Y with firmware revision Z>
<Product X made by company Y that is a device of type W>
```

Where the actual hardware IDs would represent those concepts using strings that follow the format requirements of a hardware ID.

## Creating a hardware ID for a device

Hardware IDs are reported to the Plug and Play Manager (PnP) by a device's *enumerator* (its [bus driver](../kernel/bus-drivers.md)).  Typically, when the author of a bus driver needs to create a new hardware ID for a device it will report to PnP, it will use one of the following generic formats:

`<enumerator>\<enumerator-specific-device-ID>`

This is the most common format for individual PnP devices reported to the Plug and Play (PnP) manager by a single enumerator.

`\*<generic-device-ID>`

The asterisk indicates that the device is supported by more than one enumerator, such as ISAPNP and the BIOS.

`<device-class-specific-ID>`

For more information, see [Generic Identifiers](generic-identifiers.md).

An existing device class that has established its own naming convention might use a custom format. For information about their hardware ID formats, see the hardware specification for such buses.

The number of characters of a hardware ID, excluding a NULL terminator, must be less than `MAX_DEVICE_ID_LEN`. This constraint applies to the sum of the lengths of all the fields and any `\\` field separators in a hardware ID. For more information, see the **Operations** section of [**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md).

## Hardware IDs for root enumerated devices

Root enumerated devices are special in that they can be created using APIs where a hardware ID can be provided. Root enumerated devices with hardware IDs sharing generic namespaces such as `ROOT\SYSTEM` may conflict and result in an yellow-bang error icon in Device Manager when updating Windows.

You can prevent this by using a unique namespace for each driver that has a root enumerated device. For a USB or system device, instead of using `ROOT\USB` or `ROOT\SYSTEM"` use `ROOT\[COMPANYNAME]\[DEVICENAME]`.  Then, before installing, check to see if the devnode is already present.

## Obtaining the list of hardware IDs for a device

To find the list of hardware IDs for a given device, follow these steps:

1. Open Device Manager.

1. Find the device in the tree.

1. Right-click the device and select **Properties**.

1. Select the Details tab.

1. In the **Property** drop-down, select **Hardware Ids** or **Compatible Ids**.

The list of hardware IDs can also be obtained programmatically by retrieving the [DEVPKEY_Device_HardwareIds](devpkey-device-hardwareids.md) property on a device. For example, that property can be retrieved with APIs such as [**IoGetDevicePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicepropertydata), [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw), or [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw).

The list of hardware IDs that this routine retrieves is a [REG_MULTI_SZ](/windows/desktop/SysInfo/registry-value-types) value. The maximum number of characters in a hardware list, including a NULL terminator after each hardware ID and a final NULL terminator, is `REGSTR_VAL_MAX_HCID_LEN`. The maximum possible number of IDs in a list of hardware IDs is 64.

## Examples of Hardware IDs

Here is an example of a [generic identifier](generic-identifiers.md) for a PnP device:

`root\*PNP0F08`

Here is an example of an [identifier for a PCI device](identifiers-for-pci-devices.md):

`PCI\VEN_1000&DEV_0001&SUBSYS_00000000&REV_02`
