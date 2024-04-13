---
title: Search XML Element
description: search XML Element
keywords: ["search XML Element Device and Driver Installation"]
topic_type:
- apiref
ms.topic: reference
api_name:
- search XML Element
api_type:
- NA
ms.date: 10/17/2018
---

# search XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](./difx-guidelines.md).\]

The **search** XML element directs DPInst to search recursively for INF files in specified subdirectories under the DPInst working directory. Subdirectories are specified by one or more [**subDirectory child elements**](subdirectory-xml-element.md).

### Element Tag

```cpp
<search>
```

### XML Attributes

None

### **Element Information**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Parent elements</strong></p></td>
<td align="left"><p><a href="dpinst-xml-element.md" data-raw-source="[&lt;strong&gt;dpinst&lt;/strong&gt;](dpinst-xml-element.md)"><strong>dpinst</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Child elements</strong></p></td>
<td align="left"><p><a href="subdirectory-xml-element.md" data-raw-source="[&lt;strong&gt;subDirectory&lt;/strong&gt;](subdirectory-xml-element.md)"><strong>subDirectory</strong></a> (zero or more)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Data contents</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Duplicate child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
</tr>
</tbody>
</table>

 

### <a href="" id="comments"></a>Remarks

The following code example demonstrates a **search** element that contains one **subDirectory** XML element that specifies the *i386* subdirectory. DPInst will recursively search for [driver packages](./driver-packages.md) in the *i386* subdirectory of the DPInst working directory. The text that specifies the custom subdirectory is shown in bold font style.

```cpp
<dpinst>
  ...
  <search>
    <subDirectory>i386</subDirectory>
  </search>
  ...
</dpinst>
```

**Note**  Because duplicate child elements are not permitted, each **subDirectory** child element of a **search** element must be unique.

 

## See also


[**dpinst**](dpinst-xml-element.md)

[**subDirectory**](subdirectory-xml-element.md)

 

