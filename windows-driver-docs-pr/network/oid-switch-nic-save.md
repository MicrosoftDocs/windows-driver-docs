---
title: OID\_SWITCH\_NIC\_SAVE
author: windows-driver-content
description: The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) method request of OID\_SWITCH\_NIC\_SAVE during an operation to save run-time data for an extensible switch port and its network adapter connection.
ms.assetid: FE2F9767-7186-42FF-85C1-2A8203FEF629
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_SWITCH_NIC_SAVE Network Drivers Starting with Windows Vista
---

# OID\_SWITCH\_NIC\_SAVE


The protocol edge of the Hyper-V extensible switch issues an object identifier (OID) method request of OID\_SWITCH\_NIC\_SAVE during an operation to save run-time data for an extensible switch port and its network adapter connection. The extension returns this data so that run-time data can be saved and restored at a later time. After the run-time data is saved, it is restored through OID set requests of [OID\_SWITCH\_NIC\_RESTORE](oid-switch-nic-restore.md).

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure. This structure is allocated by the protocol edge of the extensible switch.

Remarks
-------

When it receives the OID method request of OID\_SWITCH\_NIC\_SAVE, the extensible switch extension saves run-time data by doing the following:

-   The extension saves the data within the [**NDIS\_SWITCH\_NIC\_SAVE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/hh598216) structure starting from *SaveDataOffset* bytes from the start of the structure.

-   If the *SaveDataSize* provided is not large enough to hold the required save data, the extension sets the method structure’s *BytesNeeded* field to NDIS\_SIZEOF\_NDIS\_SWITCH\_NIC\_SAVE\_STATE\_REVISION\_1 plus the amount of buffer necessary to hold the save data, and completes the OID with NDIS\_STATUS\_BUFFER\_TOO\_SHORT. The OID will be reissued with the required size.

-   The extension populates the *ExtensionId* and *ExtensionFriendlyName* fields with its own identifier and name, and completes the OID method request with NDIS\_STATUS\_SUCCESS. This causes the protocol edge of the extensible switch to issue another OID method request to allow the extension to either return more save data, or allow other extensions down the stack to save their own data.

**Note**  If the extension does not have run-time data to save, it must call [**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830) to forward this OID method request to underlying extensions in the extensible switch driver stack. For more information about this procedure, see [Filtering OID Requests in an NDIS Filter Driver](https://msdn.microsoft.com/library/windows/hardware/ff549950).

 

The Hyper-V extensible switch populates the *Header*, *PortId*, *NicIdex*, *SaveDataSize* and *SaveDataOffset* fields of the structure before issuing the OID. The extension cannot modify these fields.

OID method requests of OID\_SWITCH\_NIC\_SAVE are ultimately handled by the underlying miniport edge of the extensible switch. After this OID method request has been received by the miniport edge of the extensible switch, it completes the OID request with NDIS\_STATUS\_SUCCESS. This notifies the protocol edge of the extensible switch that all extensions in the extensible switch driver stack have been queried for run-time data. The protocol edge of the extensible switch then issues an OID set request of [OID\_SWITCH\_NIC\_SAVE\_COMPLETE](oid-switch-nic-save-complete.md) to complete the save operation.

For more information on how to save run-time data for an extensible switch port, see [Saving Hyper-V Extensible Switch Run-Time Data](https://msdn.microsoft.com/library/windows/hardware/hh598299).

### Return Status Codes

The extensible switch extension returns one of the following status codes for the OID method request of OID\_SWITCH\_NIC\_SAVE.

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
<td><p>NDIS_STATUS_BUFFER_TOO_SHORT</p></td>
<td><p>The length of the information buffer is too small for the [<strong>NDIS_SWITCH_NIC_SAVE_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/hh598216) and its associated run-time data The extensible switch extension must set the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_SUCCESS</p></td>
<td><p>The extension returns this status if it is returning run-time data to save.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_<em>Xxx</em></p></td>
<td><p>The request failed for other reasons.</p></td>
</tr>
</tbody>
</table>

 

The underlying miniport edge of the extensible switch returns the following status code for the OID method request of OID\_SWITCH\_NIC\_SAVE.

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

[**NdisFOidRequest**](https://msdn.microsoft.com/library/windows/hardware/ff561830)

[OID\_SWITCH\_NIC\_RESTORE](oid-switch-nic-restore.md)

[OID\_SWITCH\_NIC\_SAVE\_COMPLETE](oid-switch-nic-save-complete.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_SWITCH_NIC_SAVE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


