---
title: .srcnoisy (Noisy Source Loading)
description: The .srcnoisy command controls the verbosity level for source file loading.
ms.assetid: c57e0d0a-7903-455a-9a92-fab75f10ca80
keywords: [".srcnoisy (Noisy Source Loading) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .srcnoisy (Noisy Source Loading)
api_type:
- NA
---

# .srcnoisy (Noisy Source Loading)


The **.srcnoisy** command controls the verbosity level for source file loading.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.srcnoisy%20%28Noisy%20Source%20Loading%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




