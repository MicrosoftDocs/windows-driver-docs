---
title: Handling a Set Power Request
description: Handling a Set Power Request
ms.assetid: c69d4a9b-009a-4320-8e20-32a9cf9113bf
keywords:
- set-power requests WDK NDIS intermediate
- Sleeping state WDK NDIS intermediate
- Working state WDK NDIS intermediate
- standby flags WDK NDIS intermediate
- power states WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling a Set Power Request





An intermediate driver must handle requests to set power to the working state (a network device power state of D0) and to sleeping states (a network device power state of D1, D2, or D3). The intermediate driver should also maintain power state variables and a StandBy flag. These issues are discussed further in this topic.

For examples of intermediate driver power management, see the [NDIS MUX Intermediate Driver and Notify Object](http://go.microsoft.com/fwlink/p/?LinkId=617916) driver sample in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

### Handling a Set Power Request to a Sleeping State

There are two cases where an intermediate driver must handle a set power request to a sleeping state:

-   NDIS requests that the virtual miniport upper edge of the intermediate driver go to a sleeping state.

-   The intermediate driver protocol lower edge handles the underlying miniport driver transition to a sleeping state when it receives a Plug and Play (PnP) event notification.

These events can happen in any order and one event does not necessarily accompany the other.

When the virtual miniport upper edge of the intermediate driver receives a request to set power to a sleeping state, the sequence of events for handling the request is as follows:

1.  NDIS calls the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function of each protocol driver bound to the virtual miniport. The call to *ProtocolNetPnPEvent* specifies a **NetEventSetPower** event for a sleeping state. Protocol drivers that are bound to the intermediate driver stop sending network data and making OID requests to the intermediate driver virtual miniport. The protocol lower edge of the intermediate driver can continue to send network data and requests down until NDIS indicates that the underlying miniport driver is making the transition to a sleeping state.

2.  NDIS pauses the overlying drivers and then the virtual miniport after issuing the **NetEventSetPower** event. The specified reason for the pause is a transition to a low-power state. For more information about pausing a virtual miniport, see [Pausing an Adapter](pausing-an-adapter.md).

    **Note**  No OID requests can be sent to the virtual miniport while it is in a low-power state, with the exception of [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780).

     

3.  NDIS issues an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) request to the virtual miniport of the intermediate driver. The intermediate driver accepts the request by returning NDIS\_STATUS\_SUCCESS. The intermediate driver must not propagate the OID\_PNP\_SET\_POWER request to the underlying miniport driver. After the intermediate driver completes this request, it should not indicate any more received network data or indicate status, even if it keeps receiving network data and status indications from the underlying miniport driver.

When the protocol lower edge of the intermediate driver transitions the underlying miniport driver to a sleeping state, the sequence of events for handling the transition is as follows:

1.  NDIS calls the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function of the intermediate driver protocol lower edge. The call to *ProtocolNetPnPEvent* specifies a **NetEventSetPower** event for a sleeping state. The intermediate driver must stop sending network data and making OID requests to the underlying miniport driver. If there are outstanding requests or sends, the intermediate driver should return NDIS\_STATUS\_PENDING from the call to *ProtocolNetPnPEvent*. The intermediate driver calls [**NdisCompleteNetPnPEvent**](https://msdn.microsoft.com/library/windows/hardware/ff561705) to complete the call to *ProtocolNetPnPEvent*. The protocol edge of an intermediate driver can still get received packet and status indications from the underlying miniport driver. Received network data can be ignored. If an intermediate driver's implementation depends upon monitoring the status of the underlying miniport driver, status indications should still be monitored.

2.  NDIS pauses the protocol edge of the intermediate driver and then pauses the underying miniport adapter after issuing the **NetEventSetPower** event. The specified reason for the pause is a transition to a low-power state. For more information about pausing a protocol binding, see [Pausing a Binding](pausing-a-binding.md).

    **Note**  No OID requests can be sent to the underlying miniport adapter while it is in a low-power state, with the exception of [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780).

     

3.  NDIS issues an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) request to the underlying miniport driver. However, if the underlying miniport driver does not support power management, it will be halted. In this case, even though NDIS halts the underlying miniport driver, it does not request the intermediate driver protocol to unbind from the underlying miniport driver and NIC. After the underlying miniport driver has successfully completed processing the OID (or the miniport driver is halted), it will not indicate any more network data or status.

