---
title: Making Outgoing Calls
description: Making Outgoing Calls
ms.assetid: 295b3f6d-d53b-4030-b7e9-35ab7524d9aa
keywords:
- CoNDIS WAN drivers WDK networking , outgoing calls
- telephonic services WDK WAN , outgoing calls
- CoNDIS TAPI WDK networking , outgoing calls
- outgoing calls WDK CoNDIS WAN
- calls WDK CoNDIS WAN
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Making Outgoing Calls





If an application attempts to make an outgoing call, it must first open a line. A line is opened as a result of an application calling the TAPI **lineOpen** function. To place a telephony call on the previously opened line, the application calls the TAPI **lineMakeCall** function and passes a pointer to the specific destination address. If anything but default call-setup parameters are requested, the application also passes a pointer to a LINECALLPARAMS structure. If the application uses default call-setup parameters, **lineMakeCall** provides those parameters in a LINECALLPARAMS structure. Members of this structure specify how the telephony call should be set up.

These TAPI-function calls cause the NDPROXY driver to first create a virtual connection (VC) with the CoNDIS WAN miniport driver and then to encapsulate TAPI parameters in NDIS structures in order to make the outgoing call. The miniport driver will use these TAPI parameters to set up the outgoing call. The following describes how the outgoing call is connected, set up, and made:

