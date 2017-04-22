---
title: AddEuro
author: windows-driver-content
description: AddEuro
ms.assetid: 1d27fbb0-787f-4fb2-8a1c-3c68598d6d41
keywords:
- minidrivers WDK Pscript , AddEuro feature
- AddEuro feature WDK print
- Euro symbol WDK print
- European Union symbol WDK print
- ADHasEuro
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# AddEuro


## <a href="" id="ddk-addeuro-gg"></a>


The Euro symbol, as shown in the following figure, is the currency symbol for the basic monetary unit used in countries/regions of the European Union.

![figure of the euro symbol](images/euro.png)

The AddEuro feature adds this symbol to the printer's device font. When AddEuro is enabled, a Euro symbol that appears on a display device will also be printed on paper when the document is sent to a printer. If this feature is unavailable or disabled, a user who selects an unaliased device font will be able to see a Euro symbol on the screen, but will see a large circular dot on paper. With this feature enabled, a user can print the Euro symbol, whether or not it is available in the printer's device font.

AddEuro uses a private [*PPD*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-postscript-printer-description--ppd-) keyword, \***ADHasEuro**, to allow printer manufacturers to set the best defaults.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Keyword and Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>*<strong>ADHasEuro</strong>: True</p></td>
<td><p>The printer already has a built-in Euro symbol that does not need to be downloaded. With this value, AddEuro is disabled by default.</p></td>
</tr>
<tr class="even">
<td><p>*<strong>ADHasEuro</strong>: False</p></td>
<td><p>The printer does not have a built-in Euro symbol; if called for by an application, this symbol should be downloaded. With this value, AddEuro is enabled by default, regardless of PostScript version.</p></td>
</tr>
</tbody>
</table>

 

If the \***ADHasEuro** keyword does not appear, the AddEuro feature is enabled by default for printers with PostScript versions before 3011, and disabled by default for versions 3011 or after.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20AddEuro%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


