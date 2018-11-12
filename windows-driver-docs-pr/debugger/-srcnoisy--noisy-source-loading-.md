---
title: .srcnoisy (Noisy Source Loading)
description: The .srcnoisy command controls the verbosity level for source file loading.
ms.assetid: c57e0d0a-7903-455a-9a92-fab75f10ca80
keywords: [".srcnoisy (Noisy Source Loading) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .srcnoisy (Noisy Source Loading)
api_type:
- NA
ms.localizationpriority: medium
---

# .srcnoisy (Noisy Source Loading)


The **.srcnoisy** command controls the verbosity level for source file loading.

```dbgcmd
.srcnoisy [Options]
```

## <span id="ddk_meta_noisy_source_loading_dbg"></span><span id="DDK_META_NOISY_SOURCE_LOADING_DBG"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Can be any one of the following options:

<span id="0"></span>0  
Disables the display of extra messages.

<span id="1"></span>1  
Displays information about the progress of source file loading and unloading.

<span id="2"></span>2  
Displays information about the progress of symbol file loading and unloading.

<span id="3"></span>3  
Displays all information displayed by options 1 and 2.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

With no parameters, **.srcnoisy** will display the current status of noisy source loading.

Noisy source loading should not be confused with noisy symbol loading -- that is controlled by the [**!sym noisy**](-sym.md) extension and by other means of controlling the [SYMOPT\_DEBUG](symbol-options.md#symopt-debug) setting.

 

 





