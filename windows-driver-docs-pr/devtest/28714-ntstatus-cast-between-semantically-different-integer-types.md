---
title: C28714
description: Warning C28714 Cast between semantically different integer types.
ms.assetid: 53acc1a1-58a9-4009-a15c-2b11f31b086d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# C28714


warning C28714: Cast between semantically different integer types

This warning indicates that an **NTSTATUS** value is being explicitly cast to a Boolean type. This is likely to give undesirable results. For example, the typical success value for **NTSTATUS**, **STATUS\_SUCCESS**, is **false** when tested as a Boolean.

In most cases, the **NT\_SUCCESS** macro should be used to test the value of an **NTSTATUS**. This macro returns **true** if the returned status value is neither a warning nor an error code. If a function returns a Boolean to indicate its failure/success, it should explicitly return the appropriate Boolean type rather than depend on casting of **NTSTATUS** to a Boolean type.

Also, occasionally a program may attempt to reuse a Boolean local variable to store **NTSTATUS** values. This practice is often error-prone; it is much safer (and likely more efficient) to use a separate **NTSTATUS** variable.

 

 





