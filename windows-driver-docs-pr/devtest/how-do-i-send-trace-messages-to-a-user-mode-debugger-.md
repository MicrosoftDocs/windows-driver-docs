---
title: How do I send trace messages to a user-mode debugger
description: How do I send trace messages to a user-mode debugger
ms.assetid: d1a9df10-3339-4518-a42a-abd1123d5e21
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20send%20trace%20messages%20to%20a%20user-mode%20debugger?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




