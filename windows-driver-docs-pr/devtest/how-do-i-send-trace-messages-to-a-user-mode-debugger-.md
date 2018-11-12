---
title: How do I send trace messages to a user-mode debugger
description: How do I send trace messages to a user-mode debugger
ms.assetid: d1a9df10-3339-4518-a42a-abd1123d5e21
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I send trace messages to a user-mode debugger?


To redirect trace messages to a user-mode debugger, add the WPP\_DEBUG macro to the source code. Put the definition directive for the macro after the WPP\_CONTROL\_GUIDS definition.

The WPP\_DEBUG macro adds code that creates a trace message and redirects the message to the destination specified in the macro. You can use a **DbgPrint** or helper routine with this macro.

The format of the statement is as follows:

```
#define WPP_DEBUG(args) printf args , printf("\n");
```

You can use **DbgPrint** or **KdPrint** instead of **printf**, for example:

```
#define WPP_DEBUG(a)   printf a   printf("/n");
```

or

```
#define WPP_DEBUG(b)   DbgPrint("PCI"), DbgPrint b,   DbgPrint("\n");
```

The format of the statement that calls the routine is as follows:

```
WPP_DEBUG((format, ...))
```

You can use most formats and arguments with WPP\_DEBUG. However, you cannot use the tracing-specific format specifications, such as %!IPADDR%.

 

 





