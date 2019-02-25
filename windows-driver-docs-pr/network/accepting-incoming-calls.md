---
title: Accepting Incoming Calls
description: Accepting Incoming Calls
ms.assetid: bca837dc-b3de-4aca-9fc2-aed2faab1377
keywords:
- CoNDIS WAN drivers WDK networking , incoming calls
- telephonic services WDK WAN , incoming calls
- CoNDIS TAPI WDK networking , incoming calls
- NDPROXY WDK networking , incoming calls
- incoming calls WDK CoNDIS WAN
- calls WDK CoNDIS WAN
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accepting Incoming Calls





Before an application can accept an incoming call, it first must have a line open. A line is opened as a result of an application calling the TAPI **lineOpen** function. This TAPI-function call causes underlying drivers to encapsulate TAPI parameters in NDIS structures in order to prepare to receive an incoming call. After the CoNDIS WAN miniport driver receives an incoming call, the miniport driver must first create a virtual connection (VC) with the NDPROXY driver and then notify NDPROXY of the incoming call. NDPROXY in turn notifies the application through TAPI. The following list describes how the incoming call is set up, connected, and made:

-   NDPROXY specifies the TAPI parameters for an incoming connection in a [**CO\_AF\_TAPI\_SAP**](https://msdn.microsoft.com/library/windows/hardware/ff545376) structure. NDPROXY fills this structure's members with the following information that was passed in the TAPI **lineOpen** function:
    -   Open-line identifier in the **ulLineID** member
    -   Address of the incoming connection in the **ulAddressID** member
    -   Media mode of the incoming connection's information stream in the **ulMediaModes** member
-   NDPROXY overlays the CO\_AF\_TAPI\_SAP structure on the **Sap** member of a [**CO\_SAP**](https://msdn.microsoft.com/library/windows/hardware/ff545392) structure and sets the **SapLength** member of CO\_SAP to the size of CO\_AF\_TAPI\_SAP. NDPROXY must also set the **SapType** member of CO\_SAP to AF\_TAPI\_SAP\_TYPE.

-   Once NDPROXY encapsulates TAPI parameters, NDPROXY calls the [**NdisClRegisterSap**](https://msdn.microsoft.com/library/windows/hardware/ff561648) function to make itself ready to receive incoming calls. In this function call, NDPROXY passes a pointer to the filled CO\_SAP structure that specifies the Service Access Point (SAP) on which NDPROXY can receive incoming calls. NDIS forwards the CO\_SAP structure to the *ProtocolCmRegisterSap* function of the CoNDIS WAN miniport call manager (MCM) driver. *ProtocolCmRegisterSap* communicates with network control devices or other media-specific agents, as necessary, to register the SAP on the network for NDPROXY. After the miniport driver has registered the SAP, it can accept an incoming-call offer directed to that SAP.

-   A CoNDIS WAN miniport driver is alerted to an incoming call by signaling messages from the network. From these signaling messages, the miniport driver extracts the call parameters for the call, including the SAP to which the incoming call is addressed.

-   Before indicating an incoming call to NDPROXY, the miniport driver calls the [**NdisMCmCreateVc**](https://msdn.microsoft.com/library/windows/hardware/ff562812) function to initiate the creation of a VC with NDPROXY. NDPROXY allocates and initializes resources required for the VC and stores the handle to the VC.

-   The CoNDIS WAN miniport driver sets the TAPI parameters for an incoming call in a [**CO\_AF\_TAPI\_INCOMING\_CALL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545372) structure. The miniport driver fills this structure's members with the following information that was extracted from signaling messages:
    -   Line identifier in the **ulLineID** member
    -   Address of the incoming call in the **ulAddressID** member
    -   CO\_TAPI\_FLAG\_INCOMING\_CALL bit in the **ulFlags** member. All other bits of **ulFlags** are reserved and must be set to 0.
    -   LINECALLPARAMS structure in the **LineCallInfo** member. Members of LINECALLPARAMS specify TAPI call parameters for an incoming call.
-   The miniport driver overlays CO\_AF\_TAPI\_INCOMING\_CALL\_PARAMETERS on the **Parameters** member of a [**CO\_SPECIFIC\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545396) structure and sets the **Length** member of CO\_SPECIFIC\_PARAMETERS to the size of CO\_AF\_TAPI\_INCOMING\_CALL\_PARAMETERS.

-   The miniport driver sets the CO\_SPECIFIC\_PARAMETERS structure to the **MediaSpecific** member of a [**CO\_MEDIA\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545388) structure.

-   The miniport driver sets a pointer to the CO\_MEDIA\_PARAMETERS structure to the **MediaParameters** member of a [**CO\_CALL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545384) structure.

-   The miniport driver must also set the **CallMgrParameters** member of the CO\_CALL\_PARAMETERS structure to specify the quality of service (QoS) of transferring packets, such as the bandwidth. To set this **CallMgrParameters** member, the miniport driver fills members of a [**CO\_CALL\_MANAGER\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff545381) structure and points this structure to **CallMgrParameters**. For example, to identify the transmit and receive speeds in bytes per second for the VC, the miniport driver must set the **PeakBandwidth** members of the **Transmit** and **Receive** members of CO\_CALL\_MANAGER\_PARAMETERS. The **Transmit** and **Receive** members are FLOWSPEC structures. For more information about the FLOWSPEC structure, see the Microsoft Windows SDK.

-   After the miniport driver encapsulates TAPI parameters and fills the **CallMgrParameters** member of CO\_CALL\_MANAGER\_PARAMETERS, it calls the [**NdisMCmDispatchIncomingCall**](https://msdn.microsoft.com/library/windows/hardware/ff562830) function to indicate the incoming call to NDPROXY. In this call, the miniport driver passes the following:
    -   A handle that identifies the SAP to which the incoming call is addressed
    -   A handle that identifies the VC for the incoming call
    -   A pointer to the filled CO\_CALL\_PARAMETERS structure
-   NDPROXY returns NDIS\_STATUS\_PENDING to the miniport driver so NDPROXY can complete **NdisMCmDispatchIncomingCall** asynchronously.

-   After the TAPI application answers the incoming call with the **lineAnswer** function, NDPROXY calls the [**NdisClIncomingCallComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561632) function. NDIS in turn calls the miniport driver's *ProtocolCmIncomingCallComplete* function. If NDPROXY returns an NDIS\_STATUS\_SUCCESS code, it indicates acceptance of the call parameters. If NDPROXY finds the call parameters unacceptable, it can request a change in the call parameters by setting the **Flags** member in the CO\_CALL\_PARAMETERS structure to CALL\_PARAMETERS\_CHANGED and by supplying revised call parameters. If NDPROXY accepts the incoming call, the miniport driver should send signaling messages to indicate to the calling entity that the call has been accepted. Otherwise, the miniport driver should send signaling messages to indicate that the call has been rejected. If NDPROXY is requesting a change in call parameters, the miniport driver sends signaling messages to request a change in call parameters.

-   The miniport driver activates the VC that the miniport driver created with NDPROXY and must also call the [**NdisMCmActivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff562792) function to notify NDPROXY that the miniport driver is ready to transfer packets on the VC.

-   If NDPROXY rejects the call, the miniport driver calls the [**NdisMCmDeactivateVc**](https://msdn.microsoft.com/library/windows/hardware/ff562818) function to deactivate the VC that the miniport driver created for the incoming call. After the VC is deactivated, the miniport driver calls the [**NdisMCmDeleteVc**](https://msdn.microsoft.com/library/windows/hardware/ff562819) function to delete the VC.

-   Depending on whether NDPROXY accepted the incoming call and whether the end-to-end connection was successfully established, the miniport driver calls either [**NdisMCmDispatchCallConnected**](https://msdn.microsoft.com/library/windows/hardware/ff562826) or [**NdisMCmDispatchIncomingCloseCall**](https://msdn.microsoft.com/library/windows/hardware/ff563541) functions. Note that if the remote calling entity tore down the call, it sends signaling messages to indicate that the end-to-end connection was not successfully established. **NdisMCmDispatchCallConnected** notifies NDPROXY that data transfers can begin on the VC that the miniport driver created and activated for the incoming call. **NdisMCmDispatchIncomingCloseCall** informs NDPROXY to tear down the incoming call.

-   If NDPROXY is directed to tear down the incoming call, it calls the [**NdisClCloseCall**](https://msdn.microsoft.com/library/windows/hardware/ff561627) function to acknowledge that it will neither attempt to send nor expect to receive data on the VC. NDIS in turn calls the miniport driver's *ProtocolCmCloseCall* function. The miniport driver then calls the **NdisMCmDeactivateVc** function to deactivate the VC. After the VC is deactivated, the miniport driver calls the **NdisMCmDeleteVc** function to delete the VC.

-   After the TAPI application accepts the incoming call and NDPROXY notifies the application that the call is connected, the application calls the TAPI **lineGetID** function to inform NDPROXY to locate the appropriate CoNDIS client. In this **lineGetID** call, the TAPI application supplies a string for a particular TAPI device class to which the application requires a handle. NDPROXY uses this string to locate the CoNDIS client that previously registered a SAP for the particular TAPI device class. If the CoNDIS client is NDISWAN, the string is NDIS. If NDPROXY locates a SAP with a string that matches the string passed by the TAPI application, NDPROXY calls **NdisMCmCreateVc** to set up a connection endpoint with NDISWAN on which it can dispatch notification of the incoming call. NDIS in turn calls NDISWAN's *ProtocolCoCreateVc* function and passes a handle that represents the VC.

-   After NDPROXY sets up the connection endpoint with NDISWAN, it calls the [**NdisCmDispatchIncomingCall**](https://msdn.microsoft.com/library/windows/hardware/ff561664) function to notify NDISWAN about the incoming call. In this call, NDPROXY passes the encapsulated CO\_AF\_TAPI\_INCOMING\_CALL\_PARAMETERS structure that contains the incoming call parameters. NDIS in turn calls NDISWAN's *ProtocolClIncomingCall* function, within which NDISWAN either accepts or rejects the requested connection.

-   After deciding whether to accept the connection and after possibly changing the call parameters, NDISWAN calls the **NdisClIncomingCallComplete** function. NDIS in turn calls the miniport driver's *ProtocolCmIncomingCallComplete* function. Depending on whether NDISWAN accepted the incoming call and whether the miniport driver accepts or rejects NDISWAN's proposed changes to the call parameters, the miniport driver calls either **NdisCmDispatchCallConnected** or **NdisCmDispatchIncomingCloseCall** functions. **NdisCmDispatchCallConnected** notifies NDISWAN that data transfers can begin on the VC that the miniport driver created for the incoming call. **NdisCmDispatchIncomingCloseCall** informs NDISWAN and NDPROXY to tear down the incoming call.

-   After NDISWAN accepts the incoming call, NDPROXY calls the [**NdisCoGetTapiCallId**](https://msdn.microsoft.com/library/windows/hardware/ff561700) function to retrieve a string that identifies NDISWAN's context for the VC. NDPROXY passes this string back to the TAPI application. The TAPI application uses this VC-context string to complete its call to **lineGetID**.

 

 





