---
title: OID_SWITCH_NIC_RESTORE_COMPLETE
author: windows-driver-content
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_RESTORE\_COMPLETE to notify Hyper-V extensible switch extensions about the completion of the operation to restore run-time data.
ms.assetid: E47EBA55-FF35-4366-AF9C-A714C2E6F8FE
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_SWITCH_NIC_RESTORE_COMPLETE Network Drivers Starting with Windows Vista
---

# OID\_SWITCH\_NIC\_RESTORE\_COMPLETE


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) set request of OID\_SWITCH\_NIC\_RESTORE\_COMPLETE to notify Hyper-V extensible switch extensions about the completion of the operation to restore run-time data. Through this operation, the extension restores its run-time data for a port and its associated network adapter connection.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure. This structure is allocated by the protocol edge of the extensible switch.

Remarks
-------

When it receives the OID set request of OID\_SWITCH\_NIC\_RESTORE\_COMPLETE, the extension must follow these guidelines:

-   The extension must not modify the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure that is associated with the OID request.
-   The extension must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward this OID set request to underlying extensions in the extensible switch driver stack. The extension must not fail the OID request.

OID set requests of OID\_SWITCH\_NIC\_RESTORE\_COMPLETE are ultimately handled by the underlying miniport edge of the extensible switch. After this OID method request has been received by the miniport edge, it completes the OID request with NDIS\_STATUS\_SUCCESS. This notifies the protocol edge of the extensible switch that all extensions in the extensible switch driver stack have completed the save operation.

For more information on how to save run-time data for an extensible switch port, see [Saving Hyper-V Extensible Switch Run-Time Data](https://msdn.microsoft.com/library/windows/hardware/hh598299).

### Return Status Codes

If the extension completes the OID set request of [OID\_SWITCH\_NIC\_RESTORE\_COMPLETE](oid-switch-nic-restore.md), it returns one of the following status codes.

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SWITCH_NIC_RESTORE_COMPLETE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


