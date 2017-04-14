---
title: FORM\_INFO\_2 Data Structure
author: windows-driver-content
description: FORM\_INFO\_2 Data Structure
ms.assetid: df953fe9-00a2-468a-a2ae-ba8f3fce9982
keywords: ["FORM_INFO_2 data structure WDK printer"]
---

# FORM\_INFO\_2 Data Structure


The print spooler and the Unidrv printer driver are enhanced in Windows Vista to provide better support printer forms in multi-language environments. The spooler supports Multi-language User Interface (MUI) strings for the form display names and the new FORM\_INFO\_2 data structure to include the additional information that you need to support the MUI strings.

The FORM\_INFO\_1 data structure is defined as follows.

```
typedef struct _FORM_INFO_1 { 
  DWORD  Flags; 
  LPTSTR  pName; 
  SIZEL   Size; 
  RECTL   ImageableArea; 
} FORM_INFO_1, *PFORM_INFO_1;
```

In FORM\_INFO\_1, the pName member is the only string field, so you can use it to create the key name that the internal search routines use to locate forms in the internal database and also as the display name that is shown to end users.

The FORM\_INFO\_2 structure, which is defined in the following code example, adds additional fields to provide MUI support.

```
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

FORM\_INFO\_2 adds the pKeyword member to enable the addition of a distinct keyword, one that can be different from the display name.

This structure also enables you to add the resource DLL and resource ID to the forms database by using the pMuiDll and dwResourceId member. When the StringType member has the value of STRING\_MUIDLL and the pMuiDll and dwResourceId members contain the resource DLL and identifier of the display name, the **AddForm** function in the spooler looks up the display name in the DLL and records it internally. When the GetForm or EnumForms function is called with a Level value of 2, the information that is returned in the FORM\_INFO\_2 structure will contain the display name that pDisplayName references and the corresponding language ID in wLangID.

Printer drivers that continue to use the FORM\_INFO\_1 structure when they call AddForm will store only the information that is found in that structure in the forms database. The members in the FORM\_INFO\_2 structure that are not found in the FORM\_INFO\_1 structure will be **NULL** or 0 when queried by a call to GetForm or EnumForms that returns a FORM\_INFO\_2 structure.

For more information about adding printer forms and about using the FORM\_INFO\_1 and FORM\_INFO\_2 data structures, see the Microsoft Windows SDK documentation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20FORM_INFO_2%20Data%20Structure%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


