---
title: DEVPKEY_Device_DHP_Rebalance_Policy
description: The DEVPKEY_Device_DHP_Rebalance_Policy device property represents a value that indicates whether a device will participate in resource rebalancing following a dynamic hardware partitioning (DHP) processor hot-add operation.
keywords: ["DEVPKEY_Device_DHP_Rebalance_Policy Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_DHP_Rebalance_Policy
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/23/2022
---

# DEVPKEY_Device_DHP_Rebalance_Policy

The DEVPKEY_Device_DHP_Rebalance_Policy device property represents a value that indicates whether a device will participate in resource rebalancing following a [dynamic hardware partitioning (DHP)](../kernel/introduction-to-dynamic-hardware-partitioning.md) processor hot-add operation.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_Device_DHP_Rebalance_Policy |
| Property-data-type identifier | [**DEVPROP_TYPE_INT32**](./devprop-type-int32.md) |
| Property access | Read and write access by applications and services. |
| Localized? | No |

## Remarks

On a dynamically partitionable server that is running Windows Server 2008 or later versions of Windows Server, the operating system initiates a system-wide resource rebalance whenever a new processor is dynamically added to the system. The DEVPKEY_Device_DHP_Rebalance_Policy device property determines whether a device participates in such a resource rebalance. The device participates in resource rebalancing under the following circumstances:

- The DEVPKEY_Device_DHP_Rebalance_Policy device property does not exist.

- The device property exists and the value of the device property is not set.

- The device property exists and the value of the device property is set to 2.

If the DEVPKEY_Device_DHP_Rebalance_Policy device property exists and the value of the property is set to 1, the device will not participate in resource rebalancing when a new processor is dynamically added to the system.

A device's [device setup class](./overview-of-device-setup-classes.md) is specified in the [**INF Version Section**](./inf-version-section.md) of the device's INF file.

The default behavior for devices in the Network Adapter (Class = Net) device setup class is that members of the class do not participate in resource rebalancing when a new processor is dynamically added to the system. The default behavior for devices in all other device setup classes is that members participate in resource rebalancing when a new processor is dynamically added to the system.

This device property does not affect whether a device will participate in a resource rebalance that is initiated for other reasons.

You can access the DEVPKEY_Device_DHP_Rebalance_Policy property by calling [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) and [**CM_Set_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_devnode_propertyw) or [**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw).

## Requirements

**Version**: Windows Server 2008 and later versions of Windows Server

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

[**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw)
