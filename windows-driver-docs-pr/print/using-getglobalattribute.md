---
title: Using GetGlobalAttribute
author: windows-driver-content
description: Using GetGlobalAttribute
ms.assetid: 0e23ecba-7d89-44f5-b6a7-7d6be9a56765
keywords: ["GetGlobalAttribute"]
---

# Using GetGlobalAttribute


## <a href="" id="ddk-using-getglobalattribute-gg"></a>


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
<td><p>*pdwDataType: kADT_BOOL</p>
<p><em>*pbData</em>: <strong>TRUE</strong> or <strong>FALSE</strong></p>
<p><em>*pcbNeeded</em>: <strong>sizeof</strong>(BOOL)</p></td>
</tr>
<tr class="even">
<td><p><strong>ColorDevice</strong></p></td>
<td><p>*pdwDataType: kADT_BOOL</p>
<p><em>*pbData</em>: <strong>TRUE</strong> or <strong>FALSE</strong></p>
<p><em>*pcbNeeded</em>: <strong>sizeof</strong>(BOOL)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Extensions</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_ASCII</p>
<p><em>pbData</em>: ASCII string (in MULTI_SZ format) containing registered values of extensionOption the printer supports.</p>
<p><em>*pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p>
<p>Note: &quot;*FileSystem: True&quot; is treated as if <strong>*Extensions</strong> had the &quot;FileSystem&quot; option. &quot;FileSystem: False&quot; is treated as if *Extensions did not have the &quot;FileSystem&quot; option.</p></td>
</tr>
<tr class="even">
<td><p><strong>FileVersion</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_DWORD</p>
<p><em>*pbData</em>: a DWORD whose high-order word contains the major version number, and whose low-order word contains the minor version number.</p>
<p><em>*pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="odd">
<td><p><strong>FreeVM</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_DWORD</p>
<p><em>*pbData</em>: value of *FreeVM</p>
<p><em>*pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="even">
<td><p><strong>LandscapeOrientation</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_ASCII</p>
<p><em>pbData</em>: NULL-terminated ASCII string of either &quot;Plus90&quot; or &quot;Minus90&quot;.</p>
<p><em>*pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p>
<p>Note: &quot;Minus90&quot; is returned only when the PPD contains &quot;*LandscapeOrientation: Minus90&quot;. In all other cases, &quot;Plus90&quot; is returned.</p></td>
</tr>
<tr class="odd">
<td><p><strong>LanguageEncoding</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_ASCII</p>
<p><em>pbData</em>: NULL-terminated ASCII string containing one of the following encodingOption values:</p>
<p>&quot;ISOLatin1&quot;</p>
<p>&quot;Unicode&quot;</p>
<p>&quot;JIS83-RKSJ&quot;</p>
<p>&quot;None&quot;</p>
<p><em>*pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p>
<p>Notes</p>
<p>&quot;WindowsANSI&quot; is treated the same as &quot;ISOLatin1&quot;. Other encodingOption values are not supported.</p>
<p>If *LanguageEncoding is absent, *LanguageVersion is used to deduce the return value.</p></td>
</tr>
<tr class="even">
<td><p><strong>LanguageLevel</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_DWORD</p>
<p><em>*pbData</em>: PostScript language level supported by the printer</p>
<p><em>*pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="odd">
<td><p><strong>NickName</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_UNICODE</p>
<p><em>pbData</em>: NULL-terminated Unicode string of the PPD's *ShortNickName value if *ShortNickName is present, or *NickName value if *ShortNickName is absent.</p>
<p><em>*pcbNeeded</em>: byte count of the Unicode string pointed to by <em>pbData</em> (including the last null character)</p></td>
</tr>
<tr class="even">
<td><p><strong>PPD-Adobe</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_DWORD</p>
<p><em>*pbData</em>: a DWORD whose high-order word contains the major version number, and whose low-order word contains the minor version number.</p>
<p><em>*pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="odd">
<td><p><strong>PrintPSErrors</strong></p></td>
<td><p>*pdwDataType: kADT_BOOL</p>
<p><em>*pbData</em>: <strong>TRUE</strong> or <strong>FALSE</strong></p>
<p><em>*pcbNeeded</em>: <strong>sizeof</strong>(BOOL)</p>
<p>Note: If *PrintPSErrors is absent, it is assumed to be <strong>TRUE</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>Product</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_BINARY</p>
<p><em>pbData</em>: the *Product value</p>
<p><em>*pcbNeeded</em>: byte count of output binary data</p>
<p>Note: only the first *Product entry is returned.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Protocols</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_ASCII</p>
<p><em>pbData</em>: ASCII string (in MULTI_SZ format) containing registered values of protocolOption the printer supports.</p>
<p><em>*pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p></td>
</tr>
<tr class="even">
<td><p><strong>PSVersion</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_BINARY</p>
<p><em>pbData</em>: the *PSVersion value</p>
<p><em>*pcbNeeded</em>: byte count of output binary data</p>
<p>Note: only the first *PSVersion entry is returned.</p></td>
</tr>
<tr class="odd">
<td><p><strong>SuggestedJobTimeout</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_DWORD</p>
<p><em>*pbData</em>: the *SuggestedJobTimeout value. If it is absent from the PPD, returns 0 by default.</p>
<p><em>*pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="even">
<td><p><strong>SuggestedWaitTimeout</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_DWORD</p>
<p><em>*pbData</em>: the *SuggestedWaitTimeout value. If it is not present in the PPD, returns 300 by default.</p>
<p><em>*pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Throughput</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_DWORD</p>
<p><em>*pbData</em>: the *Throughput value. If it is not present in the PPD, returns 0 by default.</p>
<p><em>*pcbNeeded</em>: <strong>sizeof</strong>(DWORD)</p></td>
</tr>
<tr class="even">
<td><p><strong>TTRasterizer</strong></p></td>
<td><p><em>*pdwDataType</em>: kADT_ASCII</p>
<p><em>pbData</em>: a NULL-terminated ASCII string containing one of following rasterizerOption values:</p>
<p>&quot;None&quot;</p>
<p>&quot;Accept68K&quot;</p>
<p>&quot;Type42&quot;</p>
<p>&quot;TrueImage&quot;</p>
<p><em>*pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the last null character)</p>
<p>Note: if the *TTRasterizer entry is absent, &quot;None&quot; is returned.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Using%20GetGlobalAttribute%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


