---
title: Functions Defined by Print Processors
author: windows-driver-content
description: Functions Defined by Print Processors
ms.assetid: ada376f0-515e-4995-b612-4da9523b6fcf
keywords:
- print processors WDK , functions
- functions WDK print
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Functions Defined by Print Processors





Print processors must export the functions listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>ClosePrintProcessor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545976)</p></td>
<td><p>Closes the print processor.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ControlPrintProcessor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546352)</p></td>
<td><p>Provides control over printing a document.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>EnumPrintProcessorDatatypes</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548757)</p></td>
<td><p>Enumerates the data types supported by a print processor.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>GetPrintProcessorCapabilities</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550522)</p></td>
<td><p>Returns print processor capabilities for a specified input data type.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>OpenPrintProcessor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559604)</p></td>
<td><p>Opens the print processor for printing.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>PrintDocumentOnPrintProcessor</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560724)</p></td>
<td><p>Prints a document on the print processor.</p></td>
</tr>
</tbody>
</table>

 

 

 




