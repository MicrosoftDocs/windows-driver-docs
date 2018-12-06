---
title: Using Invalid GDL Configurations
description: Using Invalid GDL Configurations
ms.assetid: a61232dd-ab64-4ca4-9eb9-68fe5c7249e4
keywords:
- GDL WDK , configurations
- configurations WDK GDL , invalid configurations
- invalid GDL configurations WDK
- configurations WDK GDL , examples
- InvalidCombination directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Invalid GDL Configurations


Not all possible configurations are valid or permitted. For example, a printing device might not allow a stiff media to be placed in any input tray because the media might jam. The GDL language enables you to also define invalid configurations by defining combinations of parameter settings that are invalid.

The \*InvalidCombination directive is used for this purpose. The value of \*InvalidCombination is a LIST that names two or more parameter settings that cannot be used together. The syntax that is used to specify a parameter setting is in EBNF notation, as the following code example shows.

```cpp
InvalidCombination_Directive :== "*InvalidCombination" S ":"  S ParamSettingsList  S LB
ParamSettingsList :== "LIST" S "("  S ParamSetting S ","  S ParamSetting ( S "," S ParamSetting)?  S ")"
ParamSetting :== ParameterName "." Value
ParameterName :== {Construct Tag of *Feature construct}
Value :==  {Construct Tag of *Option construct found within the *Feature construct.}
S :== [#x20#x09]*
LB :== [#x0A] | [#x0D] | ([#x0A] [#x0D]) | ([#x0D] [#x0A])
```

The \*InvalidCombination directive must appear at the root context of the GDL file.

For example if you wanted to prevent rain on weekends, you could specify the following code.

```cpp
*InvalidCombination: LIST(Weather.Rain, Today.Saturday)
*InvalidCombination: LIST(Weather.Rain, Today.Sunday)
```

If you wanted to prevent rain on weekends only if you were healthy, you could specify the following code.

```cpp
*InvalidCombination: LIST(Weather.Rain, Today.Saturday, Health.Well)
*InvalidCombination: LIST(Weather.Rain, Today.Sunday, Health.Well)
```

The \*InvalidCombination directive in the preceding code example specifies that any configuration that contains the specific combination (Weather.Rain, Today.Sunday, Health.Well or Weather.Rain, Today.Saturday, Health.Well) violates the directive.

The \*InvalidCombination directive is a specific type of constraint. The GDL parser functions determine if the supplied configuration violates any of the constraints that are defined in the GDL file before proceeding. If a violation is detected, the configuration is modified (or resolved) to avoid violating the constraint. This situation is called [resolving the constraint](resolving-gdl-configuration-conflicts.md). Hundreds of constraints that involve dozens of parameters might exist in a single GDL file. Constraints can form a complex web of interactions so that a change in the setting for one parameter might cause a cascade of changes in other parameters.

**Note**   You must ensure that the default configuration does not violate any constraints. If it does, none of the parser interface functions will succeed.

 

**Note**   The GDL parser also accepts a special case of \*InvalidCombination that involves only two parameter settings.

 

 

 




