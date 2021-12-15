---
title: C28101 warning
description: Warning C28101 The Drivers module has inferred that the current function is not the correct type of function.
keywords:
- warnings listed WDK PREfast for Drivers
- errors listed WDK PREfast for Drivers
ms.date: 05/01/2020
f1_keywords: 
  - "C28101"
---

# C28101


warning C28101: The Drivers module has inferred that the current function is not the correct type of function

The Code Analysis tool has detected that a function is of a particular type, such as a callback function. This is an informational message only. It does not indicate an error.

This message indicates that the Code Analysis tool is applying rules that are specific to that function type. If this inference is wrong, the Code Analysis tool will generate false-positive warnings, but those warnings can be safely ignored. For more information, see [Using Annotations to Reduce C/C++ Code Defects](/cpp/code-quality/using-sal-annotations-to-reduce-c-cpp-code-defects).

The *function signature* (the arguments and result type) are used to identify the function whenever possible. Some standard driver routines, such as [**Cancel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) and [**StartIo**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio), have the same signature, so the name is checked to see if it matches the conventional name for that function. Other functions might be checked for conventional names.

To suppress this warning when it is redundant, you can explicitly declare the function to be of a particular function type. The functions that are detected this way are typically callback functions. The proper action is to declare them using a function typedef. For more information, see [Using Function Role Type Declarations](using-function-role-type-declarations.md).

 

