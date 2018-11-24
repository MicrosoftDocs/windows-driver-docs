---
title: Can I use enumerations in my tracing code
description: Can I use enumerations in my tracing code
ms.assetid: c42ab1ad-6b8f-458f-ba29-e3553095c853
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Can I use enumerations in my tracing code?


You can use enumerations to display meaningful terms in your trace messages, instead of displaying integer values that users must decode.

For example, define the following enumeration in your code:

```
#define SPECIALDAY  0xF0000000
enum _wday {
  sunday = 0,
  monday = 55,
  tuesday = 3,
  wednesday = 1 | SPECIALDAY  ,
  thursday =  7 | SPECIALDAY,
  friday =  5,
  saturday = 6
};
```

To use the enumeration in your trace messages, add the following configuration data to your source file. This code directs WPP to extract the symbol information for the enumeration and to use the names that you have defined when displaying the enumeration logged value.

```
// begin_wpp config 
// CUSTOM_TYPE(dayset, ItemEnum(_wday) );
// end_wpp
```

Then you can use the **dayset** custom type in the format string of a trace message. For example:

```
 _wday p = wednesday;

 DoTraceMessage(NOISE " %!dayset!", p);
```

Finally, because you added configuration data to a non-configuration file (a file other than an .ini file), add the **-scan** parameter to the RUN\_WPP macro that invokes the WPP preprocessor. This notifies WPP to look for configuration data in the specified file. For example:

```
RUN_WPP -scan:trace.c
```









