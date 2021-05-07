---
title: WDI doc change history
description: This section lists documentation change history for WDI documentation pages
ms.date: 05/07/2021
ms.localizationpriority: medium
---

# WDI doc change history

## Windows 10, version 2004

Documentation updated to WDI version 1.1.9.

| Topic | Description |
| ----- | ----------- |
| [WDI message structure](wdi-wi-fi-messages.md#tlvs) | Modified TLV structure and aggregate container to allow for variable-size KCK/KEK. |
| [OID_WDI_TASK_REQUEST_FTM](oid-wdi-task-request-ftm.md) | **ScanTrigger** enum value added.</br></br>Description updated for LE with BSS list cache. |
| [WDI_AUTH_ALGORITHM](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_auth_algorithm) | Added new WDI_AUTH_ALGORITHM **WDI_AUTH_ALGO_OWE**. |
| [WDI_CIPHER_ALGORITHM](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm) | **WDI_CIPHER_ALGO_GCMP_256** new cipher added.</br></br>**WDI_CIPHER_ALGO_BIP_GMAC_256** new cipher added. |
| [WDI_TLV_CONFIGURED_CIPHER_KEY](wdi-tlv-configured-cipher-key.md) | Added entries for [WDI_TLV_CIPHER_KEY_GCMP_256_KEY](wdi-tlv-cipher-key-gcmp-256-key.md) and [WDI_TLV_CIPHER_KEY_BIP_GMAC_256_KEY](wdi-tlv-cipher-key-bip-gmac-256-key.md). |
| [WDI_TLV_CIPHER_KEY_BIP_GMAC_256_KEY](wdi-tlv-cipher-key-bip-gmac-256-key.md) | Newly added TLV type. |
| [WDI_TLV_CIPHER_KEY_GCMP_256_KEY](wdi-tlv-cipher-key-gcmp-256-key.md) | Newly added TLV type. |
| [WDI_TLV_CONNECT_PARAMETERS](wdi-tlv-connect-parameters.md) | Added reference for new TLV type [WDI_TLV_OWE_DH_IE](wdi-tlv-owe-dh-ie.md). |
| [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md) | **BandwidthUsed** field added.</br></br>**PropegationProperty** field added.</br></br>**RTT** field changed to signed integer. |
| [WDI_TLV_KCK_CONTENT](wdi-tlv-kck-content.md) | Newly added TLV type. |
| [WDI_TLV_KEK_CONTENT](wdi-tlv-kek-content.md) | Newly added TLV type. |
| [WDI_TLV_OWE_DH_IE](wdi-tlv-owe-dh-ie.md) | Newly added TLV type. |
| [WDI_TLV_PROTOCOL_OFFLOAD](wdi-tlv-protocol-offload-id.md) | Newly added TLV type. |
| [WDI_TLV_REPLAY_COUNTER](wdi-tlv-replay-counter.md) | Newly added TLV type. |
| [WDI_TLV_STATION_CAPABILITIES](wdi-tlv-station-capabilities.md) | **Host-WPA3-FIPS** mode added. |

## Windows 10, version 1903

Documentation updated to WDI version 1.1.8.

| Topic | Description |
| ----- | ----------- |
| [WDI_TLV_STATION_CAPABILITIES](wdi-tlv-station-capabilities.md) | Added support for the driver to indicate support for Fine Timing Measurement (FTM). |
| [OID_WDI_TASK_REQUEST_FTM](oid-wdi-task-request-ftm.md) | Newly added task OID that enables WDI to request that the adapter initiate FTM procedures to obtain roundtrip time (RTT) and the Location Configuration Information (LCI) report from BSS targets. |
| [WDI_TLV_FTM_REQUEST_TIMEOUT](wdi-tlv-ftm-request-timeout.md) | Newly added TLV for FTM request. |
| [WDI_TLV_FTM_TARGET_BSS_ENTRY](wdi-tlv-ftm-target-bss-entry.md) | Newly added TLV for FTM request. |
| [WDI_TLV_REQUEST_LCI_REPORT](wdi-tlv-request-lci-report.md) | Newly added TLV for FTM request. |
| [NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE](ndis-status-wdi-indication-request-ftm-complete.md) | Newly added status indication sent by the host as a task completion indication for OID_WDI_TASK_REQUEST_FTM. Contains a list of FTM responses from BSS targets. |
| [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md) | Newly added TLV for FTM response. |
| [WDI_TLV_FTM_RESPONSE_STATUS](wdi-tlv-ftm-response-status.md) | Newly added TLV for FTM response. |
| [WDI_TLV_RETRY_AFTER](wdi-tlv-retry-after.md) | Newly added TLV for FTM response. |
| [WDI_TLV_FTM_NUMBER_OF_MEASUREMENTS](wdi-tlv-ftm-number-of-measurements.md) | Newly added TLV for FTM response. |
| [WDI_TLV_RTT](wdi-tlv-rtt.md) | Newly added TLV for FTM response. |
| [WDI_TLV_RTT_ACCURACY](wdi-tlv-rtt-accuracy.md) | Newly added TLV for FTM response. |
| [WDI_TLV_RTT_VARIANCE](wdi-tlv-rtt-variance.md) | Newly added TLV for FTM response. |
| [WDI_TLV_LCI_REPORT_STATUS](wdi-tlv-lci-report-status.md) | Newly added TLV for FTM response. |
| [WDI_TLV_LCI_REPORT_BODY](wdi-tlv-lci-report-body.md) | Newly added TLV for FTM response. |
| [WDI_TLV_INTERFACE_CAPABILITIES](wdi-tlv-interface-capabilities.md) | Added new capabilities for the driver to indicate support for Multiband Operation (MBO) and beacon report offloading. |
| [**WDI_ASSOC_STATUS**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_assoc_status) | Added **WDI_ASSOC_STATUS_ASSOCIATION_DISALLOWED** status. |
| [WPA3-SAE authentication](wpa3-sae-authentication.md) | New overview of WPA3-SAE (Secure Authentication of Equals) authentication. |
| [WDI_TLV_INTERFACE_CAPABILITIES](wdi-tlv-interface-capabilities.md) | Added new capability for the driver to indicate support for SAE authentication. |
| [**WDI_AUTH_ALGORITHM**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_auth_algorithm) | Added definition for **WDI_AUTH_ALGO_WPA3_SAE**. |
| [NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED](ndis-status-wdi-indication-sae-auth-params-needed.md) | Newly added status indication sent by the driver to request SAE authentication parameters from WDI. |
| [WDI_TLV_SAE_INDICATION_TYPE](wdi-tlv-sae-indication-type.md) | Newly added TLV for SAE authentication parameters requests. |
| [WDI_TLV_SAE_COMMIT_RESPONSE](wdi-tlv-sae-commit-response.md) | Newly added TLV for SAE authentication parameters requests. |
| [WDI_TLV_SAE_CONFIRM_RESPONSE](wdi-tlv-sae-confirm-response.md) | Newly added TLV for SAE authentication parameters requests. |
| [WDI_TLV_SAE_STATUS](wdi-tlv-sae-status.md) | Newly added TLV for SAE authentication parameters requests and for setting SAE authentication parameters. |
| [OID_WDI_SET_SAE_AUTH_PARAMS](oid-wdi-set-sae-auth-params.md) | Newly added property OID that contains the parameters required to send the SAE Commit or Confirm request, or an error message indicating a failure to perform SAE with the BSSID. |
| [WDI_TLV_SAE_REQUEST_TYPE](wdi-tlv-sae-request-type.md) | Newly added TLV for setting SAE authentication parameters. |
| [WDI_TLV_SAE_COMMIT_REQUEST](wdi-tlv-sae-commit-request.md) | Newly added TLV for setting SAE authentication parameters. |
| [WDI_TLV_SAE_FINITE_CYCLIC_GROUP](wdi-tlv-sae-finite-cyclic-group.md) | Newly added TLV for setting SAE authentication parameters. |
| [WDI_TLV_SAE_SCALAR](wdi-tlv-sae-scalar.md) | Newly added TLV for setting SAE authentication parameters. |
| [WDI_TLV_SAE_ELEMENT](wdi-tlv-sae-element.md) | Newly added TLV for setting SAE authentication parameters. |
| [WDI_TLV_SAE_ANTI_CLOGGING_TOKEN](wdi-tlv-sae-anti-clogging-token.md) | Newly added TLV for setting SAE authentication parameters. |
| [WDI_TLV_SAE_CONFIRM_REQUEST](wdi-tlv-sae-confirm-request.md) | Newly added TLV for setting SAE authentication parameters. |
| [WDI_TLV_SAE_SEND_CONFIRM](wdi-tlv-sae-send-confirm.md) | Newly added TLV for setting SAE authentication parameters. |
| [WDI_TLV_SAE_CONFIRM](wdi-tlv-sae-confirm.md) | Newly added TLV for setting SAE authentication parameters. |
| [OID_WDI_TASK_P2P_SEND_REQUEST_ACTION_FRAME](oid-wdi-task-p2p-send-request-action-frame.md) | Added additional validation of P2P IEs on outgoing action frames. |
| [OID_WDI_TASK_P2P_SEND_RESPONSE_ACTION_FRAME](oid-wdi-task-p2p-send-response-action-frame.md) | Added additional validation of P2P IEs on outgoing action frames. |

## Windows 10, version 1809

Documentation updated to WDI version 1.1.7.

| Topic | Description |
| ----- | ----------- |
| [**WDI_PHY_TYPE**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_phy_type) | Added support for 802.11ax PHY. |
| [**WDI_CONNECTION_QUALITY_HINT**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_connection_quality_hint) | Changed the name of the **WDI_CONNECTION_QUALITY_HIGH_CHANNEL_AVAILABILITY** value to **WDI_CONNECTION_QUALITY_HIGH_THROUGHPUT**. No change to the description of this value. |
| [NDIS_STATUS_WDI_INDICATION_DEVICE_SERVICE_EVENT](ndis-status-wdi-indication-device-service-event.md) | Added support for unsolicited device service notifications. |

## Windows 10, version 1803

Documentation updated to WDI version 1.1.6.

| Topic | Description |
| ----- | ----------- |
| [**WDI_TLV_OS_POWER_MANAGEMENT_FEATURES**](wdi-tlv-os-power-management-features.md) | Added this TLV to [OID_WDI_GET_ADAPTER_CAPABILITIES](oid-wdi-get-adapter-capabilities.md) to indicate which OS power management (PM) features that the driver supports. |
| [**WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY**](wdi-tlv-pm-protocol-offload-80211rsn-rekey.md) | Updated this TLV to specify that drivers must now return GTK/iGTK key info, if configured, when queried in [OID_WDI_GET_PM_PROTOCOL_OFFLOAD](oid-wdi-get-pm-protocol-offload.md). |
| [NDIS_STATUS_WDI_INDICATION_CIPHER_KEY_UPDATED](ndis-status-wdi-indication-cipher-key-updated.md) | Added this indication for drivers to provide notifications of GTK/iGTK key updates when the keys are updated, while the driver is not in the Offload state. |
| [*MINIPORT_WDI_TX_SUSPECT_FRAME_LIST_ABORT*](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_tx_suspect_frame_list_abort) | Updated *TxSuspectFrameListAbortHandle* to *TxSuspectFrameListAbort*. |

## Windows 10, version 1709

Documentation updated to WDI version 1.1.5.

| Topic | Description |
| ----- | ----------- |
| [WDI_TLV_TCP_OFFLOAD_CAPABILITIES](wdi-tlv-tcp-offload-capabilities.md) | Added new [**WDI_TLV_OFFLOAD_SCOPE**](wdi-tlv-offload-scope.md) parameter to indicate whether offloads specified apply to the STA port only or to all ports. |
| [NDIS_STATUS_WDI_INDICATION_SEND_AP_ASSOCIATION_RESPONSE_COMPLETE](ndis-status-wdi-indication-send-ap-association-response-complete.md) | Changed the [**WDI\_TLV\_PHY\_TYPE\_LIST**](wdi-tlv-phy-type-list.md) parameter to make it required. |
| [User-initiated feedback with IHV trace logging](user-initiated-feedback-with-ihv-trace-logging.md) | Added a new section describing how to add IHV logging to user-initiated feedback scenarios. |

## Windows 10, version 1607

Documentation updated to WDI version 1.0.21.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-wdi-task-p2p-discover" data-raw-source="[OID_WDI_TASK_P2P_DISCOVER](./oid-wdi-task-p2p-discover.md)">OID_WDI_TASK_P2P_DISCOVER</a></p></td>
<td align="left"><p>Added new task parameters:</p>
<ul>
<li><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-asp2-service-information-discovery-entry" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY&lt;/strong&gt;](./wdi-tlv-p2p-asp2-service-information-discovery-entry.md)"><strong>WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY</strong></a></li>
<li><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-include-listen-channel" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL&lt;/strong&gt;](./wdi-tlv-p2p-include-listen-channel.md)"><strong>WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL</strong></a></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-wdi-get-adapter-capabilities" data-raw-source="[OID_WDI_GET_ADAPTER_CAPABILITIES](./oid-wdi-get-adapter-capabilities.md)">OID_WDI_GET_ADAPTER_CAPABILITIES</a></p></td>
<td align="left"><p>Added new get property result: <a href="/windows-hardware/drivers/network/wdi-tlv-supported-guids" data-raw-source="[&lt;strong&gt;WDI_TLV_SUPPORTED_GUIDS&lt;/strong&gt;](./wdi-tlv-supported-guids.md)"><strong>WDI_TLV_SUPPORTED_GUIDS</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm" data-raw-source="[&lt;strong&gt;WDI_CIPHER_ALGORITHM&lt;/strong&gt;](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_cipher_algorithm)"><strong>WDI_CIPHER_ALGORITHM</strong></a></p></td>
<td align="left"><p>Added new value: <strong>WDI_CIPHER_ALGO_GCMP</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_phy_type" data-raw-source="[&lt;strong&gt;WDI_PHY_TYPE&lt;/strong&gt;](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_phy_type)"><strong>WDI_PHY_TYPE</strong></a></p></td>
<td align="left"><p>Added new value: <strong>WDI_PHY_TYPE_DMG</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_service_discovery_type" data-raw-source="[&lt;strong&gt;WDI_P2P_SERVICE_DISCOVERY_TYPE&lt;/strong&gt;](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_p2p_service_discovery_type)"><strong>WDI_P2P_SERVICE_DISCOVERY_TYPE</strong></a></p></td>
<td align="left"><p>Added new values:</p>
<ul>
<li><strong>WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_NAME_ONLY</strong></li>
<li><strong>WDI_P2P_SERVICE_DISCOVERY_TYPE_ASP2_SERVICE_INFORMATION</strong></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-asp2-advertised-service-entry" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY&lt;/strong&gt;](./wdi-tlv-p2p-asp2-advertised-service-entry.md)"><strong>WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY</strong></a></p>
<p><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-asp2-service-information-discovery-entry" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY&lt;/strong&gt;](./wdi-tlv-p2p-asp2-service-information-discovery-entry.md)"><strong>WDI_TLV_P2P_ASP2_SERVICE_INFORMATION_DISCOVERY_ENTRY</strong></a></p>
<p><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-include-listen-channel" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL&lt;/strong&gt;](./wdi-tlv-p2p-include-listen-channel.md)"><strong>WDI_TLV_P2P_INCLUDE_LISTEN_CHANNEL</strong></a></p>
<p><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-instance-name" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_INSTANCE_NAME&lt;/strong&gt;](./wdi-tlv-p2p-instance-name.md)"><strong>WDI_TLV_P2P_INSTANCE_NAME</strong></a></p>
<p><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-instance-name-hash" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_INSTANCE_NAME_HASH&lt;/strong&gt;](./wdi-tlv-p2p-instance-name-hash.md)"><strong>WDI_TLV_P2P_INSTANCE_NAME_HASH</strong></a></p>
<p><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-service-type" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_SERVICE_TYPE&lt;/strong&gt;](./wdi-tlv-p2p-service-type.md)"><strong>WDI_TLV_P2P_SERVICE_TYPE</strong></a></p>
<p><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-service-type-hash" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_SERVICE_TYPE_HASH&lt;/strong&gt;](./wdi-tlv-p2p-service-type-hash.md)"><strong>WDI_TLV_P2P_SERVICE_TYPE_HASH</strong></a></p>
<p><a href="/windows-hardware/drivers/network/wdi-tlv-supported-guids" data-raw-source="[&lt;strong&gt;WDI_TLV_SUPPORTED_GUIDS&lt;/strong&gt;](./wdi-tlv-supported-guids.md)"><strong>WDI_TLV_SUPPORTED_GUIDS</strong></a></p></td>
<td align="left"><p>Newly added TLVs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-advertised-services" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_ADVERTISED_SERVICES&lt;/strong&gt;](./wdi-tlv-p2p-advertised-services.md)"><strong>WDI_TLV_P2P_ADVERTISED_SERVICES</strong></a></p></td>
<td align="left"><p>Added contained TLV: <a href="/windows-hardware/drivers/network/wdi-tlv-p2p-asp2-advertised-service-entry" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY&lt;/strong&gt;](./wdi-tlv-p2p-asp2-advertised-service-entry.md)"><strong>WDI_TLV_P2P_ASP2_ADVERTISED_SERVICE_ENTRY</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/network/wdi-tlv-interface-capabilities" data-raw-source="[&lt;strong&gt;WDI_TLV_INTERFACE_CAPABILITIES&lt;/strong&gt;](./wdi-tlv-interface-capabilities.md)"><strong>WDI_TLV_INTERFACE_CAPABILITIES</strong></a></p></td>
<td align="left"><p>Added a new value that specifies if the device supports IP docking capability.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-capabilities" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_CAPABILITIES&lt;/strong&gt;](./wdi-tlv-p2p-capabilities.md)"><strong>WDI_TLV_P2P_CAPABILITIES</strong></a></p></td>
<td align="left"><p>Added a new value that specifies if ASP2 Service Names Discovery is supported.</p>
<p>Added a new value that specifies if ASP2 Service Information Discovery is supported.</p></td>
</tr>
</tbody>
</table>

