---
title: Using GetGlobalAttribute
description: Using GetGlobalAttribute
ms.assetid: 0e23ecba-7d89-44f5-b6a7-7d6be9a56765
keywords:
- GetGlobalAttribute
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using GetGlobalAttribute





All of the global attribute names are the same as the keyword names defined in *PostScript Printer Description File Format Specification, v4.3*. Refer to this specification for their semantics. (This resource may not be available in some languages and countries.)

In the following table, the *pdwDataType* parameter takes values of the [**EATTRIBUTE\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff548692) enumerated type.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Global Attribute</th>
<th>Output Parameters</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>CenterRegistered</strong></p></td>
<td><p><em>pdwDataType: kADT_BOOL</p>
<p><em></em>pbData</em>: <strong>TRUE</strong> or <strong>FALSE</strong></p>
<p><em><em>pcbNeeded</em>: <strong>sizeof</strong>(BOOL)</p></td>
</tr>
<tr class="even">
<td><p><strong>ColorDevice</strong></p></td>
<td><p></em>pdwDataType: kADT_BOOL</p>
<p><em><em>pbData</em>: <strong>TRUE</strong> or <strong>FALSE</strong></p>
<p><em></em>pcbNeeded</em>: <strong>sizeof</strong>(BOOL)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Extensions</strong></p></td>
<td><p><em><em>pdwDataType</em>: kADT_ASCII</p>
<p><em>pbData</em>: ASCII string (in MULTI_SZ format) containing registered values of extensionOption the printer supports.</p>
<p><em></em>pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p>
<p>Note: &quot;<em>FileSystem: True&quot; is treated as if <strong></em>Extensions</strong> had the &quot;FileSystem&quot; option. &quot;FileSystem: False&quot; is treated as if <em>Extensions did not have the &quot;FileSystem&quot; option.</p></td>
</tr>
<tr class="even">
<td><p><strong>FileVersion</strong></p></td>
<td><p><em></em>pdwDataType</em>: kADT_DWORD</p>
<p><em><em>pbData</em>: a DWORD whose high-order word contains the major version number, and whose low-order word contains the minor version number.</p>
<p><em></em>pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="odd">
<td><p><strong>FreeVM</strong></p></td>
<td><p><em><em>pdwDataType</em>: kADT_DWORD</p>
<p><em></em>pbData</em>: value of <em>FreeVM</p>
<p><em></em>pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="even">
<td><p><strong>LandscapeOrientation</strong></p></td>
<td><p><em><em>pdwDataType</em>: kADT_ASCII</p>
<p><em>pbData</em>: NULL-terminated ASCII string of either &quot;Plus90&quot; or &quot;Minus90&quot;.</p>
<p><em></em>pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p>
<p>Note: &quot;Minus90&quot; is returned only when the PPD contains &quot;<em>LandscapeOrientation: Minus90&quot;. In all other cases, &quot;Plus90&quot; is returned.</p></td>
</tr>
<tr class="odd">
<td><p><strong>LanguageEncoding</strong></p></td>
<td><p><em></em>pdwDataType</em>: kADT_ASCII</p>
<p><em>pbData</em>: NULL-terminated ASCII string containing one of the following encodingOption values:</p>
<p>&quot;ISOLatin1&quot;</p>
<p>&quot;Unicode&quot;</p>
<p>&quot;JIS83-RKSJ&quot;</p>
<p>&quot;None&quot;</p>
<p><em><em>pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p>
<p>Notes</p>
<p>&quot;WindowsANSI&quot; is treated the same as &quot;ISOLatin1&quot;. Other encodingOption values are not supported.</p>
<p>If *LanguageEncoding is absent, *LanguageVersion is used to deduce the return value.</p></td>
</tr>
<tr class="even">
<td><p><strong>LanguageLevel</strong></p></td>
<td><p><em></em>pdwDataType</em>: kADT_DWORD</p>
<p><em><em>pbData</em>: PostScript language level supported by the printer</p>
<p><em></em>pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="odd">
<td><p><strong>NickName</strong></p></td>
<td><p><em><em>pdwDataType</em>: kADT_UNICODE</p>
<p><em>pbData</em>: NULL-terminated Unicode string of the PPD&#39;s *ShortNickName value if *ShortNickName is present, or *NickName value if *ShortNickName is absent.</p>
<p><em></em>pcbNeeded</em>: byte count of the Unicode string pointed to by <em>pbData</em> (including the last null character)</p></td>
</tr>
<tr class="even">
<td><p><strong>PPD-Adobe</strong></p></td>
<td><p><em><em>pdwDataType</em>: kADT_DWORD</p>
<p><em></em>pbData</em>: a DWORD whose high-order word contains the major version number, and whose low-order word contains the minor version number.</p>
<p><em><em>pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="odd">
<td><p><strong>PrintPSErrors</strong></p></td>
<td><p></em>pdwDataType: kADT_BOOL</p>
<p><em><em>pbData</em>: <strong>TRUE</strong> or <strong>FALSE</strong></p>
<p><em></em>pcbNeeded</em>: <strong>sizeof</strong>(BOOL)</p>
<p>Note: If <em>PrintPSErrors is absent, it is assumed to be <strong>TRUE</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>Product</strong></p></td>
<td><p><em></em>pdwDataType</em>: kADT_BINARY</p>
<p><em>pbData</em>: the <em>Product value</p>
<p><em></em>pcbNeeded</em>: byte count of output binary data</p>
<p>Note: only the first <em>Product entry is returned.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Protocols</strong></p></td>
<td><p><em></em>pdwDataType</em>: kADT_ASCII</p>
<p><em>pbData</em>: ASCII string (in MULTI_SZ format) containing registered values of protocolOption the printer supports.</p>
<p><em><em>pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p></td>
</tr>
<tr class="even">
<td><p><strong>PSVersion</strong></p></td>
<td><p><em></em>pdwDataType</em>: kADT_BINARY</p>
<p><em>pbData</em>: the <em>PSVersion value</p>
<p><em></em>pcbNeeded</em>: byte count of output binary data</p>
<p>Note: only the first <em>PSVersion entry is returned.</p></td>
</tr>
<tr class="odd">
<td><p><strong>SuggestedJobTimeout</strong></p></td>
<td><p><em></em>pdwDataType</em>: kADT_DWORD</p>
<p><em><em>pbData</em>: the *SuggestedJobTimeout value. If it is absent from the PPD, returns 0 by default.</p>
<p><em></em>pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="even">
<td><p><strong>SuggestedWaitTimeout</strong></p></td>
<td><p><em><em>pdwDataType</em>: kADT_DWORD</p>
<p><em></em>pbData</em>: the <em>SuggestedWaitTimeout value. If it is not present in the PPD, returns 300 by default.</p>
<p><em></em>pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Throughput</strong></p></td>
<td><p><em><em>pdwDataType</em>: kADT_DWORD</p>
<p><em></em>pbData</em>: the <em>Throughput value. If it is not present in the PPD, returns 0 by default.</p>
<p><em></em>pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="even">
<td><p><strong>TTRasterizer</strong></p></td>
<td><p><em><em>pdwDataType</em>: kADT_ASCII</p>
<p><em>pbData</em>: a NULL-terminated ASCII string containing one of following rasterizerOption values:</p>
<p>&quot;None&quot;</p>
<p>&quot;Accept68K&quot;</p>
<p>&quot;Type42&quot;</p>
<p>&quot;TrueImage&quot;</p>
<p><em></em>pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p>
<p>Note: if the *TTRasterizer entry is absent, &quot;None&quot; is returned.</p></td>
</tr>
</tbody>
</table>

 

 

 




