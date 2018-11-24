---
title: Pscript5 Keywords
description: Pscript5 Keywords
ms.assetid: a5f4384a-8d78-4dc6-969b-f7a1fa6cb5e7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pscript5 Keywords


Feature and option names that are passed to the helper interface from a Pscript5 plug-in are the string names of the features and options as they are defined in the PPD file. In addition, certain reserved strings are defined for features that are implemented in the Pscript5 core driver that are not represented in the PPD file. Note that all of the options that are listed in the following table can be determined at run-time by calling **EnumOptions**. However, for features that require numeric settings in ranges, the **EnumOptions** method will return a **NULL** value in its *pOptionList* parameter and a count of zero options in \**pdwNumOptions*.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Feature name</th>
<th>Options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>%AddEuro</p></td>
<td><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td><p>Add the Euro symbol to device fonts.</p>
<p>Printer-sticky.</p>
<p>Requires PostScript Level 2. See note 1 following this table.</p></td>
</tr>
<tr class="even">
<td><p>%CtrlDAfter</p></td>
<td><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td><p>Send CTRL+D after each job.</p>
<p>Printer-sticky.</p></td>
</tr>
<tr class="odd">
<td><p>%CtrlDBefore</p></td>
<td><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td><p>Send CTRL+D before each job.</p>
<p>Printer-sticky.</p></td>
</tr>
<tr class="even">
<td><p>%CustomPageSize</p></td>
<td><p>Custom page size options have a complex format. See note 2 following this table.</p></td>
<td><p>Read or specify a custom page size setting. Setting this feature also causes the <strong>dmPaperSize</strong> member of the public <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837" data-raw-source="[&lt;strong&gt;DEVMODEW&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552837)"><strong>DEVMODEW</strong></a> structure to be reset to DMPAPER_CUSTOMSIZE (indicating a PS custom size), and sets the DM_PAPERSIZE bit flag. This feature can be read only if the public DEVMODEW structure indicates that a custom paper size is in use.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="odd">
<td><p>%GraphicsAsTrueGray</p></td>
<td><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td><p>Convert gray graphics to PostScript gray.</p>
<p>Printer-sticky.</p></td>
</tr>
<tr class="even">
<td><p>%JobTimeout</p></td>
<td><p>Numeric (see note 3 following this table)</p>
<p>&quot;0&quot; through &quot;2147483647&quot;</p></td>
<td><p>Specify the job timeout in seconds.</p>
<p>Printer-sticky.</p></td>
</tr>
<tr class="odd">
<td><p>%MaxFontSizeAsBitmap</p></td>
<td><p>Numeric (see note 3)</p>
<p>&quot;0&quot; through &quot;32767&quot;</p></td>
<td><p>Specify the maximum font size to download as a bitmap.</p>
<p>Printer-sticky.</p></td>
</tr>
<tr class="even">
<td><p>%MetafileSpooling</p></td>
<td><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td><p>Enable EMF spooling. Enabling this feature is equivalent to enabling the <strong>Advanced Printing Features</strong> UI option. Note that this feature has constraints that interact with booklet printing, collating, and page ordering. This feature is given lowest precedence when resolving against any of those features.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="odd">
<td><p>%MinFontAsOutline</p></td>
<td><p>Numeric (see note 3 following this table)</p>
<p>&quot;0&quot; through &quot;32,767&quot;</p></td>
<td><p>Specify the minimum font size that should be downloaded as outline.</p>
<p>Printer-sticky.</p></td>
</tr>
<tr class="even">
<td><p>%Mirroring</p></td>
<td><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td><p>Mirror output by reversing the horizontal coordinates.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="odd">
<td><p>%Negative</p></td>
<td><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td><p>Reverse the black and white regions on the printed page.</p>
<p>Document-sticky.</p>
<p>Requires a black and white printer, not color.</p></td>
</tr>
<tr class="even">
<td><p>%Orientation</p></td>
<td><p></p>
&quot;Portrait&quot;
&quot;Landscape&quot;
&quot;RotatedLandscape&quot;</td>
<td><p>Specify the output orientation. Configuring the orientation by using this technique changes both the private and public <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837" data-raw-source="[&lt;strong&gt;DEVMODEW&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552837)"><strong>DEVMODEW</strong></a> structure values, when used with the <strong>IPrintCoreHelperPS</strong> interface. This warning does not apply to the <strong>IPrintCoreUI2</strong> interface.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="odd">
<td><p>%OutputFormat</p></td>
<td><p></p>
&quot;Speed&quot;
&quot;Portability&quot;
&quot;EPS&quot;
&quot;Archive&quot;</td>
<td><p>Specify the PostScript output format. The behavior of output format is the same as that defined for <strong>IPrintCoreUI2</strong>.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="even">
<td><p>%OutputProtocol</p></td>
<td><p></p>
&quot;ASCII&quot;
&quot;BCP&quot;
&quot;TBCP&quot;
&quot;Binary&quot;</td>
<td><p>Specify the protocol the printer will use to print jobs. The BCP and TBCP options are available only if supported. <strong>EnumOptions</strong> includes only the values that are supported. The output protocol can also be determined by checking the &quot;Protocols&quot; global attribute.</p>
<p>Printer-sticky.</p></td>
</tr>
<tr class="odd">
<td><p>%OutputPSLevel</p></td>
<td><p></p>
&quot;1&quot;
&quot;2&quot;
&quot;3&quot;</td>
<td><p>Specify which PostScript language level to generate for this print job. Available options are limited to values that are equal to or less than the language level of the device that is specified in the &quot;LanguageLevel&quot; global attribute.</p>
<p>Document-sticky.</p>
<p>Requires PostScript Level 2 or higher. See note 1 following this table.</p></td>
</tr>
<tr class="even">
<td><p>%PageOrder</p></td>
<td><p></p>
&quot;FrontToBack&quot;
&quot;BackToFront&quot;</td>
<td><p>Specify the order in which to print the pages. If EMF spooling is not available, this feature will not be listed when calling <strong>EnumFeatures</strong>, and attempts to read or write the setting for this feature will return E_FAIL. Additionaly, BackToFront will be constrained if the %MetafileSpooling feature is set to False.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="odd">
<td><p>%PagePerSheet</p></td>
<td><p></p>
&quot;1&quot;, &quot;2&quot;, &quot;4&quot;, &quot;6&quot;,
&quot;9&quot;, &quot;16&quot;, &quot;Booklet&quot;</td>
<td><p>Booklet printing is available only if duplexing is available. Setting the &quot;Booklet&quot; option will cause duplexing to be turned on if it is not on already. If duplex is turned off and booklet printing is selected, the option will be forced to 2-up. If metafile spooling is disabled, it will be represented as a constraint on booklet printing. If EMF spooling is unavailable because the print processor is being used, booklet printing will be unavailable. In that situation, booklet printing will not be listed in <strong>EnumOptions</strong>, and <strong>SetOptions</strong> will return E_FAIL if the caller requests &quot;%PagePerSheet&quot; to be set to &quot;Booklet&quot;.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="even">
<td><p>%PSErrorHandler</p></td>
<td><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td><p>Send PostScript error handler.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="odd">
<td><p>%PSMemory</p></td>
<td><p>Numeric (see note 3 following this table)</p>
<p>For PostScript Level 1 printers, range is &quot;172&quot; through &quot;2097151&quot;.</p>
<p>For Postscript Level 2 or 3 printers, range is &quot;249&quot; through &quot;2097151&quot;.</p></td>
<td><p>Specifies the number of kilobytes of virtual memory that are available on the device. Note that the values are indicated in kilobytes, and not bytes. Also, note that the valid ranges differ for level 1 and level 2 printers. Attempting to set values outside of these ranges will fail with an HRESULT of E_FAIL.</p>
<p>Printer-sticky.</p></td>
</tr>
<tr class="even">
<td><p>%TextTrueGray</p></td>
<td><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td><p>Convert gray text to PostScript gray.</p>
<p>Printer-sticky.</p></td>
</tr>
<tr class="odd">
<td><p>%TTDownloadFormat</p></td>
<td><p></p>
&quot;Automatic&quot;
&quot;Outline&quot;
&quot;Bitmap&quot;
&quot;NativeTrueType&quot;</td>
<td><p>Specify the TrueType font downloading format. NativeTrueType is available and listed in <strong>EnumOptions</strong> only if the &quot;TTRasterizer&quot; global attribute indicates support for &quot;Type42&quot;.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="even">
<td><p>%WaitTimeout</p></td>
<td><p>Numeric (see note 3 following this table)</p>
<p>&quot;0&quot; through &quot;2147483647&quot;</p></td>
<td><p>Specify the wait timeout value in seconds.</p>
<p>Printer-sticky.</p></td>
</tr>
</tbody>
</table>

 

**Note**   1
If the stated requirements are not met for a feature, that feature will not be listed in **EnumFeatures**, and attempts to get or set that feature will cause E\_FAIL to be returned. This note applies to %AddEuro, %Negative, and %OutputPSLevel.

 

**Note**   2 (%CustomPageSize)
Custom page size format is identical to that described in **IPrintCoreUI2**. **EnumOptions** returns an empty list of options.

 

**Note**   3
Numeric values are represented as ANSI strings that contain only digit characters. Sign symbols are not allowed. For example, "300" is valid, but "-20", "20.5", and "+300" are all invalid. This note applies to %JobTimeout, %MaxFontSizeAsBitmap, %MinFontAsOutline, %PSMemory, and %WaitTimeout.

 

 

 




