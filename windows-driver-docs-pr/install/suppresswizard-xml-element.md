---
title: suppressWizard XML Element
description: The suppressWizard XML element is an empty element that sets the suppressWizard flag to ON, which configures DPInst to suppress the display of wizard pages and other user messages that DPInst generates.
ms.assetid: fb72ff30-7d93-4531-9115-c299fabec7e7
keywords: ["suppressWizard XML Element Device and Driver Installation"]
topic_type:
- apiref
api_name:
- suppressWizard XML Element
api_type:
- NA
---

# suppressWizard XML Element


\[DIFx is deprecated, for more info, see [DIFx Guidelines](https://msdn.microsoft.com/windows/hardware/drivers/install/difx-guidelines).\]

The **suppressWizard** XML element is an empty element that sets the **suppressWizard** flag to ON, which configures DPInst to suppress the display of wizard pages and other user messages that DPInst generates.

**Element Tag**

```
<suppressWizard>
```

**XML Attributes**

None

**Element Information**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Parent elements</strong></p></td>
<td align="left"><p>[<strong>dpinst</strong>](dpinst-xml-element.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Child elements</strong></p></td>
<td align="left"><p>None permitted</p></td>
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

 

**Remarks**

By default, the **suppressWizard** flag is set to OFF. You can set the **suppressWizard** flag to ON by including a **suppressWizard** XML element as a child element of a **dpinst** XML element in a DPInst descriptor file or by using the **/sw** command-line switch. The **suppressWizard** flag works with the **suppressEulaPage** flag.

The following code example demonstrates a **supressWizard** element.

```
<dpinst>
  ...
  <suppressWizard/>
  ...
</dpinst>
```

## See also


[**dpinst**](dpinst-xml-element.md)

 

 






