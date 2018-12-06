---
title: OID_NIC_SWITCH_VPORT_PARAMETERS
description: An overlying driver can obtain the parameters for a virtual port (VPort) on a NIC switch that has been created on a network adapter that supports single root I/O virtualization (SR-IOV).
ms.assetid: B22C760E-F2B0-4774-A532-4044C679CD64
ms.date: 08/08/2017
keywords: 
 -OID_NIC_SWITCH_VPORT_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NIC\_SWITCH\_VPORT\_PARAMETERS


An overlying driver can obtain the parameters for a virtual port (VPort) on a NIC switch that has been created on a network adapter that supports single root I/O virtualization (SR-IOV). The driver issues an object identifier (OID) method request of OID\_NIC\_SWITCH\_VPORT\_PARAMETERS to obtain these parameters.

Overlying drivers issue an OID set request of OID\_NIC\_SWITCH\_VPORT\_PARAMETERS to set the configuration parameters of a specified VPort that is attached to the network adapter's NIC switch. These OID set requests are issued to the miniport driver of the network adapter's PCI Express (PCIe) Physical Function (PF). These OID set requests are required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure.

The overlying driver specifies the VPort for the OID method or set request by setting the **VPortId** member of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure to the identifier associated with the VPort. The overlying driver obtains the VPort identifier through one of the following ways:

-   From a previous OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md).

-   From a previous OID method request of [OID\_NIC\_SWITCH\_ENUM\_VPORTS](oid-nic-switch-enum-vports.md).

Remarks
-------

OID\_NIC\_SWITCH\_VPORT\_PARAMETERS can be used in either [OID method requests](#oid-method-requests) or [OID set requests](#oid-set-requests).

### <a href="" id="oid-method-requests"></a>Handling OID Method Requests of OID\_NIC\_SWITCH\_VPORT\_PARAMETERS

Overlying drivers issue an OID method request of OID\_NIC\_SWITCH\_VPORT\_PARAMETERS to query the current configuration parameters of a VPort that is attached to the network adapter's NIC switch. Overlying drivers specify the VPort to query by setting the **VPortId** member of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure to the VPort identifier.

NDIS handles the OID method request of OID\_NIC\_SWITCH\_VPORT\_PARAMETERS for miniport drivers. NDIS returns information that it obtained from previous OID requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md) and [OID\_NIC\_SWITCH\_ENUM\_VPORTS](oid-nic-switch-enum-vports.md).

After a successful return from the OID method request, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure. This structure contains the configuration parameters for the specified switch.

For more information, see [Querying the Parameters of a Virtual Port](https://msdn.microsoft.com/library/windows/hardware/hh440181).

### <a href="" id="oid-set-requests"></a>Handling OID Set Requests of OID\_NIC\_SWITCH\_VPORT\_PARAMETERS

Overlying drivers issue an OID set request of OID\_NIC\_SWITCH\_VPORT\_PARAMETERS to change the current configuration parameters of a VPort that is attached to a network adapter's NIC switch. This OID request can be used to update the parameters for default as well as nondefault VPorts.

Only a limited subset of configuration parameters for a VPort can be changed. The overlying driver specifies the parameter to change by setting the following members of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure:

1.  The **VPortId** member is set to the identifier of the VPort whose parameters will be changed.

2.  The appropriate NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS\_*Xxx*\_CHANGED flags are set in the **Flags** member. Members of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure can only be changed if a corresponding NDIS\_NIC\_SWITCH\_PARAMETERS\_*Xxx*\_CHANGED flag is defined in Ntddndis.h.

3.  The corresponding members of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure are set with the VPort configuration parameters that are to be changed.

After the PF miniport driver receives the OID set request of OID\_NIC\_SWITCH\_VPORT\_PARAMETERS, the driver configures the hardware with the configuration parameters. The driver can only change those configuration parameters identified by NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS\_*Xxx*\_CHANGED flags in the **Flags** member of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure.

For more information, see [Setting the Parameters of a Virtual Port](https://msdn.microsoft.com/library/windows/hardware/hh440228).

### Return Status Codes

NDIS or the PF miniport driver returns the following status code for set or method OID requests of OID\_NIC\_SWITCH\_VPORT\_PARAMETERS.

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
<td><p>The request completed successfully. The <strong>InformationBuffer</strong> points to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566583" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_CAPABILITIES&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566583)"><strong>NDIS_NIC_SWITCH_CAPABILITIES</strong></a> structure.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_NOT_SUPPORTED</p></td>
<td><p>The PF miniport driver either does not support the single root I/O virtualization (SR-IOV) interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_PARAMETER</p></td>
<td><p>One or more of the members of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451597" data-raw-source="[&lt;strong&gt;NDIS_NIC_SWITCH_VPORT_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh451597)"><strong>NDIS_NIC_SWITCH_VPORT_PARAMETERS</strong></a> structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. NDIS or the PF miniport driver sets the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member (for OID method requests) or <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member (for OID set requests) in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566710" data-raw-source="[&lt;strong&gt;NDIS_OID_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566710)"><strong>NDIS_OID_REQUEST</strong></a> structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="odd">
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
[**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md)

[OID\_NIC\_SWITCH\_ENUM\_VPORTS](oid-nic-switch-enum-vports.md)

 

 




