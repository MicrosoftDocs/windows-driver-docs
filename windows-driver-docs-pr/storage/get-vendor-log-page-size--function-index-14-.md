---
title: Get Vendor Log Page Size (Function Index 14)
description: This function returns the size of the vendor log page so that the host knows the size of the buffer it needs to allocate to read the vendor log page.
ms.assetid: 24211D67-1D36-4711-B87B-C99546E206FC
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Get Vendor Log Page Size (Function Index 14)


This function returns the size of the vendor log page so that the host knows the size of the buffer it needs to allocate to read the vendor log page.

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
<td align="left"><strong>Vendor Log Page Size</strong></td>
<td align="left">4</td>
<td align="left">4</td>
<td align="left"><p>The size of the vendor log page in multiples of 32 bytes.</p>
<p>*Byte 0 – <em>VENDOR_LOG_PAGE_SIZE</em> (0, 0x31)</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[Get Vendor Log Page (Function Index 15)](get-vendor-log-page--function-index-15-.md)

[\_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md)

 

 






