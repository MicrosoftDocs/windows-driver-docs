---
title: Summary of Kernel-Mode Safe String Functions
description: Summary of Kernel-Mode Safe String Functions
ms.assetid: 71b67d88-2a9a-4c9d-b64c-5fd7fe7e5cda
keywords: ["safe string functions WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Summary of Kernel-Mode Safe String Functions





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
<dt><a href="" id="rtlstringcbcat"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562795" data-raw-source="[&lt;strong&gt;RtlStringCbCat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562795)"><strong>RtlStringCbCat</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbcatex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562799" data-raw-source="[&lt;strong&gt;RtlStringCbCatEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562799)"><strong>RtlStringCbCatEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcat"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562834" data-raw-source="[&lt;strong&gt;RtlStringCchCat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562834)"><strong>RtlStringCchCat</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcatex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562835" data-raw-source="[&lt;strong&gt;RtlStringCchCatEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562835)"><strong>RtlStringCchCatEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcat"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562898" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562898)"><strong>RtlUnicodeStringCat</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcatex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562899" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCatEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562899)"><strong>RtlUnicodeStringCatEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcatstring"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562901" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCatString&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562901)"><strong>RtlUnicodeStringCatString</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcatstringex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562902" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCatStringEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562902)"><strong>RtlUnicodeStringCatStringEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcatstringn"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562908" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCbCatStringN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562908)"><strong>RtlUnicodeStringCbCatStringN</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcatstringnex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562910" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCbCatStringNEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562910)"><strong>RtlUnicodeStringCbCatStringNEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcatstringn"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562924" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCchCatStringN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562924)"><strong>RtlUnicodeStringCchCatStringN</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcatstringnex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562927" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCchCatStringNEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562927)"><strong>RtlUnicodeStringCchCatStringNEx</strong></a></dt>
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
<dt><a href="" id="rtlstringcbcatn"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562801" data-raw-source="[&lt;strong&gt;RtlStringCbCatN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562801)"><strong>RtlStringCbCatN</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbcatnex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562802" data-raw-source="[&lt;strong&gt;RtlStringCbCatNEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562802)"><strong>RtlStringCbCatNEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcatn"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562836" data-raw-source="[&lt;strong&gt;RtlStringCchCatN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562836)"><strong>RtlStringCchCatN</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcatnex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562837" data-raw-source="[&lt;strong&gt;RtlStringCchCatNEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562837)"><strong>RtlStringCchCatNEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcatn"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562905" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCbCatN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562905)"><strong>RtlUnicodeStringCbCatN</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcatnex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562906" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCbCatNEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562906)"><strong>RtlUnicodeStringCbCatNEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcatn"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562921" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCchCatN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562921)"><strong>RtlUnicodeStringCchCatN</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcatnex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562923" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCchCatNEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562923)"><strong>RtlUnicodeStringCchCatNEx</strong></a></dt>
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
<dt><a href="" id="rtlstringcbcopy"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562805" data-raw-source="[&lt;strong&gt;RtlStringCbCopy&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562805)"><strong>RtlStringCbCopy</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbcopyex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562807" data-raw-source="[&lt;strong&gt;RtlStringCbCopyEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562807)"><strong>RtlStringCbCopyEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbcopyunicodestring"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562815" data-raw-source="[&lt;strong&gt;RtlStringCbCopyUnicodeString&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562815)"><strong>RtlStringCbCopyUnicodeString</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbcopyunicodestringex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562817" data-raw-source="[&lt;strong&gt;RtlStringCbCopyUnicodeStringEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562817)"><strong>RtlStringCbCopyUnicodeStringEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcopy"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562841" data-raw-source="[&lt;strong&gt;RtlStringCchCopy&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562841)"><strong>RtlStringCchCopy</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcopyex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562843" data-raw-source="[&lt;strong&gt;RtlStringCchCopyEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562843)"><strong>RtlStringCchCopyEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcopyunicodestring"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562851" data-raw-source="[&lt;strong&gt;RtlStringCchCopyUnicodeString&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562851)"><strong>RtlStringCchCopyUnicodeString</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcopyunicodestringex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562852" data-raw-source="[&lt;strong&gt;RtlStringCchCopyUnicodeStringEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562852)"><strong>RtlStringCchCopyUnicodeStringEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcopy"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562942" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCopy&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562942)"><strong>RtlUnicodeStringCopy</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcopyex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562946" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCopyEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562946)"><strong>RtlUnicodeStringCopyEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcopystring"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562948" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCopyString&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562948)"><strong>RtlUnicodeStringCopyString</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcopystringex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562950" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCopyStringEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562950)"><strong>RtlUnicodeStringCopyStringEx</strong></a></dt>
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
<dt><a href="" id="rtlstringcbcopyn"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562811" data-raw-source="[&lt;strong&gt;RtlStringCbCopyN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562811)"><strong>RtlStringCbCopyN</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbcopynex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562813" data-raw-source="[&lt;strong&gt;RtlStringCbCopyNEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562813)"><strong>RtlStringCbCopyNEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcopyn"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562846" data-raw-source="[&lt;strong&gt;RtlStringCchCopyN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562846)"><strong>RtlStringCchCopyN</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchcopynex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562849" data-raw-source="[&lt;strong&gt;RtlStringCchCopyNEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562849)"><strong>RtlStringCchCopyNEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcopyn"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562913" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCbCopyN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562913)"><strong>RtlUnicodeStringCbCopyN</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcopynex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562915" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCbCopyNEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562915)"><strong>RtlUnicodeStringCbCopyNEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcopyn"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562928" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCchCopyN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562928)"><strong>RtlUnicodeStringCchCopyN</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcopynex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562931" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCchCopyNEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562931)"><strong>RtlUnicodeStringCchCopyNEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcopystringn"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562918" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCbCopyStringN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562918)"><strong>RtlUnicodeStringCbCopyStringN</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcbcopystringnex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562919" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCbCopyStringNEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562919)"><strong>RtlUnicodeStringCbCopyStringNEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcopystringn"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562934" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCchCopyStringN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562934)"><strong>RtlUnicodeStringCchCopyStringN</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringcchcopystringnex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562938" data-raw-source="[&lt;strong&gt;RtlUnicodeStringCchCopyStringNEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562938)"><strong>RtlUnicodeStringCchCopyStringNEx</strong></a></dt>
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
<dt><a href="" id="rtlstringcblength"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562820" data-raw-source="[&lt;strong&gt;RtlStringCbLength&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562820)"><strong>RtlStringCbLength</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchlength"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562856" data-raw-source="[&lt;strong&gt;RtlStringCchLength&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562856)"><strong>RtlStringCchLength</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunalignedstringcblength"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562895" data-raw-source="[&lt;strong&gt;RtlUnalignedStringCbLength&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562895)"><strong>RtlUnalignedStringCbLength</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunalignedstringcchlength"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562897" data-raw-source="[&lt;strong&gt;RtlUnalignedStringCchLength&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562897)"><strong>RtlUnalignedStringCchLength</strong></a></dt>
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
<dt><a href="" id="rtlstringcbprintf"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562824" data-raw-source="[&lt;strong&gt;RtlStringCbPrintf&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562824)"><strong>RtlStringCbPrintf</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbprintfex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562828" data-raw-source="[&lt;strong&gt;RtlStringCbPrintfEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562828)"><strong>RtlStringCbPrintfEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchprintf"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562859" data-raw-source="[&lt;strong&gt;RtlStringCchPrintf&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562859)"><strong>RtlStringCchPrintf</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchprintfex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562864" data-raw-source="[&lt;strong&gt;RtlStringCchPrintfEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562864)"><strong>RtlStringCchPrintfEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringprintf"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562961" data-raw-source="[&lt;strong&gt;RtlUnicodeStringPrintf&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562961)"><strong>RtlUnicodeStringPrintf</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringprintfex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562964" data-raw-source="[&lt;strong&gt;RtlUnicodeStringPrintfEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562964)"><strong>RtlUnicodeStringPrintfEx</strong></a></dt>
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
<dt><a href="" id="rtlstringcbvprintf"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562831" data-raw-source="[&lt;strong&gt;RtlStringCbVPrintf&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562831)"><strong>RtlStringCbVPrintf</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcbvprintfex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562832" data-raw-source="[&lt;strong&gt;RtlStringCbVPrintfEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562832)"><strong>RtlStringCbVPrintfEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchvprintf"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562865" data-raw-source="[&lt;strong&gt;RtlStringCchVPrintf&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562865)"><strong>RtlStringCchVPrintf</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlstringcchvprintfex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562868" data-raw-source="[&lt;strong&gt;RtlStringCchVPrintfEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562868)"><strong>RtlStringCchVPrintfEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringvprintf"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562983" data-raw-source="[&lt;strong&gt;RtlUnicodeStringVPrintf&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562983)"><strong>RtlUnicodeStringVPrintf</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringvprintfex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562988" data-raw-source="[&lt;strong&gt;RtlUnicodeStringVPrintfEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562988)"><strong>RtlUnicodeStringVPrintfEx</strong></a></dt>
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
<dt><a href="" id="rtlunicodestringinit"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562954" data-raw-source="[&lt;strong&gt;RtlUnicodeStringInit&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562954)"><strong>RtlUnicodeStringInit</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringinitex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562958" data-raw-source="[&lt;strong&gt;RtlUnicodeStringInitEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562958)"><strong>RtlUnicodeStringInitEx</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringvalidate"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562977" data-raw-source="[&lt;strong&gt;RtlUnicodeStringValidate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562977)"><strong>RtlUnicodeStringValidate</strong></a></dt>
<dd>
</dd>
<dt><a href="" id="rtlunicodestringvalidateex"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff562982" data-raw-source="[&lt;strong&gt;RtlUnicodeStringValidateEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff562982)"><strong>RtlUnicodeStringValidateEx</strong></a></dt>
<dd>
</dd>
</dl></td>
<td><p>Initialize or validate a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879" data-raw-source="[&lt;strong&gt;UNICODE_STRING&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564879)"><strong>UNICODE_STRING</strong></a> structure.</p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>

 

 

 




