---
title: .locale (Set Locale)
description: The .locale command sets the locale or displays the current locale.
ms.assetid: 66c2a522-886f-41ef-ab90-176a3e0b7d88
keywords: [".locale (Set Locale) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .locale (Set Locale)
api_type:
- NA
ms.localizationpriority: medium
---

# .locale (Set Locale)


The **.locale** command sets the locale or displays the current locale.

```dbgcmd
.locale [Locale] 
```

## <span id="ddk_meta_set_locale_dbg"></span><span id="DDK_META_SET_LOCALE_DBG"></span>Parameters


<span id="_______Locale______"></span><span id="_______locale______"></span><span id="_______LOCALE______"></span> *Locale*   
Specifies the locale that you want. If you omit this parameter, the debugger displays the current locale.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about locale, see the **setlocale** routine reference page.

Remarks
-------

The locale controls how Unicode strings are displayed.

The following examples show the **.locale** command.

```dbgcmd
kd> .locale
Locale: C

kd> .locale E
Locale: English_United States.1252

kd> .locale c
Locale: Catalan_Spain.1252

kd> .locale C
Locale: C
```

 

 





