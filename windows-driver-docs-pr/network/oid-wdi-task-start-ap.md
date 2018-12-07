---
title: OID_WDI_TASK_START_AP
description: OID_WDI_TASK_START_AP requests that the IHV component configures a port to start a Wi-Fi Direct Group Owner on the specified port.
ms.assetid: 647b039b-eb9a-43e7-9027-15a55df62c79
ms.date: 07/18/2017
keywords:
 - OID_WDI_TASK_START_AP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_START\_AP


OID\_WDI\_TASK\_START\_AP requests that the IHV component configures a port to start a Wi-Fi Direct Group Owner on the specified port.

| Object | Abort capable                                     | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. The abort must be followed by a dot11 reset. | 4                                     | 1                               |

 

During initialization, the driver sets the GO on 5GHz band capability in [**WDI\_TLV\_P2P\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/dn897865) to indicate whether it can start the access point on the 5 GHz band.

If GO on 5 GHz band support is set, the adapter should start the AP on the Advertised Operating channel, and if that fails, it should try the list specified in the AP band channel list parameter. The operating system will provide a hint to the driver about whether this AP would provide internet connectivity by setting the **DOT11\_WFD\_GROUP\_CAPABILITY\_CROSS\_CONNECTION\_SUPPORTED** flag in [**WDI\_TLV\_P2P\_GROUP\_OWNER\_CAPABILITY**](https://msdn.microsoft.com/library/windows/hardware/dn897954).

If **MustUseSpecifiedChannel** in [**WDI\_TLV\_START\_AP\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/dn898065) is specified, the AP may return one of the following errors if it is unable to start the AP on the specified band/channel(s).

|                                                                 |                                                                                                         |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **NDIS\_STATUS\_DOT11\_AP\_CHANNEL\_CURRENTLY\_NOT\_AVAILABLE** | Unable to start the AP on the specified channel(s) right now . Retry on the specified channel(s) later. |
| **NDIS\_STATUS\_DOT11\_AP\_BAND\_CURRENTLY\_NOT\_AVAILABLE**    | Unable to start the AP on the specified band(s) right now. Retry on the specified band(s) later.        |
| **NDIS\_STATUS\_DOT11\_AP\_CHANNEL\_NOT\_ALLOWED**              | Unable to start the AP on the specified channel(s) due to regulatory reasons.                           |
| **NDIS\_STATUS\_DOT11\_AP\_BAND\_NOT\_ALLOWED**                 | Unable to start the AP on the specified band(s) due to regulatory reasons.                              |

 

## Task parameters


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>TLV</th>
<th>Multiple TLV instances allowed</th>
<th>Optional</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898062" data-raw-source="[&lt;strong&gt;WDI_TLV_SSID&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898062)"><strong>WDI_TLV_SSID</strong></a></td>
<td></td>
<td></td>
<td>The SSID to be used by the AP.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898065" data-raw-source="[&lt;strong&gt;WDI_TLV_START_AP_PARAMETERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898065)"><strong>WDI_TLV_START_AP_PARAMETERS</strong></a></td>
<td></td>
<td></td>
<td>Additional parameters for this task.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn926141" data-raw-source="[&lt;strong&gt;WDI_TLV_AUTH_ALGO_LIST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn926141)"><strong>WDI_TLV_AUTH_ALGO_LIST</strong></a></td>
<td></td>
<td></td>
<td>The list of authentication algorithms that the connection can use.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn897847" data-raw-source="[&lt;strong&gt;WDI_TLV_MULTICAST_CIPHER_ALGO_LIST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn897847)"><strong>WDI_TLV_MULTICAST_CIPHER_ALGO_LIST</strong></a></td>
<td></td>
<td></td>
<td>The list of multicast cipher algorithms that the connection can use.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn898074" data-raw-source="[&lt;strong&gt;WDI_TLV_UNICAST_CIPHER_ALGO_LIST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn898074)"><strong>WDI_TLV_UNICAST_CIPHER_ALGO_LIST</strong></a></td>
<td></td>
<td></td>
<td>The list of multicast cipher algorithms that the connection can use.</td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/dn897869" data-raw-source="[&lt;strong&gt;WDI_TLV_P2P_CHANNEL_NUMBER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/dn897869)"><strong>WDI_TLV_P2P_CHANNEL_NUMBER</strong></a></td>
<td></td>
<td>X</td>
<td>If specified, this defines the operating channel determined in group formation. This may only be specified when the operating mode is Wi-Fi Direct GO.</td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/mt593242" data-raw-source="[&lt;strong&gt;WDI_TLV_AP_BAND_CHANNEL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/mt593242)"><strong>WDI_TLV_AP_BAND_CHANNEL</strong></a></td>
<td>X</td>
<td>X</td>
<td>Added in Windows 10, version 1511, WDI version 1.0.10.
<p>Optional list of bands and channels to start the access point on. If MustUseSpecifiedChannels is set to 1, the AP can only be started from this list. If it is not set, this list is meant to be a recommendation of channels that the firmware can pick from, and it may pick another channel if it is not possible to start the AP on any of the specified channels.</p></td>
</tr>
</tbody>
</table>

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_START\_AP\_COMPLETE](ndis-status-wdi-indication-start-ap-complete.md)
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

 

 




