---
title: OID_WWAN_CONNECT
author: windows-driver-content
description: OID\_WWAN\_CONNECT activates or deactivates a particular packet context and reads the activation state of a context.
ms.assetid: 51be35fe-750b-4c2b-aab3-a9df59711f7d
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_CONNECT Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_CONNECT


OID\_WWAN\_CONNECT activates or deactivates a particular packet context and reads the activation state of a context.

Miniport drivers must process set and query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_CONTEXT\_STATE**](ndis-status-wwan-context-state.md) status notification containing an [**NDIS\_WWAN\_CONTEXT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567906) structure that indicates the Packet Data Protocol (PDP) context state of the MB device regardless of completing set or query requests.

Callers requesting to set the Packet Data Protocol (PDP) context state of the MB device provide an [**NDIS\_WWAN\_SET\_CONTEXT\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567920) structure to the miniport driver with the appropriate information.

Remarks
-------

For more information about using this OID, see [WWAN Packet Context Management](https://msdn.microsoft.com/library/windows/hardware/ff559086).

This object activates or deactivates a particular packet context and reads the activation state of a context. The miniport driver must send appropriate event notifications whenever the activation state changes.

This object is called only if the miniport driver is in a register state of **WwanRegisterStateHome**, **WwanRegisterStatePartner**, or **WwanRegisterStateRoaming**. When packet service is active, the device must also be in an attach state of **WwanPacketServiceStateAttached**.

Both set and query operations are supported for this object.

-   Processing of a set request requires network access but not SIM access.

-   Processing of a query request does not require access to network or the SIM.

The data structure for this OID is NDIS\_WWAN\_SET\_CONTEXT\_STATE. The miniport driver issues a status indication of NDIS\_STATUS\_WWAN\_CONTEXT\_STATE for both set and query requests.

In this version of the driver model, the miniport driver attempts context activation only as instructed by the MB Service. (Miniport drivers may activate a context initiated by the network in later versions.) Miniport drivers must not automatically activate a context even after losing registration or a signal. If the access string is not provided in the activation request, a miniport driver should not attempt to provide a default string. Instead, it must proceed with activating the context with a blank access string.

On the other hand, the miniport driver may deactivate a context as instructed by the MB service. This may occur when network connectivity has been lost for a period that exceeds the threshold of temporary loss of signal, or as part of a graceful shutdown or state cleanup.

Since only one activated context is supported in this version, activating or deactivating a particular context amounts to setting up or tearing down the layer-2 MB connection.

On set requests, the MB service furnishes both **ConnectionId** and **ActivationCommand** parameters in the WWAN\_CONTEXT\_STATE data structure. It instructs the miniport driver to activate or deactivate a packet context identified by **ConnectionId**, based on the **ActivationCommand** parameter value *WwanActivationCommandActivate* or *WwanActivationCommandDeactivate*.

-   If the service or subscription requires activation, the miniport driver should return error code WWAN\_STATUS\_SERVICE\_NOT\_ACTIVATED. The PDP-activation may not happen until the service or subscription is activated. All the emergency services might be available subject to the support from the device and the operator. The operating system might call the OID\_WWAN\_SERVICE\_ACTIVATION in response to this error code.

-   If the miniport driver receives a context activation request while another packet context is currently activated, it returns error code WWAN\_STATUS\_MAX\_ACTIVATED\_CONTEXTS.

-   If the miniport driver receives a context deactivation request but the context identified by **ConnectionId** is not currently activated, it returns error code WWAN\_STATUS\_CONTEXT\_NOT\_ACTIVATED.

The miniport driver uses the following logic to determine the validity of AccessString, UserName, and Password settings from a set request:

-   If **ActivationCommand** is *WwanActivationCommandDeactivate*, the miniport driver should ignore the settings of these three parameters. The rest of the cases only consider the case when **ActivationCommand** is *WwanActivationCommandActivate*.

Context activation persists across user logon and logoff. It is not per logon user.

On query requests, the MB Service uses this object to find out the activation state.

For response to query requests, miniport driver sends the NDIS\_STATUS\_WWAN\_CONTEXT\_STATE notification.

**Important**  Note:

 

In rare, but specific circumstances, the MB Service on Windows 7 may attempt to auto-connect before connectivity to the Internet has been determined for pre-existing connections or during a momentary disruption in Internet connectivity of pre-existing connections. This could result in simultaneous MB and WLAN/Ethernet connections. For example, this can occur during system boot when MB and other connections are attempted simultaneously and the Network List Manager service is still attempting to determine the Internet connectivity of other connections using active and passive methods. It could also occur due to temporary outages in network infrastructure like a corporate proxy server or an ISP network. Thus, the MB Service may attempt to auto-connect to the internet regardless of whether the "Auto-connect only if no alternate Internet connection is available" option is selected.

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
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[WWAN Packet Context Management](https://msdn.microsoft.com/library/windows/hardware/ff559086)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_CONNECT%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


