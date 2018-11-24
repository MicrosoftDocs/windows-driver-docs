---
title: Default GDL Configurations
description: Default GDL Configurations
ms.assetid: 9963513b-52dc-4fb7-8f85-abca2975c36d
keywords:
- GDL WDK , configurations
- parser WDK GDL , creating default configurations
- configurations WDK GDL , default configurations
- default GDL configurations WDK
- configurations WDK GDL , examples
- DefaultOption directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Default GDL Configurations


If a client has no specific configuration, it can ask the parser to create and return a default configuration by calling **GetDefaultConfig()**. The parser creates the default configuration by assigning the default value to each parameter. The default value is specified by using the **\*DefaultOption** directive. The **\*DefaultOption** directive is a child entry of the **\*Feature** construct. **\*DefaultOption** should specify as its value one of the construct tags that appears in one of the **\*Option** constructs. For more information about **\*DefaultOption**, **\*Feature**, and **\*Option**, see [GDL Directives for Configurations](gdl-directives-for-configurations.md)

For example, assume that the default value of the Weather parameter is Sunny. Then, you could use the following code example to define the default values.

```cpp
*Feature: Weather
{
   *DefaultOption: Sunny
   *Option: Sunny{}
   *Option: Cloudy{}
}
```

If the **\*DefaultOption** directive is missing, the parser will assume that the first **\*Option** is the default value.

You can also [change the default GDL configuration](changing-the-default-gdl-configuration.md).

 

 




