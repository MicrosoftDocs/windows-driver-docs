---
title: Feature Conflict Priority
description: Feature Conflict Priority
ms.assetid: 1185f983-ed04-4610-8b93-684ae3e07e84
keywords:
- printer features WDK Unidrv , conflict priority
- conflict priority WDK printer features
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Feature Conflict Priority





A feature's conflict priority identifies the priority that a feature should have when Unidrv's user interface code enforces [option constraints](option-constraints.md).

The GPD parser assigns a conflict priority to a feature in the following order, from highest to lowest priority:

1.  Installable features that are actually installed. (See [Handling Installable Features and Options](handling-installable-features-and-options.md).)

2.  Features with \*FeatureType set to PRINTER\_PROPERTY.

3.  Features with \***FeatureType** set to DOC\_PROPERTY or JOB\_PROPERTY.

Features within each feature type are assigned a relative priority based on the value specified for the feature's \*ConflictPriority attribute. Thus, for example, a PRINTER\_PROPERTY feature with a \***ConflictPriority** attribute of 1 has a higher priority than a DOC\_PROPERTY feature with a \***ConflictPriority** attribute of 3. Features that do not have a \***ConflictPriority** attribute have a lower priority than those that do.

For more information about the \***FeatureType** and \***ConflictPriority** attributes, see [Feature Attributes](feature-attributes.md).

 

 




