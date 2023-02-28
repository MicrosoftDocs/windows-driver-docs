---
title: DEVPKEY_Numa_Proximity_Domain
description: The DEVPKEY_Numa_Proximity_Domain device property represents the proximity domain of a Non-Uniform Memory Architecture (NUMA).
keywords: ["DEVPKEY_Numa_Proximity_Domain Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Numa_Proximity_Domain
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
ms.topic: reference
---

# DEVPKEY_Numa_Proximity_Domain

The DEVPKEY_Numa_Proximity_Domain device property represents the proximity domain of a Non-Uniform Memory Architecture (NUMA).

| Attribute | Value |
|--|--|
| **Property key** | DEVPKEY_Numa_Proximity_Domain |
| **Property-data-type identifier** | [**DEVPROP_TYPE_INT32**](devprop-type-int32.md) |
| **Property access** | Read-only access by installation applications and installers; read and write access by a device driver |
| **Localized?** | No |

## Remarks

The value DEVPKEY_Numa_Proximity_Domain is a numeric value that represents a domain ID.

Typically, the operating system sets the value of DEVPKEY_Numa_Proximity_Domain by retrieving the corresponding information from system firmware.

You can retrieve the value of DEVPKEY_Numa_Proximity_Domain by calling **IoGetDevicePropertyData** in a device driver.

You can also call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Numa_Proximity_Domain.

The value of this property is owned by Windows and should be treated as read-only by drivers and applications.

Windows Server 2003, Windows XP, and Windows 2000 do not support this property.

## Requirements

**Version**: Windows Vista and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)
