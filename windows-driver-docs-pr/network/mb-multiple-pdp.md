---
title: Multiple PDP contexts
description: scenraio about multiple PDP contexts
keywords: MPDP, Multiple PDP context, additional PDP Context
ms.date: 03/01/2021
ms.localizationpriority: medium
---
# Multiple PDP contexts
## Usage scenarios

UWP mobile broadband apps can take advantage of multiple Packet Data Protocol (PDP) contexts to activate a special PDP context and specify rules to route data traffic. These apps can create rules for specific destinations or for all data traffic.

When the mobile broadband app needs to exchange data with the network, it checks the available and connected networks. If the mobile broadband app has a special rule for any of these networks, it uses the Connection Manager API to open a special PDP context. If this connection is successful, the PDP context provides routing rules for this connection and transfers the data using networking APIs. The mobile broadband app should repeat this if it receives the [**NetworkStatusChanged**](/uwp/api/Windows.Networking.Connectivity.NetworkInformation#Windows_Networking_Connectivity_NetworkInformation_NetworkStatusChanged) event to see whether any connections have changed and whether it needs to open a PDP context for the new connection.
	
You can use multiple PDP contexts to enable premium services.
- Differentiated Billing – You can vary the data or billing restrictions by using multiple PDP contexts. For example, Contoso is a mobile operator that developed a data backup app for their customers. As a mobile operator, Contoso could create multiple PDP contexts and let premium subscribers use the app for free. All other subscribers are charged separately to use it.

- Rich Communication Services – A global initiative created by the GSM Association to provide rich communication services, such as an enhanced phonebook, enhanced messaging, and enriched calling. Rich Communication Services provide interoperability across mobile operators and offers new ways to use existing assets and capabilities to deliver high quality and innovative communication services.

- Sponsored Connectivity – This allows users to a specific type of content without it going against their monthly data usage. The content provider makes an arrangement to reimburse the mobile operator by paying them directly, doing a revenue-sharing deal, or some other business arrangement.

- Personal Hotspot – Some mobile operators charge different rates when the connection is being used as a personal hotspot. You can use multiple PDP contexts to differentiate between the two.

For more information, see [Developing apps using multiple PDP contexts](../mobilebroadband/developing-apps-using-multiple-pdp-contexts.md).


## Primary Flow
### App activates additional PDP contexts:
![Flow diagram showing the App activating additional PDP contexts.](images/App_activate_additional_PDP_contexts.PNG?raw=true "App_activate_additional_PDP_contexts")

### Additional NetAdapter Initialization
![Additional NetAdapter Initialization.](images/Additional_NetAdapter_Initialization.PNG?raw=true "Additional_NetAdapter_Initialization")


## Decision Logic in WwanSvc for Additional PDP Context Connections

1. Double check and update the "Is Default Profile" condition logic, as it is no longer applicable.
1. WCM should no longer use the *cost* property of the default profile.
1. If the new additional pdp context APN request coincides with the default internet APN, disconnect the current additional PDP context.

![Decision Logic in WWANSVC for Connecting Additional PDP Context connection.](images/design_wwansvc_additional_pdp_contexts.png?raw=true "design_wwansvc_additional_pdp_contexts")


## Hardware Lab Kit (HLK) Tests
See [Steps for installing HLK](https://microsoft.sharepoint.com/teams/HWKits/SitePages/HWLabKit/Manual%20Controller%20Installation.aspx). 

In HLK Studio connect to the device Cellular modem driver and run the test: [Win6_4.MB.GSM.Data.TestMPDP](/windows-hardware/test/hlk/testref/08497822-4355-478b-9cba-0c0c7b663953).

## MB Multiple PDP context Troubleshooting Guide

1. Logs can be collected and decoded using these instructions: [MB Collecting Logs](mb-collecting-logs.md)
1. Open the .txt file in [TextAnalysisTool](mb-analyzing-logs.md)
1. Load the [Bacis Connectivity filter](mb-basic-connectivity-tat.md)

### Sample log
```
e 04-01 12:39:12.798 P4912 T8420 Microsoft-Windows-WWAN-NDISUIO-EVENTS WWAN NDISUIO Event: OID request sent to the driver                                                   0                    Info Microsoft-Windows-WWAN-NDISUIO-EVENTS
e 04-01 12:39:12.798 P4912 T8420 Windows Mobile Broadband Class Driver Event Provider [1] Miniport Request called Request=0xFFFFE3862EFF4A80, OID=0xE010149, OID name=OID_WWAN_MPDP RequestId=0x10F, RequestHandle=0x0, Type=1, InformationLength=32 0                    Info Windows Mobile Broadband Class Driver Event Provider
w 04-01 12:39:12.798 P4912 T8420 mbbcx         [ReqMgr][ReqId=0x04ad] Request created for OID_WWAN_MPDP [RequestContext=0xFFFFE386247597F0 OidRequest=0xFFFFE3862EFF4A80] SET=0x00000001(TRUE) MbbReqMgrCreateRequest requestmanager_cpp702 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.798 P4912 T8420 mbbcx         [ReqFsm][ReqId=0x04ad] Transition: MbbRequestStateReady -> MbbRequestStateDispatching event=MbbRequestEventDispatch MbbReqMgrQueueEvent  requestmanager_cpp1002 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.798 P4912 T8420 mbbcx         [ReqMgr][Timer] MbbTimerTypeRequest already armed at 3fc53, not re-arming                            MbbReqMgrTimerArm    requestmanager_cpp1269 TRACE_LEVEL_WARNING
w 04-01 12:39:12.798 P4912 T8420 mbbcx         [ReqMgr][ReqId=0x04ad], IsPoweredRequest [0x00000001(TRUE)], IsSerialized[0x00000001(TRUE)], IsQueueEmpty[0x00000001(TRUE)], DispatchRequest [0x00000000(FALSE)] MbbReqFsmDispatching requestmanager_cpp1522 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.798 P4912 T8420 mbbcx         MbxDevice::QueuePoweredRequest: WDFREQUEST (0x00001C79D4B06DB8) is sent                              MbxDevice::QueuePoweredRequest mbxdevice_cpp1339 TRACE_LEVEL_INFORMATION
e 04-01 12:39:12.798 P4912 T8420 Windows Mobile Broadband Class Driver Event Provider [1] Miniport REQUEST exited with status=The operation that was requested is pending completion., Request=0xFFFFE3862EFF4A80 0                    Info Windows Mobile Broadband Class Driver Event Provider
w 04-01 12:39:12.808 P0004 T0376 mbbcx         EvtCxPreD0Entry: previousPowerState: 3                                                               EvtCxPreD0Entry      mbxdevice_cpp1583 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.808 P0004 T0376 cxwmbclass    EvtDeviceD0Entry: previousPowerState: 3                                                              EvtDeviceD0Entry     power_cpp19 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.808 P0004 T0376 usbbus        Entered Enabled=1                                                                                    MbbBusSetNotificationState businit_c2606 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.808 P0004 T0376 usbbus        MbbUsbDeviceStartDataPipes: Entered                                                                  MbbUsbDeviceStartDataPipes datapipe_c228 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.809 P0004 T0376 usbbus        MbbUsbDeviceStartDataPipes: Exited                                                                   MbbUsbDeviceStartDataPipes datapipe_c286 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.809 P0004 T0376 mbbcx         MbxDevice::PostD0EntryPostHardwareEnabled: previousPowerState: 3                                     MbxDevice::PostD0EntryPostHardwareEnabled mbxdevice_cpp1933 TRACE_LEVEL_INFORMATION
e 04-01 12:39:12.810 P0004 T0376 Microsoft-Windows-NDIS Miniport {c2d9b876-8b20-4cdd-a944-044fd39a97dc}, DeviceState[0x1]                                    Power                0 Microsoft-Windows-NDIS
e 04-01 12:39:12.812 P0004 T0376 Microsoft-Windows-NDIS Miniport {156ce913-cc77-487d-8838-4811ce860b0e}, DeviceState[0x1]                                    Power                0 Microsoft-Windows-NDIS
e 04-01 12:39:12.813 P0004 T0376 Microsoft-Windows-NDIS Miniport {1e58668f-811b-407d-b288-e1f57a432a24}, DeviceState[0x1]                                    Power                0 Microsoft-Windows-NDIS
e 04-01 12:39:12.815 P0004 T0376 Microsoft-Windows-NDIS Miniport {468c0f8c-df7f-4619-85fd-c24ccebdeda3}, DeviceState[0x1]                                    Power                0 Microsoft-Windows-NDIS
w 04-01 12:39:12.815 P0004 T0376 mbbcx         MbxDevice::EnableWakeReasonReporting                                                                 MbxDevice::EnableWakeReasonReporting mbxdevice_cpp2099 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.815 P0004 T0376 cxwmbclass    EvtDeviceDisarmWakeFromS0: The device is disarmed for wake                                           EvtDeviceDisarmWakeFromS0 power_cpp130 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.815 P0004 T0376 mbbcx         MbxDevice::DisarmWake: Start                                                                         MbxDevice::DisarmWake mbxdevice_cpp1685 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.815 P0004 T0376 mbbcx         [ReqMgr][ReqId=0x04ae] Internal Request created [RequestContext=0xFFFFE38624757650]                  MbbReqMgrCreateRequest requestmanager_cpp713 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.815 P0004 T0376 mbbcx         [ReqFsm][ReqId=0x04ae] Transition: MbbRequestStateReady -> MbbRequestStateDispatching event=MbbRequestEventDispatch MbbReqMgrQueueEvent  requestmanager_cpp1002 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.815 P0004 T0376 mbbcx         [ReqMgr][Timer] MbbTimerTypeRequest already armed at 3fc53, not re-arming                            MbbReqMgrTimerArm    requestmanager_cpp1269 TRACE_LEVEL_WARNING
w 04-01 12:39:12.815 P0004 T0376 mbbcx         [ReqMgr][ReqId=0x04ae], IsPoweredRequest [0x00000000(FALSE)], IsSerialized[0x00000001(TRUE)], IsQueueEmpty[0x00000001(TRUE)], DispatchRequest [0x00000001(TRUE)] MbbReqFsmDispatching requestmanager_cpp1522 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.815 P0004 T0376 mbbcx         [ReqFsm][ReqId=0x04ae] Transition: MbbRequestStateDispatching -> MbbRequestStateSendPending event=MbbRequestEventStart MbbReqMgrQueueEvent  requestmanager_cpp1002 TRACE_LEVEL_INFORMATION
e 04-01 12:39:12.815 P0004 T0376 Windows Mobile Broadband Class Driver Event Provider Sending command with the following parameters:
Caller Request Id: 0x0
Driver Request Id: 0
Service Id: {000004ae-cc33-a289-bbbc-4f8bb6b0133e}
Command Name: REDACTED-EMBEDDED-HEXREDACTED-EMBEDDED-HEXREDACTED-EMBEDDED-HEXREDACTED-EMBEDDED-HEXBASIC_NOTIFY_DEVICE_SERVICE_UPDATES
Command Id: 19
Payload Length: 324
Payload: 0x0600000034000000640000009800000028000000C000000018000000D80000001C000000F400000034000000280100001C000000A289CC33BCBB8B4FB6B0133EC2AAE6DF140000000100000002000000030000000400000005000000060000000700000008000000090000000A0000000B0000000C0000000D0000000F000000100000001300000014000000150000001600000017000000533FBEEB14FE44679F9033A223E56C3F050000000100000002000000030000000400000005000000E550A0C85E82479E82F710ABF4C3351F01000000010000001D2B5FF70AA148B2AA5250F15767174E0200000001000000030000003D01DCC5FEF54D050D3ABEF7058E9AAF08000000010000000300000004000000050000000600000007000000080000000A00000068223D049F6C4E0F822D28441FB72340020000000100000002000000 0                    Info Windows Mobile Broadband Class Driver Event Provider
e 04-01 12:39:12.815 P0004 T0376 Windows Mobile Broadband Class Driver Event Provider for OPN Sending command MessageType: 0x3, MessageLength: 372, MessageTransactionId: 533, TotalFragments: 1, CurrentFragment: 0, ServiceId: {a289cc33-bcbb-8b4f-b6b0-133ec2aae6df}, CommandId: 19, CommandType: 1, InformationBufferLength: 324, InformationBuffer: 0x0600000034000000640000009800000028000000C000000018000000D80000001C000000F400000034000000280100001C000000A289CC33BCBB8B4FB6B0133EC2AAE6DF140000000100000002000000030000000400000005000000060000000700000008000000090000000A0000000B0000000C0000000D0000000F000000100000001300000014000000150000001600000017000000533FBEEB14FE44679F9033A223E56C3F050000000100000002000000030000000400000005000000E550A0C85E82479E82F710ABF4C3351F01000000010000001D2B5FF70AA148B2AA5250F15767174E0200000001000000030000003D01DCC5FEF54D050D3ABEF7058E9AAF08000000010000000300000004000000050000000600000007000000080000000A00000068223D049F6C4E0F822D28441FB72340020000000100000002000000 0                    Info Windows Mobile Broadband Class Driver Event Provider for OPN
w 04-01 12:39:12.815 P0004 T0376 usbbus        Sending 372 bytes on control channel                                                                 MbbBusSendMessageFragment businit_c1472 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.815 P0004 T0376 usbbus        SetActivityIdForRequest succeeded. Set request activityId = 207b1c4a-085c-0001-270f-83205c08d601     SetActivityIdForRequest businit_c1383 TRACE_LEVEL_INFORMATION
e 04-01 12:39:12.815 P0004 T0376 Windows Mobile Broadband Class Driver Event Provider [1] Send encapsulted command MessageType=0x3, MessageLength=372, TransactionId=533, TotalFrags=1, CurrentFrag=0, ServiceId={33cc89a2-bbbc-4f8b-b6b0-133ec2aae6df}, CID=19, CommandType=1, InfoLength=324 0                    Info Windows Mobile Broadband Class Driver Event Provider
w 04-01 12:39:12.815 P0004 T0376 mbbcx         [Util][ReqId=0x04ae][TID=0x00000215] Pending send Fragment 00/01                                     MbbUtilSendMessageFragments util_cpp1269 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.815 P0000 T0000 usbbus        CompletionRoutine() for request 00001C79D4105668 status=STATUS_SUCCESS                               SendCompletionRoutine businit_c1398 TRACE_LEVEL_INFORMATION
w 04-01 12:39:12.815 P0000 T0000 mbbcx         [Util][ReqId=0x04ae][TID=0x00000215] 01/01 fragment completed with status=STATUS_SUCCESS             MbbUtilSendMessageFragmentComplete util_cpp1401 TRACE_LEVEL_INFORMATION
e 04-01 12:39:12.815 P0000 T0000 Windows Mobile Broadband Class Driver Event Provider Sending command completed with status STATUS_SUCCESS. Command was sent with the following parameters:
```