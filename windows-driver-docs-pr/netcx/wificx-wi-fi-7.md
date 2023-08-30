---
title: WiFiCx Wi-Fi 7 feature requirements
description: Driver changes required to support Wi-Fi 7 functionalities in WiFiCx, including Multi-Link Operation (MLO). 
ms.date: 08/23/2023
---

# WiFiCx Wi-Fi 7 feature requirements

WiFiCx supports Wi-Fi 7 functionalities, providing faster connectivity speeds, lower latency, and improved security. WiiFiCx enables Multi-Link Operation (MLO) with roaming differentiation to leverage multiple simultaneous channels to the Wi-Fi access point (AP), and enhanced capabilities for WPA3-SAE authentication and Opportunistic Wireless Encryption (OWE) with GCMP-256 cipher. 

This article outlines the driver changes required to support these features.

## Wi-Fi 7 capability detection

The driver must support WDI version 2.0.9.11 for Wi-Fi 7 connection setup. 

To indicate support for Wi-Fi MLO connections, the driver must set the following capabilities in the [**WIFI_STATION_CAPABILITIES**](/windows-hardware/drivers/ddi/wificx/ns-wificx-wifi_station_capabilities) structure:
- The number of entries in **MLOAddressesList** must match **MaxMLOLinksSupported**, which indicates if the driver is capable of setting up MLO links.
- The number of entries in **AkmsList** must match **NumAkmsSupported**. This list should include all the AKM suites that the driver supports and must include the AKM 24 if the OS is expected to support SAE with a 384-bit PMK.
 
To support SAE connections using AKM 24 or AKM 8 with GCMP-256 cipher, the driver must add the following auth-cipher pairs when calling [**WifiDeviceSetStationCapabilities**](/windows-hardware/drivers/ddi/wificx/nf-wificx-wifidevicesetstationcapabilities):
- In **UnicastAlgorithmsList**:
{ DOT11_AUTH_ALGO_WPA3_SAE, DOT11_CIPHER_ALGO_GCMP_256 }
- In **MulticastMgmtAlgorithmsList**:
{ DOT11_AUTH_ALGO_WPA3_SAE, DOT11_CIPHER_ALGO_GCMP_256 }
 
To support OWE connections with GCMP-256 cipher, the driver must add the following auth-cipher pair when calling [**WifiDeviceSetStationCapabilities**](/windows-hardware/drivers/ddi/wificx/nf-wificx-wifidevicesetstationcapabilities):
- In **UnicastAlgorithmsList**: { DOT11_AUTH_ALGO_OWE, DOT11_CIPHER_ALGO_GCMP_256 }

## Frame MAC addresses

When the driver indicates management frames, use the link MAC address. For data frames, including 4-way handshake and 802.1x authentication frames, use the MLD MAC address.

For data frames, including 4-way handshake and 802.1x authentication frames, the MAC address is the MLD Mac address.

When Windows uses random MAC addresses, it provides a set of random addresses in [WDI_TLV_CONFIGURED_MLO_LINK_MAC_ADDRESS](wdi-tlv-configured-mlo-link-mac-address.md) when it sends the [OID_WDI_TASK_DOT11_RESET](oid-wdi-task-dot11-reset.md) task.

## AP discovery

Windows parses the beacon IEs for Multi-Link and RNR IEs. If present, it marks the AP as supporting MLO.

## Multi-Link connection setup

Windows provides a setting to the driver in the [OID_WDI_TASK_CONNECT](oid-wdi-task-connect.md) task to indicate whether the driver can connect using MLO. This setting is represented by the **MloConnectionSupported** flag in [WDI_TLV_CONNECTION_SETTINGS](wdi-tlv-connection-settings.md). When **MloConnectionSupported** is **true**, the driver can only use the AKMs specified by [WDI_TLV_RSNA_AKM_SUITE](wdi-tlv-rsna-akm-suite.md). When **MloConnectionSupported** is **false**, the driver should only expect to connect without multi-link connectivity.

