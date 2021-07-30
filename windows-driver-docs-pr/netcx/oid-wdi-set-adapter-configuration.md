---
title: OID_WDI_SET_ADAPTER_CONFIGURATION (dot11wificxintf.h)
description: The OID_WDI_SET_ADAPTER_CONFIGURATION command configures the adapter. It is an optional property and can only be sent before any ports are created.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_ADAPTER_CONFIGURATION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_ADAPTER\_CONFIGURATION (dot11wificxintf.h)


OID\_WDI\_SET\_ADAPTER\_CONFIGURATION configures the adapter. It is an optional property and can only be sent before any ports are created.

| Scope   | Set serialized with task | Normal execution time (seconds) |
|---------|--------------------------|---------------------------------|
| Adapter | Yes                      | 1                               |

 

## Set property parameters


|TLV|Multiple TLV instances allowed|Optional|Description|
|--- |--- |--- |--- |
|[**WDI_TLV_CONFIGURED_MAC_ADDRESS**](wdi-tlv-configured-mac-address.md)||X|MAC address.|
|[**WDI_TLV_UNREACHABLE_DETECTION_THRESHOLD**](wdi-tlv-unreachable-detection-threshold.md)||X|Unreachable detection threshold.|
|[**WDI_TLV_P2P_GO_INTERNAL_RESET_POLICY**](wdi-tlv-p2p-go-internal-reset-policy.md)||X|Policy used by the firmware for operating channel selection after a Wi-Fi Direct GO Reset is stopped/restarted.|
|[**WDI_TLV_BAND_ID_LIST**](wdi-tlv-band-id-list.md)||X| List of bands that are not allowed to be used by the IHV. If not specified any supported band can be used. |
|[**WDI_TLV_LINK_QUALITY_BAR_MAP**](wdi-tlv-link-quality-bar-map.md)|||Mapping of signal quality to Wi-Fi signal strength bars. This field should be ignored by the adapter and it should use the behavior specified in [NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE](ndis-status-wdi-indication-link-state-change.md) for doing Link Quality notifications.|
|[**WDI_TLV_ADAPTER_NLO_SCAN_MODE**](wdi-tlv-adapter-nlo-scan-mode.md)||X|Indicates whether the NLO scans should be performed in active or passive mode.|
|[**WDI_TLV_PLDR_SUPPORT**](wdi-tlv-pldr-support.md)|||Specifies if PLDR is supported.|

 

## Set property results


No additional data. The data in the header is sufficient.

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|


