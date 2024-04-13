---
title: Option Constraints
description: Option Constraints
keywords:
- constraints WDK Unidrv
- printer options WDK Unidrv , constraints
- simultaneous printer options WDK Unidrv
- combining printer options WDK Unidrv
ms.date: 01/30/2023
---

# Option Constraints

[!include[Print Support Apps](../includes/print-support-apps.md)]

It's sometimes necessary to constrain the ability of users to install or select certain printer options associated with printer features. The following types of option constraints can be specified:

- You can constrain an option so that it can't be selected if a conflicting option is already selected. These constraints are called [selection constraints](selection-constraints.md).

- You can constrain an installable option so that it can't be installed if a conflicting installable option is already installed. These constraints are called [installation constraints](installation-constraints.md).

- You can constrain an option so that it can't be selected if a conflicting installable option is already installed, or so that it can't be selected if a required installable option isn't installed. These constraints are called [constraints between selections and installations](constraints-between-selections-and-installations.md).

The driver's user interface code enforces constraints when the user chooses the **OK** button on the printer's property sheet dialog box. If invalid combinations of options have been selected, the user is given the choice of either correcting the conflicts by modifying the property sheet page or letting the driver attempt to make corrections automatically, based on [feature conflict priority](feature-conflict-priority.md).
