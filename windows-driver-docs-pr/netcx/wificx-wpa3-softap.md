---
title: WPA3 SoftAP
description: The WPA3 SoftAP feature enables devices to set up a SoftAP that utilizes WPA3-SAE and is capable of operating on either the 2.4 GHz or 5 GHz band.
ms.date: 02/29/2024
ms.topic: concept-article
---

# WiFiCx WPA3 SoftAP

The WPA3 SoftAP feature enables devices to set up a Soft Access Point (SoftAP) using the Wi-Fi Protected Access 3 - Simultaneous Authentication of Equals (WPA3-SAE) security protocol. This SoftAP can operate on either the 2.4 GHz or 5 GHz band. Starting in WDI version 2.0.11 and WiFiCx version 1.1, you can integrate WPA3 SoftAP functionality in your WiFiCx client driver. 

WPA3 SoftAP supports WPA3-SAE and a WPA3-SAE transition mode for backward compatibility. The transition mode accommodates both WPA2-PSK and WPA3-SAE authentication methods, ensuring secure Wi-Fi connectivity across various devices and environments.

WPA3 SoftAP is only available in the WiFiCx driver model. This article describes how to add support for WPA3 SoftAP in your WiFiCx driver.

## WPA3 SoftAP capability detection

Your client driver indicates its support for WPA3 SoftAP when it calls [**WifiDeviceSetWiFiDirectCapabilities**](/windows-hardware/drivers/ddi/wificx/nf-wificx-wifidevicesetwifidirectcapabilities). This call reports Wi-Fi direct capabilities to WiFiCx. The driver must include the authentication and cipher pair **DOT11_AUTH_ALGO_WPA3_SAE + DOT11_CIPHER_ALGO_CCMP** in the **UnicastAlgorithms** list within the [**WIFI_WIFIDIRECT_CAPABILITIES**](/windows-hardware/drivers/ddi/wificx/ns-wificx-wifi_wifidirect_capabilities) structure.

A driver that supports both WPA2-PSK and WPA3-SAE with SoftAP must report the following unicast algorithm pairs:

- **DOT11_AUTH_ALGO_WPA3_SAE + DOT11_CIPHER_ALGO_CCMP**
- **DOT11_AUTH_ALGO_RSNA_PSK + DOT11_CIPHER_ALGO_CCMP**

Listing these pairs signals to WiFiCx that the driver supports the SoftAP feature in WPA3 transition mode.

## AP start parameters

Windows modifies the [OID_WDI_TASK_START_AP](oid-wdi-task-start-ap.md) task as follows:

- The [WDI_TLV_AUTH_ALGO_LIST](wdi-tlv-auth-algo-list.md) TLV might include **WDI_AUTH_ALGO_WPA3_SAE** if the driver indicates support for WPA3 SoftAP.
- The WDI_TLV_AUTH_ALGO_LIST TLV might include both **WDI_AUTH_ALGO_WPA3_SAE** and **WDI_AUTH_ALGO_RSNA_PSK**. In this case, the driver must advertise support for both security protocols through beacons and probe responses, and must allow client authentication using either WPA2-PSK or WPA3-SAE.

## AKM support

AKM 0xac0f08 (**RSNA_AKM_SAE_PMK256**) is the only AKM supported for WPA3 SoftAP. The driver must not advertise support for other AKMs.

## Protected management frames (PMF) capability detection

The OS doesn't provide a specific flag for PMF in the AP start parameters. The driver must advertise PMF capabilities as follows:

| Auth algorithm present | PMF required | PMF capable |
|------------------------|--------------|-------------|
| WPA2-PSK               | No           | No          |
| WPA3-SAE + WPA2-PSK    | No           | Yes         |
| WPA3-SAE               | Yes          | Yes         |

If the driver reports capability for WPA3-SAE on SoftAP, the OS expects the driver to support PMF. There's no additional driver capability for PMF.

## SAE Authentication for WPA3 SoftAP

This section describes SAE authentication updates for WPA3 SoftAP scenarios.

### Hash-to-Element (H2E) and Hunt and Peck support

The OS doesn't provide a specific flag for using H2E only in the AP start parameters. Therefore, drivers must consistently indicate that they support both H2E and Hunt and Peck methods for SoftAP.

### Anti-clogging tokens

