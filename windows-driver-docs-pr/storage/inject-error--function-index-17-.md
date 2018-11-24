---
title: Inject Error (Function Index 17)
description: This function injects errors in the NVDIMM-N module firmware. The purpose of this function is to enable software validation.
ms.assetid: 4D77DC95-25BC-4D28-83B7-7A62383803E6
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Inject Error (Function Index 17)


This function injects errors in the NVDIMM-N module firmware. The purpose of this function is to enable software validation. The platform may choose to only enable error injection in specific scenarios, e.g. after the user configures a BIOS setting. The host may call [Query Error Injection Status (Function Index 16)](query-error-injection-status--function-index-16-.md) to learn whether or not the error injection functions are enabled.

&gt; \[!Note\]   
&gt;All registers marked with a star (\*) are registers defined in the Byte Addressable Energy Backed Interface specification.

 

## <span id="Input"></span><span id="input"></span><span id="INPUT"></span>Input


### <span id="Args3"></span><span id="args3"></span><span id="ARGS3"></span>Args3

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
<td align="left"><strong>Inject Operation Failures</strong></td>
<td align="left">2</td>
<td align="left">0</td>
<td align="left"><p>Specifies which operation or non-volatile memory errors will be injected.</p>
<p><em>Byte 0 – <em>INJECT_OPS_FAILURES</em> (2, 0x60)</p>
<p></em>Byte 1 – If <em>INJECT_BAD_BLOCKS</em> is 1 (bit 7 of Byte 0), this is <em>INJECT_BAD_BLOCK_CAP</em> (2, 0x67). Otherwise, it shall be 0.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>Inject Energy Source Failures</strong></td>
<td align="left">1</td>
<td align="left">2</td>
<td align="left"><p>Specifies which Energy Source (ES) errors will be injected.</p>
<p><em>Byte 0 – <em>INJECT_ES_FAILURES</em> (2, 0x64)</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>Inject Firmware Update Failures</strong></td>
<td align="left">1</td>
<td align="left">3</td>
<td align="left"><p>Specifies which firmware operation errors will be injected.</p>
<p></em>Byte 0 – <em>INJECT_FW_FAILURES</em> (2, 0x65)</p></td>
</tr>
</tbody>
</table>

 

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
<p>1: Error injection is disabled.</p>
<p>2: One or more errors could not be injected because they are not supported.</p>
<p>Go to <a href="-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md" data-raw-source="[_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)">_DSM Method Output</a> for more information.</p></td>
</tr>
</tbody>
</table>

 

&gt; \[!Note\]   
&gt;Any errors that were successfully injected will remain injected when returning Function-Specific Error Code 2. If this function returns the Function-Specific Error Code 2, call [Get Injected Errors (Function Index 18)](get-injected-errors--function-index-18-.md) to retrieve which errors could not be injected.

 

## <span id="Remarks"></span><span id="remarks"></span><span id="REMARKS"></span>Remarks


Some error injection features are optional and may not be supported by the device. Please refer to the appropriate Byte Addressable Energy Backed Interface JEDEC specification for the list of optional error injections.

The platform must detect if the host attempted to inject an error that is not supported. It does that by writing to the error injection register and then reading the same register & verifying whether or not all the intended bits are set. For example, the platform does the following to inject operational failures:

1.  Writes the value of Byte 0 of the **Inject Operation Failures** field to the *INJECT\_OPS\_FAILURES* register.

2.  Reads the *INJECT\_OPS\_FAILURES* register.

3.  If the new value of *INJECT\_OPS\_FAILURES* matches Byte 0 of the **Inject Operation Failures** field, return success. Otherwise, return the Function-Specific Error Code 2.

## <span id="related_topics"></span>Related topics


[Query Error Injection Status (Function Index 16)](query-error-injection-status--function-index-16-.md)

[Get Injected Errors (Function Index 18)](get-injected-errors--function-index-18-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






