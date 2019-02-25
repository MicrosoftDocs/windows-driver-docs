---
title: Explicit Bin Extensions
description: Explicit Bin Extensions
ms.assetid: a9f7f290-1af8-4312-b348-c1c98a3fc4a6
keywords:
- explicit bin extensions WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Explicit Bin Extensions


You can further extend an implicit bin extension by using the special construct, **BinValue**. This object determines which MIB object inside a prtInputTable or prtOutputTable table contains the new data.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>name</strong></p></td>
<td><p>The name of the bin.</p></td>
</tr>
<tr class="even">
<td><p><strong>type</strong></p></td>
<td><p>An enumerator in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545211" data-raw-source="[&lt;strong&gt;BIDI_TYPE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545211)"><strong>BIDI_TYPE</strong></a> enumeration.</p></td>
</tr>
<tr class="odd">
<td><p><strong>drvPrinterEvent</strong></p></td>
<td><p>(Optional) A Boolean value that indicates whether the port monitor sends notifications to the driver. A <strong>TRUE</strong> value indicates that the port monitor sends notifications to the driver; <strong>FALSE</strong> indicates that the port monitor does not send notifications to the driver.</p></td>
</tr>
<tr class="even">
<td><p><strong>valueId</strong></p></td>
<td><p>The MIB object in either printmib.prtInput.prtInputTable.prtInputEntry.<strong>valueId</strong> (input bin) or printmib.prtOutput.prtOutputTable.prtOutputEntry.<strong>valueId</strong> (output bin).</p></td>
</tr>
</tbody>
</table>

 

### Code Example

The following code example shows how a **BinValue** construct can be used to add a new property, **Security**. This has the effect of extending an implicit bin extension.

```cpp
<Property name="Layout">
  <Property name="InputBins">
    <InputBin name="TopBin" mibName="TRAY 1">
      <BinValue name="Security" type="BIDI_INT" valueId="19"/>
    </InputBin>
  </Property>
</Property>
```

The preceding example results in the following query:

```cpp
\Printer.Layout.InputBins.TopBin:Security
```

The following code example shows how a **BinValue** construct can be used to add a Status value. As in the preceding example, this has the effect of extending an implicit bin extension.

```cpp
<Property name="Finishing">
  <Property name="OutputBins">
    <OutputBin name="TopBin" mibName="STANDARD BIN">
       <BinValue name="Status" type="BIDI_INT" valueId="6"/>
    </OutputBin>
  </Property>
</Property>
```

The preceding example results in the following query:

```cpp
\Printer.Finishing.OutputBins.TopBin:Status
```

 

 




