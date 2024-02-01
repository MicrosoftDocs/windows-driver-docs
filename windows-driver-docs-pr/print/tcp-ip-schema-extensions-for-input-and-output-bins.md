---
title: TCP/IP Schema Extensions for Input and Output Bins
description: TCP/IP Schema Extensions for Input and Output Bins
keywords:
- TCP/IP schema extensions WDK printer
- schema extensions WDK TCP/IP
- OutputBin construct
- InputBin construct
- output bins WDK printer
- input bins WDK printer
ms.date: 01/31/2024
---

# TCP/IP schema extensions for input and output bins

The Tcpbidi.xsd file, which is used to extend the bidi schema, defines two constructs, InputBin and OutputBin, that implement extensions that are related to specific printer input and output bins. InputBin and OutputBin constructs both have the following available attributes.

| Attribute | Meaning |
|--|--|
| **name** | The bidi schema name of the bin. |
| **mibName** | The MIB name of the bin. |
| **refreshInterval** | (Optional) The value of the polling interval, in seconds. The default value is 600 seconds. |

## Code example

The following code example shows how the InputBin and OutputBin constructs can be used to identify two input bins and one output bin.

```xml
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

[Implicit bin extensions](implicit-bin-extensions.md)

[Explicit bin extensions](explicit-bin-extensions.md)

[Driver-specific bins](driver-specific-bins.md)
