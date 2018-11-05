---
title: cppexr
description: The cppexr extension displays the contents of a C++ exception record.
ms.assetid: 568c98e9-31d9-4c49-9b7a-bc8eccfed24a
keywords: ["exception records", "cppexr Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- cppexr
api_type:
- NA
ms.localizationpriority: medium
---

# !cppexr


The **!cppexr** extension displays the contents of a C++ exception record.

```dbgsyntax
    !cppexr Address 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the C++ exception record to display.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about exceptions, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md), the Windows Driver Kit (WDK) documentation, the Windows SDK documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.) Use the [**.exr**](-exr--display-exception-record-.md) command to display other exception records.

Remarks
-------

The **!cppexr** extension displays information that is related to a C++ exception that the target encounters, including the exception code, the address of the exception, and the exception flags. This exception must be one of the standard C++ exceptions that are defined in Msvcrt.dll.

You can typically obtain the *Address* parameter by using the [**!analyze -v**](-analyze.md) command.

The **!cppexr** extension is useful for determining the type of a C++ exception.

 

 





