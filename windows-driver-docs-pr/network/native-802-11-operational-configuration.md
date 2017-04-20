---
title: Native 802.11 Operational Configuration
description: Native 802.11 Operational Configuration
ms.assetid: f83ed82a-2aa8-4ec6-92c1-4f694ca0f2af
keywords:
- configurations WDK Native 802.11 , querying and setting attributes
- querying Native 802.11 configuration attributes
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Operational Configuration


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The following object identifiers (OIDs) set or query the operating attributes of the Native 802.11 miniport driver.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[OID_DOT11_ATIM_WINDOW](https://msdn.microsoft.com/library/windows/hardware/ff569105)</p></td>
<td align="left"><p>Queries or sets the value of the announcement traffic information message (ATIM) window. The ATIM window is a short period of time immediately following the transmission of each 802.11 Beacon frame in an independent basic service set (IBSS) network.</p>
<div class="alert">
<strong>Note</strong>  IBSS (Ad hoc) and SoftAP are deprecated. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](wi-fi-direct-miniport-initialization-and-configuration.md).
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_CURRENT_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569125)</p></td>
<td align="left"><p>Queries the MAC address that the 802.11 station is currently using. This MAC address could either be the NIC's permanent address, which is queried through [OID_DOT11_PERMANENT_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569399), or a locally administered address.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_CURRENT_OPERATION_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569132)</p></td>
<td align="left"><p>Queries or sets the Native 802.11 operation mode of the miniport driver. For more information about these operation modes, see [Native 802.11 Operation Modes](native-802-11-operation-modes.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_CURRENT_OPTIONAL_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569133)</p></td>
<td align="left"><p>Queries the state of the optional wireless LAN (WLAN) capabilities, such as Point Coordination Function (PCF), that are supported by the 802.11 station.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_DATA_RATE_MAPPING_TABLE](https://msdn.microsoft.com/library/windows/hardware/ff569139)</p></td>
<td align="left"><p>Queries the table of data rates supported by a PHY on the 802.11 station for transmit and receive operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_MAXIMUM_LIST_SIZE](https://msdn.microsoft.com/library/windows/hardware/ff569382)</p></td>
<td align="left"><p>Queries the maximum number of multicast addresses that are supported by the 802.11 station.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_MPDU_MAX_LENGTH](https://msdn.microsoft.com/library/windows/hardware/ff569387)</p></td>
<td align="left"><p>Queries the maximum length, in bytes, of a MAC protocol data unit (MPDU) frame that the PHY can transmit or receive.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_MULTICAST_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569388)</p></td>
<td align="left"><p>Sets or queries the multicast address list used by the 802.11 station.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_NIC_POWER_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569392)</p></td>
<td align="left"><p>Sets or queries the power state of the PHY on the 802.11 station.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_NIC_SPECIFIC_EXTENSION](https://msdn.microsoft.com/library/windows/hardware/ff569393)</p></td>
<td align="left"><p>The independent hardware vendor (IHV) uses this OID for proprietary method requests for its miniport driver. For more information about the use of OID_DOT11_NIC_SPECIFIC_EXTENSION, see [IHV Configuration Extensions](ihv-configuration-extensions.md).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_OPERATION_MODE_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569396)</p></td>
<td align="left"><p>Queries the Native 802.11 operation modes that the miniport driver supports. For more information about these operation modes, see [Native 802.11 Operation Modes](native-802-11-operation-modes.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_OPTIONAL_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569397)</p></td>
<td align="left"><p>Queries the optional WLAN capabilities that the 802.11 station supports.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_PERMANENT_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569399)</p></td>
<td align="left"><p>Queries the permanent MAC address used by the 802.11 station. This MAC address is typically encoded in the NIC hardware.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_RECV_SENSITIVITY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569407)</p></td>
<td align="left"><p>Queries the list of receive sensitivity ranges for all data rates that are supported by the PHY specified in the query request.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_RESET_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409)</p></td>
<td align="left"><p>When a method request of this OID is made, the miniport driver must reset the specified IEEE layers of the 802.11 station. After OID_DOT11_RESET_REQUEST is set, the driver must transition to the initialization (INIT) state of the current Native 802.11 operation mode. For more information about operation modes and states, see [Native 802.11 Operation Modes](native-802-11-operation-modes.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_RF_USAGE](https://msdn.microsoft.com/library/windows/hardware/ff569410)</p></td>
<td align="left"><p>Queries the radio frequency (RF) usage detected on the wireless media by the PHY on the 802.11 station.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_SCAN_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413)</p></td>
<td align="left"><p>When set, this OID requests that the 802.11 station perform a survey of all basic service set (BSS) networks within range of the NIC's radio.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_SUPPORTED_DATA_RATES_VALUE](https://msdn.microsoft.com/library/windows/hardware/ff569422)</p></td>
<td align="left"><p>Queries the transmit and receive data rates supported by the Physical Layer Convergence Procedure (PLCP) and Physical Media Dependent (PMD) sublayer of the PHY.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_SUPPORTED_PHY_TYPES](https://msdn.microsoft.com/library/windows/hardware/ff569426)</p></td>
<td align="left"><p>Queries the list of PHY types that are supported by the 802.11 station.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_SUPPORTED_POWER_LEVELS](https://msdn.microsoft.com/library/windows/hardware/ff569427)</p></td>
<td align="left"><p>Queries the number of transmit power levels supported by the Physical Media Dependent (PMD) sublayer of the PHY, and the transmit power for all the supported levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_SUPPORTED_RX_ANTENNA](https://msdn.microsoft.com/library/windows/hardware/ff569428)</p></td>
<td align="left"><p>Queries the list of antennas on the 802.11 station that support receive (RX) operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_SUPPORTED_TX_ANTENNA](https://msdn.microsoft.com/library/windows/hardware/ff569429)</p></td>
<td align="left"><p>Queries the list of antennas on the 802.11 station that support transmit (TX) operations.</p></td>
</tr>
</tbody>
</table>

 

If the miniport driver is operating in Extensible Station (ExtSTA) mode, it must support additional OIDs for the set or query of the ExtSTA operating attributes. For more information about these OIDs, see [Extensible Station Operational Configuration](extensible-station-operational-configuration.md).

 

 





