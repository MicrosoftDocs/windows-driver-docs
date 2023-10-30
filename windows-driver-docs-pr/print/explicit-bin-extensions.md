---
title: Explicit bin extensions
description: Explicit bin extensions
keywords:
- explicit bin extensions WDK printer
ms.date: 06/21/2023
---

# Explicit bin extensions

You can further extend an implicit bin extension by using the special construct, **BinValue**. This object determines which MIB object inside a prtInputTable or prtOutputTable table contains the new data.

| Attribute | Description |
|--|--|
| **name** | The name of the bin. |
| **type** | An enumerator in the [**BIDI_TYPE**](/windows-hardware/drivers/ddi/winspool/ne-winspool-bidi_type) enumeration. |
| **drvPrinterEvent** | (Optional) A Boolean value that indicates whether the port monitor sends notifications to the driver. A **TRUE** value indicates that the port monitor sends notifications to the driver; **FALSE** indicates that the port monitor does not send notifications to the driver. |
| **valueId** | The MIB object in either printmib.prtInput.prtInputTable.prtInputEntry.**valueId** (input bin) or printmib.prtOutput.prtOutputTable.prtOutputEntry.**valueId** (output bin). |

## Code Example

The following code example shows how a **BinValue** construct can be used to add a new property, **Security**. This has the effect of extending an implicit bin extension.

```xml
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

```xml
<Property name="Finishing">
  <Property name="OutputBins">
    <OutputBin name="TopBin" mibName="STANDARD BIN">
       <BinValue name="Status" type="BIDI_INT" valueId="6"/>
    </OutputBin>
  </Property>
</Property>
```

The preceding example results in the following query:

```output
\Printer.Finishing.OutputBins.TopBin:Status
```
