---
title: CODECAPI\_CHANGELISTS
description: CODECAPI\_CHANGELISTS
ms.assetid: c1b65350-32b9-4c94-a6d4-74cb9959d737
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# CODECAPI\_CHANGELISTS


## <span id="ddk_codecapi_changelists_ks"></span><span id="DDK_CODECAPI_CHANGELISTS_KS"></span>


The CODECAPI\_CHANGELISTS event is used to return a list of GUIDs that have changed as a result of a property "set" call, such as [CODECAPI\_ALLSETTINGS](codecapi-allsettings.md) and [CODECAPI\_SETALLDEFAULTS](codecapi-setalldefaults.md), or an encoder setting property.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Event descriptor type</th>
<th>Event value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes (query supported)</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561937" data-raw-source="[&lt;strong&gt;KSE_NODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561937)"><strong>KSE_NODE</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561750" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561750)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877).

The driver uses the AVStream [**KsGenerateEvents**](https://msdn.microsoft.com/library/windows/hardware/ff562597) to post a list of GUIDs that changed.

### See Also

[**KsGenerateEvents**](https://msdn.microsoft.com/library/windows/hardware/ff562597), [CODECAPI\_ALLSETTINGS](codecapi-allsettings.md), [CODECAPI\_SETALLDEFAULTS](codecapi-setalldefaults.md)

 

 





