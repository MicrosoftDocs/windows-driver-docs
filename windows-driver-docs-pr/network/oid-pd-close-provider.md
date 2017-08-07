---
title: OID\_PD\_CLOSE\_PROVIDER
author: windows-driver-content
description: An NDIS protocol or filter driver sends an object identifier (OID) method request of OID\_PD\_CLOSE\_PROVIDER to the PDPI provider to give up access to the PD capability in a PDPI provider object.
ms.assetid: 8A504A81-6DC8-415C-9FDC-F03657A0EB87
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_PD_CLOSE_PROVIDER Network Drivers Starting with Windows Vista
---

# OID\_PD\_CLOSE\_PROVIDER


An NDIS protocol or filter driver sends an object identifier (OID) method request of OID\_PD\_CLOSE\_PROVIDER to the PDPI provider to give up access to the PD capability in a PDPI provider object.

An NDIS protocol or filter driver must call this OID when it receives an unbind notification, a pause indication, a low-power event, or a PD configuration change event that indicates the PD is disabled on the binding.

Before calling this OID, the NDIS protocol or filter driver must ensure that it has closed and freed all PD objects such as queues, counters, and filters that it created over the PD provider instance. The NDIS protocol or filter driver must guarantee that there are no in-progress calls to any of the PD provider dispatch table functions before issuing this OID.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[*MiniportOidRequest*](miniportoidrequest.md)

[**NDIS\_PD\_CLOSE\_PROVIDER\_PARAMETERS**](ndis-pd-close-provider-parameters.md)

[NDIS\_STATUS\_PD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/dn931850)

[OID\_PD\_OPEN\_PROVIDER](oid-pd-open-provider.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_PD_CLOSE_PROVIDER%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


