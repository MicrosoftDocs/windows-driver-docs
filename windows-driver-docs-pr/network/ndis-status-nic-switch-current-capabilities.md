---
title: NDIS_STATUS_NIC_SWITCH_CURRENT_CAPABILITIES
author: windows-driver-content
description: The NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES status indicates to NDIS and overlying drivers that the currently enabled hardware capabilities of the NIC switch in a network adapter have changed.
ms.assetid: 8F5DF045-4993-45E6-A5B9-502B695E3C62
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_NIC_SWITCH_CURRENT_CAPABILITIES Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES


The **NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES** status indicates to NDIS and overlying drivers that the currently enabled hardware capabilities of the NIC switch in a network adapter have changed.

The status indication is made by the miniport driver of the network adapter's PCI Express (PCIe) Physical Function (PF). The PF miniport driver runs in the management operating system of the Hyper-V parent partition.

Remarks
-------

The PF miniport driver must issue an **NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES** status indication whenever it detects a change to the currently enabled hardware capabilities of the NIC switch on the network adapter. These capabilities could change when one of the following conditions is true:

-   The currently enabled NIC switch hardware capabilities are changed through a management application developed by the independent hardware vendor (IHV).

-   The currently enabled NIC switch hardware capabilities change for one or more network adapters that belong to a load balancing failover (LBFO) team managed by a MUX intermediate driver. For more information, see [NDIS MUX Intermediate Drivers](https://msdn.microsoft.com/library/windows/hardware/ff566498).

When the PF miniport driver issues the **NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES** status indication, it must follow these steps:

1.  The miniport driver initializes an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure with the currently enabled hardware capabilities of the network adapter's NIC switch.
2.  The miniport driver initializes an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure in the following way:

    -   The **StatusCode** member must be set to **NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES**.

    -   The **StatusBuffer** member must be set to the pointer to a [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure. This structure contains the currently enabled hardware capabilities of the NIC switch.

    -   The **StatusBufferSize** member must be set to sizeof([**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583)).

3.  The PF miniport driver issues the status notification by calling [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600). The driver must pass a pointer to the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure to the *StatusIndication* parameter.

Overlying drivers can use the **NDIS\_STATUS\_NIC\_SWITCH\_CURRENT\_CAPABILITIES** status indication to determine the currently enabled NIC switch capabilities on the network adapter. Alternatively, these drivers can also issue OID query requests of [OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES](oid-nic-switch-current-capabilities.md) to obtain these capabilities at any time.

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
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[OID\_NIC\_SWITCH\_CURRENT\_CAPABILITIES](oid-nic-switch-current-capabilities.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_NIC_SWITCH_CURRENT_CAPABILITIES%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


