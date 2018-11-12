---
title: Reading the LogViewer Display
description: Reading the LogViewer Display
ms.assetid: 425aff5d-780e-4600-a43a-8012d70263f1
keywords: ["LogViewer, display"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Reading the LogViewer Display


## <span id="ddk_reading_the_logviewer_display_dtoolq"></span><span id="DDK_READING_THE_LOGVIEWER_DISPLAY_DTOOLQ"></span>


LogViewer displays a list of all functions in the order they were logged.

Each row of the display contains several columns. The significance of each column is as follows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Column</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>+/-</strong></p></td>
<td align="left"><p>If this column contains a &quot;+&quot; (plus sign), it indicates that the function takes one or more parameters. To see the parameters and their values, either double-click the row or hit the right arrow key when the row is outlined in red. To hide it again, double click it again or hit the left arrow key when the row is outlined in red.</p>
<p>There is also a &quot;d#&quot; value in this column. This indicates the &quot;depth&quot; of the function call (in other words, how deep the call is nested in other logged function calls).</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>#</strong></p></td>
<td align="left"><p>The sequential row number of the function call. This is useful when you have filters applied and are interested to know how far apart two function calls are.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Thrd</strong></p></td>
<td align="left"><p>The thread number on which the function call was made. This number is not a thread ID, but is rather an assigned number based on the order that threads were created in the process.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Caller</strong></p></td>
<td align="left"><p>The instruction address that made the function call. This is derived from the return address for the call. It is actually the return address minus 5 bytes (the typical size of a <strong>call dword ptr</strong> instruction).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Module</strong></p></td>
<td align="left"><p>The module that contains the calling instruction.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>API Function</strong></p></td>
<td align="left"><p>The name of the function. The name of the module that contains the function is omitted for brevity.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Return Value</strong></p></td>
<td align="left"><p>The value returned by the function, if it is not a void function.</p></td>
</tr>
</tbody>
</table>

 

Double-clicking on a row in the viewer will expand the row to reveal the parameters to the function and their values "going in" to the function. If they are designated as OUT parameters, their value "coming out" is shown on the right.

You can also use the ENTER key or the right and left arrow keys to expand and collapse rows.

Function calls that returned failure status codes are shaded in pink.

 

 





