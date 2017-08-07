---
title: OID\_PNP\_QUERY\_POWER
author: windows-driver-content
description: OID\_PNP\_QUERY\_POWER
ms.assetid: 62675042-3339-48de-97bb-58bfa05e1b39
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_PNP_QUERY_POWER Network Drivers Starting with Windows Vista
---

# OID\_PNP\_QUERY\_POWER


## <a href="" id="ddk-oid-pnp-query-power-nr"></a>


The OID\_PNP\_QUERY\_POWER OID requests the miniport driver to indicate whether it can transition its network adapter to the low-power state specified in the *InformationBuffer*. The low-power state is specified as one of the following NDIS\_DEVICE\_POWER\_STATE values:

<a href="" id="ndisdevicestated1"></a>**NdisDeviceStateD1**  
This specifies a device state of D1.

<a href="" id="ndisdevicestated2"></a>**NdisDeviceStateD2**  
This specifies a device state of D2.

<a href="" id="ndisdevicestated3"></a>**NdisDeviceStateD3**  
This specifies a device state of D3.

An OID\_PNP\_QUERY\_POWER request is not used to request a transition to a device state of D0. NDIS simply sends an [OID\_PNP\_SET\_POWER](oid-pnp-set-power.md) request that specifies a device state of D0.

By returning NDIS\_STATUS\_SUCCESS to this OID request, the miniport driver guarantees that it will transition the network adapter to the specified device power state on receipt of a subsequent OID\_PNP\_SET\_POWER request. The miniport driver, in this case, must do nothing to jeopardize the transition.

An OID\_PNP\_QUERY\_POWER request is always followed by an OID\_PNP\_SET\_POWER request. The OID\_PNP\_SET\_POWER request may immediately follow the OID\_PNP\_QUERY\_POWER request or may arrive at an unspecified interval after the OID\_PNP\_QUERY\_POWER request. A device state of D0 specified in the OID\_PNP\_SET\_POWER request effectively cancels the OID\_PNP\_QUERY\_POWER request.

An intermediate driver must always return NDIS\_STATUS\_SUCCESS to a query of OID\_PNP\_QUERY\_POWER. An intermediate driver should never propagate an OID\_PNP\_QUERY\_POWER request to an underlying miniport driver.

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
<td><p>Supported for NDIS 5.1, and NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_PNP_QUERY_POWER%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


