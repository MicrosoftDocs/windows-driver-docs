---
title: Obtaining PCI Segment Values
description: Shows how to obtain segment value for PCI single and multi segment using DEVPKEY_Device_LocationInfo
keywords:
- PCI Single Segment
- PCI Multi Segment
- DEVPKEY_Device_LocationInfo
- IoGetDeviceProperty
ms.date: 12/06/2021
---

# Obtaining PCI Segment Values

To obtain the Segment value for PCI Multi-Segment, use the [DEVPKEY_Device_LocationInfo](/windows-hardware/drivers/install/devpkey-device-locationinfo) key.

Supported methods to obtain this property are:

* Kernel mode:
    * [**IoGetDeviceProperty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty)
    * [**IoGetDevicePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdevicepropertydata)
* User mode:
    * [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
    * [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw)

Upon successful call, you'll need to parse the returned string.

On single-segment system the string is in this format: `PCI bus 1, device 2, function 3`

On multi-segment system it looks like this: `PCI segment 1 bus 2, device 3, function 4`
