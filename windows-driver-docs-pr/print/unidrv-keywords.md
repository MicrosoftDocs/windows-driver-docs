---
title: Unidrv Keywords
description: Unidrv Keywords
ms.assetid: b76fcf53-cd75-4e85-a7a2-00a69cc82a97
---

# Unidrv Keywords


Unidrv plug-ins should use strings as they appear in the GPD view (not the GDL view) of the configuration file for calls to methods on the helper interface. In addition, Unidrv-provided features are preceded by a percent sign (%). The following table lists the simulated features that are supported.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Feature name</th>
<th align="left">Options</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">%MetafileSpooling</td>
<td align="left"><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td align="left"><p>Enable EMF spooling.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>%PageOrder</strong></p></td>
<td align="left"><p>&quot;FrontToBack&quot;</p>
<p>&quot;BackToFront&quot;</p></td>
<td align="left"><p>Specify the order in which pages are printed.</p>
<p>This feature is available only if the print processor is able to perform EMF spooling.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>%PagePerSheet</strong></p></td>
<td align="left"><p></p>
&quot;1&quot;, &quot;2&quot;, &quot;4&quot;, 6&quot;,
&quot;9&quot;, &quot;16&quot;, &quot;Booklet&quot;</td>
<td align="left"><p>Specify the number of logical pages that are printed on a physical page. The &quot;Booklet&quot; option is available only if the duplex feature is defined.</p>
<p>This feature is available only if the print processor is able to perform EMF spooling.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>%TextAsGraphics</strong></p></td>
<td align="left"><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td align="left"><p>Print text as graphics.</p>
<p>Document-sticky.</p></td>
</tr>
</tbody>
</table>

 

Some GPD syntax is expanded at parse time to create features and options. The most common syntax that falls into this category is the \***MemConfigKB** keyword. Others include the \***MemConfigMB**, \***MemoryConfigKB**, and \***Installable** keywords.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Unidrv%20Keywords%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




