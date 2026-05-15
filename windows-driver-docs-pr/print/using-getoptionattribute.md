---
title: Using GetOptionAttribute
description: Using GetOptionAttribute
keywords:
- GetOptionAttribute
ms.date: 02/21/2024
ms.topic: concept-article
---

# Using GetOptionAttribute

[!include[Print Support Apps](../includes/print-support-apps.md)]

This function is supported only for PostScript Printer Driver (PPD) features. If a certain attribute isn't available, **GetOptionAttribute** returns E_INVALIDARG.

## Output parameters for general option attributes

In the following table, the *pdwDataType* parameter takes values of the [**EATTRIBUTE_DATATYPE**](/windows-hardware/drivers/ddi/printoem/ne-printoem-_eattribute_datatype) enumerated type.

| General option attribute | Output parameters |
|--|--|
| **DisplayName** | *pdwDataType*: kADT_UNICODE<br><br>*pbData*: null-terminated Unicode string of the option keyword name's translation string<br><br>*pcbNeeded*: byte count of the Unicode string pointed to by pbData (including the null terminator)<br><br>This option attribute is available to any option that **EnumOptions** can return on a PPD feature. |
| **Invocation** | *pdwDataType*: kADT_BINARY<br><br>*pbData*: byte array for the option's InvocationValue<br><br>*pcbNeeded*: byte count of the binary data pointed to by pbData<br><br>This option attribute is available to any option that **EnumOptions** can return on a PPD feature. If the option's InvocationValue is empty, the function sets *pdwDataType* as above, set *pcbNeeded* = 0, and then return S_OK. |
| **OrderDependencyValue** | *pdwDataType*: kADT_LONG<br><br>*pbData*: the relative order specified by the PPD's OrderDependency or NonUIOrderDependency keyword for this option. Notice that the first parameter of these keywords is a real number that is converted to a LONG and returned.<br><br>*pcbNeeded*: sizeof(LONG)<br><br>This option attribute is available only for an option that has an OrderDependency or*NonUIOrderDependency entry in the PPD, and the entry doesn't omit optionKeyword. |
| **OrderDependencySection** | *pdwDataType*: kADT_ASCII<br><br>*pbData*: null-terminated ASCII string containing one of following section names: "ExitServer" "Prolog" "DocumentSetup" "PageSetup" "JCLSetup" "AnySetup"<br><br>*pcbNeeded*: byte count of the ASCII string pointed to by pbData (including the null terminator)<br><br>This option attribute is available only for an option that has an OrderDependency or NonUIOrderDependency entry in the PPD, and the entry doesn't omit optionKeyword. |

## Output parameters for specific option attributes

In addition to the general option attributes described earlier, the option attributes listed in the following tables can have limitations on when they're available. Some attributes are available to all options of a specific PPD feature, while others are available only to specific options of their PPD feature. Any such limitations are listed for each option attribute.

