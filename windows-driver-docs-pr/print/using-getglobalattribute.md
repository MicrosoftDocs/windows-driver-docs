---
title: Using GetGlobalAttribute
description: Using GetGlobalAttribute
keywords:
- GetGlobalAttribute
ms.date: 01/31/2023
---

# Using GetGlobalAttribute

[!include[Print Support Apps](../includes/print-support-apps.md)]

All of the global attribute names are the same as the keyword names defined in *PostScript Printer Description File Format Specification, v4.3*. Refer to this specification for their semantics. (This resource may not be available in some languages and countries.)

In the following table, the *pdwDataType* parameter takes values of the [**EATTRIBUTE_DATATYPE**](/windows-hardware/drivers/ddi/printoem/ne-printoem-_eattribute_datatype) enumerated type.

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
<p>Note: "<em>FileSystem: True" is treated as if <strong></em>Extensions</strong> had the "FileSystem" option. "FileSystem: False" is treated as if <em>Extensions did not have the "FileSystem" option.</p></td>
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
<p><em>pbData</em>: NULL-terminated ASCII string of either "Plus90" or "Minus90".</p>
<p><em></em>pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p>
<p>Note: "Minus90" is returned only when the PPD contains "<em>LandscapeOrientation: Minus90". In all other cases, "Plus90" is returned.</p></td>
</tr>
<tr class="odd">
<td><p><strong>LanguageEncoding</strong></p></td>
<td><p><em></em>pdwDataType</em>: kADT_ASCII</p>
<p><em>pbData</em>: NULL-terminated ASCII string containing one of the following encodingOption values:</p>
<p>"ISOLatin1"</p>
<p>"Unicode"</p>
<p>"JIS83-RKSJ"</p>
<p>"None"</p>
<p><em><em>pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p>
<p>Notes</p>
<p>"WindowsANSI" is treated the same as "ISOLatin1". Other encodingOption values are not supported.</p>
<p>If *LanguageEncoding is absent,*LanguageVersion is used to deduce the return value.</p></td>
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
<p><em>pbData</em>: NULL-terminated Unicode string of the PPD's *ShortNickName value if*ShortNickName is present, or *NickName value if*ShortNickName is absent.</p>
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
<p>"None"</p>
<p>"Accept68K"</p>
<p>"Type42"</p>
<p>"TrueImage"</p>
<p><em></em>pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p>
<p>Note: if the*TTRasterizer entry is absent, "None" is returned.</p></td>
</tr>
</tbody>
</table>
