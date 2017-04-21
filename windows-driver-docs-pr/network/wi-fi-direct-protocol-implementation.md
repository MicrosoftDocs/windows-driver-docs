---
title: Wi-Fi Direct Protocol Implementation
description: Wi-Fi Direct Action FramesWindows uses OIDs to request the miniport driver to send certain Wi-Fi Direct related action frames.
ms.assetid: F893DFD7-E333-494C-9066-82B51D412104
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Wi-Fi Direct Protocol Implementation


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

**Wi-Fi Direct Action Frames**

Windows uses OIDs to request the miniport driver to send certain Wi-Fi Direct related action frames. These transmission requests can be for frames that would receive a response from another device, or can be responses to requests from other Wi-Fi Direct devices and the miniport driver's behavior would be slightly different depending on the request. The table below shows the frames that Windows is involved in exchanging with the peer device. Windows does not initiate transmission of or process reception of any Wi-Fi Direct actions frames not listed in the table below (including Device/GO Discoverability and Service Discovery frames)

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Action Frame</strong></p></td>
<td align="left"><p><strong>Send Triggered by OS</strong></p></td>
<td align="left"><p><strong>Port Remains Available After Successful Transmission For Receiving Replies</strong></p></td>
<td align="left"><p><strong>Receive Indicated to OS</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>GO Negotiation Request</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p>GO Negotiation Response</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes if [OID_DOT11_WFD_SEND_GO_NEGOTIATION_RESPONSE](https://msdn.microsoft.com/library/windows/hardware/hh451805). Status = DOT11_WFD_STATUS_SUCCESS</p>
<p>No Otherwise</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p>GO Negotiation Confirmation</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p>P2P Invitation Request</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p>P2P Invitation Response</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Provision Discovery Request</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
</tr>
<tr class="even">
<td align="left"><p>Provision Discovery Response</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
</tr>
</tbody>
</table>

 

Prior to issuing an OID to send a GO Negotiation request, a P2P invitation request, or a Provision Discovery request, Windows queries the miniport driver for the Dialog Token to use in the send request. When Windows submits an OID request to a port to send one of the action frames in the table above, the miniport driver should:

1.  Use the specified dialog token for sending the action frame.
2.  Complete the OID request.
3.  Sync with the Wi-Fi Direct device to which the frame is targeted. Depending on the implementation, if the send is in response to a received request (eg. Invitation Response sent on reception of an invitation request), this may not be necessary.
4.  Send the frame & wait for an ACK.
5.  Once the ACK for the frame is received or if none of the retry attempts get an ACK, send a NDIS\_STATUS indication to Windows to notify about the transmission status of the action frame. This indication must include the IEs from the packet.
6.  If the send was for a frame that would receive a reply from the peer device and the transmission was successful, the port must remain available for the peer device to send reply action frames to the miniport driver. The timeout and mechanism of being available should follow the Wi-Fi Peer-To-Peer Technical Specification.

The miniport driver is not required to maintain a state machine for each of the Wi-Fi Direct action frames.

When a port is in one of the Wi-Fi Direct operation mode and it receives certain Wi-Fi Direct related action frames, after validation of the header fields, it must send a NDIS\_STATUS Indication to the OS. It must not drop packets because of internal state machines or because it is currently waiting for a response to a different request (for example dropping GO Negotiation Requests, while it is waiting for GO Negotiation Responses).

If the received Wi-Fi Direct action frame is a request that expects a response, Windows may submit a Direct OID to the miniport driver to send a response. This direct OID will be submitted before the call to **NdisMIndicateStatusEx** function to indicate the status has returned. If the direct OID is not sent to the miniport driver, it must not send a response to the received packet.

In the NDIS\_STATUS indication for received Wi-Fi Direct action the miniport driver can optionally include a PVOID to hold context information for the received packet. Windows will forward this context value to the miniport driver when the direct OID is submitted to the miniport driver. If included in the indication, the context must remain valid until the **NdisMIndicateStatusEx** function for the indication returns.

When indicating NDIS\_STATUS notifications, the miniport driver must perform de-multiplexing of the received frame to the appropriate Wi-Fi Direct port. Public action frames must only be indicated on the NDIS\_PORT configured in Wi-Fi Direct Device mode.

**Device Address and Interface Address**
The miniport driver is required to support one P2P Device Address and as many P2P Interface Addresses as the number of Wi-Fi Direct Groups it can support simultaneously. The Device and supported Interface addresses are reported during initialization. The miniport driver is expected to send and receive packets using its Device Address only on the NDIS PORT that is configured in Wi-Fi Direct Device Mode. It is expected to support sending and receiving of packets using an Interface Address on the other Wi-Fi Direct role ports.

If the miniport driver only supports one Wi-Fi Direct group, it may use the same address as both its Device Address and Interface Address. In this case, it is responsible for doing appropriate filtering and de-multiplexing of received packets to NDIS\_PORTs when indicating the packets to Windows.

The miniport driver must use the appropriate interface address for each of the Wi-Fi Direct Role port. This address should match the MAC address reported by the miniport during port creation ([**DOT11\_MAC\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff548689) structure of [OID\_DOT11\_CREATE\_MAC](https://msdn.microsoft.com/library/windows/hardware/ff569124)).

**IE Creation And Parsing**
The miniport driver is responsible for creating the P2P Attributes and P2P Information Elements for inclusion in transmitted packets. Windows will provide the miniport driver the WPS IEs that it should include in the transmitted packets. Windows may include other IEs that the miniport driver should add in the packet. However, Windows will never pass P2P IEs in this list of IEs.

When the miniport driver receives certain types of packets, it needs to inform Windows about the reception. In the notification (which can be a NDIS\_STATUS indication or completion of an OID), it would pass all the information elements from the received packets to Windows. It need not parse the P2P or WPS IEs to pass the information to Windows. However, it can parse the IEs to collect any P2P parameters that it is interested in.

The miniport driver should never need to create the Wi-Fi Protected Setup (WPS) IEs in Wi-Fi Direct packets. Windows provides the miniport driver with the WPS IEs it needs to add to specific packets and will parse the WPS IEs in received packets. When responding to probe requests, the miniport driver may need to parse the WPS IEs to match any Request Device Type attributes against programmed primary and secondary device types.

**P2P Capability bitmask**
The miniport driver is responsible for populating the P2P Capability bitmask in the P2P Capability attributes. Windows uses OIDs to specify the criteria for settings the bits. The criteria are based on the capability reported by the miniport via the [**DOT11\_WFD\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/hh406574) structure.

The logic for setting specific bits is described below.

**P2P DEVICE CAPABILITY BITMASK**

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Bit</strong></p></td>
<td align="left"><p><strong>Information</strong></p></td>
<td align="left"><p><strong>Criterion to set the bit</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>0</p></td>
<td align="left"><p>Service Discovery</p></td>
<td align="left"><p>[OID_DOT11_WFD_DEVICE_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451792). bServiceDiscoveryEnabled</p></td>
</tr>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>P2P Client Discoverability</p></td>
<td align="left"><p>[OID_DOT11_WFD_DEVICE_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451792). bClientDiscoverabilityEnabled</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Concurrent Operation</p></td>
<td align="left"><p>[OID_DOT11_WFD_DEVICE_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451792). bConcurrentOperationSupported</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>P2P Infrastructure Managed</p></td>
<td align="left"><p>[OID_DOT11_WFD_DEVICE_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451792). bInfrastructureManagementEnabled</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>P2P Device Limit</p></td>
<td align="left"><p>[OID_DOT11_WFD_DEVICE_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451792). bDeviceLimitReached</p></td>
</tr>
<tr class="odd">
<td align="left"><p>5</p></td>
<td align="left"><p>P2P Invitation Procedure</p></td>
<td align="left"><p>[OID_DOT11_WFD_DEVICE_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451792). bInvitationProcedureEnabled</p></td>
</tr>
</tbody>
</table>

 

When a port is configured to enable a particular capability, it must set the corresponding bit. If Windows disables a specific capability, the port must clear the related bit and disable the capability.

**P2P GROUP CAPABILITY BITMASK**

*WI-FI DIRECT DEVICE PORT* - The Wi-Fi Direct Device Port uses the DOT11\_WFD\_GROUP\_CAPABILITY field passed in the action frame send OID for populating the P2P Group Capability Bitmask of the packet. For OIDs which do not specify this field, the Device Port will use the behavior as required by the Wi-Fi Peer To Peer Technical Specification for Wi-Fi Direct Device that is not a Group Owner.

*WI-FI DIRECT ROLE PORT IN GROUP OWNER OPERATION MODE* - The Wi-Fi Direct Port in Group Owner operation mode must use the settings from [OID\_DOT11\_WFD\_GROUP\_OWNER\_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451799) to configure its Group Capability bitmask. The following table describes the criteria for setting each bit.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Bit</strong></p></td>
<td align="left"><p><strong>Information</strong></p></td>
<td align="left"><p><strong>Criterion to set the bit</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>0</p></td>
<td align="left"><p>P2P Group Owner</p></td>
<td align="left"><p>This bit is set to 1 by the driver on the Wi-Fi Direct ports that are currently operating as a Group Owner.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>Persistent P2P Group</p></td>
<td align="left"><p>[OID_DOT11_WFD_GROUP_OWNER_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451799). bPersistentGroupEnabled</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>P2P Group Limit</p></td>
<td align="left"><p>The value of this bit is set by the driver when it has reached its Group Limit. The default Group Limit of the driver is reported by the uGORoleClientTableSize field of [<strong>DOT11_WFD_ATTRIBUTES</strong>](https://msdn.microsoft.com/library/windows/hardware/hh406574). Windows can specify a smaller group limit using [OID_DOT11_WFD_GROUP_OWNER_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451799). uMaximumGroupLimit</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Intra-BSS Distribution</p></td>
<td align="left"><p>[OID_DOT11_WFD_GROUP_OWNER_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451799).bIntraBSSDistributionSupported</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Cross Connection</p></td>
<td align="left"><p>[OID_DOT11_WFD_GROUP_OWNER_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451799).bCrossConnectionSupported</p></td>
</tr>
<tr class="odd">
<td align="left"><p>5</p></td>
<td align="left"><p>Persistent Reconnect</p></td>
<td align="left"><p>[OID_DOT11_WFD_GROUP_OWNER_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451799).bPersistenReconnectSupported</p></td>
</tr>
<tr class="even">
<td align="left"><p>6</p></td>
<td align="left"><p>Group Formation</p></td>
<td align="left"><p>[OID_DOT11_WFD_GROUP_OWNER_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451799).bGroupFormationEnabled</p></td>
</tr>
</tbody>
</table>

 

**Managed Device**
Windows does not provide support for Managed P2P Device operations. The miniport driver may choose to implement this functionality on its Wi-Fi Direct and its ExtSTA ports. If it supports Managed Device operations, it must set the bInfrastructureManagementSupported bit in [**DOT11\_WFD\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/hh406574) structure.

 

 





