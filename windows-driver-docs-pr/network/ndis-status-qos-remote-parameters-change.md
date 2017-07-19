---
title: NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE
author: windows-driver-content
description: The miniport driver that supports NDIS Quality of Service (QoS) issues an NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE status indication when its remote NDIS QoS parameters are either received from a peer for the first time or change later.
ms.assetid: 3DA5F4FA-193F-4716-8678-7B6FB833E68E
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_QOS_REMOTE_PARAMETERS_CHANGE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE


The miniport driver that supports NDIS Quality of Service (QoS) issues an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication when its remote NDIS QoS parameters are either received from a peer for the first time or change later. The miniport driver receives these QoS parameters from a remote peer through the IEEE 802.1Qaz Data Center Bridging Exchange (DCBX) protocol.

When the miniport driver makes this status indication, it sets the **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure to a pointer to an [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure. The driver initializes this structure with its remote NDIS QoS parameters.

**Note**  This NDIS status indication is valid only for miniport drivers that support the IEEE 802.1 Data Center Bridging (DCB) interface.

 

Remarks
-------

The miniport driver uses the DCBX protocol to receive the QoS parameters for a remote peer. The miniport driver resolves its operational NDIS QoS parameters based on its local and remote QoS settings. Once the operational parameters are resolved, the miniport driver configures the network adapter with these parameters for QoS packet transmission.

For more information about how the driver resolves its operational NDIS QoS parameter settings, see [Resolving Operational NDIS QoS Parameters](https://msdn.microsoft.com/library/windows/hardware/hh440220).

The miniport driver must follow these guidelines for issuing an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication:

-   If the miniport driver has not received a DCBX frame from a remote peer, it must not issue an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication.

-   The miniport driver must issue an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication after it has first received the QoS settings from a remote peer.

    **Note**  The miniport driver must issue this status indication if the network adapter receives remote QoS parameter settings from a peer before the driver's local QoS parameters are set. For more information, see [Setting Local NDIS QoS Parameters](https://msdn.microsoft.com/library/windows/hardware/hh440225).

     

-   After this initial status indication, the miniport driver must only issue an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication when it determines a change in the QoS settings on the remote peer.

    **Note**  Miniport drivers must not issue an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication if there have been no changes to the remote NDIS QoS parameters. If the driver does make this type of status indication, NDIS may not pass the indication to overlying drivers.

     

**Note**  Overlying drivers can use the **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication to determine the remote NDIS QoS parameters. Alternatively, these drivers can also issue OID query requests of [OID\_QOS\_REMOTE\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451841) to obtain the remote NDIS QoS parameters at any time.

 

For more information on how the miniport driver issues an **NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE** status indication, see [Indicating Changes to the Remote NDIS QoS Parameters](https://msdn.microsoft.com/library/windows/hardware/hh406724).

For more information about the remote NDIS QoS parameters, see [Overview of NDIS QoS Parameters](https://msdn.microsoft.com/library/windows/hardware/hh440130).

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

[OID\_QOS\_REMOTE\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451841)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_QOS_REMOTE_PARAMETERS_CHANGE%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


