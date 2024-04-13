---
title: C28623 Warning
description: Warning C28623 Unsigned cast of GetMessagePos() coordinates. Use GET_X_LPARAM/GET_Y_LPARAM instead of LOWORD/HIWORD.
ms.date: 04/20/2017
f1_keywords: 
  - "C28623"
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

