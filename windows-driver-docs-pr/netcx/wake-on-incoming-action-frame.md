---
title: Wake on Incoming Action Frame
description: Wake on Incoming Action Frame wakes a WiFiCx device from a low power state when it receives specific action frames from the AP.
ms.date: 03/07/2024
---

## Wake on Incoming Action Frame

The Wake on Incoming Action Frame feature wakes a WiFiCx device from a low power state when it receives specific action frames from the AP. WiFiCx drivers must support Wake on Incoming Action Frame to support [QoS R1](qos-r1.md) features, including Mirrored Stream Classification Service (MSCS) and QoS Mapping (DSCP-to-UP Mapping).

To support Wake on Incoming Action Frame, the driver must:

1. Set the **IncomingActionFrame** field in [**WIFI_ADAPTER_WAKE_CAPABILITIES**](/windows-hardware/drivers/ddi/wificx/ns-wificx-wifi_adapter_wake_capabilities) to **TRUE**.

1. Set the **MaxNumConfigurableActionFrameWakePatterns** field in [**WIFI_STATION_CAPABILITIES**](/windows-hardware/drivers/ddi/wificx/ns-wificx-wifi_station_capabilities) to the largest number of patterns reasonably configurable by the firmware. This value must be nonzero if the driver indicates **IncomingActionFrame** support. If the **IncomingActionFrame** field of **WIFI_ADAPTER_WAKE_CAPABILITIES** is true, the driver must set **MaxNumConfigurableActionFrameWakePatterns** to:
    * **1** to support MSCS.
    * **2** to support QoS Mapping.

If **MaxNumConfigurableActionFrameWakePatterns** is less than the minimum value required for each feature, the OS will disable the feature.

The number of wake pattern requirements for MSCS, QoS Mapping, and any other feature that needs Wake on Incoming Action Frame is subject to change in the future.

**Note**: The total number of **WifiPowerOffloadTypeWakeOnIncomingActionFrame** offloads can exceed **MaxNumConfigurableActionFrameWakePatterns** because identical wake patterns can be offloaded on each NETADAPTER. For example, a Wake on Incoming Action Frame offload for DSCP-to-UP Mapping Configure can be sent to both the primary and secondary STA. However, the total number of unique patterns offloaded to the device will be less than or equal to **MaxNumConfigurableActionFrameWakePatterns**. 

When the device is in Dx and it receives an action frame matching one of the offloaded patterns, it must wake, and the driver must report **WifiWakeReasonTypeIncomingActionFrame** using the [**WifiAdapterReportWakeReason**](/windows-hardware/drivers/ddi/wificx/nf-wificx-wifiadapterreportwakereason) function and indicate the received action frame.