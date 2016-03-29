---
title: Feature Conflict Priority
description: Feature Conflict Priority
ms.assetid: 1185f983-ed04-4610-8b93-684ae3e07e84
keywords: ["printer features WDK Unidrv , conflict priority", "conflict priority WDK printer features"]
---

# Feature Conflict Priority


## <a href="" id="ddk-feature-conflict-priority-gg"></a>


A feature's conflict priority identifies the priority that a feature should have when Unidrv's user interface code enforces [option constraints](option-constraints.md).

The GPD parser assigns a conflict priority to a feature in the following order, from highest to lowest priority:

1.  Installable features that are actually installed. (See [Handling Installable Features and Options](handling-installable-features-and-options.md).)

2.  Features with \*FeatureType set to PRINTER\_PROPERTY.

3.  Features with \***FeatureType** set to DOC\_PROPERTY or JOB\_PROPERTY.

Features within each feature type are assigned a relative priority based on the value specified for the feature's \*ConflictPriority attribute. Thus, for example, a PRINTER\_PROPERTY feature with a \***ConflictPriority** attribute of 1 has a higher priority than a DOC\_PROPERTY feature with a \***ConflictPriority** attribute of 3. Features that do not have a \***ConflictPriority** attribute have a lower priority than those that do.

For more information about the \***FeatureType** and \***ConflictPriority** attributes, see [Feature Attributes](feature-attributes.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Feature%20Conflict%20Priority%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




