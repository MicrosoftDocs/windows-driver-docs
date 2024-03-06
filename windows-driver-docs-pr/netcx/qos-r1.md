---
title: WiFiCx QoS R1
description: This article specifies the WiFiCx driver modifications required for QoS R1 features, including MSCS and QoS Mapping.
ms.date: 03/01/2024
---

# WiFiCx QoS R1

QoS R1 introduces advanced traffic management capabilities for WiFiCx devices. QoS R1 enables prioritization of Wi-Fi data packets through Mirrored Stream Classification Service (MSCS) and QoS Mapping (DSCP-to-UP Mapping). These features enhance network efficiency and user experience by applying appropriate QoS policies to different types of traffic. 

QoS R1 functionality encompasses sections 3.1 and 3.2 in the [WFA Wi-Fi QoS Management Specification](https://www.wi-fi.org/file/wi-fi-qos-management-specification).

Starting with WiFiCx version 1.2, you can incorporate QoS R1 features into your WiFiCx client driver. QoS R1 is only available in the WiFiCx driver model. This article outlines the driver changes required to support these features.

## QOS R1 driver requirements

To support the QoS R1 feature suite, a WiFiCx client driver must:

1.	Support WiFiCx version 1.2 or higher.
1.	Support WMM (Wi-Fi Multimedia) standards.
1.	Have the capability to send/receive action frames.
1.	Introduce support for OS-configurable Wake on Incoming Action Frame.
1.	Communicate OS support of QoS features to Access Points (AP) through (re)association frames.
1.	Indicate driver support for both MSCS and QoS Mapping if the preceding criteria are met.

## MSCS support

To indicate support for MSCS:

1. The driver sets the **MSCSSupported** field in [**WIFI_STATION_CAPABILITIES**](/windows-hardware/drivers/ddi/wificx/ns-wificx-wifi_station_capabilities) to true. 
1. If the driver sets **MSCSSupported** to true,  Windows will indicate MSCS support by marking the **MSCSSupported** bit in [WDI_TLV_CONNECTION_SETTINGS](wdi-tlv-connection-settings.md). 
1. If Windows sets the **MSCSSupported** bit to **1**, the driver must set the Mirrored SCS field of the Extended Capabilities element (Bit 85) to **1** in the (re)association request.

Following a successful association, Windows will attempt to set up an MSCS session with the AP:
 
1. Windows sends an [OID_WDI_TASK_SEND_REQUEST_ACTION_FRAME](oid-wdi-task-send-request-action-frame.md) task to the driver. 
1. This task prompts the driver to send an MSCS Request Action Frame to the AP with default TCLAS mask parameters (as specified in the WFA test specification). 
1. The driver indicates the status of the Action Frame response via [NDIS_STATUS_WDI_INDICATION_ACTION_FRAME_RECEIVED](ndis-status-wdi-indication-action-frame-received.md). 

Windows will only send one MSCS request following a successful association. If the OS doesn’t receive an MSCS Response within MSCS_Response_Timeout time, it will consider the MSCS session setup failed, and won't try again. 

If the returned response status is failure, MSCS isn't active and the OS won't try to renegotiate an MSCS session. Any subsequent MSCS responses from the AP (including MSCS response frames with the status CHANGE) will either terminate an existing MSCS session or be ignored by the OS. If an MSCS session is terminated (due to OS teardown, AP teardown, or roam/disassociation), the OS will only attempt to establish MSCS again after successful reassociation.

When MSCS support is indicated, the driver must support [Wake on Incoming Action Frame](#wake-on-incoming-action-frame-support) for MSCS. When going to Dx with an active MSCS session, the OS will configure the driver to wake on receipt of an MSCS response frame.

The OS may prompt the driver to send an MSCS Request Action Frame to the AP to request MSCS teardown via the OID_WDI_TASK_SEND_REQUEST_ACTION_FRAME task.

## QoS Mapping support

To indicate support for QoS Mapping:

1. The driver sets the **DSCPToUPMappingSupported** field in [**WIFI_STATION_CAPABILITIES**](/windows-hardware/drivers/ddi/wificx/ns-wificx-wifi_station_capabilities) to true. 
1. If the driver sets **DSCPToUPMappingSupported** to true, Windows will indicate support for QoS Mapping by marking the **DSCPToUPMappingSupportedEit** bit in [WDI_TLV_CONNECTION_SETTINGS](wdi-tlv-connection-settings.md). 
1. If Windows sets the **DSCPToUPMappingSupportedEit** bit to **1**, the driver must set the QoS Map field of the Extended Capabilities element (Bit 32) to **1** in the (re)association request.

After QoS Mapping is established through either (re)association or a QoS Map Configure Action Frame that includes a QoS Map element, the OS will set appropriate UP values based on mapping received from the AP. 

For successful associations in which QoS Mapping support is indicated, the driver must:
1. Include the [WDI_TLV_ASSOCIATION_RESPONSE_FRAME](wdi-tlv-association-response-frame.md) in the [WDI_TLV_ASSOCIATION_RESULT](wdi-tlv-association-result.md). 
1. Indicate incoming QoS Map Configure Action Frames to the OS via  [NDIS_STATUS_WDI_INDICATION_ACTION_FRAME_RECEIVED](ndis-status-wdi-indication-action-frame-received.md).

When QoS Mapping support is indicated, the driver must support [Wake on Incoming Action Frame](#wake-on-incoming-action-frame-support) for DSCP. When going to Dx with QoS Mapping established, the OS will configure the driver to wake on receipt of a QoS Map Configure Action Frame.

## Wake on Incoming Action Frame support

To support QoS features, the driver must indicate support for Wake on Incoming Action Frame. The driver must:
1. Set the **IncomingActionFrame** field in [**WIFI_ADAPTER_WAKE_CAPABILITIES**](/windows-hardware/drivers/ddi/wificx/ns-wificx-wifi_adapter_wake_capabilities).
1. Set the **MaxNumConfigurableActionFrameWakePatterns** field in [**WIFI_STATION_CAPABILITIES**](/windows-hardware/drivers/ddi/wificx/ns-wificx-wifi_station_capabilities). If the **IncomingActionFrame** field of **WIFI_ADAPTER_WAKE_CAPABILITIES** is true, the driver must set **MaxNumConfigurableActionFrameWakePatterns** to:
    * **1** to support MSCS.
    * **2** to support QoS Mapping.

If **MaxNumConfigurableActionFrameWakePatterns** is less than the minimum value required for each feature, the OS will disable the feature.

**Note**: The total number of **WifiPowerOffloadTypeWakeOnIncomingActionFrame** offloads can exceed **MaxNumConfigurableActionFrameWakePatterns** because identical wake patterns can be offloaded on each NETADAPTER. For example, a Wake on Incoming Action Frame offload for DSCP to UP Mapping Configure can be sent to both the primary and secondary STA. However, the total number of unique patterns offloaded to the device will be less than or equal to **MaxNumConfigurableActionFrameWakePatterns**. 

When the device is in Dx and it receives an action frame matching one of the offloaded patterns, it must wake, and the driver must report **WifiWakeReasonTypeIncomingActionFrame** using the [**WifiAdapterReportWakeReason**](/windows-hardware/drivers/ddi/wificx/nf-wificx-wifiadapterreportwakereason) function and indicate the received action frame.
