---
title: Implicit Bin Extensions
author: windows-driver-content
description: Implicit Bin Extensions
ms.assetid: 2aaa9e48-59f9-4c87-b592-ed60469cf747
keywords:
- implicit bin extensions WDK printer
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Implicit Bin Extensions


Each InputBin or OutputBin construct extends the schema with two or more queries. An InputBin extension generates four new schema values: Installed, Level, MediaType, and MediaSize. An OutputBin extension generates two new schema values: Installed and Level.

These schemas are defined in the Tcpbidi.xsd file under the **InputBins** and **OutputBins** properties.

```
<InputBin name="TopBin" mibName="TRAY 1"/>
```

The preceding InputBin construct results in the following four queries:

```
\Printer.Layout.InputBins.TopBin:Installed
\Printer.Layout.InputBins.TopBin:Level
\Printer.Layout.InputBins.TopBin:MediaType
\Printer.Layout.InputBins.TopBin:MediaSize

<OutputBin name="TopBin" mibName="STANDARD BIN"/>
```

The preceding OutputBin construct results in the following two queries:

```
\Printer.Finishing.OutputBins.TopBin:Installed
\Printer.Finishing.OutputBins.TopBin:Level
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Implicit%20Bin%20Extensions%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


