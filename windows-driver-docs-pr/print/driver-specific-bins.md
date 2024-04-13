---
title: Driver-Specific Bins
description: Driver-Specific Bins
keywords:
- device-specific bins WDK printer
ms.date: 04/20/2017
---

# Driver-Specific Bins


You are free to extend the bidi communications schema with driver-specific bin names. In this case, only the driver will be able to recognize the additional bin names.

```cpp
<InputBin name="AAA" mibName="TRAY A"/>
```

The preceding code example results in the following four queries. Recall that an InputBin construct generates four new queries.

```cpp
\Printer.Layout.InputBins.AAA:Installed
\Printer.Layout.InputBins.AAA:Level
\Printer.Layout.InputBins.AAA:MediaType
\Printer.Layout.InputBins.AAA:MediaSize

<OutputBin name="BBB" mibName="BIN B"/>
```

The preceding code example results in the following two queries. Recall that an OutputBin construct generates two new queries.

```cpp
\Printer.Finishing.OutputBins.BBB:Installed
\Printer.Finishing.OutputBins.BBB:Level
```

 

 




