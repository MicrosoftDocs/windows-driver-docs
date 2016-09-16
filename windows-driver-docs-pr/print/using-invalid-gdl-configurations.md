---
title: Using Invalid GDL Configurations
author: windows-driver-content
description: Using Invalid GDL Configurations
MS-HAID:
- 'gplfiles\_492483c1-e65c-43a8-86d9-f444ec207301.xml'
- 'print.using\_invalid\_gdl\_configurations'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a61232dd-ab64-4ca4-9eb9-68fe5c7249e4
keywords: ["GDL WDK , configurations", "configurations WDK GDL , invalid configurations", "invalid GDL configurations WDK", "configurations WDK GDL , examples", "InvalidCombination directive WDK GDL"]
---

# Using Invalid GDL Configurations


Not all possible configurations are valid or permitted. For example, a printing device might not allow a stiff media to be placed in any input tray because the media might jam. The GDL language enables you to also define invalid configurations by defining combinations of parameter settings that are invalid.

The \*InvalidCombination directive is used for this purpose. The value of \*InvalidCombination is a LIST that names two or more parameter settings that cannot be used together. The syntax that is used to specify a parameter setting is in EBNF notation, as the following code example shows.

```
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

```
*InvalidCombination: LIST(Weather.Rain, Today.Saturday)
*InvalidCombination: LIST(Weather.Rain, Today.Sunday)
```

If you wanted to prevent rain on weekends only if you were healthy, you could specify the following code.

```
*InvalidCombination: LIST(Weather.Rain, Today.Saturday, Health.Well)
*InvalidCombination: LIST(Weather.Rain, Today.Sunday, Health.Well)
```

The \*InvalidCombination directive in the preceding code example specifies that any configuration that contains the specific combination (Weather.Rain, Today.Sunday, Health.Well or Weather.Rain, Today.Saturday, Health.Well) violates the directive.

The \*InvalidCombination directive is a specific type of constraint. The GDL parser functions determine if the supplied configuration violates any of the constraints that are defined in the GDL file before proceeding. If a violation is detected, the configuration is modified (or resolved) to avoid violating the constraint. This situation is called [resolving the constraint](resolving-gdl-configuration-conflicts.md). Hundreds of constraints that involve dozens of parameters might exist in a single GDL file. Constraints can form a complex web of interactions so that a change in the setting for one parameter might cause a cascade of changes in other parameters.

**Note**   You must ensure that the default configuration does not violate any constraints. If it does, none of the parser interface functions will succeed.

 

**Note**   The GDL parser also accepts a special case of \*InvalidCombination that involves only two parameter settings.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Using%20Invalid%20GDL%20Configurations%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


