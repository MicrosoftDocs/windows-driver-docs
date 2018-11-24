---
title: DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION
description: A DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION constant specifies a type of management action that is performed by the driver on the data-set attributes for a device.
ms.assetid: cc64c7ad-7d1c-45c7-b236-a43e57086f8d
topic_type:
- apiref
api_name:
- DeviceDsmAction_None
- DeviceDsmAction_Trim
- DeviceDsmAction_Notification
- DeviceDsmAction_OffloadRead
- DeviceDsmAction_OffloadWrite
- DeviceDsmAction_Allocation
- DeviceDsmAction_Repair
- DeviceDsmAction_Scrub
- DeviceDsmAction_DrtQuery
- DeviceDsmAction_DrtClear
- DeviceDsmAction_DrtDisable
- DeviceDsmAction_NvCache_Change_Priority
- DeviceDsmAction_NvCache_Evict
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION


A **DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION** constant specifies a type of management action that is performed by the driver on the data-set attributes for a device.

The management action is specified in the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552527) structure contained in the system buffer of an [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff560573) request.

<span id="DeviceDsmAction_None"></span><span id="devicedsmaction_none"></span><span id="DEVICEDSMACTION_NONE"></span>**DeviceDsmAction\_None**
0
For structure initialization purposes only.

<span id="DeviceDsmAction_Trim"></span><span id="devicedsmaction_trim"></span><span id="DEVICEDSMACTION_TRIM"></span>**DeviceDsmAction\_Trim**
1
The driver will perform a trim operation.

<span id="DeviceDsmAction_Notification"></span><span id="devicedsmaction_notification"></span><span id="DEVICEDSMACTION_NOTIFICATION"></span>**DeviceDsmAction\_Notification**
(2 | DeviceDsmActionFlag\_NonDestructive)
The driver will perform a notification operation.

For this action, the **ParameterBlockOffset** and **ParameterBlockLength** members of the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552527) structure specify the parameters of the notification operation. These parameters are formatted as a [**DEVICE\_DSM\_NOTIFICATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff819207) structure.

&gt; \[!Note\]
&gt;  Supported in Windows 7 and later versions of Windows.

 

<span id="DeviceDsmAction_OffloadRead"></span><span id="devicedsmaction_offloadread"></span><span id="DEVICEDSMACTION_OFFLOADREAD"></span>**DeviceDsmAction\_OffloadRead**
(3 | DeviceDsmActionFlag\_NonDestructive)
The driver performs an offload read operation.

For this action, the **ParameterBlockOffset** and **ParameterBlockLength** members of the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552527) structure specify the parameters of the offload read operation. These parameters are formatted as a [**DEVICE\_DSM\_OFFLOAD\_READ\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh439639) structure.

&gt; \[!Note\]
&gt;  Supported in Windows 8 and later versions of Windows.

 

<span id="DeviceDsmAction_OffloadWrite"></span><span id="devicedsmaction_offloadwrite"></span><span id="DEVICEDSMACTION_OFFLOADWRITE"></span>**DeviceDsmAction\_OffloadWrite**
4
The driver will perform an offload write operation.

For this action, the **ParameterBlockOffset** and **ParameterBlockLength** members of the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552527) structure specify the parameters of the offload write operation. These parameters are formatted as a [**DEVICE\_DSM\_OFFLOAD\_WRITE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh439644) structure.

&gt; \[!Note\]
&gt;  Supported in Windows 8 and later versions of Windows.

 

<span id="DeviceDsmAction_Allocation"></span><span id="devicedsmaction_allocation"></span><span id="DEVICEDSMACTION_ALLOCATION"></span>**DeviceDsmAction\_Allocation**
(5 | DeviceDsmActionFlag\_NonDestructive)
The driver will perform a logical block provisioning operation.

The logical block range is specified in a single [**DEVICE\_DATA\_SET\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff552523) structure.

&gt; \[!Note\]
&gt;  Supported in Windows 8 and later versions of Windows.

 

<span id="DeviceDsmAction_Repair"></span><span id="devicedsmaction_repair"></span><span id="DEVICEDSMACTION_REPAIR"></span>**DeviceDsmAction\_Repair**
(6 | DeviceDsmActionFlag\_NonDestructive)
The driver will perform a storage spaces repair operation.

The logical block range is specified in a single [**DEVICE\_DATA\_SET\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff552523) structure. The number of repair copies is specified in a **DEVICE\_DATA\_SET\_REPAIR\_PARAMETERS** structure located in the input buffer as specified by the **ParameterBlockOffset** member of the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552527) structure.

&gt; \[!Note\]
&gt;  Supported in Windows 8 and later versions of Windows.

 

<span id="DeviceDsmAction_Scrub"></span><span id="devicedsmaction_scrub"></span><span id="DEVICEDSMACTION_SCRUB"></span>**DeviceDsmAction\_Scrub**
(7 | DeviceDsmActionFlag\_NonDestructive)
The driver will perform a storage spaces scrub operation.

The logical block range is specified in a single [**DEVICE\_DATA\_SET\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff552523) structure.

&gt; \[!Note\]
&gt;  Supported in Windows 8 and later versions of Windows.

 

