---
title: PostScript Printer Standard Features
description: The PostScript printer standard features are the common ones that are provided by most PostScript printers.
ms.assetid: F904B8DD-7790-44FA-8C20-BCC3720B3528
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PostScript Printer Standard Features


The PostScript printer standard features are the common ones that are provided by most PostScript printers.

The standard features are identified by predefined names that the PPD language recognizes, and the following table shows the mappings between the feature names and the standard keyword used in the PPD files.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Feature name</th>
<th>Default Print Schema feature keyword</th>
<th>Description</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Collate</p>
<ul>
<li><p>true</p></li>
<li><p>false</p></li>
</ul></td>
<td>DocumentCollate</td>
<td><p>Page collation</p>
<ul>
<li><p>Collated</p></li>
<li><p>Uncollated</p></li>
</ul></td>
<td><p>Optional</p>
<p>If not specified, collation is not supported.</p></td>
</tr>
<tr class="even">
<td>JCLResolution</td>
<td>PageResolution</td>
<td>Page resolution</td>
<td>At least one kind of Resolution feature (JCLResolution or Resolution) is required. At least one option must be specified.</td>
</tr>
<tr class="odd">
<td><p>Duplex</p>
<ul>
<li><p>DuplexTumble</p></li>
<li><p>DuplexNoTumble</p></li>
<li><p>Any other option</p></li>
</ul></td>
<td>JobDuplexAllDocumentsContiguously</td>
<td><p>Two-sided printing</p>
<ul>
<li><p>TwoSidedShortEdge</p></li>
<li><p>TwoSidedLongEdge</p></li>
<li><p>OneSided</p></li>
</ul></td>
<td><p>Optional</p>
<p>If not specified, only single sided printing is supported.</p></td>
</tr>
<tr class="even">
<td>InputSlot</td>
<td>JobInputBin</td>
<td>Types of input bins</td>
<td><p>Required</p>
<p>Customized input bin names must be 24 characters or less.</p></td>
</tr>
<tr class="odd">
<td>MediaType</td>
<td>PageMediatype</td>
<td>Types of printing media</td>
<td><p>Optional</p>
<p>If not specified, the printer’s default medium is always used.</p></td>
</tr>
<tr class="even">
<td>OutputBin</td>
<td>JobOutputBin</td>
<td>Types of output bins</td>
<td><p>Optional</p>
<p>If not specified, the print system does not attempt to select an output bin.</p></td>
</tr>
<tr class="odd">
<td>PageSize</td>
<td>PageMediaSize</td>
<td>Paper sizes</td>
<td><p>Required</p>
<p>At least one option must be specified.</p></td>
</tr>
<tr class="even">
<td>Stapling</td>
<td>JobStapleAllDocuments</td>
<td>Stapling types</td>
<td>Optional</td>
</tr>
</tbody>
</table>

 

## Related topics
[Pscript Minidrivers](pscript-minidrivers.md)  
[Standard Options](standard-options.md)  



