---
title: Default GDL Configurations
author: windows-driver-content
description: Default GDL Configurations
MS-HAID:
- 'gplfiles\_86c34cbb-56fe-4249-a4d8-e66bd063d67d.xml'
- 'print.default\_gdl\_configurations'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9963513b-52dc-4fb7-8f85-abca2975c36d
keywords: ["GDL WDK , configurations", "parser WDK GDL , creating default configurations", "configurations WDK GDL , default configurations", "default GDL configurations WDK", "configurations WDK GDL , examples", "DefaultOption directive WDK GDL"]
---

# Default GDL Configurations


If a client has no specific configuration, it can ask the parser to create and return a default configuration by calling **GetDefaultConfig()**. The parser creates the default configuration by assigning the default value to each parameter. The default value is specified by using the **\*DefaultOption** directive. The **\*DefaultOption** directive is a child entry of the **\*Feature** construct. **\*DefaultOption** should specify as its value one of the construct tags that appears in one of the **\*Option** constructs. For more information about **\*DefaultOption**, **\*Feature**, and **\*Option**, see [GDL Directives for Configurations](gdl-directives-for-configurations.md)

For example, assume that the default value of the Weather parameter is Sunny. Then, you could use the following code example to define the default values.

```
*Feature: Weather
{
   *DefaultOption: Sunny
   *Option: Sunny{}
   *Option: Cloudy{}
}
```

If the **\*DefaultOption** directive is missing, the parser will assume that the first **\*Option** is the default value.

You can also [change the default GDL configuration](changing-the-default-gdl-configuration.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Default%20GDL%20Configurations%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


