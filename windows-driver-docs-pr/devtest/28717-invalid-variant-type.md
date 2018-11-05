---
title: C28717
description: Warning C28717 Invalid VARIANT type.
ms.assetid: e1373005-a1ff-4722-98f9-00c7e4f89370
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28717


warning C28717: Invalid VARIANT type

The **vt** field of a **VARIANT struct** can take only certain values. Assigning any other value to it is an error.

The **vt** field of a **VARIANT** or **VARIANTARG** struct can only take the following values (possibly ORed by **VT\_BYREF** and/or **VT\_ARRAY**): **VT\_EMPTY**, **VT\_NULL**, **VT\_I2**, **VT\_I4**, **VT\_R4**, **VT\_R8**, **VT\_CY**, **VT\_DATE**, **VT\_BSTR**, **VT\_DISPATCH**, **VT\_ERROR**, **VT\_BOOL**, **VT\_VARIANT**, **VT\_DECIMAL**, **VT\_RECORD, VT\_UNKNOWN**, **VT\_I1**, **VT\_UI1**, **VT\_UI2**, **VT\_UI4**, **VT\_INT**, **VT\_UINT** (**VT\_EMPTY** and **VT\_NULL** cannot be combined with **VT\_ARRAY**).

### <span id="example"></span><span id="EXAMPLE"></span>Example

PREfast reports the warning for the following example.

```
VARIANT var;
var.vt = VT_SAFEARRAY | VT_INT;
```

The following example avoids the error.

```
VARIANT var;
var.vt = VT_ARRAY | VT_INT;
```

 

 





