---
title: WiFiCx low latency connection quality
description: This section describes how to maintain quality with low latency connections in WiFiCx
ms.date: 09/30/2021
---

# WiFiCx low latency connection quality


A port can be configured for low latency mode operation if there is an application running on the system that needs low latency data traffic (for example, VoIP applications). When in this mode of operation, the driver should modify any behavior (such as scanning or better AP roaming) that would cause it to move off of the channel of the port that is configured for low latency mode. It should also follow the specified guidance for the [NDIS\_STATUS\_WDI\_INDICATION\_LINK\_STATE\_CHANGE](./ndis-status-wdi-indication-link-state-change.md) indication. The host provides [**WDI\_TLV\_LOW\_LATENCY\_CONNECTION\_QUALITY\_PARAMETERS**](./wdi-tlv-low-latency-connection-quality-parameters.md) that the port should use when it is in this mode. This specifies the maximum time that the port should be off channel and the minimum link quality value that the connection must fall down to before initiating a low latency roam (including sending [NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED](./ndis-status-wdi-indication-roaming-needed.md)).

For scans, the host provides the maximum channel dwell time (there are different values for active and passive channels) and the adapter should not go above the maximum time. The host also throttles unnecessary scans. However, the adapter can throttle the scan further if the [**WDI\_SCAN\_TRIGGER**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_scan_trigger) is **WDI\_SCAN\_TRIGGER\_BACKGROUND** or **WDI\_SCAN\_TRIGGER\_ROAM**. If the adapter performs its own scans in this mode, it is recommended that it includes the SSID it is looking for (unless it is after a resume from sleep) to reduce the dwell time on a channel. In addition, it should avoid scanning multiple channels in single off-channel scan so that it is under the overall off-channel time limit.

The host considers [NDIS\_STATUS\_WDI\_INDICATION\_ROAMING\_NEEDED](./ndis-status-wdi-indication-roaming-needed.md) a strong request from the adapter to roam, so when in this mode, the adapter should be careful about how often this indication is sent up. If the adapter performs its own roaming/AP selection decisions, it must employ appropriate mechanisms (such as neighbor reports or PMKIDs) to find and select/rank APs.

To optimize the association process, the adapter should use the cached BSS entry for TSF timer synchronization during join if possible. The cached entry should be good enough for TSF timer synchronization, which is fresh enough most of time because it was obtained from a recent probe request. TSF synchronization can be done later, even when the driver decides to pick an AP that does not have an up-to-date cached probe response. The driver can disable Wi-Fi power save until it receives the next beacon, which usually occurs within 100ms.

When operating in multi-channel concurrency mode, it is recommended that the adapter employ ECSA or other mechanisms for enabling seamless/no jitter experience when performing channel multiplexing.

 

