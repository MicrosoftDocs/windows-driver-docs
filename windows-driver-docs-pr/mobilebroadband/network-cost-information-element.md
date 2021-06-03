---
title: Network cost information element
description: Network cost information element
ms.date: 05/31/2021
ms.localizationpriority: medium
---

# Network cost information element


To communicate the cost of the Wi-Fi network to clients, Microsoft has defined a vendor extension to the 802.11 protocol. This extension is the Network Cost IE.

**Note**  
The 802.11 protocol allows vendor-defined information elements (IEs), and requires clients that do not understand a particular IE to ignore it and continue processing the remaining IEs. This minimizes the compatibility risk of adding a new IE to products that interact with existing clients of other operating system types.

 

The following table shows the Network Cost IE format:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Field name</th>
<th>Size (octets)</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Attribute ID</p></td>
<td><p>1</p></td>
<td><p>0xDD</p></td>
<td><p>Type (vendor extension)</p></td>
</tr>
<tr class="even">
<td><p>Length</p></td>
<td><p>1</p></td>
<td><p>0x08</p></td>
<td><p>Length of the following fields</p></td>
</tr>
<tr class="odd">
<td><p>Organizationally Unique Identifier (OUI)</p></td>
<td><p>3</p></td>
<td><p>0x00, 0x50, 0xF2</p></td>
<td><p>Vendor (Microsoft)</p></td>
</tr>
<tr class="even">
<td><p>OUI Type</p></td>
<td><p>1</p></td>
<td><p>0x11</p></td>
<td><p>OUI type (network cost)</p></td>
</tr>
<tr class="odd">
<td><p>Cost Level</p></td>
<td><p>1</p></td>
<td><p>Exactly one of <b>Cost Level</b> values. See below.</p></td>
<td><p>Cost Level. One of exact values.</p></td>
</tr>
<tr class="even">
<td><p>RESERVED</p></td>
<td><p>1</p></td>
<td><p>0x00</p></td>
<td><p>Reserved. Should be 0x00</p></td>
</tr>
<tr class="odd">
<td><p>Cost Flags</p></td>
<td><p>1</p></td>
<td><p>OR'ed <b>Cost Flags</b>. See below.</p></td>
<td><p>Cost Flags. Can be OR'ed</p></td>
</tr>
<tr class="even">
<td><p>RESERVED</p></td>
<td><p>1</p></td>
<td><p>0x00</p></td>
<td><p>Reserved. Should be 0x00</p></td>
</tr>
</tbody>
</table>

The following table shows the possible <b>Cost Level</b> bits (exactly one is required):

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0x00</p></td>
<td><p>Unknown</p></td>
<td><p>The usage is unknown or unrestricted.</p></td>
</tr>
<tr class="even">
<td><p>0x01</p></td>
<td><p>Unrestricted</p></td>
<td><p>No incremental cost applies for transferring data on this connection.</p></td>
</tr>
<tr class="odd">
<td><p>0x02</p></td>
<td><p>Fixed</p></td>
<td><p>
  Data transfer is metered and counts against a data limit. No difference in cost applies within this limit.<br>
  When this value is set, Windows clients automatically treat connection as metered.
</p></td>
</tr>
<tr class="even">
<td><p>0x04</p></td>
<td><p>Variable</p></td>
<td><p>
  Incremental cost applies for all usage on this link.
  When this value is set, Windows clients automatically treat connection as metered.
</p></td>
</tr>
</tbody>
</table>

 

The following tables shows the possible <b>Cost flag</b> bits. Those values MAY be or'ed

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0x00</p></td>
<td><p>The connection cost is unknown.</p></td>
<td><p></p></td>
</tr>
<tr class="even">
<td><p>0x01</p></td>
<td><p>Over Data Limit</p></td>
<td><p>Usage has exceeded the data limit of the metered network; different network costs or conditions might apply.</p></td>
</tr>
<tr class="odd">
<td><p>0x02</p></td>
<td><p>Congested</p></td>
<td><p>The network operator is experiencing or expecting heavy load.</p></td>
</tr>
<tr class="even">
<td><p>0x04</p></td>
<td><p>Roaming</p></td>
<td><p>The tethering connection is roaming outside the provider's home network or affiliates.</p></td>
</tr>
<tr class="odd">
<td><p>0x08</p></td>
<td><p>Approaching Data Limit</p></td>
<td><p>Usage is near the data limit of the metered network; different network costs or conditions might apply once the limit is reached.</p></td>
</tr>
</tbody>
</table>

The following table shows some sample cost attribute values (last four bytes of IE):

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Default WLAN</p></td>
<td><p>0x01, 0x00, 0x00, 0x00</p></td>
<td><p>Unrestricted connection; standard WLAN backed by fixed broadband.</p></td>
</tr>
<tr class="even">
<td><p>Portable Hotspot Default</p></td>
<td><p>0x02, 0x00, 0x00, 0x00</p></td>
<td><p>Metered network; limit unknown or not yet reached; matches Windows default for mobile broadband connections.</p></td>
</tr>
<tr class="odd">
<td><p>Over Limit / Throttled</p></td>
<td><p>0x01, 0x00, 0x01, 0x00</p></td>
<td><p>User has exceeded data limit; speed is reduced, but no further usage limitation applies.</p></td>
</tr>
<tr class="even">
<td><p>Over Limit / Charges</p></td>
<td><p>0x04, 0x00, 0x01, 0x00</p></td>
<td><p>User has exceeded data limit; additional usage incurs incremental charges.</p></td>
</tr>
<tr class="odd">
<td><p>Portable Hotspot / Roaming</p></td>
<td><p>0x04, 0x00, 0x04, 0x00</p></td>
<td><p>Connection is roaming; incremental charges apply due to network state.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Add_network_cost_support_to_your_device"></span><span id="add_network_cost_support_to_your_device"></span><span id="ADD_NETWORK_COST_SUPPORT_TO_YOUR_DEVICE"></span>Add network cost support to your device


1.  Add the IE to your device’s WLAN beacon and probe response, which is fixed to the **Portable Hotspot Default** value shown in the table with the sample cost attribute values. Verify that a Windows 8, Windows 8.1, or Windows 10 computer that connects to this network automatically selects the **Reduce network usage** option for this network.

2.  When roaming, replace the default value with the **Portable Hotspot / Roaming** value that is listed in the table with the sample cost attribute values.

3.  Optionally, work with your partner carriers to determine cases where other values may be appropriate, such as the following:

    -   Unrestricted while on certain bearers (LTE, HSPA+, etc.),

    -   Defined channel to detect over-limit states.

    -   Operator-defined behavior when past data limit.

4.  Optionally, if your device can use Wi-Fi as a second-hop network, check for this IE on the network to which you connect and relay its value (or its absence) to your own SSID. If none is present, use the **Default WLAN** value that is listed in the table with the sample cost attribute values.

## <span id="related_topics"></span>Related topics


[Communication channels](communication-channels.md)

[[MS-NCT] Network Cost Transfer protocol documentation](/openspecs/windows_protocols/ms-nct/7c4adf77-f13b-43aa-8491-637ef4543d96)

 

 






