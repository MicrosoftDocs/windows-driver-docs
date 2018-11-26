---
title: OID_SWITCH_NIC_RESTORE
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID_SWITCH_NIC_RESTORE to notify the extensible switch extension about run-time data that can be restored for an extensible switch port and its network adapter connection.
ms.assetid: 252FB1D2-932F-4FB8-83D6-2690171D746D
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_NIC_RESTORE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_NIC\_RESTORE


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_RESTORE to notify the extensible switch extension about run-time data that can be restored for an extensible switch port and its network adapter connection.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure. This structure is allocated by the protocol edge of the extensible switch.

Remarks
-------

When it receives the OID set request of OID\_SWITCH\_NIC\_RESTORE, the extensible switch extension must first determine whether it owns the run-time data. The extension does this by comparing the value of the **ExtensionId** member of the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure to the GUID value that the extension uses to identify itself.

If the extension owns the run-time data for an extensible switch port, it restores this data in the following way:

1.  The extension copies the run-time data in the **SaveData** member to extension-allocated storage.

    **Note**  The value of the **PortId** member of the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure may be different from the **PortId** value at the time that the run-time data was saved. This can occur if run-time data was saved during a Live Migration from one host to another. However, the configuration of the extensible switch port is retained during the Live Migration. This enables the extension to restore the run-time data to the extensible switch port by using the new **PortId** value.

     

2.  The extension completes the OID set request with NDIS\_STATUS\_SUCCESS.

If the extension does not own the specified run-time data, the extension calls [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward this OID set request to underlying extensions in the extensible switch driver stack. In this case, the extension must not modify the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure that is associated with the OID request.

If the OID\_SWITCH\_NIC\_RESTORE set request is received by the miniport edge of the extensible switch, it completes the OID request with NDIS\_STATUS\_SUCCESS. This notifies the protocol edge of the extensible switch that no extension owns the run-time data.

For more information about how to restore run-time data, see [Restoring Hyper-V Extensible Switch Run-Time Data](https://msdn.microsoft.com/library/windows/hardware/hh598298).

**Note**  If the extension fails the OID set request, the extensible switch will fail the entire restore operation. As a result, the extension should avoid failing the OID request if it is possible. For example, if the extension cannot allocate the resource necessary to restore the run-time data, it should fail the OID request if it cannot function properly without restoring the run-time data. However, if the extension can recover from the failure condition, it should not fail the OID set request.

 

### Return Status Codes

If the extension completes the OID set request of OID\_SWITCH\_NIC\_RESTORE, it returns one of the following status codes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NDIS_STATUS_SUCCESS</p></td>
<td><p>The OID request completed successfully.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_<em>Xxx</em></p></td>
<td><p>The request failed for other reasons.</p></td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216)

[**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830)

 

 




