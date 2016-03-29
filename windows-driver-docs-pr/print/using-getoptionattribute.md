---
title: Using GetOptionAttribute
description: Using GetOptionAttribute
ms.assetid: d35f0811-d572-422c-8672-ffd29bf69efa
keywords: ["GetOptionAttribute"]
---

# Using GetOptionAttribute


## <a href="" id="ddk-using-getoptionattribute-gg"></a>


This function is supported only for PPD features. If a certain attribute is not available, **GetOptionAttribute** returns E\_INVALIDARG.

In the following table, the *pdwDataType* parameter takes values of the [**EATTRIBUTE\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff548692) enumerated type.

### Output Parameters for General Option Attributes

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">General Option Attribute</th>
<th align="left">Output Parameters</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>DisplayName</strong></p></td>
<td align="left"><p><em>*pdwDataType</em>: kADT_UNICODE</p>
<p><em>pbData</em>: null-terminated Unicode string of the option keyword name's translation string</p>
<p><em>*pcbNeeded</em>: byte count of the Unicode string pointed to by <em>pbData</em> (including the null terminator)</p>
<p>This option attribute is available to any option that <strong>EnumOptions</strong> can return on a PPD feature.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Invocation</strong></p></td>
<td align="left"><p><em>*pdwDataType</em>: kADT_BINARY</p>
<p><em>pbData</em>: byte array for the option's InvocationValue.</p>
<p><em>*pcbNeeded</em>: byte count of the binary data pointed to by <em>pbData</em></p>
<p>This option attribute is available to any option that <strong>EnumOptions</strong> can return on a PPD feature. If the option's InvocationValue is empty, the function will set <em>pdwDataType</em> as above, set <em>*pcbNeeded</em> = 0, and then return S_OK.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>OrderDependencyValue</strong></p></td>
<td align="left"><p>*pdwDataType: kADT_LONG</p>
<p><em>*pbData</em>: the relative order specified by the PPD's *OrderDependency or *NonUIOrderDependency keyword for this option. Notice that the first parameter of these keywords is a real number that is converted to a LONG and returned.</p>
<p><em>*pcbNeeded</em>: <strong>sizeof</strong>(LONG)</p>
<p>This option attribute is available only for an option that has an *OrderDependency or *NonUIOrderDependency entry in the PPD, and the entry does not omit optionKeyword.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>OrderDependencySection</strong></p></td>
<td align="left"><p><em>*pdwDataType</em>: kADT_ASCII</p>
<p><em>pbData</em>: null-terminated ASCII string containing one of following section names: &quot;ExitServer&quot; &quot;Prolog&quot; &quot;DocumentSetup&quot; &quot;PageSetup&quot; &quot;JCLSetup&quot; &quot;AnySetup&quot;.</p>
<p><em>*pcbNeeded</em>: byte count of the ASCII string pointed to by <em>pbData</em> (including the null terminator)</p>
<p>This option attribute is available only for an option that has an *OrderDependency or *NonUIOrderDependency entry in the PPD, and the entry does not omit optionKeyword.</p></td>
</tr>
</tbody>
</table>

 

### Output Parameters for Specific Option Attributes

In addition to the general option attributes described earlier, the option attributes listed in the following tables can have limitations on when they are available. Some attributes are available to all options of a specific PPD feature, while others are available only to specific options of their PPD feature. Any such limitations are listed for each option attribute.

Feature
Option Attribute
Output Parameters
Keyword
\*InputSlot

**RequiresPageRegion**

\*pdwDataType: kADT\_BOOL

*\*pbData*: **TRUE** if \*PageRegion invocation code must be sent with the \*InputSlot invocation code, and **FALSE** otherwise. This is based on the PPD's \*RequiresPageRegion keyword. If the keyword is omitted for this input slot option, **TRUE** is returned for this attribute.

*\*pcbNeeded*: **sizeof**(BOOL)

This option attribute is available to any option of the "InputSlot" PPD feature, except for the driver-generated option "\*UseFormTrayTable".

\*OutputBin

**OutputOrderReversed**

\*pdwDataType: kADT\_BOOL

*\*pbData*: **TRUE** if the binOption's output order is "Reverse", and **FALSE** if the output order is "Normal". This is based on the PPD's \*DefaultOutputOrder and \*PageStackOrder keywords.

*\*pcbNeeded*: **sizeof**(BOOL)

This option attribute is available to any option of the "OutputBin" PPD feature.

\*PageSize

**ImageableArea**

\*pdwDataType: kADT\_RECT