<span id="DeviceDsmAction_DrtQuery"></span><span id="devicedsmaction_drtquery"></span><span id="DEVICEDSMACTION_DRTQUERY"></span>**DeviceDsmAction\_DrtQuery**
(8 | DeviceDsmActionFlag\_NonDestructive)
The driver will perform a query for the logical block range specified and checks if it is included in storage spaces dirty range tracking. The synchronization status of the range is returned in the **OperationStatus** member of the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES\_OUTPUT**](https://msdn.microsoft.com/library/windows/hardware/hh439656) structure.

The logical block range is specified, on input, in a single [**DEVICE\_DATA\_SET\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff552523) structure.

&gt; \[!Note\]
&gt;  Supported in Windows 8 and later versions of Windows.

 

<span id="DeviceDsmAction_DrtClear"></span><span id="devicedsmaction_drtclear"></span><span id="DEVICEDSMACTION_DRTCLEAR"></span>**DeviceDsmAction\_DrtClear**
(9 | DeviceDsmActionFlag\_NonDestructive)
The driver will clear dirty range status for the for the logical block range specified.

The logical block range is specified in a single [**DEVICE\_DATA\_SET\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff552523) structure.

&gt; \[!Note\]
&gt;  Supported in Windows 8 and later versions of Windows.

 

<span id="DeviceDsmAction_DrtDisable"></span><span id="devicedsmaction_drtdisable"></span><span id="DEVICEDSMACTION_DRTDISABLE"></span>**DeviceDsmAction\_DrtDisable**
(10 | DeviceDsmActionFlag\_NonDestructive)
The driver will disable dirty range tracking for the logical block range specified.

The logical block range is specified in a single [**DEVICE\_DATA\_SET\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff552523) structure.

&gt; \[!Note\]
&gt;  Supported in Windows 8 and later versions of Windows.

 

<span id="DeviceDsmAction_NvCache_Change_Priority"></span><span id="devicedsmaction_nvcache_change_priority"></span><span id="DEVICEDSMACTION_NVCACHE_CHANGE_PRIORITY"></span>**DeviceDsmAction\_NvCache\_Change\_Priority**
(14 | DeviceDsmActionFlag\_NonDestructive)
The driver will change the caching priority of specified ranges of logical blocks.

The new target priority is set in a **DEVICE\_DSM\_NVCACHE\_CHANGE\_PRIORITY\_PARAMETERS** structure which is located at **ParameterBlockOffset** in [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552527). The logical block ranges to change priority for are given in one or more [**DEVICE\_DATA\_SET\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff552523) structures.

The **DEVICE\_DSM\_NVCACHE\_CHANGE\_PRIORITY\_PARAMETERS** is defined in *ntddstor.h* and has the following members:

<span id="Size"></span><span id="size"></span><span id="SIZE"></span>Size  
Size of this structure. Set to **sizeof**(DEVICE\_DSM\_NVCACHE\_CHANGE\_PRIORITY\_PARAMETERS).

<span id="TargetPriority"></span><span id="targetpriority"></span><span id="TARGETPRIORITY"></span>TargetPriority  
The new target priority for the logical block ranges given.

<span id="Resrved_3_"></span><span id="resrved_3_"></span><span id="RESRVED_3_"></span>Resrved\[3\]  
Reserved bytes.

&gt; \[!Note\]
&gt;  Supported in Windows 8.1 and later versions of Windows.

 

<span id="DeviceDsmAction_NvCache_Evict"></span><span id="devicedsmaction_nvcache_evict"></span><span id="DEVICEDSMACTION_NVCACHE_EVICT"></span>**DeviceDsmAction\_NvCache\_Evict**
(15 | DeviceDsmActionFlag\_NonDestructive)
The driver will evict data from the caching medium. To evict all data, set the DEVICE\_DSM\_FLAG\_ENTIRE\_DATA\_SET\_RANGE flag in the **Flags** member of [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552527) and do not include any [**DEVICE\_DATA\_SET\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff552523) structures.

Specific logical block ranges to evict are given in one or more [**DEVICE\_DATA\_SET\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff552523) structures.

The **DeviceDsmAction\_NvCache\_Evict** action is executed synchronously. No other actions are serviced until the evict action has either succeeded or failed. In order to limit its impact on applications using the device, each **DeviceDsmAction\_NvCache\_Evict** action issued should include relatively small data ranges. They should not exceed 10 MB and ideally be smaller than 2 MB. This will minimize the chance that user level applications will experience noticeable delays when accessing data on the device.

&gt; \[!Note\]
&gt;  Supported in Windows 8.1 and later versions of Windows.

 

Remarks
-------

If a bitwise **OR** of the **DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION** constant value and the **DeviceDsmActionFlag\_NonDestructive** flag is performed, the specified action is nondestructive. If this flag is set, the driver can safely forward the [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff560573) request to the next lower driver in the stack even if the driver does not handle the specified action.

&gt; \[!Note\]
&gt;  Before it forwards the [**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff560573) request, the driver still performs the normal processing of the block of data set ranges that are specified in the [**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552527) structure. This block is located at **DataSetRangesOffset** and consists of one or more contiguous entries formatted as [**DEVICE\_DATA\_SET\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/ff552523) structures. The length, in bytes, of the data set ranges is set in the **DataSetRangesLength** member of **DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**.

 

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
<td align="left"><p>Available starting with Windows 7.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntddstor.h (include Ntddstor.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**DEVICE\_DSM\_NOTIFICATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff819207)

[**DEVICE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552527)

[**IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff560573)

 

 






