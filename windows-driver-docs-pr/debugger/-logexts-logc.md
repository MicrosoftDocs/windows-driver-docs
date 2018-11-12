---
title: logexts.logc
description: The logexts.logc extension displays all API categories, displays all APIs in a specific category, or enables and disables the logging of APIs in one or more categories.
ms.assetid: b0132055-da13-45a8-8e83-06ddcb8b90d7
keywords: ["logexts.logc Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- logexts.logc
api_type:
- NA
ms.localizationpriority: medium
---

# !logexts.logc


The **!logexts.logc** extension displays all API categories, displays all APIs in a specific category, or enables and disables the logging of APIs in one or more categories.

```dbgcmd
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

```dbgcmd
0:000> !logexts.logc e *
```

The following command will disable the logging of category 7:

```dbgcmd
0:000> !logexts.logc d 7
```

The following command will enable the logging of categories 13 and 15:

```dbgcmd
0:000> !logexts.logc e 13 15
```

The following command will display all APIs belonging to category 3:

```dbgcmd
0:000> !logexts.logc p 3
```

 

 





