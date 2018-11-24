---
title: Get Energy Source Identification (Function Index 3)
description: This function returns identification information about the Energy Source (ES), which can be host-managed or device-managed.
ms.assetid: E1589FD0-5D03-42EF-8078-0AE53CFB1ACA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Get Energy Source Identification (Function Index 3)


This function returns identification information about the Energy Source (ES), which can be host-managed or device-managed.

&gt; \[!Note\]   
&gt;All registers marked with a star (\*) are registers defined in the Byte Addressable Energy Backed Interface specification.



## <span id="Input"></span><span id="input"></span><span id="INPUT"></span>Input


### <span id="Args3"></span><span id="args3"></span><span id="ARGS3"></span>Args3

None.

## <span id="Output"></span><span id="output"></span><span id="OUTPUT"></span>Output


<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Byte Length</th>
<th align="left">Byte Offset</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>Status</strong></td>
<td align="left">4</td>
<td align="left">0</td>
<td align="left"><p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for information.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Energy Source Policy</strong></td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left"><p>Information regarding the Energy Source policy supported by the module.</p>
<p>*Byte 0 – <em>ENERGY_SOURCE_POLICY</em> (0, 0x14)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Device-Managed ES Identification</strong></td>
<td align="left">11</td>
<td align="left">5</td>
<td align="left">&amp;gt; [!Note]<br/><p>&amp;gt;This field contains valid data only if the current ES policy is device-managed (i.e. bit 2 of SET_ES_POLICY_STATUS (0, 0x70) is set). For all other ES policies, this field shall be 0.</p>

<p>See Device-Managed ES Identification for information.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Host-Managed ES Identification</strong></td>
<td align="left">3</td>
<td align="left">16</td>
<td align="left">&amp;gt; [!Note]<br/><p>&amp;gt;This field contains valid data only if the current ES policy is host-managed (i.e. bit 3 of SET_ES_POLICY_STATUS (0, 0x70) is set). For all other ES policies, this field shall be 0.</p>

<p>See Host-Managed ES Identification for information.</p></td>
</tr>
</tbody>
</table>



### <span id="Device_Managed_ES_Identification"></span><span id="device_managed_es_identification"></span><span id="DEVICE_MANAGED_ES_IDENTIFICATION"></span>Device-Managed ES Identification

If the value of ES policy is 0, the Device-Managed ES Identification field is valid and has the following fields:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Byte Length</th>
<th align="left">Byte Offset</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>ES Hardware Revision</strong></td>
<td align="left">2</td>
<td align="left">5</td>
<td align="left"><p>The ES hardware revision.</p>
<p><em>Byte 0 – <em>ES_HWREV</em> (1, 0x04)</p>
<p>Byte 1 - Reserved.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>ES Firmware Revision</strong></td>
<td align="left">2</td>
<td align="left">7</td>
<td align="left"><p>The ES firmware revision.</p>
<p></em>Byte 0 – <em>ES_FWREV0</em> (1, 0x06)</p>
<p><em>Byte 1 – <em>ES_FWREV1</em> (1, 0x07)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>ES Health Check Frequency</strong></td>
<td align="left">1</td>
<td align="left">9</td>
<td align="left"><p>The current frequency of the module&#39;s ES health assessment.</p>
<p></em>Byte 0 – <em>AUTO_ES_HEALTH_CHECK_FREQUENCY</em> (0, 0xA9)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>ES Charge Timeout</strong></td>
<td align="left">2</td>
<td align="left">10</td>
<td align="left"><p>The worst case (in seconds) ES charge time. The value shall be greater than 0.</p>
<p><em>Byte 0 – <em>ES_CHARGE_TIMEOUT0</em> (1, 0x10)</p>
<p></em>Byte 1 – <em>ES_CHARGE_TIMEOUT1</em> (1, 0x11)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>ES Minimum Operating Temperature</strong></td>
<td align="left">1</td>
<td align="left">12</td>
<td align="left"><p>The minimum operating temperature (in degrees Celsius) of the ES. The minimum value supported shall be 0.</p>
<p><em>Byte 0 – <em>MIN_ES_OPERATING_TEMP</em> (1, 0x12)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>ES Maximum Operating Temperature</strong></td>
<td align="left">1</td>
<td align="left">13</td>
<td align="left"><p>The maximum operating temperature (in degrees Celsius) of the ES.</p>
<p></em>Byte 0 – <em>MAX_ES_OPERATING_TEMP</em> (1, 0x13)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>ES Attributes</strong></td>
<td align="left">1</td>
<td align="left">14</td>
<td align="left"><p>Attributes regarding the ES.</p>
<p><em>Byte 0 – <em>ES_ATTRIBUTES</em> (1, 0x14)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>ES Technology</strong></td>
<td align="left">1</td>
<td align="left">15</td>
<td align="left"><p>The technology used in the ES.</p>
<p></em>Byte 0 – <em>ES_TECH</em> (1, 0x15)</p></td>
</tr>
</tbody>
</table>



### <span id="Host_Managed_ES_Identification"></span><span id="host_managed_es_identification"></span><span id="HOST_MANAGED_ES_IDENTIFICATION"></span>Host-Managed ES Identification

If the value of ES policy is 1, the Host-Managed ES Identification field is valid and has the following fields:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Byte Length</th>
<th align="left">Byte Offset</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>ES Health Check Frequency</strong></td>
<td align="left">1</td>
<td align="left">16</td>
<td align="left"><p>The current frequency of the platform&#39;s ES health assessment.</p>
<p><em>Byte 0 – <em>AUTO_ES_HEALTH_FREQUENCY</em> (0, 0xA9).</p></td>
</tr>
<tr class="even">
<td align="left"><strong>ES Attributes</strong></td>
<td align="left">1</td>
<td align="left">17</td>
<td align="left"><p>Attributes for the host-managed Energy Source.</p>
<p></em>Byte 0 – <em>HOST_MANAGED_ES_ATTRIBUTES</em> (2, 0x82)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>ES Technology</strong></td>
<td align="left">1</td>
<td align="left">18</td>
<td align="left"><p>Bitmask:</p>
<ul>
<li><p>[0] : Undefined</p></li>
<li><p>[1] : Supercapacitor</p></li>
<li><p>[2] : Battery</p></li>
<li><p>[3] : Hybrid capacitor</p></li>
<li><p>[7:4] Reserved</p></li>
</ul></td>
</tr>
</tbody>
</table>



## <span id="related_topics"></span>Related topics


[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)










