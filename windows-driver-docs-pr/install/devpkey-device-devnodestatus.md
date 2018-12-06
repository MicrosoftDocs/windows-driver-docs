---
title: DEVPKEY_Device_DevNodeStatus
description: DEVPKEY_Device_DevNodeStatus
ms.assetid: 538a78f0-c704-444e-8314-38b2e0421c39
keywords: ["DEVPKEY_Device_DevNodeStatus Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_DevNodeStatus
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_DevNodeStatus


The DEVPKEY_Device_DevNodeStatus device property represents the status of a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_DevNodeStatus</p></td>
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

 

Remarks
-------

The value of DEVPKEY_Device_DevNodeStatus is a bitwise OR of the DN_*Xxx* bit flags that are defined in Cfg.h.

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY_Device_DevNodeStatus.

Windows Server 2003, Windows XP, and Windows 2000 do not directly support this property. For information about how to access the status of a device instance on these earlier versions of Windows, see [Retrieving the Status and Problem Code for a Device Instance](https://msdn.microsoft.com/library/windows/hardware/ff550651).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**CM_Get_DevNode_Status**](https://msdn.microsoft.com/library/windows/hardware/ff538514)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






