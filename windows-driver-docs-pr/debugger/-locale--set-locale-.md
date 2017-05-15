---
title: .locale (Set Locale)
description: The .locale command sets the locale or displays the current locale.
ms.assetid: 66c2a522-886f-41ef-ab90-176a3e0b7d88
keywords: [".locale (Set Locale) Windows Debugging"]
topic_type:
- apiref
api_name:
- .locale (Set Locale)
api_type:
- NA
---

# .locale (Set Locale)


The **.locale** command sets the locale or displays the current locale.

``` syntax
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

For more information about locale, see the **setlocale** routine in the MSDN Library.

Remarks
-------

The locale controls how Unicode strings are displayed.

The following examples show the **.locale** command.

```
kd> .locale
Locale: C

kd> .locale E
Locale: English_United States.1252

kd> .locale c
Locale: Catalan_Spain.1252

kd> .locale C
Locale: C
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.locale%20%28Set%20Locale%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




