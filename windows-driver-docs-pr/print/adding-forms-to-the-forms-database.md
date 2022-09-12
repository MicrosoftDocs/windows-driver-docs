---
title: Add forms to the forms database
description: Provides information about how to add forms to the forms database.
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
ms.date: 09/06/2022
---

# Add forms to the forms database

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

Inside the Unidrv printer driver that is provided with Windows Vista, the **FORM_INFO_2** structure is populated by data that is read from the GPD file, as the following table shows. If the GPD file for your printer already contains the information that is required to fill in this structure, you do not need to change anything to use the new features that the Windows Vista Unidrv printer driver provides.

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

|FORM_INFO_2 field  |GPD value used  |Field description  |
|---------|---------|---------|
|Flags     |  FORM_PRINTER<br><br>This value is assigned by the Unidrv printer driver because it is adding the form. A value from the GPD file is not used for this field.       |   The properties of structure.      |
|pName     |    The localized name of the form as obtained from the resource DLL or from the *rcName field in the GPD file.     |   A pointer to a null-terminated string that specifies the name of the form. This string is used to identify the form in the forms database and must be unique.      |
|Size     |     Size information that is read from the *PageDimensions option in the GPD file.    |      The width and height, in thousandths of millimeters, of the form.   |
|ImageableArea     |     Size information that is read from the *PrintableArea option in the GPD file.    |    The width and height, in thousandths of millimeters, of the area of the page on which the printer can print.     |
|pKeyword     |     The value of the *Option entry in the GPD file.    |     A pointer to a non-localizable string identifier of the form. When passed to AddForm or SetForm, this pointer gives the caller a way to identify the form in all locales.    |
|StringType     |   STRING_MUIDLL<br><br>If the GPD uses the \*rcNameId option and the form name is available from the resource DLL, the STRING_MUIDLL value is assigned. If the \*rcName option is used in the GPD file instead, the value for this field is STRING_NONE. A value from the GPD file is not used for this field.      |      Specifies how a localized display name for the form is obtained at runtime.   |
|pMuiDll     |     The value of the \*ResourceDLL entry in GPD file if the \*rcNameId option is used. If the \*rcName option is used in the GPD file instead, the value for this field is **NULL**.    |     The MUI localized resource DLL that contains the localized display name when **StringType** contains STRING_MUIDLL.    |
|dwResourceId     |    The value of the \*rcNameID entry in the GPD file. If the *rcName option is used in the GPD file instead, the value for this field is 0.     |    The resource ID, in **pMuiDll**, of the form's display name when **StringType** contains STRING_MUIDLL.     |
|pDisplayName     |    **NULL**<br><br>This field is not used.     |   The form's display name in the language that **wLangId** specifies when **StringType** contains STRING_LANGPAIR.      |
|wLangId     |   0<br><br>This field is not used.      |     The language of **pDisplayName** when **StringType** contains STRING_LANGPAIR.    |