For SAE-based connections, Windows sets the AKM and cipher in the SAE Commit request, which tells the driver which AKM and cipher to use later on in the association request.

## Authentication

For SAE authentication using Wi-Fi 7 MLO, Windows sets the selected AKM and cipher that the driver uses in [WDI_TLV_SAE_COMMIT_PARAMS](wdi-tlv-sae-commit-params.md) when calling [OID_WDI_SET_SAE_AUTH_PARAMS](oid-wdi-set-sae-auth-params.md). These values are specified in the [WDI_TLV_RSNA_AKM_SUITE](wdi-tlv-rsna-akm-suite.md) and [WDI_TLV_CIPHER_ALGORITHM](wdi-tlv-cipher-algorithm.md) TLVs.

In the [NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED](ndis-status-wdi-indication-sae-auth-params-needed.md) indication, the driver should:

- Set the **BSSID** ([WDI_TLV_BSSID](wdi-tlv-bssid.md)) to the AP's Link MAC address.
- Set the **LocalMloLinkBssId** ([WDI_TLV_MLO_LINK_BSSID](wdi-tlv-mlo-link-bssid.md)) to the local Link MAC address.

Include the appropriate Multi-Link IE(s) in the authentication frames when connecting for MLO.

## Association

When Windows sends [OID_WDI_TASK_CONNECT](oid-wdi-task-connect.md) and [OID_WDI_TASK_ROAM](oid-wdi-task-roam.md) tasks, the driver should only connect to APs using Wi-Fi 7 MLO if the AP supports Multi-Link connectivity with the AKMs listed in [WDI_TLV_RSNA_AKM_SUITE](wdi-tlv-rsna-akm-suite.md) in the [WDI_TLV_CONNECT_PARAMETERS](wdi-tlv-connect-parameters.md) TLV.

The driver includes the appropriate Multi-Link IE(s) in the association frames when connecting for MLO. On Association-Completion, Windows checks the Multi-Link IEs in the Association Request/Response frames in the [NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT](ndis-status-wdi-indication-association-result.md) indication to determine if MLO was used in the connection.

Windows requires that the driver indicates the Association Request and Response frames in [WDI_TLV_ASSOCIATION_RESULT](./wdi-tlv-association-result.md) when indicating NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT.

For association using Wi-Fi 7 MLO, the driver must set the following values in NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT:

- Set the **BSSID** ([WDI_TLV_BSSID](wdi-tlv-bssid.md)) in [WDI_TLV_ASSOCIATION_RESULT](./wdi-tlv-association-result.md) to the AP's Link MAC address.
- Set the **LocalLinkBssId** ([WDI_TLV_MLO_LINK_BSSID](wdi-tlv-mlo-link-bssid.md)) in WDI_TLV_ASSOCIATION_RESULT to the local Link MAC address.

Note: If the **LocalLinkBssId** isn't set, Windows can't use MLO for the connection.

## 4-way handshake

Windows supports GCMP-256 in the 4-way handshake. It also updated the WDI interface to provide link information when setting the GTK/IGTK/BIGTK keys.

When setting the group keys (GTK/IGTK/BIGTK) for MLO connections, Windows calls the [OID_WDI_SET_ADD_CIPHER_KEYS](oid-wdi-set-add-cipher-keys.md) command with an array of elements, one for each key that is added.

## Link state indication

The [NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE](ndis-status-wdi-indication-link-state-change.md) indication now provides the following information per link in [WDI_TLV_LINK_INFO](wdi-tlv-link-info.md):

- Link ID
- Connected band/channel
- Received signal strength indicator (RSSI)
- Current bandwidth
- Current Tx MCS
- Current Rx MCS

For MLO connections, the link state indication provides information for each link. For non-MLO connections, it provides information for a single link.

## Disassociation

The driver sends the [NDIS_STATUS_WDI_INDICATION_DISASSOCIATION](ndis-status-wdi-indication-disassociation.md) indication only when all links have been disassociated. If the driver connects on a new link or is disconnected from a currently connected link, the driver just sends a [NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE](ndis-status-wdi-indication-link-state-change.md) notification to update the set of links on which it's currently associated.