### Handling a Set Power Request to the Working State

There are two cases where an intermediate driver handles a set power request to the working state:

-   NDIS requests that the virtual miniport upper edge of the intermediate driver go to the working state.

-   The intermediate driver protocol lower edge handles the underlying miniport driver transition to the working state, when it receives a Plug and Play (PnP) event notification.

These events can occur in any order and one event does not necessarily accompany the other.

When the virtual miniport upper edge of the intermediate driver receives a request to set power to a working state, the sequence of events for handling the request is as follows:

1.  NDIS issues an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) to the virtual miniport of the intermediate driver. The intermediate driver returns NDIS\_STATUS\_SUCCESS to the set power request. The intermediate driver must not propagate the OID\_PNP\_SET\_POWER request to the underlying miniport driver.

2.  NDIS restarts the virtual miniport and then restarts the overlying drivers after issuing the set power OID. For more information about restarting a virtual miniport, see [Starting an Adapter](starting-an-adapter.md).

3.  NDIS calls the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function of the overlying protocol drivers. The call to *ProtocolNetPnPEvent* specifies a **NetEventSetPower** event to set the working state (D0). Bound protocol drivers can start sending network data to the intermediate driver's virtual miniport.

When the protocol lower edge of the intermediate driver transitions the underlying miniport driver to a working state, the sequence of events for handling the transition is as follows:

1.  NDIS issues an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) to the underlying miniport driver or calls its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) handler if the underlying miniport driver was halted.

2.  NDIS restarts the underlying miniport driver and then the protocol edge of the intermediate NDIS and the underlying miniport adapter after issuing the OID. For more information about pausing a protocol binding, see [Restarting a Binding](restarting-a-binding.md).

3.  NDIS calls the [*ProtocolNetPnPEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570263) function of the intermediate driver. The call to *ProtocolNetPnPEvent* specifies a **NetEventSetPower** event to set the working state (D0). The intermediate driver can start sending network data to the underlying miniport driver.

### Power States and the Standby Flag

The intermediate driver should maintain a separate power state variable for each virtual miniport instance and for each underlying miniport driver to which the driver is bound. The intermediate driver should also maintain a StandingBy flag for each virtual miniport that is:

-   Set to **TRUE** when the power state of either the virtual miniport or the underlying miniport driver leaves D0.

-   Set to **FALSE** when the power state of either the virtual miniport or the underlying miniport driver returns to D0.

**Note**  For MUX intermediate drivers, there can be multiple virtual miniports that are associated with an underlying miniport driver or multiple underlying miniports that are associated with each virtual miniport. When the power state of any miniport adapter changes, the behavior of all of the associated miniports are also affected. How the behavior is affected is implementation-specific. For example, a driver that implements a Load Balancing Failover (LBFO) solution might not deactivate the virtual miniports when a single underlying miniport driver is deactivated. However, a driver implementation that depends on all underlying miniport drivers would require deactivation of virtual miniports when any underlying miniport driver is deactivated.

 

The intermediate driver should use the StandingBy flag and power state variables when processing requests as follows:

-   The driver's [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function should fail unless the virtual miniport and its underlying miniport adapter are both in D0.

-   The driver's [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function should always succeed OID\_PNP\_QUERY\_POWER to ensure that the driver receives the subsequent OID\_PNP\_SET\_POWER requests.

-   The driver's [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function should fail if the virtual miniport is not in D0 or if StandingBy is **TRUE**. Otherwise, it should queue a single request if the underlying miniport driver is not in D0. A queued request should be processed when the underlying miniport driver state becomes D0.

-   The intermediate driver virtual miniport should report status only if both the underlying miniport driver and virtual miniport are in D0.

 

 





