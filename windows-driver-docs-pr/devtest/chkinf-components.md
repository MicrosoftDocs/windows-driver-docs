---
title: ChkINF Components
description: ChkINF Components
ms.assetid: f0437daf-45cd-4260-814b-25dbf5c92a4a
keywords:
- ChkINF components WDK
- ChkINF WDK
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ChkINF Components


ChkINF and its components reside in the Tools\\chkinf subdirectory of the Windows Driver Kit (WDK). ChkINF can be executed on all supported 32-bit and 64-bit CPU platforms.

ChkINF consists of a variety of Perl scripts and support applications. The following table describes the main components of the ChkINF tool.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Component name</th>
<th align="left">WDK directory</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ChkInf.bat</p></td>
<td align="left"><p>tools\chkinf</p></td>
<td align="left"><p>A script that parses command-line arguments and invokes parsing modules.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ChkInf.htm</p></td>
<td align="left"><p>tools\chkinf</p></td>
<td align="left"><p>A readme file for the ChkINF tool.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ChkInf.pm</p></td>
<td align="left"><p>tools\chkinf</p></td>
<td align="left"><p>The main INF parsing module.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ChkSD.exe</p></td>
<td align="left"><p>tools\chkinf\i386</p></td>
<td align="left"><p>A support application that is called by the parsing modules to validate any security descriptors that are specified within an INF file.</p>
<p>For more information, see [Specifying a Security Descriptor From an INF File](http://go.microsoft.com/fwlink/p/?linkid=151340) in the MSDN documentation.</p></td>
</tr>
</tbody>
</table>

 

 

 





