---
title: Feature Conflict Priority
description: Feature Conflict Priority
keywords:
- printer features WDK Unidrv , conflict priority
- conflict priority WDK printer features
ms.date: 01/27/2023
---

# Feature Conflict Priority

[!include[Print Support Apps](../includes/print-support-apps.md)]

A feature's conflict priority identifies the priority that a feature should have when Unidrv's user interface code enforces [option constraints](option-constraints.md).

The GPD parser assigns a conflict priority to a feature in the following order, from highest to lowest priority:

1. Installable features that are installed. (See [Handling Installable Features and Options](handling-installable-features-and-options.md).)

2. Features with \*FeatureType set to PRINTER_PROPERTY.

3. Features with \***FeatureType** set to DOC_PROPERTY or JOB_PROPERTY.

Features within each feature type are assigned a relative priority based on the value specified for the feature's \*ConflictPriority attribute. Thus, for example, a PRINTER_PROPERTY feature with a \***ConflictPriority** attribute of 1 has a higher priority than a DOC_PROPERTY feature with a \***ConflictPriority** attribute of 3. Features that don't have a \***ConflictPriority** attribute have a lower priority than features that do.

For more information about the \***FeatureType** and \***ConflictPriority** attributes, see [Feature Attributes](feature-attributes.md).
