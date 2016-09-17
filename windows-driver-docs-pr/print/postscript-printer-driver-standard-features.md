---
title: PostScript Printer Standard Features
author: windows-driver-content
description: The PostScript printer standard features are the common ones that are provided by most PostScript printers.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: F904B8DD-7790-44FA-8C20-BCC3720B3528
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PostScript%20Printer%20Standard%20Features%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


