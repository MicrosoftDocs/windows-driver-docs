---
title: Making a NeighborReachabilityQuery Indication
description: Making a NeighborReachabilityQuery Indication
ms.assetid: 131c30e1-5a1b-464d-ab88-92de35ba94e1
keywords:
- NeighborReachabilityQuery indication WDK TCP chimney offload
- HostReachability time WDK TCP chimney offload
- NICReachability time WDK TCP chimney offload
- neighbor reachability WDK TCP chimney offload
- neighbor solicitations WDK TCP chimney offload
- events WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Making a NeighborReachabilityQuery Indication


\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target calls the [**NdisMOffloadEventIndicate**](https://msdn.microsoft.com/library/windows/hardware/ff563619) function to make a **NeighborReachabilityQuery** indication to the host stack. The host stack uses this indication to detect neighbor reachability for both IPv4 and IPv6. Note that the IPv6 neighbor reachability algorithm is much more robust than the traditional IPv4 Address Resolution Protocol (ARP) algorithm for detecting neighbor reachability. Thus, the host stack uses the neighbor reachability algorithm for both IPv4 and IPv6 to determine whether a specific neighbor state object should be invalidated. For IPv6, the host stack uses IPv6 Neighbor Solicitation (NS) messages to perform address resolution (see RFC 2461). For IPv4, the host stack uses ARP messages (see RFC 826).

### Calculating the HostReachability Time and the NICReachability Time

When the host stack offloads a neighbor state object, it supplies values for the following two neighbor state variables:

-   HostReachabilityDelta (HRD). This variable is a cached variable that is maintained by the host stack.

-   NicReachabilityDelta (NRD). This variable is a delegated variable that is maintained by the offload target.

The offload target uses these variables to calculate the following timestamps after the neighbor state object has been offloaded:

-   HostReachabilityTime (HRT). This timestamp equals the network interface card's (NIC's) current time (NCT) minus the value of the HRD variable.

-   NICReachabilityTime (NRT). This timestamp equals NCT minus the value of the NRD variable.

As described in the following paragraphs, NRT is the only variable that the offload target updates on a per-packet basis.

The host stack specifies the HRD and NRD values in units of ticks. The host stack specifies the number of ticks per second in the **TicksPerSecond** member of the [**NDIS\_TASK\_TCP\_CONNECTION\_OFFLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff567873) structure when the host stack sets the [OID\_TCP\_TASK\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569815) OID. Based on the specified number of ticks per second, the offload target must scale the HRD and NRD values to match the offload target's timer resolution.

HRD, NRD, HRT, and NRT are unsigned variables of ULONG length, so the preceding calculations can cause HRT and NRT to wrap. The offload target must use modular arithmetic when making the calculations.

When the neighbor state object is offloaded, HRD and NRD are equal. Thus, HRT and NRT are also equal. While the offload target or host stack sends IP datagrams on the connection that uses the neighbor state object, the values of HRT and NRT diverge.

### NeighborReachability Processing

Forward progress is made on a TCP connection when TCP segments that are received from the remote peer indicate that the remote peer is receiving segments from the offload target or the local host stack (see RFC 2461). Examples of such TCP segments include:

-   A TCP acknowledgment (ACK) that is received in response to a segment that was sent by the host stack or the offload target.

-   A TCP segment that is received with a sequence number that was generated in response to an ACK that was sent by host stack or the offload target.

Whenever an offload target receives confirmation of forward progress on a connection, it finds the neighbor state object that was used by the connection and sets the neighbor state object's NRT to the NCT. This action resets the NRD value to zero.

Before the host stack sends an IP datagram on an offloaded connection, it checks its own neighbor cache entry (NCE) for the connection. (For more information about NCEs, see RFC 2461.) If the reachability state of the NCE is DELAY, the host stack calls the [**MiniportQueryOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559423) function of the offload target to query the NRD variable for the connection. The host uses the queried NRD value to determine whether its NCE should transition to the PROBE reachability state. (For more information about NCE reachability states, see RFC 2461.)