*\*pbData*: a bounding box of the PageSize option's imageable area, as specified by the PPD's \*ImageableArea keyword, is returned in a RECT structure (defined in the Microsoft Windows SDK documentation), whose **left** and **bottom** members contain the llx and lly values, and whose **right** and **top** members contain the urx and ury values. All values are in microns. The PPD's llx, and lly values are rounded up to the nearest integer before being converted into microns. The PPD's urx and ury values are rounded down to the nearest integer before being converted into microns.

*\*pcbNeeded*: **sizeof**(RECT)

This option attribute is available to any option of "PageSize" PPD feature, except the "CustomPageSize" option.

**PaperDimension**

\*pdwDataType: kADT\_SIZE

*\*pbData*: the physical dimension of the PageSize option, as specified by the PPD's \*PaperDimension keyword, is returned in a SIZE structure (defined in the Windows SDK documentation), whose **cx** member contains the width value and whose **cy** member contains the height value. All values are in microns.

*\*pcbNeeded*: **sizeof**(SIZE)

This option attribute is available to any option of the "PageSize" PPD feature, except the "CustomPageSize" option.

\*PageSize: CustomPageSize

**HWMargins**

\*pdwDataType: kADT\_RECT

*\*pbData*: the four values specified by the PPD's \*HWMargins keyword are returned in a RECT structure (defined in the Windows SDK documentation). All values are in microns.

*\*pcbNeeded*: **sizeof**(RECT)

This option attribute is available only to the "CustomPageSize" option of the "PageSize" PPD feature.

**MaxMediaHeight**

*\*pdwDataType*: kADT\_DWORD

*\*pbData*: the value specified by the PPD's \*MaxMediaHeight keyword, in microns.

*\*pcbNeeded*: **sizeof**(DWORD)

This option attribute is available only to the "CustomPageSize" option of the "PageSize" PPD feature.

**MaxMediaWidth**

*\*pdwDataType*: kADT\_DWORD

*\*pbData*: the value specified by the PPD's \*MaxMediaWidth keyword, in microns.

*\*pcbNeeded*: **sizeof**(DWORD)

This option attribute is available only to the "CustomPageSize" option of the "PageSize" PPD feature.

**ParamCustomPageSize**

*\*pdwDataType*: kADT\_CUSTOMSIZEPARAMS

*pbData*: an array of CUSTOMPARAM\_MAX elements, where each element is a [**CUSTOMSIZEPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff547337) structure. Each element of this array stores values specified in the PPD's \*ParamCustomPageSize keyword's paramOption entry. For paramOption other than "Orientation", lMinVal and lMaxVal values are in microns. For "Orientation", lMinVal and lMaxVal values are in the range of \[0, 3\].

*\*pcbNeeded*: **sizeof**(CUSTOMSIZEPARAM) \* CUSTOMPARAM\_MAX

This option attribute is available only to the "CustomPageSize" option of the "PageSize" PPD feature.

See following note.

\*InstalledMemory

**VMOption**

*\*pdwDataType*: kADT\_DWORD

*\*pbData*: the value specified by the PPD's \*VMOption keyword, or 0 if the PPD does not specify the \*VMOption keyword for this option.

*\*pcbNeeded*: **sizeof**(DWORD)

This option attribute is available to any option of the "InstalledMemory" PPD feature.

**FCacheSize**

*\*pdwDataType*: kADT\_DWORD

*\*pbData*: the value specified by the PPD's \*FCacheSize keyword, or 0 if the PPD does not specify the \*FCacheSize keyword for this option.

*\*pcbNeeded*: **sizeof**(DWORD)

This option attribute is available to any option of the "InstalledMemory" PPD feature.

 

### Note on ParamCustomPageSize

Here is some sample code that shows how to obtain the PPD file's original order, min, and max values of the "\*ParamCustomPageSize Width" entry. The CUSTOMPARAM\_WIDTH constant, which is defined in printoem.h, indicates the offset of the [**CUSTOMSIZEPARAM**](https://msdn.microsoft.com/library/windows/hardware/ff547337) structure that contains the information related to the Width entry. This structure is one of CUSTOMPARAM\_MAX CUSTOMSIZEPARAM structures that form an array of such structures. The printoem.h header defines a set of constants named CUSTOMPARAM\_XXX listing the offsets of the structures in this array (Width, Height, WidthOffset, HeightOffset, and Orientation).

```
PCUSTOMSIZEPARAM  pCSParam;

pCSParam = (PCUSTOMSIZEPARAM)pbData + CUSTOMPARAM_WIDTH;

order = pCSParam->dwOrder;
// Convert lMinVal and lMaxVal from microns to points.
//   To convert microns to inches, divide by 25400.
//   To convert inches to points, multiply by 72.
min = pCSParam->lMinVal / 25400.0 * 72.0;
max = pCSParam->lMaxVal / 25400.0 * 72.0;
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Using%20GetOptionAttribute%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




