---
title: TCP/IP Schema Extensions for Input and Output Bins
author: windows-driver-content
description: TCP/IP Schema Extensions for Input and Output Bins
MS-HAID:
- 'autocfg\_c33855bb-9cd5-415d-9279-487333b24439.xml'
- 'print.tcp\_ip\_schema\_extensions\_for\_input\_and\_output\_bins'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 942325e8-588c-4171-91fa-366db6e2cb16
keywords: ["TCP/IP schema extensions WDK printer", "schema extensions WDK TCP/IP", "OutputBin construct", "InputBin construct", "output bins WDK printer", "input bins WDK printer"]
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20TCP/IP%20Schema%20Extensions%20for%20Input%20and%20Output%20Bins%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


