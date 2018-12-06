---
title: OID_QOS_PARAMETERS
description: The Data Center Bridging (DCB) component (Msdcb.sys) issues an object identifier (OID) method request of OID_QOS_PARAMETERS to configure the local NDIS Quality of Service (QoS) parameters on a network adapter.
ms.assetid: 1CA97C8A-8F5B-4AB2-B68E-DF1FA772C08F
ms.date: 08/08/2017
keywords: 
 -OID_QOS_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_QOS\_PARAMETERS


The Data Center Bridging (DCB) component (Msdcb.sys) issues an object identifier (OID) method request of OID\_QOS\_PARAMETERS to configure the local NDIS Quality of Service (QoS) parameters on a network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure.

**Note**  This OID method request is mandatory for miniport drivers that support NDIS QoS for the IEEE 802.1 Data Center Bridging (DCB) interface.



Remarks
-------

Miniport drivers obtain the local NDIS QoS parameters through an OID method request of OID\_QOS\_PARAMETERS. These parameters define how the network adapter prioritizes transmit, or *egress*, packets. For more information about these parameters, see [Overview of NDIS QoS Parameters](https://msdn.microsoft.com/library/windows/hardware/hh440130).

**Note**  Only the DCB component can issue an OID method request of OID\_QOS\_PARAMETERS. An overlying protocol or filter driver must not issue this OID. For more information on the DCB component, see [NDIS QoS Architecture for Data Center Bridging](https://msdn.microsoft.com/library/windows/hardware/hh451627).



The DCB component issues an OID\_QOS\_PARAMETERS request under the following conditions:

-   The system administrator installs or uninstalls the Microsoft DCB server feature.

    For more information about the DCB server feature, see [System-Provided DCB Components](https://msdn.microsoft.com/library/windows/hardware/hh440259).

-   The system administrator enables or disables the DCB server feature while the feature is still installed.

-   The system administrator changes any of the DCB server feature parameters.

-   The operating system starts or restarts while the DCB server feature is installed.

When the miniport driver handles the OID method request of OID\_QOS\_PARAMETERS, it must follow these guidelines:

-   The miniport driver copies the data within the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure to its cache of local NDIS QoS parameters. The driver then resolves its operational NDIS QoS parameters based on its cache of local NDIS QoS parameters and its cache of NDIS QoS parameters that it received from a remote peer.

    For more information about how the miniport driver resolves its operational parameters, see [Resolving Operational NDIS QoS Parameters](https://msdn.microsoft.com/library/windows/hardware/hh440220).

-   The miniport driver must not modify any data that is contained within the [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure. The driver must complete the OID method request and return the original data within the **NDIS\_QOS\_PARAMETERS** structure.

-   The **NDIS\_QOS\_PARAMETERS\_WILLING** flag specifies whether the miniport driver enables or disables the local Data Center Bridging Exchange (DCBX) Willing state. The driver handles this flag in the following way:

    -   If this flag is set, the miniport driver must enable the local DCBX Willing state. This allows the driver to be remotely configured with QoS settings. In this case, the driver resolves its operational QoS parameters based on the remote QoS parameters. The miniport driver can also resolve its operational QoS parameters based on any proprietary QoS settings that are defined by the independent hardware vendor (IHV).

    -   If this flag is not set, the miniport driver must disable the local DCBX Willing state. This allows the driver to resolve its operational QoS parameters from its local QoS parameters instead of remote QoS parameters. The miniport driver must also disable or override any local QoS parameter for which the related **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CONFIGURED** flag is not set.

        For example, the miniport driver can override an unconfigured local QoS parameter with its proprietary settings for the QoS parameter that is defined by the IHV. If there are no proprietary settings for local QoS parameters that are not specified with an **NDIS\_QOS\_PARAMETERS\_*Xxx*\_CONFIGURED** flag, the driver must disable the use of these QoS parameters on the network adapter.

        **Note**  The driver can also override configured local QoS parameters if they compromise the QoS parameters used by protocols or technologies that are enabled on the network adapter. For example, the driver can override the local QoS parameters if the network adapter is enabled for remote boot through the Fibre Channel over Ethernet (FCoE) protocol.

    For more information about the local DCBX Willing state, see [Managing the Local DCBX Willing State](https://msdn.microsoft.com/library/windows/hardware/hh706282).

For more information on how the miniport driver overrides local QoS parameters, see [Managing NDIS QoS Parameters](https://msdn.microsoft.com/library/windows/hardware/hh464015).

**Note**  Overriding the local QoS parameters should not cause the miniport driver to fail the OID method request of OID\_QOS\_PARAMETERS.

For more information on how the miniport driver manages the local QoS parameters, see [Setting Local NDIS QoS Parameters](https://msdn.microsoft.com/library/windows/hardware/hh440225).

### Return Status Codes

The miniport driver returns one of the following status codes.

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
<tr class="even">
<td><p>NDIS_STATUS_PENDING</p></td>
<td><p>The OID request is pending completion. When the miniport driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff563622" data-raw-source="[&lt;strong&gt;NdisMOidRequestComplete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563622)"><strong>NdisMOidRequestComplete</strong></a>, NDIS will pass the final status code and results to the OID request completion handler of the caller after the request is completed.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_NOT_SUPPORTED</p></td>
<td><p>The miniport driver does not support the NDIS QoS interface.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_PARAMETER</p></td>
<td><p>One or more members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451640" data-raw-source="[&lt;strong&gt;NDIS_QOS_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451640)"><strong>NDIS_QOS_PARAMETERS</strong></a> structure contain incorrect values.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The length of the information buffer is less than <strong>sizeof</strong>(<a href="https://msdn.microsoft.com/library/windows/hardware/hh451640" data-raw-source="[&lt;strong&gt;NDIS_QOS_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451640)"><strong>NDIS_QOS_PARAMETERS</strong></a>). NDIS sets the <strong>DATA.QUERY_INFORMATION.BytesNeeded</strong> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
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
[**NdisMOidRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563622)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[**NDIS\_QOS\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/hh451629)

[**NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439810)

[**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812)








