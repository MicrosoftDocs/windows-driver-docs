---
title: Reading the LogViewer Display
description: Reading the LogViewer Display
ms.assetid: 425aff5d-780e-4600-a43a-8012d70263f1
keywords: ["LogViewer, display"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Reading%20the%20LogViewer%20Display%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




