---
title: NDIS_STATUS_QOS_OPERATIONAL_PARAMETERS_CHANGE
author: windows-driver-content
description: The miniport driver that supports NDIS Quality of Service (QoS) issues an NDIS_STATUS_QOS_OPERATIONAL_PARAMETERS_CHANGE status indication when its operational NDIS QoS parameters are either resolved for the first time or changed later.
ms.assetid: 15D2B139-1AEA-4252-8599-0EA4ED2E3733
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_QOS_OPERATIONAL_PARAMETERS_CHANGE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE


The miniport driver that supports NDIS Quality of Service (QoS) issues an **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication when its operational NDIS QoS parameters are either resolved for the first time or changed later. The miniport driver configures the network adapter with these operational parameters to perform QoS packet transmission.

When the miniport driver makes this status indication, it sets the **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure to a pointer to an [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure. The driver initializes this structure with its operational NDIS QoS parameters.

**Note**  This NDIS status indication is valid only for miniport drivers that support the IEEE 802.1 Data Center Bridging (DCB) interface.

 

Remarks
-------

The miniport driver issues an **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication under the following conditions:

-   The miniport driver must issue an **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication after it has initially resolved its operational NDIS QoS parameters and configured the network adapter with them.

-   After this initial status indication, the miniport driver must issue an **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication when its operational NDIS QoS parameters are changed. This can happen when either the local or remote NDIS QoS parameters are changed.

-   Miniport drivers obtain the local NDIS QoS parameters from the Windows operating system when the Data Center Bridging (DCB) component (Msdcb.sys) issues an object identifier (OID) method request of [OID\_QOS\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451835). This OID request contains an [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure that specifies the local NDIS QoS parameters.

    There may be situations when the miniport driver has to override the local NDIS QoS parameters when it resolves its operational NDIS QoS parameters. This is especially true if the local QoS parameters compromise the operational QoS parameters that are being used by any underlying protocols or technologies that are currently enabled on the network adapter. For example, the driver can override the local QoS parameters if the network adapter is enabled for remote boot through the Fibre Channel over Ethernet (FCoE) protocol.

    The miniport driver notifies NDIS and overlying drivers of its intention to override the local NDIS QoS parameters by issuing an **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication.

    For more information, see [Managing NDIS QoS Parameters](https://msdn.microsoft.com/library/windows/hardware/hh464015).

**Note**  Overlying drivers can use the **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication to determine the operational NDIS QoS parameters. Alternatively, these drivers can also issue OID query requests of [OID\_QOS\_OPERATIONAL\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451832) to obtain the operational NDIS QoS parameters at any time.

 

For information on how the miniport driver issues an **NDIS\_STATUS\_QOS\_OPERATIONAL\_PARAMETERS\_CHANGE** status indication, see [Indicating Changes to the Operational NDIS QoS Parameters](https://msdn.microsoft.com/library/windows/hardware/hh451447).

For more information about the various types of NDIS QoS parameters, see [Overview of NDIS QoS Parameters](https://msdn.microsoft.com/library/windows/hardware/hh440130).

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
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640)

[OID\_QOS\_OPERATIONAL\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451832)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_QOS_OPERATIONAL_PARAMETERS_CHANGE%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


