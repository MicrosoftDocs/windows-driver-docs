---
title: OID_WWAN_MODEM_CONFIG_INFO
author: windows-driver-content
description: OID_WWAN_MODEM_CONFIG_INFO retrieves information about the modem configuration information.
ms.assetid: 527B970C-09FC-4E49-A309-44D5C6A39778
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 - OID_WWAN_MODEM_CONFIG_INFO Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_MODEM\_CONFIG\_INFO


OID\_WWAN\_MODEM\_CONFIG\_INFO retrieves information about the modem configuration information.

MBB drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request before later sending an [NDIS\_STATUS\_WWAN\_MODEM\_CONFIG\_INFO](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-wwan-modem-config-info) status notification containing an [**NDIS\_WWAN\_MODEM\_CONFIG\_INFO**](netvista-ndis_wwan_modem_config_info) structure, which in turn contains a [**WWAN\_MODEM\_CONFIG\_INFO**](netvista-wwan_modem_config_info) structure, to provide information about the modem's configuration.

Set requests are not applicable.

Remarks
-------

The MBB driver may not have valid information yet from the modem during early queries. The non-valid information will be set to zero.

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
<td><p>the next major update to Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[NDIS\_STATUS\_WWAN\_MODEM\_CONFIG\_INFO](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-status-wwan-modem-config-info)

[**NDIS\_WWAN\_MODEM\_CONFIG\_INFO**](netvista-ndis_wwan_modem_config_info)

[**WWAN\_MODEM\_CONFIG\_INFO**](netvista-wwan_modem_config_info)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_MODEM_CONFIG_INFO%20%20RELEASE:%20%288/4/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


