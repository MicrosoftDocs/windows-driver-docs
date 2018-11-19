---
title: Adding Forms to the Forms Database
description: Adding Forms to the Forms Database
ms.assetid: ac306f05-6150-4e47-9272-e81e658a1ea6
keywords:
- additional forms WDK Unidrv
- adding forms to Unidrv printer driver
- Unidrv, forms added to database
- GPD files WDK Unidrv , forms added to database
- printer forms WDK
- forms WDK printer
- special forms WDK printer
- special paper sizes WDK printer
- paper sizes WDK forms
- custom forms WDK printer
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding Forms to the Forms Database


If your printer supports additional forms, you can add them to your Unidrv printer driver by describing them in the GPD file for the printer driver. If you use a resource ID with the \*rcNameId field and a resource DLL for the form display name string, your driver will automatically use the new localization enhancements features that the Windows Vista Unidrv printer driver provides. Unidrv printer driver plug-ins also benefit from these changes to the spooler automatically and do not require any additional modifications. For more information about these enhancements, see [Changes to Printer Forms in Windows Vista](changes-to-printer-forms-in-windows-vista.md).

If you are not using a resource DLL for the localizable strings in the GPD file, you should remove the localizable strings, store them in a resource DLL, and replace the strings with the corresponding resource ID in the GPD file.

The following code example is an excerpt from a GPD file that uses a resource ID for the display name.

```GDL
*Feature: PaperSize
{
    *Option: Option2
    {
 *rcNameID: 259
        (form definition)
    }
    (other form definitions).
}
```

Inside the Unidrv printer driver that is provided with Windows Vista, the FORM\_INFO\_2 structure is populated by data that is read from the GPD file, as the following table shows. If the GPD file for your printer already contains the information that is required to fill in this structure, you do not need to change anything to use the new features that the Windows Vista Unidrv printer driver provides.

```cpp
typedef struct _FORM_INFO_2 { 
  DWORD    Flags; 
  LPTSTR   pName; 
  SIZEL    Size; 
  RECTL    ImageableArea;
  LPCSTR   pKeyword;
  DWORD    StringType;
  LPCTSTR  pMuiDll;
  DWORD    dwResourceId;
  LPCTSTR  pDisplayName;
  LANGID   wLangId; 
} FORM_INFO_2, *PFORM_INFO_2;
```

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>FORM_INFO_2 field</th>
<th>GPD value used</th>
<th>Field description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Flags</p></td>
<td><p>FORM_PRINTER</p>
<p>This value is assigned by the Unidrv printer driver because it is adding the form. A value from the GPD file is not used for this field.</p></td>
<td><p>The properties of structure.</p></td>
</tr>
<tr class="even">
<td><p>pName</p></td>
<td><p>The localized name of the form as obtained from the resource DLL or from the *rcName field in the GPD file.</p></td>
<td><p>A pointer to a null-terminated string that specifies the name of the form. This string is used to identify the form in the forms database and must be unique.</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>Size information that is read from the *PageDimensions option in the GPD file.</p></td>
<td><p>The width and height, in thousandths of millimeters, of the form.</p></td>
</tr>
<tr class="even">
<td><p>ImageableArea</p></td>
<td><p>Size information that is read from the *PrintableArea option in the GPD file.</p></td>
<td><p>The width and height, in thousandths of millimeters, of the area of the page on which the printer can print.</p></td>
</tr>
<tr class="odd">
<td><p>pKeyword</p></td>
<td><p>The value of the *Option entry in the GPD file.</p></td>
<td><p>A pointer to a non-localizable string identifier of the form. When passed to AddForm or SetForm, this pointer gives the caller a way to identify the form in all locales.</p></td>
</tr>
<tr class="even">
<td><p>StringType</p></td>
<td><p>STRING_MUIDLL</p>
<p>If the GPD uses the *rcNameId option and the form name is available from the resource DLL, the STRING_MUIDLL value is assigned. If the *rcName option is used in the GPD file instead, the value for this field is STRING_NONE. A value from the GPD file is not used for this field.</p></td>
<td><p>Specifies how a localized display name for the form is obtained at runtime.</p></td>
</tr>
<tr class="odd">
<td><p>pMuiDll</p></td>
<td><p>The value of the *ResourceDLL entry in GPD file if the *rcNameId option is used. If the *rcName option is used in the GPD file instead, the value for this field is <strong>NULL</strong>.</p></td>
<td><p>The MUI localized resource DLL that contains the localized display name when <strong>StringType</strong> contains STRING_MUIDLL.</p></td>
</tr>
<tr class="even">
<td><p>dwResourceId</p></td>
<td><p>The value of the *rcNameID entry in the GPD file. If the *rcName option is used in the GPD file instead, the value for this field is 0.</p></td>
<td><p>The resource ID, in <strong>pMuiDll</strong>, of the form&#39;s display name when <strong>StringType</strong> contains STRING_MUIDLL.</p></td>
</tr>
<tr class="odd">
<td><p>pDisplayName</p></td>
<td><p><strong>NULL</strong></p>
<p>This field is not used.</p></td>
<td><p>The form&#39;s display name in the language that <strong>wLangId</strong> specifies when <strong>StringType</strong> contains STRING_LANGPAIR.</p></td>
</tr>
<tr class="even">
<td><p>wLangId</p></td>
<td><p>0</p>
<p>This field is not used.</p></td>
<td><p>The language of <strong>pDisplayName</strong> when <strong>StringType</strong> contains STRING_LANGPAIR.</p></td>
</tr>
</tbody>
</table>

 

 

 




