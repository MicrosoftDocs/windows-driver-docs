---
title: OID_PM_PARAMETERS
author: windows-driver-content
description: As a query, protocol drivers can use the OID\_PM\_PARAMETERS OID to query the power management hardware capabilities of a network adapter that are currently enabled.
ms.assetid: c3431724-1b5f-4634-8b1e-27fed9031f01
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_PM_PARAMETERS Network Drivers Starting with Windows Vista
---

# OID\_PM\_PARAMETERS


As a query, protocol drivers can use the OID\_PM\_PARAMETERS OID to query the power management hardware capabilities of a network adapter that are currently enabled. After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure.

As a set, protocol drivers can use the OID\_PM\_PARAMETERS OID to enable or disable the current hardware capabilities of a network adapter. The protocol driver provides a pointer to an [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure in the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure.

Remarks
-------

Starting with NDIS 6.20, overlying protocol and filter drivers use OID\_PM\_PARAMETERS to query and set the power management hardware capabilities of a network adapter that are currently enabled.

When an overlying driver queries the OID\_PM\_PARAMETERS OID, NDIS completes the request without forwarding it to the miniport driver. NDIS stores the requested settings and combines them with the settings from other such requests. Before NDIS transitions the network adapter to the low power state, NDIS sends a set request to the miniport driver that contains the combined settings from all of the requests that NDIS stored.

The capabilities that are currently enabled can be a subset of the capabilities that the hardware supports. For more information about the capabilities that the hardware supports, see [OID\_PM\_HARDWARE\_CAPABILITIES](oid-pm-hardware-capabilities.md).

**Note**  If NDIS sets the NDIS\_PM\_SELECTIVE\_SUSPEND\_ENABLED flag in the **WakeUpFlags** member of [**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759) structure, it issues the OID set request of OID\_PM\_PARAMETERS directly to the miniport driver. This allows NDIS to bypass the processing by filter drivers in the networking driver stack.

 

NDIS or the miniport driver returns one of the following status codes for the request:

<a href="" id="ndis-status-success"></a>NDIS\_STATUS\_SUCCESS  
The request completed successfully.

<a href="" id="ndis-status-pending"></a>NDIS\_STATUS\_PENDING  
The request is pending completion. NDIS will pass the final status code and results to the OID request completion handler of the caller after the request is complete.

<a href="" id="ndis-status-buffer-too-short"></a>NDIS\_STATUS\_BUFFER\_TOO\_SHORT  
The information buffer was too short. NDIS set the **DATA.QUERY\_INFORMATION.BytesNeeded** member in the NDIS\_OID\_REQUEST structure to the minimum buffer size that is required.

<a href="" id="ndis-status-invalid-parameter"></a>NDIS\_STATUS\_INVALID\_PARAMETER  
The request failed because it tried to enable a capability that the underlying network adapter does not support.

<a href="" id="ndis-status-failure"></a>NDIS\_STATUS\_FAILURE  
The request failed for reasons other than the preceding reasons.

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
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_PM\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566759)

[OID\_PM\_HARDWARE\_CAPABILITIES](oid-pm-hardware-capabilities.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_PM_PARAMETERS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


