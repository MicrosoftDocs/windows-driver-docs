---
title: Implicit Bin Extensions
description: Implicit Bin Extensions
keywords:
- implicit bin extensions WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Implicit Bin Extensions


Each InputBin or OutputBin construct extends the schema with two or more queries. An InputBin extension generates four new schema values: Installed, Level, MediaType, and MediaSize. An OutputBin extension generates two new schema values: Installed and Level.

These schemas are defined in the Tcpbidi.xsd file under the **InputBins** and **OutputBins** properties.

```cpp
<InputBin name="TopBin" mibName="TRAY 1"/>
```

The preceding InputBin construct results in the following four queries:

```cpp
\Printer.Layout.InputBins.TopBin:Installed
\Printer.Layout.InputBins.TopBin:Level
\Printer.Layout.InputBins.TopBin:MediaType
\Printer.Layout.InputBins.TopBin:MediaSize

<OutputBin name="TopBin" mibName="STANDARD BIN"/>
```

The preceding OutputBin construct results in the following two queries:

```cpp
\Printer.Finishing.OutputBins.TopBin:Installed
\Printer.Finishing.OutputBins.TopBin:Level
```

 

 




