---
title: Using String Objects
description: This topic describes the support that Windows Driver Frameworks (WDF) provides for string objects. It applies to both Kernel-Mode Driver Framework (KMDF).
keywords:
- string objects WDK KMDF
- framework objects WDK KMDF , string objects
- Unicode strings WDK KMDF
ms.date: 04/20/2017
---

# Using String Objects


This topic describes the support that Windows Driver Frameworks (WDF) provides for string objects. It applies to both Kernel-Mode Driver Framework (KMDF) drivers and User-Mode Driver Framework (UMDF) drivers starting in version 2.




WDF uses only Unicode strings. All of the methods that are defined by framework objects accept only Unicode strings.

The framework defines the *framework string object* that KMDF and UMDF drivers can use to represent Unicode strings.

Your driver can call [**WdfStringCreate**](/windows-hardware/drivers/ddi/wdfstring/nf-wdfstring-wdfstringcreate) to create a string object and to optionally assign a Unicode string to the object.

Some of the framework's object methods, such as [**WdfRegistryQueryString**](/windows-hardware/drivers/ddi/wdfregistry/nf-wdfregistry-wdfregistryquerystring), accept a string object handle as input and assign a string to the string object.

To access the string that is assigned to a string object, your driver can call [**WdfStringGetUnicodeString**](/windows-hardware/drivers/ddi/wdfstring/nf-wdfstring-wdfstringgetunicodestring).

 

