---
title: Using String Objects
description: This topic describes the support that Windows Driver Frameworks (WDF) provides for string objects. It applies to both Kernel-Mode Driver Framework (KMDF).
ms.assetid: b1d52a18-ebd5-4ba7-b5c7-3ef3d298c82e
keywords:
- string objects WDK KMDF
- framework objects WDK KMDF , string objects
- Unicode strings WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using String Objects


This topic describes the support that Windows Driver Frameworks (WDF) provides for string objects. It applies to both Kernel-Mode Driver Framework (KMDF) drivers and User-Mode Driver Framework (UMDF) drivers starting in version 2.




WDF uses only Unicode strings. All of the methods that are defined by framework objects accept only Unicode strings.

The framework defines the *framework string object* that KMDF and UMDF drivers can use to represent Unicode strings.

Your driver can call [**WdfStringCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550046) to create a string object and to optionally assign a Unicode string to the object.

Some of the framework's object methods, such as [**WdfRegistryQueryString**](https://msdn.microsoft.com/library/windows/hardware/ff549923), accept a string object handle as input and assign a string to the string object.

To access the string that is assigned to a string object, your driver can call [**WdfStringGetUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff550049).

 

 





