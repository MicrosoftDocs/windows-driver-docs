---
title: IPrintOemCommon COM Interface
description: IPrintOemCommon COM Interface
ms.assetid: 1d4b2f77-6682-4a4b-8d7f-34acd03523e1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrintOemCommon COM Interface


The `IPrintOemCommon` COM interface enables a plug-in to specify or get device information. This interface provides functionality that is common between the user interface and rendering plug-ins.

The following table lists and describes all the methods that the `IPrintOemCommon` interface defines.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>IPrintOemCommon::DevMode</strong></p></td>
<td><p>Performs operations on private DEVMODEW members.</p></td>
</tr>
<tr class="even">
<td><p><strong>IPrintOemCommon::GetInfo</strong></p></td>
<td><p>Returns a plug-in&#39;s identification information.</p></td>
</tr>
</tbody>
</table>

 

For information about how these methods are implemented for UI plug-ins, see [IPrintOemUI COM Interface](iprintoemui-com-interface.md).

 

 




