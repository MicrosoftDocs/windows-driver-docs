---
title: Resolving GDL Configuration Conflicts
description: Resolving GDL Configuration Conflicts
ms.assetid: 02a2da63-0b7f-4aa9-b3c3-72784f409d94
keywords:
- GDL WDK , configurations
- configurations WDK GDL , invalid configurations
- configurations WDK GDL , conflicts
- invalid GDL configurations WDK
- configurations WDK GDL , resolving conflicts
- resolving GDL configuration conflicts WDK GDL
- ConflictPriority directive WDK GDL
- FeatureType directive WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Resolving GDL Configuration Conflicts


Although the GDL parser will automatically modify the configuration to avoid violating a constraint, keep the following information in mind so that the parser knows your intentions.

For example, if the configuration that is passed into the parser function contains the parameter settings of Weather.Rain, Today.Sunday, Health.Well, the invalid combination from the previous section can be resolved by changing the setting for any one of the parameters that are named in this constraint. The parser has to decide which parameter's setting to change. In many cases, you might know which setting should be changed. typically, the more important parameter is left unchanged. In this case the conflict can be removed by changing the parameters to Weather:Sunny, Today:Monday, or Health:Sick, respectively. Most people will prefer to change Weather first, Today second, and hope to avoid changing Health.

The \*ConflictPriority directive enables you to specify preferences about which parameter to change in a conflict. \*ConflictPriority accepts a positive integer value that specifies the relative importance of each parameter. When two or more parameters come into conflict, the parser will modify the parameter setting of the parameter with the lower priority. This directive conforms to the common usage that the highest priority item is labeled with the smallest ordinal. Thus the highest priority parameter should be assigned \*ConflictPriority: 1. The values that are selected for \*ConflictPriority: do not need to be consecutive, but they should be unique. \*ConflictPriority should appear as a child entry of the \*Feature construct.

The \*FeatureType directive also influences the priority of a parameter. \*FeatureType is actually a GPD/Unidrv-specific keyword. For non-Unidrv clients, you must simply set \*FeatureType: PARAMETER\_PROPERTY. This setting will avoid unanticipated behaviors in the future. \*FeatureType should appear as a child entry of the \*Feature construct.

When GDL changes a parameter's setting to resolve a conflict, it will use the default setting, unless that is also constrained. In some cases, you might want the parser to use a different default setting when resolving conflicts under different configurations. To set such a different default setting, define multiple \*DefaultOption directives within Switch and Case directives or within a nested set of Switch Case directives. The parser will evaluate the Switch and Case given the current configuration to determine the \*DefaultOption to use. Because the resolver algorithm determines the setting of parameters starting with the highest priority (that is, the smallest ordinal), the settings of parameters with priorities that are lower than the priority of the parameter under evaluation are unknown. You must ensure that any Switch construct that surrounds the \*DefaultOption directive uses parameters that have priorities that are higher (that is, smaller ordinals) than the parameter whose default value is being defined by using the \*DefaultOption. If you do not observe this rule, the parser functions will fail. Because of this difficulty, you should avoid inserting \*DefaultOption into a Switch and Case construction if at all possible.

The **ResolveConstraint()** parser interface function can be called to explicitly check a configuration for constraint violations and to resolve the conflict if any are found. The new configuration is returned to the caller. The caller can then examine the configuration for acceptability or can use the configuration to obtain a [snapshot](gdl-snapshots.md). The snapshot indicates which parameter settings are constrained under the configuration that is specified in its creation. This information might be useful for clients that create user interfaces.

 

 




