---
title: Bug Check 0xCA PNP_DETECTED_FATAL_ERROR
description: The PNP_DETECTED_FATAL_ERROR bug check has a value of 0x000000CA. This indicates that the Plug and Play Manager encountered a severe error.
ms.assetid: 2092c4a7-e068-461f-b28e-8063faf5a031
keywords: ["Bug Check 0xCA PNP_DETECTED_FATAL_ERROR", "PNP_DETECTED_FATAL_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PNP_DETECTED_FATAL_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xCA: PNP\_DETECTED\_FATAL\_ERROR


The PNP\_DETECTED\_FATAL\_ERROR bug check has a value of 0x000000CA. This indicates that the Plug and Play Manager encountered a severe error, probably as a result of a problematic Plug and Play driver.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## PNP\_DETECTED\_FATAL\_ERROR Parameters


Parameter 1 identifies the type of violation.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>Address of newly-reported PDO</p></td>
<td align="left"><p>Address of older PDO which has been duplicated</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong>Duplicate PDO:</strong> A specific instance of a driver has enumerated multiple PDOs with identical device ID and unique IDs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>Address of purported PDO</p></td>
<td align="left"><p>Address of driver object</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong>Invalid PDO:</strong> An API which requires a PDO has been called with random memory, or with an FDO, or with a PDO which hasn&#39;t been initialized.</p>
<p>(An uninitialized PDO is one that has not been returned to Plug and Play by <strong>QueryDeviceRelation</strong> or <strong>QueryBusRelations</strong>.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3</p></td>
<td align="left"><p>Address of PDO whose IDs were queried</p></td>
<td align="left"><p>Address of ID buffer</p></td>
<td align="left"><p><strong>1:</strong> DeviceID</p>
<p><strong>2:</strong> UniqueID</p>
<p><strong>3:</strong> HardwareIDs</p>
<p><strong>4:</strong> CompatibleIDs</p></td>
<td align="left"><p><strong>Invalid ID:</strong> An enumerator has returned an ID which contains illegal characters or isn&#39;t properly terminated. (IDs must contain only characters in the ranges 0x20 - 0x2B and 0x2D - 0x7F.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x4</p></td>
<td align="left"><p>Address of PDO with DOE_DELETE_PENDING set</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong>Invalid enumeration of deleted PDO:</strong> An enumerator has returned a PDO which it had previously deleted using <strong>IoDeleteDevice</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x5</p></td>
<td align="left"><p>Address of PDO</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong>PDO freed while linked in devnode tree:</strong> The object manager reference count on a PDO dropped to zero while the devnode was still linked in the tree. (This usually indicates that the driver is not adding a reference when returning the PDO in a query IRP.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x8</p></td>
<td align="left"><p>Address of PDO whose stack returned the invalid bus relation</p></td>
<td align="left"><p>Total number of PDOs returned as bus relations</p></td>
<td align="left"><p>The index (zero-based) at which the first <strong>NULL</strong> PDO was found</p></td>
<td align="left"><p><strong>NULL pointer returned as a bus relation:</strong> One or more of the devices present on the bus is a <strong>NULL</strong> PDO.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x9</p></td>
<td align="left"><p>Connection type that was passed</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong>Invalid connection type passed to IoDisconnectInterruptEx:</strong> A driver has passed an invalid connection type to <strong>IoDisconnectInterruptEx</strong>. The connection type passed to this routine must match the one returned by a corresponding successful call to <strong>IoConnectInterruptEx</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA</p></td>
<td align="left"><p>Driver object</p></td>
<td align="left"><p>IRQL after returning from driver callback</p></td>
<td align="left"><p>Combined APC disable count after returning from driver callback</p></td>
<td align="left"><p><strong>Incorrect notify callback behavior:</strong> A driver failed to preserve IRQL or combined APC disable count across a Plug &#39;n&#39; Play notification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xB</p></td>
<td align="left"><p>Related PDO</p></td>
<td align="left"><p>Removal relations</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p><strong>Deleted PDO reported as relation:</strong> One of the removal relations for the device being removed has already been deleted.</p></td>
</tr>
</tbody>
</table>

 

 

 