The OS might respond to a peer commit request by requesting an anti-clogging token. The OS calls [OID_WDI_SET_SAE_AUTH_PARAMS](oid-wdi-set-sae-auth-params.md) with:
* The request type **WDI_SAE_REQUEST_TYPE_COMMIT_PARAMS** or **WDI_SAE_REQUEST_TYPE_COMMIT_PARAMS_H2E** (if H2E is used).
* The commit frame **StatusCode** ([WDI_TLV_SAE_COMMIT_PARAMS](wdi-tlv-sae-commit-params.md) > [WDI_TLV_SAE_STATUS_CODE](wdi-tlv-sae-status-code.md)) set to **DOT11_FRAME_STATUS_ANTI_CLOGGING_TOKEN_REQUIRED**. 

The peer provides an anti-clogging token as part of the commit parameters.

In a SoftAP scenario, when an anti-clogging token is included in the commit parameters, Scalar/Element values aren't generated. These fields are therefore optional in the WDI_TLV_SAE_COMMIT_PARAMS TLV, and the driver should check for their presence before accessing them. This change remains compatible with existing drivers. New drivers should validate the presence of these optional fields in all paths.

### Rejected groups

The OS only supports Group 19. If the OS receives a commit frame from a peer that indicates a group that the OS doesn't support, the OS sends an [OID_WDI_SET_SAE_AUTH_PARAMS](oid-wdi-set-sae-auth-params.md) command. In the command, the OS sets:

* **WDI_SAE_REQUEST_TYPE** to **WDI_SAE_REQUEST_TYPE_COMMIT_PARAMS** or **WDI_SAE_REQUEST_TYPE_COMMIT_H2E_PARAMS** (if H2E is used).
* **SaeStatus** to **WDI_SAE_STATUS_COMMIT_MESSAGE_UNSUPPORTED_FINITE_GROUP**.
* The commit frame **StatusCode** ([WDI_TLV_SAE_COMMIT_PARAMS](wdi-tlv-sae-commit-params.md) > [WDI_TLV_SAE_STATUS_CODE](wdi-tlv-sae-status-code.md)) to **DOT11_FRAME_STATUS_UNSUPPORTED_FINITE_CYCLIC_GROUP**.
* The commit frame **FiniteCyclicGroup** ([WDI_TLV_SAE_COMMIT_PARAMS](wdi-tlv-sae-commit-params.md) > [WDI_TLV_SAE_FINITE_CYCLIC_GROUP](wdi-tlv-sae-finite-cyclic-group.md)) to the rejected group (not to be confused with the **RejectedGroups** field, which contains groups that the peer rejects).

If the OS receives a commit frame from a peer that includes a group within the **RejectedGroups** field that the OS actually supports, the OS will still fail the SAE authentication. The OS will send an [OID_WDI_SET_SAE_AUTH_PARAMS](oid-wdi-set-sae-auth-params.md) command with:

* **WDI_SAE_REQUEST_TYPE** set to **WDI_SAE_REQUEST_TYPE_FAILURE**. 
* **SaeStatus** set to **WDI_SAE_STATUS_COMMIT_MESSAGE_INVALID_REJECTED_GROUP**.

### SAE authentication sequence

Once the [OID_WDI_TASK_START_AP](oid-wdi-task-start-ap.md) task is called, the driver allows devices to send SAE authentication frames if **DOT11_AUTH_ALGO_WPA3_SAE** is set in the authentication algorithms list in OID_WDI_TASK_START_AP.  The driver uses the [NDIS_STATUS_WDI_INDICATION_SAE_AUTH_PARAMS_NEEDED](ndis-status-wdi-indication-sae-auth-params-needed.md) indication to pass the SAE authentication parameters to the OS.

Windows calls [OID_WDI_SET_SAE_AUTH_PARAMS](oid-wdi-set-sae-auth-params.md) with **WDI_SAE_COMMIT_PARAMS** and **WDI_SAE_CONFIRM_PARAMS** to complete the SAE exchange.

After the driver receives the confirm parameters from the OS and sends them to the peer, it can accept an association request and indicate it to the OS.

## High performance SoftAP

For scenarios like Augmented Reality (AR) or Virtual Reality (VR), drivers should optimize SoftAP performance as much as possible and prioritize it over the STA connection. This process involves strategic decisions when starting the SoftAP, such as band/channel selection and coexistence with the STA connection. It also involves optimization while sustaining the SoftAP.

