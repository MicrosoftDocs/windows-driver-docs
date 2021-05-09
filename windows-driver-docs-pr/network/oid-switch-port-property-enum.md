---
title: OID_SWITCH_PORT_PROPERTY_ENUM
description: The Hyper-V extensible switch extension issues an object identifier (OID) method request of OID_SWITCH_PORT_PROPERTY_ENUM to obtain an array.
ms.date: 08/08/2017
keywords: 
 -OID_SWITCH_PORT_PROPERTY_ENUM Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_SWITCH\_PORT\_PROPERTY\_ENUM


The Hyper-V extensible switch extension issues an object identifier (OID) method request of OID\_SWITCH\_PORT\_PROPERTY\_ENUM to obtain an array. This array contains the provisioned port policies that match the specified criteria. Each element in the array specifies the properties of a policy for a specified extensible switch port.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure contains a pointer to a buffer. This buffer contains the following data:

-   An [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_property_enum_parameters) structure that specifies the parameters for the policy enumeration of a specified port.

-   An array of [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_property_enum_info) structures. Each of these structures contains information about the properties of an extensible switch port policy.

    **Note**  If the **NumProperties** member of the [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_property_enum_parameters) structure is set to zero, no [**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_property_enum_info) structures are returned.

     

## Remarks

Before it issues an OID method request of OID\_SWITCH\_PORT\_PROPERTY\_ENUM, the extensible switch extension must follow these guidelines:

-   The extension can only issue the OID\_SWITCH\_PORT\_PROPERTY\_ENUM request after the protocol edge of the extensible switch issues an [OID\_SWITCH\_PORT\_CREATE](oid-switch-port-create.md) request and before it issues an [OID\_SWITCH\_PORT\_TEARDOWN](oid-switch-port-teardown.md) request.

-   The extension must call [*ReferenceSwitchPort*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_reference_switch_port) before it calls [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) to issue the OID\_SWITCH\_PORT\_PROPERTY\_ENUM request. This ensures that the specified port will not be deleted until after the OID request is completed.

    After the OID request is completed, the extension must call [*DereferenceSwitchPort*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_dereference_switch_port). The extension must call this function regardless of whether the OID request was completed with NDIS\_STATUS\_SUCCESS.

The OID\_SWITCH\_PORT\_PROPERTY\_ENUM OID must only be issued when the Hyper-V extensible switch has completed activation. Please see [Querying the Hyper-V Extensible Switch Configuration](./querying-the-hyper-v-extensible-switch-configuration.md) for more details.

**Note**  If the extension receives the OID method request of OID\_SWITCH\_PORT\_PROPERTY\_ENUM, it must not complete the OID request. Instead, it must call [**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest) to forward the OID request down the extensible switch driver stack.

 

### Return Status Codes

The underlying miniport edge of the extensible switch completes the OID query request of OID\_SWITCH\_PORT\_PROPERTY\_ENUM and returns the following status code.

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
</tbody>
</table>

 

## Requirements

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
[*DereferenceSwitchPort*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_dereference_switch_port)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request)

[**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_property_enum_info)

[**NDIS\_SWITCH\_PORT\_PROPERTY\_ENUM\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_switch_port_property_enum_parameters)

[**NdisFOidRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfoidrequest)

[Querying the Hyper-V Extensible Switch Configuration](./querying-the-hyper-v-extensible-switch-configuration.md)

[*ReferenceSwitchPort*](/windows-hardware/drivers/ddi/ndis/nc-ndis-ndis_switch_reference_switch_port)

 