When the driver sends the NDIS_STATUS_WDI_INDICATION_DISASSOCIATION indication, it should set the MAC address in [WDI_TLV_DISASSOCIATION_INDICATION_PARAMETERS](wdi-tlv-disassociation-indication-parameters.md) as the AP's MLD MAC address.

## SAE authentication changes

### Sending an SAE authentication frame

The following types and TLVs have been renamed for the [OID_WDI_SET_SAE_AUTH_PARAMS](oid-wdi-set-sae-auth-params.md) command:

- Renamed **WDI_SAE_REQUEST_TYPE_COMMIT_REQUEST** to **WDI_SAE_REQUEST_TYPE_COMMIT_PARAMS** in the [**WDI_SAE_REQUEST_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_sae_request_type) enum.
- Renamed **WDI_SAE_REQUEST_TYPE_CONFIRM_REQUEST** to **WDI_SAE_REQUEST_TYPE_CONFIRM_PARAMS** in the [**WDI_SAE_REQUEST_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_sae_request_type) enum.
- Renamed WDI_TLV_SAE_COMMIT_REQUEST to [WDI_TLV_SAE_COMMIT_PARAMS](wdi-tlv-sae-commit-params.md). This TLV is used to send both commit-request and commit-response frames.
- Renamed WDI_TLV_SAE_CONFIRM_REQUEST to [WDI_TLV_SAE_CONFIRM_PARAMS](wdi-tlv-sae-confirm-params.md). This TLV is used to send both confirm-request and confirm-response frames.

### Indicating an SAE authentication frame

The following types and TLVs have been renamed for the [NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED](ndis-status-wdi-indication-sae-auth-params-needed.md) indication: 

- Renamed **WDI_SAE_INDICATION_COMMIT_RESPONSE** to **WDI_SAE_INDICATION_COMMIT_FRAME** in the [**WDI_SAE_INDICATION_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_sae_indication_type) enum.
- Renamed **WDI_SAE_INDICATION_CONFIRM_RESPONSE** to **WDI_SAE_INDICATION_CONFIRM_FRAME** in the [**WDI_SAE_INDICATION_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_sae_indication_type) enum.
- Renamed WDI_TLV_SAE_COMMIT_RESPONSE to [WDI_TLV_SAE_COMMIT_FRAME](wdi-tlv-sae-commit-frame.md).
- Renamed WDI_TLV_SAE_CONFIRM_RESPONSE to [WDI_TLV_SAE_CONFIRM_FRAME](wdi-tlv-sae-confirm-frame.md).

In the call to WDI_SET_SAE_AUTH_PARAMS, the OS provides the AKM and cipher as optional parameters that the driver will use when sending the association request. The AKM/cipher combination will be determined during the SAE exchange.

## OWE connection

For OWE connections, Windows checks if the AP supports GCMP-256 cipher. If supported, Windows initially tries to use Group 20 for association. If the AP fails the association request with the error **DOT11_FRAME_STATUS_UNSUPPORTED_FINITE_CYCLIC_GROUP** (77), the OS falls back to using Group 19 for association.

Initially, the OS sets the DH parameters for OWE in [OID_WDI_TASK_CONNECT](oid-wdi-task-connect.md) to Group 20. If the AP fails the association request with an unsupported group error, the OS sends the [OID_WDI_SET_OWE_DH_IE](oid-wdi-set-owe-dh-ie.md) OID to the driver with the updated OWE information for Group 19. The driver should use the updated OWE information for the next association request.

Note: For the OS to properly process the **DOT11_FRAME_STATUS_UNSUPPORTED_FINITE_CYCLIC_GROUP** error, the driver must also set the WDI status in the [NDIS_STATUS_WDI_INDICATION_ASSOCIATION_RESULT](ndis-status-wdi-indication-association-result.md) indication to **WDI_ASSOC_STATUS_ASSOC_FAILED_BY_PEER**.