The OS indicates scenarios that require high-performance SoftAP using a new flag, **favorOverSta**, in the [OID_WDI_TASK_START_AP](oid-wdi-task-start-ap.md) task. 

The OS doesn't dictate how the driver should optimize the SoftAP link, leaving it largely to the driver’s discretion. The driver can degrade the STA link to improve the SoftAP link.

When the OS initiates SoftAP with the **favorOverSta** flag set, the driver is authorized and encouraged to roam the STA connection to a different band/channel if it enhances the SoftAP link. 

If the OS-requested band/channel parameters conflict with the current STA connection, the driver should consider whether roaming the STA connection would enable it to start the SoftAP with the requested parameters.

When a SoftAP started with the **favorOverSta** flag is running, the OS might send a [OID_WDI_SET_CONNECTION_QUALITY](oid-wdi-set-connection-quality.md) task to request optimized performance on the SoftAP link. The driver should honor this task, but should also strive to enhance the SoftAP link even if it doesn’t receive specific requirements through a OID_WDI_SET_CONNECTION_QUALITY task.

### Expected behavior when roaming the STA port

The OS requests "any" band/channel:

* The driver should start the SoftAP on the best band/channel, considering the current configuration and STA connection. Usually, the best band/channel is the one used by the STA link. The driver should then successfully complete the [OID_WDI_TASK_START_AP](oid-wdi-task-start-ap.md) task.

  If moving the STA could potentially improve the SoftAP link, the driver can send a roam request to the OS using [NDIS_STATUS_WDI_INDICATION_ROAMING_NEEDED](ndis-status-wdi-indication-roaming-needed.md). When the roam succeeds, the driver can move the SoftAP link to a new band/channel that would optimize performance.

The OS requests a specific band/channel:

* If the driver can sustain the SoftAP on the OS-requested band/channel with reasonable performance, it should successfully complete the OID_WDI_TASK_START_AP task. 

* If the driver can't currently sustain the SoftAP on the requested band/channel, it should check if the following conditions are met.

  1. An alternative BSS is available for the STA to roam to.
  2. The driver can sustain the SoftAP on the OS-requested band/channel after roaming the STA link.
  3. It's unlikely that the roam will fail.

  If these conditions are met, the driver should complete OID_WDI_TASK_START_AP successfully and send a roam request to move the STA connection.

  Otherwise, the driver should fail the OID_WDI_TASK_START_AP task with a relevant error code.

After the driver completes the OID_WDI_TASK_START_AP task, it can send a roam request to move the STA connection to maintain or enhance SoftAP performance. 

If the roam fails and the driver can't sustain the SoftAP without moving the STA connection, the driver should stop the SoftAP. The driver informs the operating system by sending [NDIS_STATUS_WDI_INDICATION_STOP_AP](ndis-status-wdi-indication-stop-ap.md) with a relevant reason code (typically, WDI_STOP_AP_REASON_FREQUENCY_NOT_AVAILABLE).

When the SoftAP stops, users might notice a "flickering" effect, where the SoftAP starts and then stops almost instantly. This behavior should be avoided as much as possible. If the driver requires a roam to sustain the SoftAP, the driver should be confident that the roam will succeed before completing the OID_WDI_TASK_START_AP task.


### SoftAP error codes
 
If the SoftAP can't be started because the band/channel isn't allowed for a regulatory reason, the driver should fail the OID_WDI_TASK_START_AP task with the error code **STATUS_NDIS_DOT11_AP_CHANNEL_NOT_ALLOWED** or **STATUS_NDIS_DOT11_AP_BAND_NOT_ALLOWED**.

If the SoftAP can't be started because the STA is operating on a band/channel that is incompatible with the requested band/channel, and no reasonable candidate is available for roaming, the driver should fail the OID_WDI_TASK_START_AP task with the error code **STATUS_NDIS_DOT11_AP_CHANNEL_CURRENTLY_NOT_AVAILABLE** or **STATUS_NDIS_DOT11_AP_BAND_CURRENTLY_NOT_AVAILABLE**.

If the SoftAP can't be started for another reason (unsupported band/channel, generic driver issue, etc.), the driver should use  a generic error code, such as **STATUS_NOT_SUPPORTED**.

If the SoftAP can't be sustained because it was necessary to roam the STA connection, but the roam failed, the driver should stop the SoftAP with the reason code
**WDI_STOP_AP_REASON_FREQUENCY_NOT_AVAILABLE**.