## March 2016

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_tx_target_desc_deinit" data-raw-source="[&lt;em&gt;MINIPORT_WDI_TX_TARGET_DESC_DEINIT&lt;/em&gt;](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_tx_target_desc_deinit)"><em>MINIPORT_WDI_TX_TARGET_DESC_DEINIT</em></a></p></td>
<td align="left"><p>Added note that the IHV miniport is not permitted to make any indication in the context of this call.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_tx_target_desc_init" data-raw-source="[&lt;em&gt;MINIPORT_WDI_TX_TARGET_DESC_INIT&lt;/em&gt;](/windows-hardware/drivers/ddi/dot11wdi/nc-dot11wdi-miniport_wdi_tx_target_desc_init)"><em>MINIPORT_WDI_TX_TARGET_DESC_INIT</em></a></p></td>
<td align="left"><p>Added note that the IHV miniport is not permitted to make any indication in the context of this call.</p></td>
</tr>
</tbody>
</table>

## Windows 10, version 1511

Documentation updated to WDI version 1.0.10.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-wdi-task-start-ap" data-raw-source="[OID_WDI_TASK_START_AP](./oid-wdi-task-start-ap.md)">OID_WDI_TASK_START_AP</a></p></td>
<td align="left"><p>Added a new task parameter: <a href="/windows-hardware/drivers/network/wdi-tlv-ap-band-channel" data-raw-source="[&lt;strong&gt;WDI_TLV_AP_BAND_CHANNEL&lt;/strong&gt;](./wdi-tlv-ap-band-channel.md)"><strong>WDI_TLV_AP_BAND_CHANNEL</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/network/oid-wdi-set-adapter-configuration" data-raw-source="[OID_WDI_SET_ADAPTER_CONFIGURATION](./oid-wdi-set-adapter-configuration.md)">OID_WDI_SET_ADAPTER_CONFIGURATION</a></p></td>
<td align="left"><p>Added a new task parameter: <a href="/windows-hardware/drivers/network/wdi-tlv-pldr-support" data-raw-source="[&lt;strong&gt;WDI_TLV_PLDR_SUPPORT&lt;/strong&gt;](./wdi-tlv-pldr-support.md)"><strong>WDI_TLV_PLDR_SUPPORT</strong></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/network/wdi-tlv-ap-band-channel" data-raw-source="[&lt;strong&gt;WDI_TLV_AP_BAND_CHANNEL&lt;/strong&gt;](./wdi-tlv-ap-band-channel.md)"><strong>WDI_TLV_AP_BAND_CHANNEL</strong></a></p></td>
<td align="left"><p>Newly added TLV type.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/network/wdi-tlv-p2p-capabilities" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_CAPABILITIES&lt;/strong&gt;](./wdi-tlv-p2p-capabilities.md)"><strong>WDI_TLV_P2P_CAPABILITIES</strong></a></p></td>
<td align="left"><p>Added a new value that specifies whether the adapter supports operating a GO on the 5GHz band.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/network/wdi-tlv-pldr-support" data-raw-source="[&lt;strong&gt;WDI_TLV_PLDR_SUPPORT&lt;/strong&gt;](./wdi-tlv-pldr-support.md)"><strong>WDI_TLV_PLDR_SUPPORT</strong></a></p></td>
<td align="left"><p>Newly added TLV type.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/network/wdi-tlv-start-ap-parameters" data-raw-source="[&lt;strong&gt;WDI_TLV_START_AP_PARAMETERS&lt;/strong&gt;](./wdi-tlv-start-ap-parameters.md)"><strong>WDI_TLV_START_AP_PARAMETERS</strong></a></p></td>
<td align="left"><p>Added a new value that specifies whether to allow legacy SoftAP clients to connect.</p>
<p>Added a new value that specifies whether the AP can only be started on the channels specified in <a href="/windows-hardware/drivers/network/oid-wdi-task-start-ap" data-raw-source="[OID_WDI_TASK_START_AP](./oid-wdi-task-start-ap.md)">OID_WDI_TASK_START_AP</a> task parameters with <a href="/windows-hardware/drivers/network/wdi-tlv-ap-band-channel" data-raw-source="[&lt;strong&gt;WDI_TLV_AP_BAND_CHANNEL&lt;/strong&gt;](./wdi-tlv-ap-band-channel.md)"><strong>WDI_TLV_AP_BAND_CHANNEL</strong></a>.</p></td>
</tr>
</tbody>
</table>

## Windows 10

Initial version.
