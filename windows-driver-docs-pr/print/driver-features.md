---
title: Driver Features
description: Driver Features
ms.assetid: 56efebda-970f-4885-9c5f-1eac97aecfdd
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Features





Driver features are non-PPD features that are synthesized by the driver (for example, the **%OutputFormat** feature). To avoid name conflicts with PPD feature keywords, all driver feature keyword names are preceded by a "%" character. Driver feature/option keywords are also case sensitive.

To obtain a list of all driver feature keywords that the driver supports, a plug-in can call EnumFeatures, which will return the feature keyword list containing both driver features and PPD features. The plug-in can then search for feature keyword names that begin with the "%" prefix to get the driver feature list.

The following table lists the currently supported driver features. Each row in the table lists a driver feature keyword, shows the supported options, states whether the feature's options can be enumerated in a call to EnumOptions, and provides a brief description.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Driver Feature</th>
<th>Supported Options</th>
<th>Enum Options?</th>
<th>Description and Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>%AddEuro</strong></p></td>
<td><p>&quot;True&quot;</p>
<p>&quot;False&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Add the Euro symbol to device fonts.</p>
<p>This feature is supported only for Level 2+ printers. For Level 1 printers, <strong>SetOptions</strong> ignores this feature, and <strong>GetOptions</strong> always returns &quot;False&quot;.</p>
<p>Printer-sticky</p></td>
</tr>
<tr class="even">
<td><p><strong>%CtrlDAfter</strong></p></td>
<td><p>&quot;True&quot;</p>
<p>&quot;False&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Send Ctrl-D after each job.</p>
<p>Printer-sticky</p></td>
</tr>
<tr class="odd">
<td><p><strong>%CtrlDBefore</strong></p></td>
<td><p>&quot;True&quot;</p>
<p>&quot;False&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Send Ctrl-D before each job.</p>
<p>Printer-sticky</p></td>
</tr>
<tr class="even">
<td><p><strong>%CustomPageSize</strong></p></td>
<td><p>See Note (1) below for more information.</p></td>
<td><p>No</p></td>
<td><p>Specify PostScript custom page size parameters.</p>
<p>Document-sticky</p>
<p>See Note (2) below.</p></td>
</tr>
<tr class="odd">
<td><p><strong>%GraphicsTrueGray</strong></p></td>
<td><p>&quot;True&quot;</p>
<p>&quot;False&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Convert gray graphics to PostScript gray.</p>
<p>Printer-sticky</p></td>
</tr>
<tr class="even">
<td><p><strong>%JobTimeout</strong></p></td>
<td><p>A NULL-terminated ANSI string containing decimal digit characters that represents the unsigned integer number of seconds for the time-out, in the range 0 through 2,147,483,647.</p>
<p>For <strong>SetOptions</strong>, extra tab or space characters before or after the decimal digits are allowed, but a sign symbol is not allowed.</p></td>
<td><p>No</p></td>
<td><p>Specify the job time-out value.</p>
<p>Printer-sticky</p></td>
</tr>
<tr class="odd">
<td><p><strong>%MaxFontSizeAsBitmap</strong></p></td>
<td><p>A NULL-terminated ANSI string containing decimal digit characters that represents the unsigned integer number of pixels, in the range 0 through 32,767.</p>
<p>For <strong>SetOptions</strong>, extra tab or space characters before or after the decimal digits are allowed, but a sign symbol is not allowed.</p></td>
<td><p>No</p></td>
<td><p>Specify the maximum font size to download as a bitmap.</p>
<p>Printer-sticky</p></td>
</tr>
<tr class="even">
<td><p><strong>%MetafileSpooling</strong></p></td>
<td><p>&quot;True&quot;</p>
<p>&quot;False&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Enable/disable advanced printing features.</p>
<p>Document-sticky</p>
<p>See Note (3) below.</p></td>
</tr>
<tr class="odd">
<td><p><strong>%MinFontSizeAsOutline</strong></p></td>
<td><p>A NULL-terminated ANSI string containing decimal digit characters that represents the unsigned integer number of pixels, in the range 0 through 32,767.</p>
<p>For <strong>SetOptions</strong>, extra tab or space characters before or after the decimal digits are allowed, but a sign symbol is not allowed.</p></td>
<td><p>No</p></td>
<td><p>Specify the minimum font size to download as outline.</p>
<p>Printer-sticky</p></td>
</tr>
<tr class="even">
<td><p><strong>%Mirroring</strong></p></td>
<td><p>&quot;True&quot;</p>
<p>&quot;False&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Mirror output by reversing the horizontal coordinates.</p>
<p>Document-sticky</p></td>
</tr>
<tr class="odd">
<td><p><strong>%Negative</strong></p></td>
<td><p>&quot;True&quot;</p>
<p>&quot;False&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Produce negative output by reversing values for black and white. This feature is supported only for black and white printers. For color printers, <strong>SetOptions</strong> ignores this feature, and <strong>GetOptions</strong> always returns &quot;False&quot;.</p>
<p>Document-sticky</p></td>
</tr>
<tr class="even">
<td><p><strong>%Orientation</strong></p></td>
<td><p>&quot;Portrait&quot;, &quot;Landscape&quot;, &quot;RotatedLandscape&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Specify the output orientation.</p>
<p>Document-sticky</p></td>
</tr>
<tr class="odd">
<td><p><strong>%OutputFormat</strong></p></td>
<td><p>&quot;Speed&quot;, &quot;Portability&quot;, &quot;EPS&quot;, &quot;Archive&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Specify the PostScript output format.</p>
<p>Document-sticky</p>
<p>See Note (6) below.</p></td>
</tr>
<tr class="even">
<td><p><strong>%OutputProtocol</strong></p></td>
<td><p>&quot;ASCII&quot;, &quot;BCP&quot;, &quot;TBCP&quot;, &quot;Binary&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Specify the protocol the printer will use for print jobs. PostScript printers are assumed to support &quot;ASCII&quot; and &quot;Binary&quot;, so these options are always available. The &quot;BCP&quot; and &quot;TBCP&quot; options are available only if they are supported. (To find this out, check the global attribute &quot;Protocols&quot;.</p>
<p>Printer-sticky</p></td>
</tr>
<tr class="odd">
<td><p><strong>%OutputPSLevel</strong></p></td>
<td><p>&quot;1&quot;, &quot;2&quot;, &quot;3&quot;</p></td>
<td><p>No</p></td>
<td><p>Specify which PostScript language level to use for the print job. The setting will never be greater than the value specified in the &quot;LanguageLevel&quot; global attribute.</p>
<p>Document-sticky</p></td>
</tr>
<tr class="even">
<td><p><strong>%PageOrder</strong></p></td>
<td><p>&quot;FrontToBack&quot;</p>
<p>&quot;BackToFront&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Specify the order in which pages will be printed.</p>
<p>Document-sticky</p>
<p>See Note (4) below.</p></td>
</tr>
<tr class="odd">
<td><p><strong>%PagePerSheet</strong></p></td>
<td><p>&quot;1&quot;, &quot;2&quot;, &quot;4&quot;, &quot;6&quot;,</p>
<p>&quot;9&quot;, &quot;16&quot;, &quot;Booklet&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Specify the number of logical pages per physical sheet. This feature is also known as &quot;N-up&quot; printing.</p>
<p>Document-sticky</p>
<p>See Note (5) below.</p></td>
</tr>
<tr class="even">
<td><p><strong>%PSErrorHandler</strong></p></td>
<td><p>&quot;True&quot;</p>
<p>&quot;False&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Send PostScript error handler.</p>
<p>Document-sticky</p></td>
</tr>
<tr class="odd">
<td><p><strong>%PSMemory</strong></p></td>
<td><p>A NULL-terminated ANSI string containing decimal digit characters that represents the unsigned integer number of kilobytes of PostScript memory, in the range 0 through 2,147,483,647.</p>
<p>For <strong>SetOptions</strong>, extra tab or space characters before or after the decimal digits are allowed, but a sign symbol is not allowed.</p></td>
<td><p>No</p></td>
<td><p>Specify the amount of available PostScript virtual memory.</p>
<p>The core driver requires a certain amount of available PostScript virtual memory for its processing. If <strong>%PSMemory</strong> is set below this minimum, the minimum value will be used as the new value. Currently the minimum value is 172 KB for Level 1 printers and 249 KB for Level 2+ printers.</p>
<p>Printer-sticky</p></td>
</tr>
<tr class="even">
<td><p><strong>%TextTrueGray</strong></p></td>
<td><p>&quot;True&quot;</p>
<p>&quot;False&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Convert gray text to PostScript gray.</p>
<p>Printer-sticky</p></td>
</tr>
<tr class="odd">
<td><p><strong>%TTDownloadFormat</strong></p></td>
<td><p>&quot;Automatic&quot;, &quot;Outline&quot;, &quot;Bitmap&quot;, &quot;NativeTrueType&quot;</p></td>
<td><p>Yes</p></td>
<td><p>Specify TrueType font downloading format. &quot;NativeTrueType&quot; is supported only when the &quot;TTRasterizer&quot; global attribute indicates support for &quot;Type42&quot;.</p>
<p>Document-sticky</p></td>
</tr>
<tr class="even">
<td><p><strong>%WaitTimeout</strong></p></td>
<td><p>A NULL-terminated ANSI string containing decimal digit characters that represents the unsigned integer number of seconds for the time-out, in the range 0 through 2,147,483,647.</p>
<p>For <strong>SetOptions</strong>, extra tab or space characters before or after the decimal digits are allowed, but a sign symbol is not allowed.</p></td>
<td><p>No</p></td>
<td><p>Specify wait time-out value.</p>
<p>Printer-sticky</p></td>
</tr>
</tbody>
</table>

 

### Notes on Driver Feature Keywords

1.  The **%CustomPageSize** driver feature has five option values: x, y, WidthOffset, HeightOffset, and FeedDirection. Please refer to section 5.16 of the *PostScript Printer Description File Format Specification, Version 4.3*, for a detailed explanation of these parameters.

    A **%CustomPageSize** entry contains the **%CustomPageSize** keyword, together with values for the x, y, WidthOffset, HeightOffset, and FeedDirection options. The first item is the %CustomPageSize keyword, followed by a NULL character. The values for x, y, WidthOffset, and HeightOffset follow this keyword, and appear as substrings of unsigned decimal digits, each representing the number of PostScript points for the corresponding option value. Each of these numeric values is followed by one or more space or tab characters. The final item in the string is the value for FeedDirection, which is terminated by a NULL character. The options for FeedDirection are "LongEdge", "ShortEdge" (corresponding to orientations 0 and 1), and "LongEdgeFlip", "ShortEdgeFlip" (corresponding to orientations 2 and 3). Check the **\*LeadingEdge** PPD feature keyword for supported feed directions.

    For **GetOptions**, the output buffer pointed to by *pmszFeatureOptionBuf* is as described in the previous paragraph. In the following example, the value for x is 612, the value for y is 792, the values for WidthOffset and HeightOffset are both 0, and the value for FeedDirection is "ShortEdge".

    ```cpp
    "%CustomPageSize\0612 792 0 0 ShortEdge\0"
    ```

    For **SetOptions**, extra tab or space characters before or after the decimal digits are allowed, but a sign symbol is not allowed. Otherwise, the input buffer pointed to by *pmszFeatureOptionBuf* should be constructed as described above.

2.  <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td><pre><code></code></pre></td>
    </tr>
    </tbody>
    </table>

3.  The **%CustomPageSize** driver feature is supported only if all three of the following conditions are met:
    1.  The PPD file contains the **\*CustomPageSize** feature.
    2.  The **\*PPD-Adobe** keyword has a value greater than or equal to 4.3, or **\*UseHWMargin**: **False** is specified to indicate a roll-fed device.
    3.  The **\*PageSize** PPD feature's currently selected option is CustomPageSize.

4.  On Windows NT 4.0, the **%MetafileSpooling** feature is always supported. On Windows 2000 and later operating system versions, this feature is supported only when spooler EMF spooling is enabled.

    When supported, setting this feature's option to "False" causes changes to the following EMF-related features:

    1.  On Windows 2000 and later operating system releases, if **%PagePerSheet** is "Booklet", it will be changed to "1".
    2.  If Collate is set to "True" (which can be set either directly in the public portion of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure or by calling **SetOptions** on the **\*Collate** PPD feature), but the Collate feature is not currently available, Collate will be set to "False".
    3.  On Windows 2000 and later operating system releases, if **%PageOrder** is the opposite of the printer's current output order setting, **%PageOrder** will be reversed to the printer's value.

5.  On Windows NT 4.0, the **%PageOrder** driver feature is not supported. On Windows 2000 and later operating system releases, this feature is supported only when spooler EMF spooling is enabled.

    When it is supported, setting this feature can cause the following to occur:

    1.  If the printer's PPD file includes the **\*OutputOrder** feature keyword, then its option selection will be changed to match the output order of the new setting for the **%PageOrder** feature. This is done to prevent the spooler from performing unnecessary page order simulation.
    2.  If the printer's PPD file does not include the **\*OutputOrder** feature, and the new setting for the **%PageOrder** driver feature is the opposite of the printer's current output order setting, and the **%MetafileSpooling** driver feature is "False", then **%MetafileSpooling** will be reset to "True".

6.  On Windows NT 4.0, the "Booklet" option is not supported for the **%PagePerSheet** driver feature. On Windows 2000 and later operating system releases, the "Booklet" option is supported only when spooler EMF spooling is enabled and the Duplex feature is available.

    When the "Booklet" option is supported, setting the **%PagePerSheet** driver feature to "Booklet" can cause the following changes:

    1.  If the **%MetafileSpooling** driver feature is "False", it will be reset to "True".
    2.  If the **\*Duplex** PPD feature is set to None, the **\*Duplex** feature will be reset to the first non-Simplex option defined in the PPD file.

7.  Except for "EPS" (Encapsulated PostScript), the formats specified in the **%OutputFormat** driver feature are categorized according to the following two characteristics:
    1.  Is the output PostScript code independent of page order?
    2.  Does the output PostScript code contain device control commands, (which usually use the **setpagedevice** operator)?

        <table>
        <colgroup>
        <col width="33%" />
        <col width="33%" />
        <col width="33%" />
        </colgroup>
        <thead>
        <tr class="header">
        <th></th>
        <th>Page Order Independent</th>
        <th>setpagedevice</th>
        </tr>
        </thead>
        <tbody>
        <tr class="odd">
        <td><p>Archive</p></td>
        <td><p>Yes</p></td>
        <td><p>No</p></td>
        </tr>
        <tr class="even">
        <td><p>Portability</p></td>
        <td><p>Yes</p></td>
        <td><p>Yes</p></td>
        </tr>
        <tr class="odd">
        <td><p>Speed</p></td>
        <td><p>No</p></td>
        <td><p>Yes</p></td>
        </tr>
        </tbody>
        </table>

         

When **GetOptions** is called on driver feature keywords, if a requested feature keyword is not recognized, or if the feature keyword is recognized but not supported in the current [*document-sticky*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-document-sticky) or [*printer-sticky*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-printer-sticky) mode (see [Replacing Driver-Supplied Property Sheet Pages](replacing-driver-supplied-property-sheet-pages.md)), the feature will simply be ignored and the output buffer will not contain its feature/option keyword pair.

For example, suppose the **GetOptions** method is called, and the *pmszFeaturesRequested* input buffer contains the following string (in MULTI\_SZ format):

```cpp
"Resolution\0%CustomPageSize\0Unknown_Name\0%Orientation\0\0"
```

After **GetOption** returns, the *pmszFeatureOptionBuf* output buffer could contain this string (also in MULTI\_SZ format):

```cpp
"Resolution\0300dpi\0%CustomPageSize\0612 792 0 0 ShortEdge\0%Orientation\0RotatedLandscape\0\0"
```

Notice that the Unknown\_Name feature (which does not exist) listed in the first string does not appear in the second string, since it was not recognized by the Pscript driver. The other features, Resolution, **%CustomPageSize**, and **%Orientation**, appear in the output string, together with their current options, which are "300dpi", "612 792 0 0 ShortEdge", and "RotatedLandscape", respectively. See Driver Features for an explanation of the **%CustomPageSize** options.

When **SetOptions** is called on driver feature keywords, if a requested feature keyword or its option keyword in the input buffer pointed to by *pmszFeatureOptionBuf* is not recognized, or the feature is recognized but not supported in the current document-sticky or printer-sticky mode (see [Replacing Driver-Supplied Property Sheet Pages](replacing-driver-supplied-property-sheet-pages.md)), or both the feature keyword and its option keyword are recognized but the option keyword is invalid for that feature (for example, trying to set **%TTDownloadFormat** to "NativeTrueType" on a printer that does not support Type42 TTRasterizer), then that feature/option pair will be ignored and the current option for that feature will continue to be in effect.

The order of feature/option keyword pairs in the buffer pointed to by *pmszFeatureOptionBuf* can affect the result of the **SetOptions** call. For example, the following two different orders have different results.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th><em>pmszFeatureOptionBuf</em></th>
<th>%PagePerSheet</th>
<th>%MetafileSpooling</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>&quot;%MetafileSpooling\0False\0%PagePerSheet\0Booklet\0\0&quot;</p></td>
<td><p>&quot;Booklet&quot;</p></td>
<td><p>&quot;True&quot;</p></td>
</tr>
<tr class="even">
<td><p>&quot;%PagePerSheet\0Booklet\0%MetafileSpooling\0False\0\0&quot;</p></td>
<td><p>&quot;1&quot;</p></td>
<td><p>&quot;False&quot;</p></td>
</tr>
</tbody>
</table>

 

For an explanation of why these results occur, see Note 3 on **%MetafileSpooling**, above.

 

 




