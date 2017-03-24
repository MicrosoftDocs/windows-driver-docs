---
title: C28623
description: Warning C28623 Unsigned cast of GetMessagePos() coordinates. Use GET\_X\_LPARAM/GET\_Y\_LPARAM instead of LOWORD/HIWORD.
ms.assetid: 155da4f5-4e77-451e-b26b-69a39c32effa
---

# C28623


warning C28623: Unsigned cast of GetMessagePos() coordinates. Use GET\_X\_LPARAM/GET\_Y\_LPARAM instead of LOWORD/HIWORD

Systems with multiple monitors can have negative x-coordinates and y-coordinates. On such systems, **GetMessagePos** may therefore return negative values. However, because **LOWORD** and **HIWORD** treat the coordinates as unsigned quantities, they should not be used.

### <span id="example"></span><span id="EXAMPLE"></span>Example

PREfast reports the warning for the following example.

```
DWORD dw = GetMessagePos();
POINT ppt;

ppt.x = LOWORD(dw);
ppt.y = HIWORD(dw);
```

The following example avoids the error.

```
DWORD dw = GetMessagePos();
POINT ppt;

ppt.x = GET_X_LPARAM(dw);
ppt.y = GET_Y_LPARAM(dw);
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28623%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




