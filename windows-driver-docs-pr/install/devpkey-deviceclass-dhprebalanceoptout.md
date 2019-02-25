---
title: DEVPKEY_DeviceClass_DHPRebalanceOptOut
description: The DEVPKEY_DeviceClass_DHPRebalanceOptOut device property represents a value that indicates whether an entire device class will participate in resource rebalancing after a dynamic hardware partitioning (DHP) processor hot-add operation has occurred.Property keyDEVPKEY_DeviceClass_DHPRebalanceOptOutProperty-data-type identifierDEVPROP_TYPE_BOOLEANProperty accessRead and write access by applications and services.Localized No RemarksOn a dynamically partitionable server that is running Windows Server 2008 or later versions of Windows Server, the operating system initiates a system-wide resource rebalance whenever a new processor is dynamically added to the system. The device class participates in resource rebalancing under the following circumstances The DEVPKEY_DeviceClass_DHPRebalanceOptOut device property does not exist.The device property exists and the value of the device property is not set.The device property exists and the value of the device property is set to FALSE.If the DEVPKEY_DeviceClass_DHPRebalanceOptOut device property exists and the value of the property is set to TRUE, the device class does not participate in resource rebalancing when a new processor is dynamically added to the system.A device's device setup class is specified in the INF Version Section of the device's INF file.The default value for this property for the Network Adapter (Class Net) is TRUE. The default value for this property for all other device setup classes is FALSE.This device property does not affect whether a device class participates in a resource rebalance that is initiated for other reasons.You can access the DEVPKEY_DeviceClass_DHPRebalanceOptOut property by calling SetupDiGetClassProperty and SetupDiSetClassProperty.
ms.assetid: e620ef24-b65d-4cf6-a21d-ffecad5804b4
keywords: ["DEVPKEY_DeviceClass_DHPRebalanceOptOut Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceClass_DHPRebalanceOptOut
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceClass_DHPRebalanceOptOut


The DEVPKEY_DeviceClass_DHPRebalanceOptOut device property represents a value that indicates whether an entire device class will participate in resource rebalancing after a [dynamic hardware partitioning (DHP)](https://msdn.microsoft.com/library/windows/hardware/ff544234) processor hot-add operation has occurred.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_DeviceClass_DHPRebalanceOptOut</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-boolean.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_BOOLEAN&lt;/strong&gt;](devprop-type-boolean.md)"><strong>DEVPROP_TYPE_BOOLEAN</strong></a></p></td>
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

 

**Remarks**

On a dynamically partitionable server that is running Windows Server 2008 or later versions of Windows Server, the operating system initiates a system-wide resource rebalance whenever a new processor is dynamically added to the system. The device class participates in resource rebalancing under the following circumstances:

-   The DEVPKEY_DeviceClass_DHPRebalanceOptOut device property does not exist.

-   The device property exists and the value of the device property is not set.

-   The device property exists and the value of the device property is set to **FALSE**.

If the DEVPKEY_DeviceClass_DHPRebalanceOptOut device property exists and the value of the property is set to **TRUE**, the device class does not participate in resource rebalancing when a new processor is dynamically added to the system.

A device's [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) is specified in the [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of the device's INF file.

The default value for this property for the Network Adapter (Class = Net) is **TRUE**. The default value for this property for all other device setup classes is **FALSE**.

This device property does not affect whether a device class participates in a resource rebalance that is initiated for other reasons.

You can access the DEVPKEY_DeviceClass_DHPRebalanceOptOut property by calling [**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086) and [**SetupDiSetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552128).

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


[**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086)

[**SetupDiSetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552128)

 

 






