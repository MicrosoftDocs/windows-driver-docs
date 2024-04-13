---
title: DEVPKEY_Device_ContainerId
description: The DEVPKEY_Device_ContainerId device property is used by the Plug and Play (PnP) manager to group one or more device nodes into a device container that represents an instance of a physical device.
keywords: ["DEVPKEY_Device_ContainerId Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_ContainerId
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/23/2022
ms.topic: reference
---

# DEVPKEY_Device_ContainerId

The DEVPKEY_Device_ContainerId device property is used by the Plug and Play (PnP) manager to group one or more device nodes (*devnodes*) into a *device container* that represents an instance of a physical device.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_Device_ContainerId |
| Property-data-type identifier | [**DEVPROP_TYPE_GUID**](./devprop-type-guid.md) |
| Property access | Read-only access by installation applications and installers |
| Localized? | No |

## Remarks

Starting with Windows 7, the PnP manager uses the device container and its identifier (*ContainerID*) to group one or more *devnodes* that originated from and belong to each instance of a particular physical device. The ContainerID for a device instance is referenced through the DEVPKEY_Device_ContainerId device property.

When you group all the devnodes that originated from an instance of a single device into containers, you accomplish the following results:

- The operating system can determine how functionality is related among *devnodes* that originate from a physical device.

- The user or applications are presented with a device-centric view of devices instead of the traditional function-centric view.

The DEVPKEY_Device_ContainerId can be used to determine the device container grouping of *devnodes* in a system. For a given devnode, you can determine all the devnodes that belong to the same container by completing the following steps:

- Call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to query DEVPKEY_Device_ContainerId for the given devnode. Windows returns the ContainerID *GUID* value for the device container to which that devnode belongs.

- Enumerate all devnodes on the computer and query each devnode for its DEVPKEY_Device_ContainerId. Each ContainerId value that matches the ContainerId value of the original devnode is part of same container.

**Note**  All *devnodes* that belong to a container on a given bus type must share the same ContainerID value.

For more information about ContainerIDs, see [Container IDs](./container-ids.md).

## Requirements

**Version**: Windows 7 and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[Container IDs](./container-ids.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
