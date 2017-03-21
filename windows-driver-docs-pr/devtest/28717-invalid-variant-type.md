---
title: C28717
description: Warning C28717 Invalid VARIANT type.
ms.assetid: e1373005-a1ff-4722-98f9-00c7e4f89370
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28717%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




