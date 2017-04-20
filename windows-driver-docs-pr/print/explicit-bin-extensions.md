---
title: Explicit Bin Extensions
author: windows-driver-content
description: Explicit Bin Extensions
ms.assetid: a9f7f290-1af8-4312-b348-c1c98a3fc4a6
keywords:
- explicit bin extensions WDK printer
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>An enumerator in the [<strong>BIDI_TYPE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545211) enumeration.</p></td>
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

```
<Property name="Layout">
  <Property name="InputBins">
    <InputBin name="TopBin" mibName="TRAY 1">
      <BinValue name="Security" type="BIDI_INT" valueId="19"/>
    </InputBin>
  </Property>
</Property>
```

The preceding example results in the following query:

```
\Printer.Layout.InputBins.TopBin:Security
```

The following code example shows how a **BinValue** construct can be used to add a Status value. As in the preceding example, this has the effect of extending an implicit bin extension.

```
<Property name="Finishing">
  <Property name="OutputBins">
    <OutputBin name="TopBin" mibName="STANDARD BIN">
       <BinValue name="Status" type="BIDI_INT" valueId="6"/>
    </OutputBin>
  </Property>
</Property>
```

The preceding example results in the following query:

```
\Printer.Finishing.OutputBins.TopBin:Status
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Explicit%20Bin%20Extensions%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


