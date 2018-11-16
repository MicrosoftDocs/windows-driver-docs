---
title: TCP/IP Schema Extensions for Input and Output Bins
description: TCP/IP Schema Extensions for Input and Output Bins
ms.assetid: 942325e8-588c-4171-91fa-366db6e2cb16
keywords:
- TCP/IP schema extensions WDK printer
- schema extensions WDK TCP/IP
- OutputBin construct
- InputBin construct
- output bins WDK printer
- input bins WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TCP/IP Schema Extensions for Input and Output Bins


The Tcpbidi.xsd file, which is used to extend the bidi schema, defines two constructs, InputBin and OutputBin, that implement extensions that are related to specific printer input and output bins. InputBin and OutputBin constructs both have the following available attributes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>name</strong></p></td>
<td><p>The bidi schema name of the bin.</p></td>
</tr>
<tr class="even">
<td><p><strong>mibName</strong></p></td>
<td><p>The MIB name of the bin.</p></td>
</tr>
<tr class="odd">
<td><p><strong>refreshInterval</strong></p></td>
<td><p>(Optional) The value of the polling interval, in seconds. The default value is 600 seconds.</p></td>
</tr>
</tbody>
</table>

 

### Code Example

The following code example shows how the InputBin and OutputBin constructs can be used to identify two input bins and one output bin.

```cpp
<Property name="Printer">
  <Property name="Layout">
    <Property name="InputBins">
      <InputBin name="TopBin"    mibName="TRAY 1"/>
      <InputBin name="BottomBin" mibName="TRAY 2"/>
    </Property>
  </Property>
  <Property name="Finishing">
    <Property name="OutputBins">
      <OutputBin name="TopBin" mibName="STANDARD BIN"/>
    </Property>
  </Property>
</Property>
```

This section includes the following topics.

[Implicit Bin Extensions](implicit-bin-extensions.md)

[Explicit Bin Extensions](explicit-bin-extensions.md)

[Driver-Specific Bins](driver-specific-bins.md)

 

 




