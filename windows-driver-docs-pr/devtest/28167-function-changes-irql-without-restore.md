---
title: C28167 Warning
description: Warning C28167 The function changes the IRQL and does not restore the IRQL before it exits. It should be annotated to reflect the change or the IRQL should be restored.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 04/20/2017
f1_keywords: 
  - "C28167"
---

# C28167


warning C28167: The function changes the IRQL and does not restore the IRQL before it exits. It should be annotated to reflect the change or the IRQL should be restored.

This warning indicates that the following conditions are true:

-   The function changes the IRQL at which the driver is running.

-   There is at least one path through a function that does not, by function exit, restore the IRQL to the original IRQL that the driver was running at function entry.

This warning occurs when an IRQL annotation on a function is required, but one doesn't exist.

To avoid this warning, the driver must correctly save the initial IRQL value and restore the same IRQL value at function exit if it did not intend to change the IRQL.

Functions that intentionally change the IRQL to a value that is different than the IRQL at which the driver was running at function entry should be annotated to indicate this behavior. For example, you could use the **\_IRQL\_raises\_**(*irql*) annotation to indicate that the function changes the IRQL from the IRQL at which the function was called. You could also save and restore the IRQL value and apply the corresponding annotations (**\_IRQL\_saves\_**, **\_IRQL\_restores\_**). The annotation will suppress this warning. For more information, see [IRQL annotations for drivers](irql-annotations-for-drivers.md). Functions that change the IRQL by mistake should be fixed.

