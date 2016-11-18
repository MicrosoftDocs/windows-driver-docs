---
title: Can I use enumerations in my tracing code
description: Can I use enumerations in my tracing code
ms.assetid: c42ab1ad-6b8f-458f-ba29-e3553095c853
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Can%20I%20use%20enumerations%20in%20my%20tracing%20code?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




