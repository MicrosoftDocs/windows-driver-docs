---
title: DEVPKEY_Device_BaseContainerId
description: DEVPKEY_Device_BaseContainerId
ms.assetid: ccc20b78-60a3-4351-9809-e2a285ad0a19
keywords: ["DEVPKEY_Device_BaseContainerId Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_BaseContainerId
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_BaseContainerId


The DEVPKEY_Device_BaseContainerId device property represents the [*GUID*](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-guid) value of the base container identifier (*ID*) .The Windows Plug and Play (PnP) manager assigns this value to the device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_BaseContainerId</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><a href="devprop-type-guid.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_GUID&lt;/strong&gt;](devprop-type-guid.md)"><strong>DEVPROP_TYPE_GUID</strong></a></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPDRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_BASE_CONTAINERID</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The PnP manager determines the container ID for a devnode by using one of the following methods:

-   A bus driver provides a container ID.

    When the PnP manager assigns a container ID to a devnode, it first checks whether the bus driver of the devnode can provide a container ID. Bus drivers provide a container ID through an [**IRP_MN_QUERY_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679) query request with the **Parameters.QueryId.IdType** field set to **BusQueryContainerID**.

-   The PnP manager generates a container ID by using the removable device capability.

    If a bus driver cannot provide a container ID for a devnode that it is enumerating, the PnP manager uses the removable device capability to generate a container ID for all devnodes that are enumerated for the device. The bus driver reports this device capability in response to an [**IRP_MN_QUERY_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664) request.

-   The PnP manager generates a container ID by using an override of the removable device capability.

    Although the override mechanism does not change the value of the removable device capability, it forces the PnP manager to use the override setting and not the value of the removable device capability when it generates container IDs for devices.

For more information about these methods, see [How Container IDs are Generated](https://msdn.microsoft.com/library/windows/hardware/ff546193).

Regardless of how the container ID value is obtained, the PnP manager assigns the value to the DEVPKEY_Device_BaseContainerId property of the devnode.

The DEVPKEY_Device_BaseContainerId property can be used to force the grouping of a new devnode with other devnodes that exists in the system. This lets you use the new devnode as the parent (or *base*) container ID for other related devnodes. To do this, you must first obtain the DEVPKEY_Device_BaseContainerID GUID of the existing devnode. Then, you must return the container ID GUID of the new devnode in response to an [**IRP_MN_QUERY_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679) query request that has the **Parameters.QueryId.IdType** field set to **BusQueryContainerID**.

**Note**   The value that is returned by a query of the DEVPKEY_Device_BaseContainerId or [**DEVPKEY_Device_ContainerId**](devpkey-device-containerid.md) properties can be different for the same devnode.

 

**Note**  Do not use the DEVPKEY_Device_BaseContainerId property to reconstruct device container groupings in the system. Use the [**DEVPKEY_Device_ContainerId**](devpkey-device-containerid.md) property instead.

 

For more information about container IDs, see [Container IDs](https://msdn.microsoft.com/library/windows/hardware/ff540024).

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
<td align="left"><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[Container IDs](https://msdn.microsoft.com/library/windows/hardware/ff540024)

[**DEVPKEY_Device_ContainerId**](devpkey-device-containerid.md)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

 

 






