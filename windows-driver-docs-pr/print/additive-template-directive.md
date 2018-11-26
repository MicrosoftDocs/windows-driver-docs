---
title: Additive Template Directive
description: Additive Template Directive
ms.assetid: 94883a51-a3a6-492e-9597-6a2f913d40bc
keywords:
- Additive directive WDK GDL
- templates WDK GDL , order of definitions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Additive Template Directive


The \***Additive**: directive defines the order of template definitions.

The **Additive** directive can have one of the following values:

-   MOST\_RECENT. Only the most recent definition appears.

-   LEAST\_RECENT. Only the least recent (first) definition appears.

-   MOST\_TO\_LEAST\_RECENT. All definitions appear ordered from most to least recent.

-   LEAST\_TO\_MOST\_RECENT. All definitions appear ordered from least to most recent.

If this directive is absent, a default value of MOST\_RECENT will be assumed.

If this directive is itself multiply defined within a template or appears in several templates that are related by inheritance, only the most recently defined directive in the most derived template will be honored.

 

 




