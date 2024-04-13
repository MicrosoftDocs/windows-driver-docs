---
title: Compatible ID
description: A compatible ID is a vendor-defined identification string that Windows uses to match a device to an INF file.
ms.date: 04/08/2022
---

# Compatible ID

A compatible ID is a vendor-defined identification string that Windows uses to match a device to a [driver package](driver-packages.md). A compatible ID identifies what a device is to some level of specificity and is indicating that any driver package that declares it can work with a device that has that ID can work with this device for some degree of functionality. Compatible IDs have the same format as [hardware IDs](hardware-ids.md) but tend to be a more generic description of a device than a hardware ID. A device can have associated with it a list of compatible IDs. The compatible IDs should be listed in order of decreasing suitability. If Windows cannot locate a driver package that matches one of a device's hardware IDs, it uses compatible IDs to locate a driver package. For example, the list of conceptual compatible IDs for a device might look like the following:

```syntax
<Product X made by company Y>
<Device of type W made by company Y>
<Device of type W>
```

Where the actual compatible IDs would represent those concepts using strings that follow the format requirements of a compatible ID.

To find compatible IDs for a given device, select the device in Device Manager, choose **Properties**, then the **Details** tab, then use the Properties drop-down.

If a vendor ships a driver package that specifies a compatible ID for a driver node, the vendor should make sure that their driver package can support all the hardware that exposes that compatible ID.

The list of compatible IDs can be obtained programmatically by retrieving the [DEVPKEY_Device_CompatibleIds](devpkey-device-compatibleids.md) property on a device. For example, that property can be retrieved with APIs such as [**IoGetDevicePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicepropertydata), [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw), or [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw).

The list of compatible IDs that this routine retrieves is a [REG_MULTI_SZ](/windows/desktop/SysInfo/registry-value-types) value. The maximum number of characters in a compatible ID list, including a NULL terminator after each compatible ID and a final NULL terminator, is `REGSTR_VAL_MAX_HCID_LEN`. The maximum possible number of IDs in a list of compatible IDs is 64.

## Related information

[Hardware IDs](hardware-ids.md)
