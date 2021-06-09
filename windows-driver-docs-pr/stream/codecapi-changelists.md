---
title: CODECAPI\_CHANGELISTS
description: CODECAPI\_CHANGELISTS
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
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-kse_node" data-raw-source="[&lt;strong&gt;KSE_NODE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-kse_node)"><strong>KSE_NODE</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](/windows-hardware/drivers/ddi/_stream/index).

The driver uses the AVStream [**KsGenerateEvents**](/windows-hardware/drivers/ddi/ks/nf-ks-ksgenerateevents) to post a list of GUIDs that changed.

### See Also

[**KsGenerateEvents**](/windows-hardware/drivers/ddi/ks/nf-ks-ksgenerateevents), [CODECAPI\_ALLSETTINGS](codecapi-allsettings.md), [CODECAPI\_SETALLDEFAULTS](codecapi-setalldefaults.md)

