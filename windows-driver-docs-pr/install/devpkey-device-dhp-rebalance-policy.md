---
title: DEVPKEY_Device_DHP_Rebalance_Policy
description: DEVPKEY_Device_DHP_Rebalance_Policy
ms.assetid: a882a114-9d1b-41ca-ab24-c2cdda952177
keywords: ["DEVPKEY_Device_DHP_Rebalance_Policy Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_DHP_Rebalance_Policy
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_DHP_Rebalance_Policy


The DEVPKEY_Device_DHP_Rebalance_Policy device property represents a value that indicates whether a device will participate in resource rebalancing following a [dynamic hardware partitioning (DHP)](https://msdn.microsoft.com/library/windows/hardware/ff544234) processor hot-add operation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_DHP_Rebalance_Policy</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-int32.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_INT32&lt;/strong&gt;](devprop-type-int32.md)"><strong>DEVPROP_TYPE_INT32</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by applications and services.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

On a dynamically partitionable server that is running Windows Server 2008 or later versions of Windows Server, the operating system initiates a system-wide resource rebalance whenever a new processor is dynamically added to the system. The DEVPKEY_Device_DHP_Rebalance_Policy device property determines whether a device participates in such a resource rebalance. The device participates in resource rebalancing under the following circumstances:

-   The DEVPKEY_Device_DHP_Rebalance_Policy device property does not exist.

-   The device property exists and the value of the device property is not set.

-   The device property exists and the value of the device property is set to 2.

If the DEVPKEY_Device_DHP_Rebalance_Policy device property exists and the value of the property is set to 1, the device will not participate in resource rebalancing when a new processor is dynamically added to the system.

A device's [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) is specified in the [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of the device's INF file.

The default behavior for devices in the Network Adapter (Class = Net) device setup class is that members of the class do not participate in resource rebalancing when a new processor is dynamically added to the system. The default behavior for devices in all other device setup classes is that members participate in resource rebalancing when a new processor is dynamically added to the system.

This device property does not affect whether a device will participate in a resource rebalance that is initiated for other reasons.

You can access the DEVPKEY_Device_DHP_Rebalance_Policy property by calling [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) and [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163).

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
<td align="left"><p>Available in Windows Server 2008 and later versions of Windows Server.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

[**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163)

 

 