| Keyword | Option attribute | Output parameters |
|--|--|--|
| **InputSlot** |  |  |
|  | **RequiresPageRegion** | *pdwDataType*: kADT_BOOL<br><br>*pbData*: **TRUE** if PageRegion invocation code must be sent with the InputSlot invocation code, and **FALSE** otherwise. This is based on the PPD's RequiresPageRegion keyword. If the keyword is omitted for this input slot option, **TRUE** is returned for this attribute.<br><br>*pcbNeeded*: sizeof(BOOL)<br><br>This option attribute is available to any option of the "InputSlot" PPD feature, except for the driver-generated option "*UseFormTrayTable". |
| **OutputBin** |  |  |
|  | **OutputOrderReversed** | *pdwDataType*: kADT_BOOL<br><br>*pbData*: **TRUE** if the binOption's output order is "Reverse", and **FALSE** if the output order is "Normal". This is based on the PPD's DefaultOutputOrder and ageStackOrder keywords.<br><br>*pcbNeeded*: sizeof(BOOL)<br><br>This option attribute is available to any option of the "OutputBin" PPD feature. |
| **PageSize**  |  |  |
|  | **ImageableArea** | *pdwDataType*: kADT_RECT<br><br>*pbData*: a bounding box of the PageSize option's imageable area, as specified by the PPD's ImageableArea keyword, is returned in a RECT structure, whose **left** and **bottom** members contain the llx and lly values, and whose **right** and **top** members contain the urx and ury values. All values are in microns. The PPD's llx, and lly values are rounded up to the nearest integer before being converted into microns. The PPD's urx and ury values are rounded down to the nearest integer before being converted into microns.<br><br>*pcbNeeded*: sizeof(RECT)<br><br>This option attribute is available to any option of "PageSize" PPD feature, except the "CustomPageSize" option.  |
|  | **PaperDimension** | *pdwDataType*: kADT_SIZE<br><br>*pbData*: the physical dimension of the PageSize option, as specified by the PPD's PaperDimension keyword, is returned in a SIZE structure, whose cx member contains the width value and whose cy member contains the height value. All values are in microns.<br><br>*pcbNeeded*: sizeof(SIZE)<br><br>This option attribute is available to any option of the "PageSize" PPD feature, except the "CustomPageSize" option. |
| **PageSize: CustomPageSize** |  |  |
|  | **HWMargins** | *pdwDataType*: kADT_RECT<br><br>*pbData*: the four values specified by the PPD's HWMargins keyword are returned in a RECT structure. All values are in microns.<br><br>*pcbNeeded*: sizeof(RECT)<br><br>This option attribute is available only to the "CustomPageSize" option of the "PageSize" PPD feature. |
|  | **MaxMediaHeight** | *pdwDataType*: kADT_DWORD<br><br>*pbData*: the value specified by the PPD's *MaxMediaHeight keyword, in microns.<br><br>*pcbNeeded*: sizeof(DWORD)<br><br>This option attribute is available only to the "CustomPageSize" option of the "PageSize" PPD feature. |
|  | **MaxMediaWidth** | *pdwDataType*: kADT_DWORD<br><br>*pbData*: the value specified by the PPD's MaxMediaWidth keyword, in microns.<br><br>*pcbNeeded*: sizeof(DWORD)<br><br>This option attribute is available only to the "CustomPageSize" option of the "PageSize" PPD feature. |
|  | **ParamCustomPageSize** | *pdwDataType*: kADT_CUSTOMSIZEPARAMS<br><br>*pbData*: an array of CUSTOMPARAM_MAX elements, where each element is a [**CUSTOMSIZEPARAM**](/windows-hardware/drivers/ddi/printoem/ns-printoem-_customsizeparam) structure. Each element of this array stores values specified in the PPD's ParamCustomPageSize keyword's paramOption entry. For paramOption other than "Orientation", lMinVal and lMaxVal values are in microns. For "Orientation", lMinVal and lMaxVal values are in the range of [0, 3].<br><br>*pcbNeeded*: sizeof(CUSTOMSIZEPARAM) * CUSTOMPARAM_MAX<br><br>This option attribute is available only to the "CustomPageSize" option of the "PageSize" PPD feature.<br><br>For more information, see following note on ParamCustomPageSize. |
| **InstalledMemory** |  |  |
|  | **VMOption** | *pdwDataType*: kADT_DWORD<br><br>*pbData*: the value specified by the PPD's VMOption keyword, or 0 if the PPD doesn't specify the VMOption keyword for this option.<br><br>*pcbNeeded*: sizeof(DWORD)<br><br>This option attribute is available to any option of the "InstalledMemory" PPD feature. |
|  |**FCacheSize**  | *pdwDataType*: kADT_DWORD<br><br>*pbData*: the value specified by the PPD's FCacheSize keyword, or 0 if the PPD doesn't specify the FCacheSize keyword for this option.<br><br>*pcbNeeded*: sizeof(DWORD)<br><br>This option attribute is available to any option of the "InstalledMemory" PPD feature. |

### Note on ParamCustomPageSize

Here's some sample code that shows how to obtain the PPD file's original order, min, and max values of the "ParamCustomPageSize Width" entry. The CUSTOMPARAM_WIDTH constant, which is defined in printoem.h, indicates the offset of the [**CUSTOMSIZEPARAM**](/windows-hardware/drivers/ddi/printoem/ns-printoem-_customsizeparam) structure that contains the information related to the Width entry. This structure is one of CUSTOMPARAM\_MAX CUSTOMSIZEPARAM structures that form an array of such structures. The printoem.h header defines a set of constants named CUSTOMPARAM_XXX listing the offsets of the structures in this array (Width, Height, WidthOffset, HeightOffset, and Orientation).

```cpp
PCUSTOMSIZEPARAM  pCSParam;

pCSParam = (PCUSTOMSIZEPARAM)pbData + CUSTOMPARAM_WIDTH;

order = pCSParam->dwOrder;
// Convert lMinVal and lMaxVal from microns to points.
//   To convert microns to inches, divide by 25400.
//   To convert inches to points, multiply by 72.
min = pCSParam->lMinVal / 25400.0 * 72.0;
max = pCSParam->lMaxVal / 25400.0 * 72.0;
```
