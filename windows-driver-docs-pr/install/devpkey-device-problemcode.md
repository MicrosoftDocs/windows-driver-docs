---
title: DEVPKEY_Device_ProblemCode
description: DEVPKEY_Device_ProblemCode
keywords: ["DEVPKEY_Device_ProblemCode Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_ProblemCode
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 02/28/2020
---

# DEVPKEY_Device_ProblemCode


The DEVPKEY_Device_ProblemCode device property represents the problem code for a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr>
<th>Attribute</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_ProblemCode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-int32.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_INT32&lt;/strong&gt;](devprop-type-int32.md)"><strong>DEVPROP_TYPE_INT32</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The value of DEVPKEY_Device_ProblemCode is one of the CM_PROB_*Xxx* problem codes that are defined in Cfg.h.

You can call [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_ProblemCode.

Windows Server 2003, Windows XP, and Windows 2000 do not directly support this property. For information about how to access the problem code for a device instance on these earlier versions of Windows, see [Retrieving the Status and Problem Code for a Device Instance](./retrieving-the-status-and-problem-code-for-a-device-instance.md).

For info on finding problem status in Device Manager or the kernel debugger, see [Retrieving the Status and Problem Code for a Device Instance](retrieving-the-status-and-problem-code-for-a-device-instance.md).

For additional information that may help with the problem code, see [**DEVPKEY_Device_ProblemStatus**](devpkey-device-problemstatus.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**CM_Get_DevNode_Status**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_status)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

[**DEVPKEY_Device_ProblemStatus**](devpkey-device-problemstatus.md)

