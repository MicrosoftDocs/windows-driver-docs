---
title: .locale (Set Locale)
description: The .locale command sets the locale or displays the current locale.
keywords: [".locale (Set Locale) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .locale (Set Locale)
api_type:
- NA
---

# .locale (Set Locale)


The **.locale** command sets the locale or displays the current locale.

```dbgcmd
.locale [Locale] 
```

## <span id="ddk_meta_set_locale_dbg"></span><span id="DDK_META_SET_LOCALE_DBG"></span>Parameters


<span id="_______Locale______"></span><span id="_______locale______"></span><span id="_______LOCALE______"></span> *Locale*   
Specifies the locale that you want. If you omit this parameter, the debugger displays the current locale.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For more information about locale, see the **setlocale** routine reference page.

## Remarks

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

 

 





