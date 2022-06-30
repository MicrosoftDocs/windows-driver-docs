---
title: DEVPKEY_Device_ProblemStatus
description: The DEVPKEY_Device_ProblemStatus device property is an NTSTATUS value that is set when a problem code is generated.
keywords: ["DEVPKEY_Device_ProblemStatus Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_ProblemStatus
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/24/2022
---

# DEVPKEY_Device_ProblemStatus

The DEVPKEY_Device_ProblemStatus device property is an NTSTATUS value that is set when a problem code is generated. It provides more context on why the problem code was set. If no additional context is available, ProblemStatus shows as STATUS_SUCCESS (0x00000000).

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_Device_ProblemStatus |
| Property-data-type identifier | [**DEVPROP_TYPE_NTSTATUS**](devprop-type-int32.md) |
| Property access | Read-only access by installation applications and installers |
| Localized? | No |

## Remarks

For info on finding problem status in Device Manager or the kernel debugger, see [Retrieving the Status and Problem Code for a Device Instance](retrieving-the-status-and-problem-code-for-a-device-instance.md).

For more info about NTSTATUS values, see [Using NTSTATUS Values](../kernel/using-ntstatus-values.md).

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_ProblemStatus.

## Requirements

**Version**: Windows 8 and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**CM_Get_DevNode_Status**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_status)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
