---
title: Functions Defined by Print Processors
author: windows-driver-content
description: Functions Defined by Print Processors
MS-HAID:
- 'provider\_7749dff2-5b74-4984-bafe-db35f155ab7b.xml'
- 'print.functions\_defined\_by\_print\_processors'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ada376f0-515e-4995-b612-4da9523b6fcf
keywords: ["print processors WDK , functions", "functions WDK print"]
---

# Functions Defined by Print Processors


## <a href="" id="ddk-functions-defined-by-print-processors-gg"></a>


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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Functions%20Defined%20by%20Print%20Processors%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


