---
title: DEVPKEY_Device_BaseContainerId
description: The DEVPKEY_Device_BaseContainerId device property represents the GUID value of the base container identifier (ID).
keywords: ["DEVPKEY_Device_BaseContainerId Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_BaseContainerId
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/23/2022
---

# DEVPKEY_Device_BaseContainerId

The DEVPKEY_Device_BaseContainerId device property represents the *GUID* value of the base container identifier (*ID*). The Windows Plug and Play (PnP) manager assigns this value to the device node (*devnode*).

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_Device_BaseContainerId |
| Property-data-type identifier | [**DEVPROP_TYPE_GUID**](./devprop-type-guid.md) |
| Property access | Read-only access by installation applications and installers. |
| Corresponding SPDRP_*Xxx* identifier | SPDRP_BASE_CONTAINERID |
| Localized? | No |

## Remarks

The PnP manager determines the container ID for a devnode by using one of the following methods:

- A bus driver provides a container ID.

    When the PnP manager assigns a container ID to a devnode, it first checks whether the bus driver of the devnode can provide a container ID. Bus drivers provide a container ID through an [**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md) query request with the **Parameters.QueryId.IdType** field set to **BusQueryContainerID**.

- The PnP manager generates a container ID by using the removable device capability.

    If a bus driver cannot provide a container ID for a devnode that it is enumerating, the PnP manager uses the removable device capability to generate a container ID for all devnodes that are enumerated for the device. The bus driver reports this device capability in response to an [**IRP_MN_QUERY_CAPABILITIES**](../kernel/irp-mn-query-capabilities.md) request.

- The PnP manager generates a container ID by using an override of the removable device capability.

    Although the override mechanism does not change the value of the removable device capability, it forces the PnP manager to use the override setting and not the value of the removable device capability when it generates container IDs for devices.

For more information about these methods, see [How Container IDs are Generated](./how-container-ids-are-generated.md).

Regardless of how the container ID value is obtained, the PnP manager assigns the value to the DEVPKEY_Device_BaseContainerId property of the devnode.

The DEVPKEY_Device_BaseContainerId property can be used to force the grouping of a new devnode with other devnodes that exists in the system. This lets you use the new devnode as the parent (or *base*) container ID for other related devnodes. To do this, you must first obtain the DEVPKEY_Device_BaseContainerID GUID of the existing devnode. Then, you must return the container ID GUID of the new devnode in response to an [**IRP_MN_QUERY_ID**](../kernel/irp-mn-query-id.md) query request that has the **Parameters.QueryId.IdType** field set to **BusQueryContainerID**.

> [!NOTE]
> The value that is returned by a query of the DEVPKEY_Device_BaseContainerId or [**DEVPKEY_Device_ContainerId**](devpkey-device-containerid.md) properties can be different for the same devnode.

> [!NOTE]
> Do not use the DEVPKEY_Device_BaseContainerId property to reconstruct device container groupings in the system. Use the [**DEVPKEY_Device_ContainerId**](devpkey-device-containerid.md) property instead.

For more information about container IDs, see [Container IDs](./container-ids.md).

## Requirements

**Version**: Windows 7 and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[Container IDs](./container-ids.md)

[**DEVPKEY_Device_ContainerId**](devpkey-device-containerid.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
