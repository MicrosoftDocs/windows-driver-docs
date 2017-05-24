---
title: .ignore\_missing\_pages (Suppress Missing Page Errors)
description: The .ignore\_missing\_pages command suppresses the error messages when a Kernel Memory Dump has missing pages.
ms.assetid: 74f4944e-6f0b-4541-b32f-a2da58df7f03
keywords: ["Suppress Missing Page Errors (.ignore_missing_pages) command", ".ignore_missing_pages (Suppress Missing Page Errors) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .ignore_missing_pages (Suppress Missing Page Errors)
api_type:
- NA
---

# .ignore\_missing\_pages (Suppress Missing Page Errors)


The **.ignore\_missing\_pages** command suppresses the error messages when a Kernel Memory Dump has missing pages.

``` syntax
.ignore_missing_pages 0
.ignore_missing_pages 1
.ignore_missing_pages 
```

## <span id="ddk_meta_suppress_missing_page_errors_dbg"></span><span id="DDK_META_SUPPRESS_MISSING_PAGE_ERRORS_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Displays all missing page errors while debugging a Kernel Memory Dump. This is the default behavoir of the debugger.

<span id="_______1"></span> **1**  
Suppresses the display of missing page errors while debugging a Kernel Memory Dump.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Dump file debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to debug these dump files, see [Kernel Memory Dump](kernel-memory-dump.md).

Remarks
-------

Without parameters, **.ignore\_missing\_pages** displays the current status of this setting.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.ignore_missing_pages%20%28Suppress%20Missing%20Page%20Errors%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




