---
title: Unidrv Keywords
description: Unidrv Keywords
ms.assetid: b76fcf53-cd75-4e85-a7a2-00a69cc82a97
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<th>Feature name</th>
<th>Options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>%MetafileSpooling</td>
<td><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td><p>Enable EMF spooling.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="even">
<td><p><strong>%PageOrder</strong></p></td>
<td><p>&quot;FrontToBack&quot;</p>
<p>&quot;BackToFront&quot;</p></td>
<td><p>Specify the order in which pages are printed.</p>
<p>This feature is available only if the print processor is able to perform EMF spooling.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="odd">
<td><p><strong>%PagePerSheet</strong></p></td>
<td><p></p>
&quot;1&quot;, &quot;2&quot;, &quot;4&quot;, 6&quot;,
&quot;9&quot;, &quot;16&quot;, &quot;Booklet&quot;</td>
<td><p>Specify the number of logical pages that are printed on a physical page. The &quot;Booklet&quot; option is available only if the duplex feature is defined.</p>
<p>This feature is available only if the print processor is able to perform EMF spooling.</p>
<p>Document-sticky.</p></td>
</tr>
<tr class="even">
<td><p><strong>%TextAsGraphics</strong></p></td>
<td><p></p>
&quot;True&quot;
&quot;False&quot;</td>
<td><p>Print text as graphics.</p>
<p>Document-sticky.</p></td>
</tr>
</tbody>
</table>

 

Some GPD syntax is expanded at parse time to create features and options. The most common syntax that falls into this category is the \***MemConfigKB** keyword. Others include the \***MemConfigMB**, \***MemoryConfigKB**, and \***Installable** keywords.

 

 




