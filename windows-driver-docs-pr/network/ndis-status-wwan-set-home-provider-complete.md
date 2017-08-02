---
title: NDIS_STATUS_WWAN_SET_HOME_PROVIDER_COMPLETE
author: windows-driver-content
description: Miniport drivers use the NDIS_STATUS_WWAN_SET_HOME_PROVIDER_COMPLETE notification to inform the MB Service about the completion of OID_WWAN_HOME_PROVIDER set requests. This notification uses the NDIS_WWAN_SET_HOME_PROVIDER structure.
ms.assetid: 458B5AF6-4785-4A19-9B8D-5A7CF04D5AB4
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WWAN_SET_HOME_PROVIDER_COMPLETE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_SET\_HOME\_PROVIDER\_COMPLETE


Miniport drivers use the NDIS\_STATUS\_WWAN\_SET\_HOME\_PROVIDER\_COMPLETE notification to inform the MB Service about the completion of [OID\_WWAN\_HOME\_PROVIDER](https://msdn.microsoft.com/library/windows/hardware/ff569826) set requests.

This notification uses the [**NDIS\_WWAN\_SET\_HOME\_PROVIDER**](https://msdn.microsoft.com/library/windows/hardware/hh439841) structure.

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
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WWAN_SET_HOME_PROVIDER_COMPLETE%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


