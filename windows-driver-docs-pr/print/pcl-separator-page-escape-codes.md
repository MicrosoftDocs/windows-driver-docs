---
title: PCL Separator Page Escape Codes
author: windows-driver-content
description: PCL Separator Page Escape Codes
ms.assetid: 8e571fcd-f6ee-4a56-8d8a-20bf3a5c333c
keywords: ["PCL separator page escape codes WDK PCL XL", "PCL XL vector graphics WDK Unidrv , separator page escape codes", "escape codes WDK PCL XL"]
---

# PCL Separator Page Escape Codes


## <a href="" id="ddk-pcl-separator-page-escape-codes-gg"></a>


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
<td><p>\</p></td>
<td><p>The first line of the separator file must contain only this character. The separator file interpreter reads the separator file command as a delimiter.</p></td>
</tr>
<tr class="even">
<td><p>\<em>n</em></p></td>
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PCL%20Separator%20Page%20Escape%20Codes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


