---
title: OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES
author: windows-driver-content
description: An overlying driver issues an object identifier (OID) query request of OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES to obtain the currently enabled hardware capabilities of the NIC switch in a network adapter.
ms.assetid: 529dc5d5-9b84-4891-9e7a-1f9f7850c6d7
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_NIC_SWITCH_CURRENT_CAPABILITIES Network Drivers Starting with Windows Vista
---

# OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES


An overlying driver issues an object identifier (OID) query request of OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES to obtain the currently enabled hardware capabilities of the NIC switch in a network adapter.

After a successful return from the OID query request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure.

Remarks
-------

Starting with NDIS 6.20, miniport drivers supply the currently enabled NIC switch hardware capabilities on the network adapter when its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called. The driver initializes an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure with the NIC switch hardware capabilities and sets the **CurrentNicSwitchCapabilities** member of the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure to a pointer to the **NDIS\_NIC\_SWITCH\_CAPABILITIES** structure. The miniport driver then calls the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function and sets the *MiniportAttributes* parameter to a pointer to an **NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES** structure.

**Note**  Starting with NDIS 6.30, miniport drivers that support the single root I/O virtualization (SR-IOV) interface must register the enabled hardware capabilities of the NIC switch. Drivers register these capabilities by calling [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672).

 

Overlying protocol and filter drivers do not have to issue OID query requests of OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES. NDIS provides the currently enabled NIC switch hardware capabilities of a network adapter to these drivers in the following way:

-   NDIS reports the currently enabled NIC switch hardware capabilities of an underlying network adapter to overlying protocol drivers in the **NicSwitchCapabilities** member of the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure during the bind operation.

-   NDIS reports the currently enabled NIC switch hardware capabilities of an underlying network adapter to overlying filter drivers in the **NicSwitchCapabilities** member of the [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure during the attach operation.

### Return Status Codes

NDIS handles the OID query request of the OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES request for miniport drivers. The drivers will not be issued this OID request.

When NDIS handles the OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES request, it returns one of the following status codes:

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
<td><p>The request completed successfully. The <strong>InformationBuffer</strong> points to an [<strong>NDIS_NIC_SWITCH_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_NOT_SUPPORTED</p></td>
<td><p>The miniport driver either does not support the single root I/O virtualization (SR-IOV) interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than sizeof([<strong>NDIS_NIC_SWITCH_CAPABILITIES</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566583)). The miniport driver must set the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_FAILURE</p></td>
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
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832)

[**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481)

[**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924)

[**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_NIC_SWITCH_CURRENT_CAPABILITIES%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


