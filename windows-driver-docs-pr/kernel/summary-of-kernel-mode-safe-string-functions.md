---
title: Summary of Kernel-Mode Safe String Functions
author: windows-driver-content
description: Summary of Kernel-Mode Safe String Functions
ms.assetid: 71b67d88-2a9a-4c9d-b64c-5fd7fe7e5cda
keywords: ["safe string functions WDK"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Summary of Kernel-Mode Safe String Functions


## <a href="" id="ddk-summary-of-kernel-mode-safe-string-functions-kg"></a>


The following table summarizes the safe string functions that are available to kernel-mode drivers, and it indicates the C/C++ language runtime library functions that they replace. If a function's name contains **Cb**, the function treats strings as byte-counted. If a function's name contains **Cch**, the function treats strings as character-counted.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Functions</th>
<th>Purpose</th>
<th>Replaces</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p></p>
<dl>
<dt><a href="" id="rtlstringcbcat"></a>[<strong>RtlStringCbCat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562795)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbcatex"></a>[<strong>RtlStringCbCatEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562799)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcat"></a>[<strong>RtlStringCchCat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562834)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcatex"></a>[<strong>RtlStringCchCatEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562835)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcat"></a>[<strong>RtlUnicodeStringCat</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562898)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcatex"></a>[<strong>RtlUnicodeStringCatEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562899)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcatstring"></a>[<strong>RtlUnicodeStringCatString</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562901)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcatstringex"></a>[<strong>RtlUnicodeStringCatStringEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562902)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcatstringn"></a>[<strong>RtlUnicodeStringCbCatStringN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562908)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcatstringnex"></a>[<strong>RtlUnicodeStringCbCatStringNEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562910)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcatstringn"></a>[<strong>RtlUnicodeStringCchCatStringN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562924)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcatstringnex"></a>[<strong>RtlUnicodeStringCchCatStringNEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562927)</dt>
<dd>
</dd>
</dl></td>
<td><p>Concatenate two strings.</p></td>
<td><p></p>
<dl>
<dt><strong>strcat</strong></dt>
<dd>
</dd>
<dt><strong>wcscat</strong></dt>
<dd>
</dd>
</dl></td>
</tr>
<tr class="even">
<td><p></p>
<dl>
<dt><a href="" id="rtlstringcbcatn"></a>[<strong>RtlStringCbCatN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562801)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbcatnex"></a>[<strong>RtlStringCbCatNEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562802)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcatn"></a>[<strong>RtlStringCchCatN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562836)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcatnex"></a>[<strong>RtlStringCchCatNEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562837)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcatn"></a>[<strong>RtlUnicodeStringCbCatN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562905)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcatnex"></a>[<strong>RtlUnicodeStringCbCatNEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562906)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcatn"></a>[<strong>RtlUnicodeStringCchCatN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562921)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcatnex"></a>[<strong>RtlUnicodeStringCchCatNEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562923)</dt>
<dd>
</dd>
</dl></td>
<td><p>Concatenate two byte-counted strings, while limiting the size of the appended string.</p></td>
<td><p></p>
<dl>
<dt><strong>strncat</strong></dt>
<dd>
</dd>
<dt><strong>wcsncat</strong></dt>
<dd>
</dd>
</dl></td>
</tr>
<tr class="odd">
<td><p></p>
<dl>
<dt><a href="" id="rtlstringcbcopy"></a>[<strong>RtlStringCbCopy</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562805)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbcopyex"></a>[<strong>RtlStringCbCopyEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562807)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbcopyunicodestring"></a>[<strong>RtlStringCbCopyUnicodeString</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562815)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbcopyunicodestringex"></a>[<strong>RtlStringCbCopyUnicodeStringEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562817)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcopy"></a>[<strong>RtlStringCchCopy</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562841)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcopyex"></a>[<strong>RtlStringCchCopyEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562843)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcopyunicodestring"></a>[<strong>RtlStringCchCopyUnicodeString</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562851)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcopyunicodestringex"></a>[<strong>RtlStringCchCopyUnicodeStringEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562852)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcopy"></a>[<strong>RtlUnicodeStringCopy</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562942)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcopyex"></a>[<strong>RtlUnicodeStringCopyEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562946)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcopystring"></a>[<strong>RtlUnicodeStringCopyString</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562948)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcopystringex"></a>[<strong>RtlUnicodeStringCopyStringEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562950)</dt>
<dd>
</dd>
</dl></td>
<td><p>Copy a string into a buffer.</p></td>
<td><p></p>
<dl>
<dt><strong>strcpy</strong></dt>
<dd>
</dd>
<dt><strong>wcscpy</strong></dt>
<dd>
</dd>
</dl></td>
</tr>
<tr class="even">
<td><p></p>
<dl>
<dt><a href="" id="rtlstringcbcopyn"></a>[<strong>RtlStringCbCopyN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562811)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbcopynex"></a>[<strong>RtlStringCbCopyNEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562813)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcopyn"></a>[<strong>RtlStringCchCopyN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562846)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcopynex"></a>[<strong>RtlStringCchCopyNEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562849)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcopyn"></a>[<strong>RtlUnicodeStringCbCopyN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562913)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcopynex"></a>[<strong>RtlUnicodeStringCbCopyNEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562915)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcopyn"></a>[<strong>RtlUnicodeStringCchCopyN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562928)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcopynex"></a>[<strong>RtlUnicodeStringCchCopyNEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562931)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcopystringn"></a>[<strong>RtlUnicodeStringCbCopyStringN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562918)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcopystringnex"></a>[<strong>RtlUnicodeStringCbCopyStringNEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562919)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcopystringn"></a>[<strong>RtlUnicodeStringCchCopyStringN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562934)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcopystringnex"></a>[<strong>RtlUnicodeStringCchCopyStringNEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562938)</dt>
<dd>
</dd>
</dl></td>
<td><p>Copy a string into a buffer, while limiting the size of the copied string.</p></td>
<td><p></p>
<dl>
<dt><strong>strncpy</strong></dt>
<dd>
</dd>
<dt><strong>wcsncpy</strong></dt>
<dd>
</dd>
</dl></td>
</tr>
<tr class="odd">
<td><p></p>
<dl>
<dt><a href="" id="rtlstringcblength"></a>[<strong>RtlStringCbLength</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562820)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchlength"></a>[<strong>RtlStringCchLength</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562856)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunalignedstringcblength"></a>[<strong>RtlUnalignedStringCbLength</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562895)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunalignedstringcchlength"></a>[<strong>RtlUnalignedStringCchLength</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562897)</dt>
<dd>
</dd>
</dl></td>
<td><p>Determine the length of a supplied string.</p></td>
<td><p></p>
<dl>
<dt><strong>strlen</strong></dt>
<dd>
</dd>
<dt><strong>wcslen</strong></dt>
<dd>
</dd>
</dl></td>
</tr>
<tr class="even">
<td><p></p>
<dl>
<dt><a href="" id="rtlstringcbprintf"></a>[<strong>RtlStringCbPrintf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562824)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbprintfex"></a>[<strong>RtlStringCbPrintfEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562828)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchprintf"></a>[<strong>RtlStringCchPrintf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562859)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchprintfex"></a>[<strong>RtlStringCchPrintfEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562864)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringprintf"></a>[<strong>RtlUnicodeStringPrintf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562961)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringprintfex"></a>[<strong>RtlUnicodeStringPrintfEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562964)</dt>
<dd>
</dd>
</dl></td>
<td><p>Create a formatted text string that is based on a format string and a set of additional function arguments.</p></td>
<td><p></p>
<dl>
<dt><strong>sprintf</strong></dt>
<dd>
</dd>
<dt><strong>swprintf</strong></dt>
<dd>
</dd>
<dt><strong>_snprintf</strong></dt>
<dd>
</dd>
<dt><strong>_snwprintf</strong></dt>
<dd>
</dd>
</dl></td>
</tr>
<tr class="odd">
<td><p></p>
<dl>
<dt><a href="" id="rtlstringcbvprintf"></a>[<strong>RtlStringCbVPrintf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562831)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbvprintfex"></a>[<strong>RtlStringCbVPrintfEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562832)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchvprintf"></a>[<strong>RtlStringCchVPrintf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562865)</dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchvprintfex"></a>[<strong>RtlStringCchVPrintfEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562868)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringvprintf"></a>[<strong>RtlUnicodeStringVPrintf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562983)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringvprintfex"></a>[<strong>RtlUnicodeStringVPrintfEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562988)</dt>
<dd>
</dd>
</dl></td>
<td><p>Create a formatted text string that is based on a format string and one additional function argument.</p></td>
<td><p></p>
<dl>
<dt><strong>vsprintf</strong></dt>
<dd>
</dd>
<dt><strong>vswprintf</strong></dt>
<dd>
</dd>
<dt><strong>_vsnprintf</strong></dt>
<dd>
</dd>
<dt><strong>_vsnwprintf</strong></dt>
<dd>
</dd>
</dl></td>
</tr>
<tr class="even">
<td><p></p>
<dl>
<dt><a href="" id="rtlunicodestringinit"></a>[<strong>RtlUnicodeStringInit</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562954)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringinitex"></a>[<strong>RtlUnicodeStringInitEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562958)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringvalidate"></a>[<strong>RtlUnicodeStringValidate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562977)</dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringvalidateex"></a>[<strong>RtlUnicodeStringValidateEx</strong>](https://msdn.microsoft.com/library/windows/hardware/ff562982)</dt>
<dd>
</dd>
</dl></td>
<td><p>Initialize or validate a [<strong>UNICODE_STRING</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564879) structure.</p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Summary%20of%20Kernel-Mode%20Safe%20String%20Functions%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


