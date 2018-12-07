---
title: Template Directive Example
description: Template Directive Example
ms.assetid: ae8fe5e6-ee79-424d-80b3-fd6300257977
keywords:
- Production directive WDK GDL
- templates WDK GDL , examples
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Template Directive Example


The following example shows a simple production.

```cpp
  *Production: EXACTLY_ONE
  {
        *Production: SATISFY_ALL
        {
            *Member: GENERIC_OPTION {*Occurs: [1-*] }
            *Member: DEFAULT_OPT {*Occurs: [0-*] }
        }
        *Production: SATISFY_ALL
        {
            *Member: GENERIC_OPTION {*Occurs: [0] }
            *Member: DEFAULT_OPT {*Occurs: [0] }
        }
  }
```

The construct instances that are bound to the host template by this production can contain any of the following combinations:

-   No instances of either DEFAULT\_OPT or GENERIC\_OPTION.

-   One or more instances of GENERIC\_OPTION and no instances of DEFAULT\_OPT.

-   One or more instances of GENERIC\_OPTION and one or more instances of DEFAULT\_OPT.

-   The construct instances cannot have one or more instances of DEFAULT\_OPT without at least one instance of GENERIC\_OPTION.

If the host template inherits from other templates, the productions that are defined in the inherited templates are also evaluated and must also be **TRUE** for the production in the host template to evaluate to **TRUE**.

 

 




