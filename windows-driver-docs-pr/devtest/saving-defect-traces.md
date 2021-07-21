---
title: Saving Defect Traces
description: Saving Defect Traces in Static Driver Verifier
keywords:
- Static Driver Verifier WDK , Static Driver Verifier Report
- StaticDV WDK , Static Driver Verifier Report
- SDV WDK , Static Driver Verifier Report
- Static Driver Verifier WDK , locating errors
- StaticDV WDK , locating errors
- SDV WDK , locating errors
- locating errors WDK Static Driver Verifier
- errors WDK Static Driver Verifier
- export WDK Static Driver Verifier
- Static Driver Verifier Report WDK
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Saving Defect Traces

The Static Driver Verifier Defect Viewer has functionality that allows you to save a specific defect trace in an easily shareable format.  

To save a trace, select "Save as..." from the file menu, or press Ctrl-S.  

![screen shot of the defect viewer window, showing the location of the save functionality.](images/sdv-savedefecttrace.png)

Then specify a folder where the trace folder ("sdvdefect") will be placed.

The saved defect trace will contain copies of the relevant source code, the defect trace, and the necessary SDV files and executables to view the trace.  To view the trace, simply double-click the sdvdefect.exe file.

