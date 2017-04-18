---
title: How do I include the source line number in the trace message prefix
description: How do I include the source line number in the trace message prefix
ms.assetid: 07fbdd27-59a9-4fe1-8662-6c2489efdb7f
---

# How do I include the source line number in the trace message prefix?


WPP automatically records data about each trace message, much of which is not displayed by default. This data includes the function name, file name, source line number, component name, subcomponent name, and trace level of the trace message.

To display this information in the [trace message prefix](trace-message-prefix.md) that precedes each trace message, add the predefined prefix variables to the %TRACE\_FORMAT\_PREFIX% environment variable. [Tracefmt](tracefmt.md) and other trace consumers use %TRACE\_FORMAT\_PREFIX% when formatting trace messages.

For example, to add the component name, function name, file name, and line number to the trace message prefix, add the following variables to the value of %TRACE\_FORMAT\_PREFIX%:

<span id="__COMPNAME_"></span><span id="__compname_"></span>**%!COMPNAME!**  
Adds the component name.

<span id="__FUNC_"></span><span id="__func_"></span>**%!FUNC!**  
Adds the function name.

<span id="_2"></span>**%2**  
Adds the name of the source file and the line number of the trace statement.

The **%2** variable returns the following string:

```
filename_NNN
```

where the dot (**.**) in the file name is replaced by an underscore (**\_**) and *NNN* is the line number.

The following sample SET statement adds the **%!COMPNAME**, **%!FUNC!** and **%2** variables to the default value of %TRACE\_FORMAT\_PREFIX%. The **!s!** subparameter specifies that the value of **%2** is formatted as a string. The added variables are shown in bold text.

set TRACE\_FORMAT\_PREFIX="\[%9!d!\]%8!04X!.%3!04X!::%4!s! \[%1!s!\](**%!COMPNAME!**:**%!FUNC!**:**%2**!s!)"

The resulting prefix has the following format. The new elements are shown in parentheses.

\[*CPUNumber*\]*ProcessID*.*ThreadID*::*SystemTime* \[*MessageGUIDFriendlyName*\](*ComponentName*:*FunctionName*:*Filename***\_***LineNumber*)

For a detailed example, see [Example 7: Customizing the Trace Message Prefix](example-7--customizing-the-trace-message-prefix.md). For a list of all predefined variables that can appear in the trace message prefix, see [Trace Message Prefix](trace-message-prefix.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20include%20the%20source%20line%20number%20in%20the%20trace%20message%20prefix?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




