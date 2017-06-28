---
title: logexts.logc
description: The logexts.logc extension displays all API categories, displays all APIs in a specific category, or enables and disables the logging of APIs in one or more categories.
ms.assetid: b0132055-da13-45a8-8e83-06ddcb8b90d7
keywords: ["logexts.logc Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- logexts.logc
api_type:
- NA
---

# !logexts.logc


The **!logexts.logc** extension displays all API categories, displays all APIs in a specific category, or enables and disables the logging of APIs in one or more categories.

```
!logexts.logc e Categories 
!logexts.logc d Categories 
!logexts.logc p Category 
!logexts.logc 
```

## <span id="ddk__logexts_logc_dbg"></span><span id="DDK__LOGEXTS_LOGC_DBG"></span>Parameters


<span id="_______e______"></span><span id="_______E______"></span> **e**   
Enables logging of the specified categories.

<span id="_______d______"></span><span id="_______D______"></span> **d**   
Disables logging of the specified categories.

<span id="_______Categories______"></span><span id="_______categories______"></span><span id="_______CATEGORIES______"></span> *Categories*   
Specifies the categories to be enabled or disabled. If multiple categories are listed, separate them with spaces. An asterisk (\*) can be used to indicate all categories.

<span id="_______p______"></span><span id="_______P______"></span> **p**   
Displays all APIs that belong to the specified category.

<span id="_______Category______"></span><span id="_______category______"></span><span id="_______CATEGORY______"></span> *Category*   
Specifies the category whose APIs will be displayed. Only one category can be specified with the **p** option.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Logexts.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Logexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Logger and LogViewer](logger-and-logviewer.md).

Remarks
-------

Without any options, **!logexts.logc** will display the current list of available categories and will indicate which ones are enabled and disabled.

If a category is disabled, the hooks for all APIs in that category will be removed so there is no longer any performance overhead. COM hooks are not removed, because they cannot be re-enabled at will.

Enabling only certain categories can be useful when you are only interested in a particular type of interaction that the program is having with Windows (for example, file operations). This reduces the log file size and also reduces the effect that Logger has on the execution speed of the process.

The following command will enable the logging of all categories:

```
0:000> !logexts.logc e *
```

The following command will disable the logging of category 7:

```
0:000> !logexts.logc d 7
```

The following command will enable the logging of categories 13 and 15:

```
0:000> !logexts.logc e 13 15
```

The following command will display all APIs belonging to category 3:

```
0:000> !logexts.logc p 3
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!logexts.logc%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