Before an offload target sends an IP datagram on an offloaded connection, it performs the following test:

```syntax
If ((NCT - NRT) > NCEStaleTicks & (NCT - HRT) > NCEStaleTicks) 
```

Note that the host stack supplies the NceStaleTicks value when setting [OID\_TCP\_TASK\_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff569815).

If this test is **TRUE**, the offload target does the following:

-   Calculates NRD (NRD = NCT - NRT).

-   Calls the [**NdisMOffloadEventIndicate**](https://msdn.microsoft.com/library/windows/hardware/ff563619) function with the *IndicationCode* parameter set to **NeighborReachabilityQuery**. The offload target also passes a pointer in the *OffloadBlockList* parameter to the **NdisMOffloadEventIndicate** function. This pointer references a single [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure that is immediately followed by:
    -   A [**NEIGHBOR\_OFFLOAD\_STATE\_CACHED**](https://msdn.microsoft.com/library/windows/hardware/ff568323) structure. This structure contains the HRD variable.
    -   A [**NEIGHBOR\_OFFLOAD\_STATE\_DELEGATED**](https://msdn.microsoft.com/library/windows/hardware/ff568325) structure. This structure contains the NRD variable.

In the call to **NdisMOffloadEventIndicate**, the offload target supplies the current value of the NRD variable and the HRD variable for the neighbor state object.

In response to a **NeighborReachabilityQuery** indication, the host stack synchronously returns a value for the neighbor's HRD variable. The offload target uses the HRD value to update HRT (HRT = NCT - HRD). The offload target performed this same calculation after the neighbor state object was offloaded.

The value of the HRD variable depends on whether the host stack's NCE for the neighbor is stale:

-   If the host stack's NCE is stale, the host stack returns a value of zero for HRD. This action causes the offload target's HRT variable to be equal to NCT, which prevents the offload target from making another **NeighborReachabilityQuery** indication for at least the value of NCEStaleTicks. The **NeighborReachabilityQuery** indication causes the host stack to start a timer. When that timer expires, the host stack queries the offload target's NRD value for the NCE:
    -   If the offload target has received confirmation of forward progress on the connection since it made the **NeighborReachabilityQuery** indication, it will have updated the NRT value. This update will cause the queried value of NRD to be less than the value of NRD that was supplied by the offload target in the **NeighborReachabilityQuery** indication. The host stack uses the queried value of NRD to update its copy of the HRD value. This update ends the **NeighborReachabilityQuery** indication procedure.
    -   If the offload target has not received confirmation of forward progress on the connection since it made the **NeighborReachabilityQuery** indication, the value of the queried NRD variable is greater than the value of NRD that is supplied by the offload target in the **NeighborReachabilityQuery** indication. In this situation, the host stack sends unicast Neighbor Solicitation probes to verify reachability of the neighbor. If the host stack does not receive a Neighbor Advertisement message in response to the probes, it invalidates its copy of the NCE and also invalidates the offload target's copy of the NCE by causing NDIS to call the offload target's [**MiniportInvalidateOffload**](https://msdn.microsoft.com/library/windows/hardware/ff559406) function.

<!-- -->

-   If the NCE for the host stack is in the REACHABLE state, the host stack returns a nonzero value for HRD, which the offload target uses to update its value for HRT (HRT = NCT - HRD). This update ends the **NeighborReachabilityQuery** indication procedure.

**Note**  If there is no valid TCP connection, then there is no forward progress, and the NIC cannot update the NRT. In this case, the staleness test will pass, and the offload target will call the [**NdisMOffloadEventIndicate**](https://msdn.microsoft.com/library/windows/hardware/ff563619) function. The rest of the processing will be as described above, and the stack will try to resolve the neighbor by sending ARP or NS.

 

 

 





