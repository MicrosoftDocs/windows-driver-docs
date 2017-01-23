---
title: NDIS-WDF Class Extension (Cx) Limitation
description: Due to some NetAdapterCx implementation details, certain existing WDF APIs need to be used carefully
ms.assetid: 
---

# NDIS-WDF Class Extension (Cx) Limitations

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

\[NetAdapterCx is preview only in the next major update to Windows 10\]

The following WDF APIs have restrictions when used in a NetAdapterCx client driver.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>WdfDeviceInitAssignSDDLString</p></td>
<td align="left"><p>By default NetAdapterDeviceInitConfig assings SDDL_DEVOBJ_SYS_ALL_ADM_RWX_WORLD_RW_RES_R as the default SDDL. Any more restrictive SDDL can have an impact on how the OS communicates with the adapter. For example, the adapter's statistics page might not be able to query the needed information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>WdfDeviceInitSetFileObjectConfig</p></td>
<td align="left"><p>If the client driver wants to use WDF File Objects, it should not let the framework use the first FsContext. This can be configured in WDF_FILEOBJECT_CONFIG (FileObjectClass field).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WdfDeviceInitAssignName, WdfDeviceInitSetReleaseHardwareOrderOnFailure, WdfDeviceInitSetDeviceType, WdfDeviceInitSetCharacteristics, WdfDeviceInitSetIoType and WdfDeviceInitSetPowerPageable</p></td>
<td align="left"><p>All of these APIs are called from NetAdapterDeviceInitConfig on behalf of the client driver. Calling these might result in unpredicted behavior.</p></td>
</tr>
<tr class="even">
<td align="left"><p>WdfDeviceCreateDeviceInterface</p></td>
<td align="left"><p>If the client driver calls this API with the ReferenceString parameter equal to NULL, all the IO sent to the device interface will be intercepted by NDIS. To bypass this the client driver can specify any reference string.</p></td>
</tr>
</tbody>
</table>