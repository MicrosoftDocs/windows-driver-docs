---
title: PCL Separator Page Escape Codes
description: PCL Separator Page Escape Codes
ms.assetid: 8e571fcd-f6ee-4a56-8d8a-20bf3a5c333c
keywords:
- PCL separator page escape codes WDK PCL XL
- PCL XL vector graphics WDK Unidrv , separator page escape codes
- escape codes WDK PCL XL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PCL Separator Page Escape Codes





The escape codes shown in the following table can be used when you create a PCL separator page.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Escape Code</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>&lt;/p&gt;</td>
<td><p>The first line of the separator file must contain only this character. The separator file interpreter reads the separator file command as a delimiter.</p></td>
</tr>
<tr class="even">
<td><p>&lt;em&gt;n</em></p></td>
<td><p>Skips the number of lines specified by <em>n</em> (from 0 through 9). Skipping 0 lines moves printing to the next line.</p></td>
</tr>
<tr class="odd">
<td><p>\B\M</p></td>
<td><p>Prints text in double-width block characters until \U is encountered.</p></td>
</tr>
<tr class="even">
<td><p>\B\S</p></td>
<td><p>Prints text in single-width block characters until \U is encountered.</p></td>
</tr>
<tr class="odd">
<td><p>\D</p></td>
<td><p>Prints the date the job was printed. The time is displayed in the format specified under Regional Options (Windows 2000) or Regional and Language Options (Windows XP and later) in Control Panel.</p></td>
</tr>
<tr class="even">
<td><p>\E</p></td>
<td><p>Ejects a page from the printer. Use this code to start a new separator page or to end the separator page file. If you get an extra blank separator page when you print, remove this code from your separator page file.</p></td>
</tr>
<tr class="odd">
<td><p>\F<em>pathname</em></p></td>
<td><p>Prints the contents of the file specified by <em>pathname</em>, starting on an empty line. The contents of this file are copied directly to the printer without processing.</p></td>
</tr>
<tr class="even">
<td><p>\H<em>nn</em></p></td>
<td><p>Sets a printer-specific control sequence, where <em>nn</em> is a hexadecimal ASCII code sent directly to the printer. See your printer manual to determine the specific numbers.</p></td>
</tr>
<tr class="odd">
<td><p>\I</p></td>
<td><p>Prints the job number.</p></td>
</tr>
<tr class="even">
<td><p>\L<em>xxx</em></p></td>
<td><p>Prints the string of text that appears after the \L escape code. If you enter \LTest, the text &quot;Test&quot; appears in the separator page.</p></td>
</tr>
<tr class="odd">
<td><p>\N</p></td>
<td><p>Prints the user name of the person who submitted the job.</p></td>
</tr>
<tr class="even">
<td><p>\U</p></td>
<td><p>Turns off block character printing.</p></td>
</tr>
<tr class="odd">
<td><p>\W<em>nn</em></p></td>
<td><p>Sets the width of the separator page. The default width is 80 characters, and the maximum width is 256 characters. Characters beyond this width are deleted.</p></td>
</tr>
</tbody>
</table>

 

After the local print provider passes a job through the print processor and the separator page processor, it sends the job from the spooler to the appropriate port print monitor.

 

 




