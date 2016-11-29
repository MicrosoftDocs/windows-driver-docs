---
title: ChkINF Components
description: ChkINF Components
ms.assetid: f0437daf-45cd-4260-814b-25dbf5c92a4a
keywords: ["ChkINF components WDK", "ChkINF WDK"]
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20ChkINF%20Components%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




