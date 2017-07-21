---
title: NDIS\_STATUS\_RESET\_END
author: windows-driver-content
description: The NDIS\_STATUS\_RESET\_END status indicates that a miniport adapter reset operation is complete.
ms.assetid: 09ced263-9e4b-45e3-ae5e-db033a03b5b6
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_RESET_END Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_RESET\_END


The NDIS\_STATUS\_RESET\_END status indicates that a miniport adapter reset operation is complete.

Remarks
-------

Miniport drivers should not call the [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) function to signal the start and finish of each reset operation because NDIS notifies overlying drivers when a reset operation begins and ends.

When a miniport driver starts a reset operation, NDIS notifies the overlying drivers with an [**NDIS\_STATUS\_RESET\_START**](ndis-status-reset-start.md) status indication.

After a bound protocol driver receives an NDIS\_STATUS\_RESET\_END status indication, the protocol driver can resume sending data and making OID requests.

After an overlying filter or intermediate driver receives an NDIS\_STATUS\_RESET\_END status indication, the driver can resume sending data and making OID requests to overlying drivers.

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
<td><p>Supported for NDIS 6.0 and NDIS 5.1 drivers in Windows Vista. Supported for NDIS 5.1 drivers in Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_RESET\_START**](ndis-status-reset-start.md)

[**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_RESET_END%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


