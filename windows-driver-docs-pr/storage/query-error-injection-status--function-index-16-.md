---
title: Query Error Injection Status (Function Index 16)
description: This function returns the status of NVDIMM-N error injection.
ms.assetid: 7CE07551-666F-4E07-8115-806F6256B595
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Query Error Injection Status (Function Index 16)


This function returns the status of NVDIMM-N error injection. The platform may choose to only enable error injection in specific scenarios, e.g. after the user configures a BIOS setting.

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
<td align="left"><strong>Error Injection Enabled</strong></td>
<td align="left">1</td>
<td align="left">4</td>
<td align="left"><p>Whether or not error injection is enabled.</p>
<p>If 0, error injection is disabled.</p>
<p>If 1, error injection is enabled.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Inject Error (Function Index 17)](inject-error--function-index-17-.md)

[Get Injected Errors (Function Index 18)](get-injected-errors--function-index-18-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