-   NDPROXY calls [**NdisCoCreateVc**](https://msdn.microsoft.com/library/windows/hardware/ff561696) to initiate the creation of the VC with the miniport driver. After NDPROXY calls **NdisCoCreateVc**, NDIS calls, as a synchronous operation, the *ProtocolCoCreateVc* function of the call manager integrated into the miniport driver. NDIS passes to *ProtocolCoCreateVc* a handle that represents the VC. If the call to **NdisCoCreateVc** is successful, NDIS fills and returns the VC handle. *ProtocolCoCreateVc* performs any necessary allocations of dynamic resources and structures that the miniport call manager (MCM) driver requires to perform subsequent operations on the VC that will later be activated. Such resources include, but are not limited to, memory buffers, data structures, events, and other such similar resources.

-   NDPROXY specifies the TAPI parameters for an outgoing call in a [**CO\_AF\_TAPI\_MAKE\_CALL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545373) structure. NDPROXY fills this structure's members with the following information that was passed in the TAPI **lineMakeCall** function:
    -   The destination address in the **DestAddress** member
    -   The open-line identifier in the **ulLineID** member
    -   The LINECALLPARAMS structure in the **LineCallParams** member
-   NDPROXY overlays the CO\_AF\_TAPI\_MAKE\_CALL\_PARAMETERS structure on the **Parameters** member of a [**CO\_SPECIFIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545396) structure and sets the **Length** member of CO\_SPECIFIC\_PARAMETERS to the size of CO\_AF\_TAPI\_MAKE\_CALL\_PARAMETERS.

-   NDPROXY sets the CO\_SPECIFIC\_PARAMETERS structure to the **MediaSpecific** member of a [**CO\_MEDIA\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545388) structure.

-   NDPROXY sets a pointer to the CO\_MEDIA\_PARAMETERS structure to the **MediaParameters** member of a [**CO\_CALL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545384) structure.

-   Once NDPROXY encapsulates TAPI parameters, NDPROXY calls the [**NdisClMakeCall**](https://msdn.microsoft.com/library/windows/hardware/ff561635) function to initiate the outgoing call. In this function call, NDPROXY passes a pointer to the filled CO\_CALL\_PARAMETERS structure. NDIS in turn calls the [**ProtocolCmMakeCall**](https://msdn.microsoft.com/library/windows/hardware/ff570246) function of the CoNDIS WAN miniport driver's call manager. The miniport driver should examine only the CO\_AF\_TAPI\_MAKE\_CALL\_PARAMETERS structure embedded in CO\_CALL\_PARAMETERS. No other call parameters are meaningful in this case. If the miniport driver subsequently activates the VC for the outgoing call, the miniport driver calls the [**NdisMCmActivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff562792) function and passes a pointer to the filled CO\_CALL\_PARAMETERS.

-   After the miniport driver has negotiated with the network to establish the telephony-call parameters for the VC and set up a NIC for those call parameters, the miniport driver calls the [**NdisMCmMakeCallComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563544) function to indicate that it is ready to make data transfers on the VC. In this call, the miniport driver must pass the handle to the VC and modifications made to telephony-call parameters.

-   The miniport driver must modify the **CallMgrParameters** member of the CO\_CALL\_PARAMETERS structure to specify the quality of service (QoS) of transferring packets, such as the bandwidth. To set this **CallMgrParameters** member, the miniport driver fills members of a [**CO\_CALL\_MANAGER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545381) structure and points this structure to **CallMgrParameters**. For example, to identify the transmit and receive speeds in bytes per second for the VC, the miniport driver must set the **PeakBandwidth** members of the **Transmit** and **Receive** members of CO\_CALL\_MANAGER\_PARAMETERS. The **Transmit** and **Receive** members are FLOWSPEC structures. For more information about the FLOWSPEC structure, see the Microsoft Windows SDK.

-   If the miniport driver has modified telephony-call parameters, it must set the **Flags** member in the CO\_CALL\_PARAMETERS structure with CALL\_PARAMETERS\_CHANGED. As a result of the **NdisMCmMakeCallComplete** call made by the miniport driver, NDIS calls NDPROXY's *ProtocolClMakeCallComplete* function to complete the asynchronous operations that were initiated with **NdisClMakeCall**.

-   After the miniport driver successfully completes the outgoing call, NDPROXY notifies a TAPI application that the call is connected. This TAPI application then calls the TAPI **lineGetID** function to inform NDPROXY to locate the appropriate CoNDIS client. In this **lineGetID** call, the TAPI application supplies a string for a particular TAPI device class to which the application requires a handle. NDPROXY uses this string to locate the CoNDIS client that previously registered a SAP for the particular TAPI device class. If the CoNDIS client is NDISWAN, the string is NDIS. If NDPROXY locates a SAP with a string that matches the string passed by the TAPI application, NDPROXY calls [**NdisMCmCreateVc**](https://msdn.microsoft.com/library/windows/hardware/ff562812) to set up a connection endpoint with NDISWAN on which it can dispatch notification of the outgoing call that was made. NDIS in turn calls NDISWAN's *ProtocolCoCreateVc* function and passes a handle that represents the VC.

-   After NDPROXY sets up the connection endpoint with NDISWAN, it calls the [**NdisCmDispatchIncomingCall**](https://msdn.microsoft.com/library/windows/hardware/ff561664) function to notify NDISWAN about the outgoing call. In this call, NDPROXY passes the encapsulated CO\_AF\_TAPI\_MAKE\_CALL\_PARAMETERS structure that contains the outgoing call parameters. NDIS in turn calls NDISWAN's *ProtocolClIncomingCall* function, within which NDISWAN either accepts or rejects the requested connection. If NDISWAN changes the call parameters passed to it, it must set the **Flags** member in the CO\_CALL\_PARAMETERS structure with CALL\_PARAMETERS\_CHANGED.

-   After deciding whether to accept the connection and after possibly changing the call parameters, NDISWAN calls the [**NdisClIncomingCallComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561632) function. NDIS in turn calls the miniport driver's *ProtocolCmIncomingCallComplete* function. Depending on whether NDISWAN accepted the outgoing call and whether the miniport driver accepts or rejects NDISWAN's proposed changes to the call parameters, the miniport driver calls either [**NdisCmDispatchCallConnected**](https://msdn.microsoft.com/library/windows/hardware/ff561661) or [**NdisCmDispatchIncomingCloseCall**](https://msdn.microsoft.com/library/windows/hardware/ff561670) functions. **NdisCmDispatchCallConnected** notifies NDISWAN that data transfers can begin on the VC that NDPROXY created for the outgoing call. **NdisCmDispatchIncomingCloseCall** informs NDISWAN and NDPROXY to tear down the proposed outgoing call.

-   After NDISWAN accepts the outgoing call, NDPROXY calls the [**NdisCoGetTapiCallId**](https://msdn.microsoft.com/library/windows/hardware/ff561700) function to retrieve a string that identifies NDISWAN's context for the VC. NDPROXY passes this string back to the TAPI application. The TAPI application uses this VC-context string to complete its call to **lineGetID**.

 

 





