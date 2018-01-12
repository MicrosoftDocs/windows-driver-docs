---
title: Get Save Operation Requirements (Function Index 2)
description: This function returns information about hardware requirements for a save operation.
ms.assetid: 502DAF89-F390-40A4-846C-C3B4DF3E505D
---

# Get Save Operation Requirements (Function Index 2)


This function returns information about hardware requirements for a save operation. This function shall succeed for all NVDIMM-Ns that support a host-managed Energy Source (ES) policy, but may return a failure status if the device supports device-managed ES policy and save operation requirements are not available.

&gt; \[!Note\]   
&gt;All registers marked with a star (\*) are registers defined in the Byte Addressable Energy Backed Interface specification.

 

## <span id="Input"></span><span id="input"></span><span id="INPUT"></span>Input


### <span id="Arg3"></span><span id="arg3"></span><span id="ARG3"></span>Arg3

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
<td align="left"><p>This function can return the following Function-Specific Error Codes:</p>
<p>1: The NVDIMM-N does not report save operation requirements.</p>
<p>Go to [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md#dsm-method-output) for more information.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Average Power Requirement</strong></td>
<td align="left">2</td>
<td align="left">4</td>
<td align="left"><p>The average power (in milliwatts) required for the save operation.</p>
<p>*Byte 0 – <em>CSAVE_POWER_REQ0</em> (0, 0x29)</p>
<p>*Byte 1 – <em>CSAVE_POWER_REQ1</em> (0, 0x2A)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Idle Power Requirement</strong></td>
<td align="left">2</td>
<td align="left">6</td>
<td align="left"><p>The average power (in milliwatts) the module requires after the save operation completes.</p>
<p>*Byte 0 – <em>CSAVE_IDLE_POWER_REQ0</em> (0, 0x2B)</p>
<p>*Byte 1 – <em>CSAVE_IDLE_POWER_REQ1</em> (0, 0x2C)</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Minimum Voltage Requirement</strong></td>
<td align="left">2</td>
<td align="left">8</td>
<td align="left"><p>The minimum voltage (in millivolts) the ES has to service during a save operation</p>
<p>*Byte 0 – <em>CSAVE_MIN_VOLT_REQ0</em> (0, 0x2D)</p>
<p>*Byte 1 – <em>CSAVE_MIN_VOLT_REQ1</em> (0, 0x2E)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Maximum Voltage Requirement</strong></td>
<td align="left">2</td>
<td align="left">10</td>
<td align="left"><p>The maximum voltage (in millivolts) the ES has to service during a save operation</p>
<p>*Byte 0 – <em>CSAVE_MAX_VOLT_REQ0</em> (0, 0x2F)</p>
<p>*Byte 1 – <em>CSAVE_MAX_VOLT_REQ1</em> (0, 0x30)</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Get%20Save%20Operation%20Requirements%20%28Function%20Index%202%29%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





