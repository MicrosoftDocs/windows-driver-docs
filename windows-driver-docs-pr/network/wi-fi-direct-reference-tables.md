---
title: Wi-Fi Direct Reference Tables
description: WI-FI DIRECT OIDS.
ms.assetid: 5111D62E-275B-4B1E-8670-FBE81C37FE46
---

# Wi-Fi Direct Reference Tables


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

**WI-FI DIRECT OIDS**

The table below lists the various Operation Modes that Wi-Fi Direct OID Query (Q) and Set (S) requests are valid for. Direct OIDs are Set Only and are marked as D.

**OID**

**DEVICE**

**GROUP OWNER**

**CLIENT**

**INIT**

**INIT**

**OP**

**INIT**

**OP**

[OID\_DOT11\_WFD\_DEVICE\_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451792)

S

S

S

S

S

[OID\_DOT11\_WFD\_GROUP\_OWNER\_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451799)

-

S

S

-

-

[OID\_DOT11\_WFD\_DEVICE\_INFO](https://msdn.microsoft.com/library/windows/hardware/hh451793)

S

S

-

S

-

[OID\_DOT11\_WFD\_DEVICE\_LISTEN\_CHANNEL](https://msdn.microsoft.com/library/windows/hardware/hh738803)

S,Q

-

-

-

-

[OID\_DOT11\_WFD\_SECONDARY\_DEVICE\_TYPE\_LIST](https://msdn.microsoft.com/library/windows/hardware/hh451802)

S

S

S

S

S

[OID\_DOT11\_WFD\_ADDITIONAL\_IE](https://msdn.microsoft.com/library/windows/hardware/hh451790)

S

S

S

S

S

[OID\_DOT11\_WFD\_DISCOVER\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451795)

S

-

-

-

-

[OID\_DOT11\_WFD\_STOP\_DISCOVERY](https://msdn.microsoft.com/library/windows/hardware/hh738804)

S

-

-

-

-

[OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST](https://msdn.microsoft.com/library/windows/hardware/hh451796)

Q

-

-

-

-

[OID\_DOT11\_WFD\_LISTEN\_STATE\_DISCOVERABILITY](https://msdn.microsoft.com/library/windows/hardware/hh451801)

S,Q

-

-

-

-

[OID\_DOT11\_WFD\_FLUSH\_DEVICE\_LIST](https://msdn.microsoft.com/library/windows/hardware/hh451797)

S

-

-

-

-

[OID\_DOT11\_WFD\_GET\_DIALOG\_TOKEN](https://msdn.microsoft.com/library/windows/hardware/hh451798)

Q

-

-

-

-

[OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451804)

S

-

-

-

-

[OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_RESPONSE](https://msdn.microsoft.com/library/windows/hardware/hh451805)

D

-

-

-

-

[OID\_DOT11\_WFD\_SEND\_GO\_NEGOTIATION\_CONFIRMATION](https://msdn.microsoft.com/library/windows/hardware/hh451803)

D

-

-

-

-

[OID\_DOT11\_WFD\_SEND\_INVITATION\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451806)

S

-

-

-

-

[OID\_DOT11\_WFD\_SEND\_INVITATION\_RESPONSE](https://msdn.microsoft.com/library/windows/hardware/hh451807)

D

-

-

-

-

[OID\_DOT11\_WFD\_SEND\_PROVISION\_DISCOVERY\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh464156)

S

-

-

-

-

[OID\_DOT11\_WFD\_SEND\_PROVISION\_DISCOVERY\_RESPONSE](https://msdn.microsoft.com/library/windows/hardware/hh451808)

D

-

-

-

-

[OID\_DOT11\_WFD\_DESIRED\_GROUP\_ID](https://msdn.microsoft.com/library/windows/hardware/hh451791)

-

S

-

S

-

[OID\_DOT11\_WFD\_START\_GO\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451809)

-

S

-

-

-

[OID\_DOT11\_WFD\_CONNECT\_TO\_GROUP\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh464154)

-

-

-

S

-

[OID\_DOT11\_WFD\_DISCONNECT\_FROM\_GROUP\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451794)

-

-

-

-

S

[OID\_DOT11\_WFD\_GROUP\_START\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451800)

-

S

-

-

-

[OID\_DOT11\_WFD\_GROUP\_JOIN\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh464155)

-

-

-

S

-

 

**ExtSTA OIDs Applied to Wi-Fi Direct Client Mode**

The following Extensible Station OIDs/Indications/Data Types have been replaced with new OIDs when operating in Wi-Fi Direct Client mode. The miniport driver need not support these ExtSTA OIDs/Indications/Data Types when operating in Wi-Fi Direct Client mode.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>ExtSTA OID/Indication/Data Type</strong></p></td>
<td align="left"><p><strong>Wi-Fi Direct Group Owner OID/Indication/Data Type</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_CONNECT_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569122)</p></td>
<td align="left"><p>[OID_DOT11_WFD_CONNECT_TO_GROUP_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh464154)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_DISCONNECT_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569147)</p></td>
<td align="left"><p>[OID_DOT11_WFD_DISCONNECT_FROM_GROUP_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451794)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_DESIRED_SSID_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569145)</p></td>
<td align="left"><p>[OID_DOT11_WFD_DESIRED_GROUP_ID](https://msdn.microsoft.com/library/windows/hardware/hh451791)</p></td>
</tr>
</tbody>
</table>

 

The table below lists additional Extensible Station OIDs /Indications/Data Types that are not valid in Wi-Fi Direct Client Operation Mode

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>OIDs, NDIS_STATUS_INDICATIONs and Data Types</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_AUTO_CONFIG_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569106)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_ENUM_BSS_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569360)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_EXTSTA_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569366)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_FLUSH_BSS_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569367)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_HIDDEN_NETWORK_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569371)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_IBSS_PARAMS](https://msdn.microsoft.com/library/windows/hardware/ff569378)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_SAFE_MODE_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569412)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_SCAN_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413)</p></td>
</tr>
</tbody>
</table>

 

The miniport driver must support all the other mandatory ExtSTA OIDs and Indications when operating in Wi-Fi Direct Client mode.

**ExtAP OIDs Applied to Wi-Fi Direct GO Mode**

The following Extensible Access Point OIDs/Indications/Data Types have been replaced with new OIDs when operating in Wi-Fi Direct Group Owner Mode. The miniport driver need not support these ExtAP OIDs/Indications/Data Types when operating in Wi-Fi Direct Group Owner Mode.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>ExtAP OID/Indication/Data Type</strong></p></td>
<td align="left"><p><strong>Wi-Fi Direct Group Owner OID/Indication/Data Type</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_START_AP_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569418)</p></td>
<td align="left"><p>[OID_DOT11_WFD_START_GO_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451809)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_DESIRED_SSID_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569145)</p></td>
<td align="left"><p>[OID_DOT11_WFD_DESIRED_GROUP_ID](https://msdn.microsoft.com/library/windows/hardware/hh451791)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_ADDITIONAL_IE](https://msdn.microsoft.com/library/windows/hardware/ff569103)</p></td>
<td align="left"><p>[OID_DOT11_WFD_ADDITIONAL_IE](https://msdn.microsoft.com/library/windows/hardware/hh451790)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>DOT11_INCOMING_ASSOC_DECISION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548654)</p></td>
<td align="left"><p>[<strong>DOT11_INCOMING_ASSOC_DECISION_V2</strong>](https://msdn.microsoft.com/library/windows/hardware/hh406480)</p></td>
</tr>
</tbody>
</table>

 

The table below lists additional Extensible Access Point OIDs /Indications/Data Types that are not valid in Wi-Fi Direct Group Owner Operation Mode.

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>OIDs, NDIS_STATUS_INDICATIONs and Data Types</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_AUTO_CONFIG_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569106)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_ENUM_BSS_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569360)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[OID_DOT11_FLUSH_BSS_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569367)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[OID_DOT11_SCAN_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569413)</p></td>
</tr>
</tbody>
</table>

 

The miniport driver must support all the other mandatory ExtAP OIDs and Indications when operating in Wi-Fi Direct Group Owner mode.

 

 





