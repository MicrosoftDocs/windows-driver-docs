---
title: OID_PNP_QUERY_POWER
description: OID_PNP_QUERY_POWER
ms.assetid: 62675042-3339-48de-97bb-58bfa05e1b39
ms.date: 08/08/2017
keywords: 
 -OID_PNP_QUERY_POWER Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PNP\_QUERY\_POWER





The OID\_PNP\_QUERY\_POWER OID requests the miniport driver to indicate whether it can transition its network adapter to the low-power state specified in the *InformationBuffer*. The low-power state is specified as one of the following NDIS\_DEVICE\_POWER\_STATE values:

<a href="" id="ndisdevicestated1"></a>**NdisDeviceStateD1**  
This specifies a device state of D1.

<a href="" id="ndisdevicestated2"></a>**NdisDeviceStateD2**  
This specifies a device state of D2.

<a href="" id="ndisdevicestated3"></a>**NdisDeviceStateD3**  
This specifies a device state of D3.

An OID\_PNP\_QUERY\_POWER request is not used to request a transition to a device state of D0. NDIS simply sends an [OID\_PNP\_SET\_POWER](oid-pnp-set-power.md) request that specifies a device state of D0.

By returning NDIS\_STATUS\_SUCCESS to this OID request, the miniport driver guarantees that it will transition the network adapter to the specified device power state on receipt of a subsequent OID\_PNP\_SET\_POWER request. The miniport driver, in this case, must do nothing to jeopardize the transition.

Miniport drivers must always return NDIS\_STATUS\_SUCCESS to this OID request. Any other return code is an error.

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

 

 




