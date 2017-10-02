---
title: OID_NIC_SWITCH_PARAMETERS
author: windows-driver-content
description: An overlying driver issues an object identifier (OID) method request of OID\_NIC\_SWITCH\_PARAMETERS to obtain the current configuration parameters of a specified NIC switch on a network adapter.
ms.assetid: 3F2FF2C0-8710-4243-8583-CD80F244FCFB
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_NIC_SWITCH_PARAMETERS Network Drivers Starting with Windows Vista
---

# OID\_NIC\_SWITCH\_PARAMETERS


An overlying driver issues an object identifier (OID) method request of OID\_NIC\_SWITCH\_PARAMETERS to obtain the current configuration parameters of a specified NIC switch on a network adapter. NDIS handles these OID method requests for the miniport driver.

Overlying drivers issue an OID set request of OID\_NIC\_SWITCH\_PARAMETERS to set the configuration parameters of a specified NIC switch on a network adapter. These OID set requests are issued to the miniport driver of the network adapter's PCI Express (PCIe) Physical Function (PF). These OID set requests are required for PF miniport drivers that support the single root I/O virtualization (SR-IOV) interface.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains a pointer to an [**NDIS\_NIC\_SWITCH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451587) structure.

The overlying driver specifies the NIC switch for the OID method or set request by setting the **SwitchId** member of the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451587) structure to the switch identifier. The overlying driver obtains the switch identifier through one of the following ways:

-   From a previous OID method request of [OID\_NIC\_SWITCH\_ENUM\_SWITCHES](oid-nic-switch-enum-switches.md).

-   From the **NicSwitchArray** member of the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure. NDIS passes a pointer to this structure in the *BindParameters* parameter of the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function.

-   From the **NicSwitchArray** member of the [**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481) structure. NDIS passes a pointer to this structure in the *AttachParameters* parameter of the [*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905) function.

**Note**  Starting with Windows Server 2012, Windows supports only the default NIC switch on the network adapter. The **SwitchId** member of the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451587) structure must be set to NDIS\_DEFAULT\_SWITCH\_ID.

 

Remarks
-------

The overlying driver issues OID\_NIC\_SWITCH\_PARAMETERS requests in the following way:

-   The overlying driver issues an OID method request of OID\_NIC\_SWITCH\_PARAMETERS to obtain the current parameters of a specified NIC switch. For more information, see [Querying the Parameters of a NIC Switch](https://msdn.microsoft.com/library/windows/hardware/hh440179).

    **Note**  NDIS handles OID method requests of OID\_NIC\_SWITCH\_PARAMETERS for the PF miniport driver.

     

-   The overlying driver issues an OID set request of OID\_NIC\_SWITCH\_PARAMETERS to change the current parameters of a specified NIC switch. For more information, see [Setting the Parameters of a NIC Switch](https://msdn.microsoft.com/library/windows/hardware/hh440227).

    **Note**  The PF miniport driver handles OID set requests of OID\_NIC\_SWITCH\_PARAMETERS.

     

### Return Status Codes

NDIS or the PF miniport driver returns the following status codes for set or method OID requests of OID\_NIC\_SWITCH\_PARAMETERS.

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
<td><p>The PF miniport driver either does not support the single root I/O virtualization (SR-IOV) interface or is not enabled to use the interface.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_INVALID_PARAMETER</p></td>
<td><p>One or more of the members of the [<strong>NDIS_NIC_SWITCH_PARAMETERS</strong>](https://msdn.microsoft.com/library/windows/hardware/hh451587) structure have invalid values.</p></td>
</tr>
<tr class="even">
<td><p>NDIS_STATUS_INVALID_LENGTH</p></td>
<td><p>The information buffer was too short. NDIS or the PF miniport driver sets the <strong>DATA.METHOD_INFORMATION.BytesNeeded</strong> member (for OID method requests) or <strong>DATA.SET_INFORMATION.BytesNeeded</strong> member (for OID set requests) in the [<strong>NDIS_OID_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure to the minimum buffer size that is required.</p></td>
</tr>
<tr class="odd">
<td><p>NDIS_STATUS_REINIT_REQUIRED</p></td>
<td><p>The PF miniport driver requires a reinitialization of the network adapter to apply the changes to the NIC switch.</p></td>
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
[*FilterAttach*](https://msdn.microsoft.com/library/windows/hardware/ff549905)

[**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832)

[**NDIS\_FILTER\_ATTACH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565481)

[**NDIS\_NIC\_SWITCH\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451587)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

[OID\_NIC\_SWITCH\_CREATE\_SWITCH](oid-nic-switch-create-switch.md)

[OID\_NIC\_SWITCH\_ENUM\_SWITCHES](oid-nic-switch-enum-switches.md)

[*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_NIC_SWITCH_PARAMETERS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


