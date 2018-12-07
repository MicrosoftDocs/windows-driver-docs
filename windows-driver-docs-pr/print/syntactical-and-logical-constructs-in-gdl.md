---
title: Syntactical and Logical Constructs in GDL
description: Syntactical and Logical Constructs in GDL
ms.assetid: f0802424-319c-4ba4-a8cd-539006f4d22c
keywords:
- syntactical constructs WDK GDL
- logical constructs WDK GDL
- constructs WDK GDL , syntactical constructs
- constructs WDK GDL , logical constructs
- GDL WDK , constructs
- parser WDK GDL , handling constructs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Syntactical and Logical Constructs in GDL


GDL distinguishes between the constructs that are literally defined by entries in the GDL source file and the representation of those constructs in GDL's internal data. The former is a syntactical representation, and the latter is a logical representation. The representations differ when constructs are defined in the source file. The GDL parser creates only one logical representation of a construct for a given construct type and construct tag, no matter how many times such a construct is defined in the GDL source file.

 

 




