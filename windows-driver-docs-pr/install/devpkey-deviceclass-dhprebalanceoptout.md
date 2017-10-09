---
title: DEVPKEY\_DeviceClass\_DHPRebalanceOptOut
description: The DEVPKEY\_DeviceClass\_DHPRebalanceOptOut device property represents a value that indicates whether an entire device class will participate in resource rebalancing after a dynamic hardware partitioning (DHP) processor hot-add operation has occurred.Property keyDEVPKEY\_DeviceClass\_DHPRebalanceOptOutProperty-data-type identifierDEVPROP\_TYPE\_BOOLEANProperty accessRead and write access by applications and services.Localized No RemarksOn a dynamically partitionable server that is running Windows Server 2008 or later versions of Windows Server, the operating system initiates a system-wide resource rebalance whenever a new processor is dynamically added to the system. The device class participates in resource rebalancing under the following circumstances The DEVPKEY\_DeviceClass\_DHPRebalanceOptOut device property does not exist.The device property exists and the value of the device property is not set.The device property exists and the value of the device property is set to FALSE.If the DEVPKEY\_DeviceClass\_DHPRebalanceOptOut device property exists and the value of the property is set to TRUE, the device class does not participate in resource rebalancing when a new processor is dynamically added to the system.A device's device setup class is specified in the INF Version Section of the device's INF file.The default value for this property for the Network Adapter (Class Net) is TRUE. The default value for this property for all other device setup classes is FALSE.This device property does not affect whether a device class participates in a resource rebalance that is initiated for other reasons.You can access the DEVPKEY\_DeviceClass\_DHPRebalanceOptOut property by calling SetupDiGetClassProperty and SetupDiSetClassProperty.
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
---

# DEVPKEY\_DeviceClass\_DHPRebalanceOptOut


The DEVPKEY\_DeviceClass\_DHPRebalanceOptOut device property represents a value that indicates whether an entire device class will participate in resource rebalancing after a [dynamic hardware partitioning (DHP)](https://msdn.microsoft.com/library/windows/hardware/ff544234) processor hot-add operation has occurred.

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
<td align="left"><p>[<strong>DEVPROP_TYPE_BOOLEAN</strong>](devprop-type-boolean.md)</p></td>
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

-   The DEVPKEY\_DeviceClass\_DHPRebalanceOptOut device property does not exist.

-   The device property exists and the value of the device property is not set.

-   The device property exists and the value of the device property is set to **FALSE**.

If the DEVPKEY\_DeviceClass\_DHPRebalanceOptOut device property exists and the value of the property is set to **TRUE**, the device class does not participate in resource rebalancing when a new processor is dynamically added to the system.

A device's [device setup class](https://msdn.microsoft.com/library/windows/hardware/ff541509) is specified in the [**INF Version Section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of the device's INF file.

The default value for this property for the Network Adapter (Class = Net) is **TRUE**. The default value for this property for all other device setup classes is **FALSE**.

This device property does not affect whether a device class participates in a resource rebalance that is initiated for other reasons.

You can access the DEVPKEY\_DeviceClass\_DHPRebalanceOptOut property by calling [**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086) and [**SetupDiSetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552128).

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20DEVPKEY_DeviceClass_DHPRebalanceOptOut%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





