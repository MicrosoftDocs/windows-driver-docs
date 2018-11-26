---
title: OID_WDI_TASK_CONNECT
description: OID_WDI_TASK_CONNECT requests that the IHV component connects to an Access Point or to a Wi-Fi Direct GO.
ms.assetid: 63ba3979-6b30-49bf-91a9-fa01f0ef4922
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_CONNECT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_CONNECT


OID\_WDI\_TASK\_CONNECT requests that the IHV component connects to an Access Point or to a Wi-Fi Direct GO.

| Object | Abort capable                                     | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. The abort must be followed by a dot11 reset. | 4                                     | 10                              |

 

As part of the connect, the IHV component must synchronize with, authenticate to, and associate to the BSS. The host provides the BSS entries that the IHV component can attempt to connect to. Once the IHV component has successfully connected to one of those entries, it should complete the connect process. If it is unable to connect to any of the BSS entries, it should complete the connect process with a failure.

The IHV component does not need to perform a scan to find candidate BSS entries. It can use the list provided by the host for the connect. It can attempt to connect to each one, one after another. The host sorts the networks by RSSI, but the IHV component can use its own order for connection. If the adapter does not specify "Connect BSS Selection Override", it must only use the entries provided by the host for the connect. The host may issue an abort on an outstanding connect. On receiving the abort, the port must end the connection attempts and report a completion to the host.

If the adapter specifies "Connect BSS Selection Override", it can perform scans on its own to find candidate BSS entries. It can connect to any BSS entry it finds as long as it meets the parameters configured by the host. It should optimize this selection to ensure that it meets any configured connection quality requirements. This could include optimizing roam scan, optimize AP selection, optimize association process, and minimize the security handshake needed. During a scan, if the device needs additional association parameters for a found BSS entry (for example, PMKID for roaming), it can send a [NDIS\_STATUS\_WDI\_INDICATION\_ASSOCIATION\_PARAMETERS\_REQUEST](ndis-status-wdi-indication-association-parameters-request.md) indication to get the parameters. When available, the host configures these parameters with [OID\_WDI\_SET\_ASSOCIATION\_PARAMETERS](oid-wdi-set-association-parameters.md).

If the connect fails or is aborted, the port should not reset any settings that may have been configured outside of the connect command. It must support the host issuing a second connect call on the same port.

The status of the connect attempt for each BSS entry must be reported by the port at the end of the association attempt. This includes the successful attempt and also any failed attempts. At any time, the port must be associated with no more than one Access Point or Wi-Fi Direct GO.

While a connect is ongoing, the port must maintain any connections established on other ports (for example, Infrastructure or Wi-Fi Direct). However, the port may reduce the amount of medium access provided to the other ports to finish the connection. During the connect, the host can submit packet send requests on other ports.

If the authentication algorithm that is used for the connection requires 802.1x port authorization for network access, the host authorizes the port after the association operation has completed successfully.

The 802.11 station uses the PMKID cache for pre-authentication to access points that have enabled the Robust Security Network Association (RSNA) authentication algorithm. If the 802.11 station is associating or reassociating to a BSSID that has a provided PMKID, the 802.11 station must use the PMKID data in the RSN information element (RSN IE) of its Association or Reassociation frame.

If the port declares support for Host FIPS mode in [**WDI\_TLV\_STATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/dn898066), HostFIPSModeEnabled may be set to 1 in the connection parameters.

If HostFIPSModeEnabled is set to 1, the following rules apply.

-   The port must follow the guidelines for sending/receiving data frames in Send operations in FIPS mode and Receive operations in FIPS mode.
-   The port must not declare support for any QoS protocol in the association request sent to a non-HT access point. QoS support is required for HT connections.
-   The port must not negotiate TSpec and must not perform transmit MSDU aggregation.
-   The port must ensure that the SPP A-MSDU capable bit (bit 10) of the RSN capabilities IE it transmits is set to zero. Only PP A-MSDU are supported in this mode.

The connection parameters must not have MFPEnabled and HostFIPSModeEnabled both set to 1. Management Frame Protection (802.11w) requires the port to encrypt/decrypt certain management and action frames, so it cannot be enabled for a connection using Host FIPS mode. In addition, Wake on Wireless LAN features are not applicable in Host-FIPS mode.

## Task parameters


| TLV                                                                      | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|--------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_CONNECT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn926266) |                                |          | The connection parameters.                                                                                                                                                                                                                                                                                                                                                                                   |
| [**WDI\_TLV\_CONNECT\_BSS\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/dn926264)  | X                              |          | The preferred list of candidate connect BSS entries. The port should attempt to connect to any of these BSS entries until the list is exhausted or the connection completed successfully. The port can reprioritize the entries if needed. If the adapter has set the Connect BSS Selection Override bit, then it can pick a BSS that is not in this list as long as it follows the Allowed/Disallowed list. |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_CONNECT\_COMPLETE](ndis-status-wdi-indication-connect-complete.md)
## Unsolicited indication


[NDIS\_STATUS\_WDI\_INDICATION\_ASSOCIATION\_RESULT](ndis-status-wdi-indication-association-result.md)
Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 




