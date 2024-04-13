---
title: Changing Floating-Point Control State
description: Changing Floating-Point Control State
keywords:
- floating-point control state WDK display
ms.date: 04/20/2017
---

# Changing Floating-Point Control State


All functions of a display miniport driver and a user-mode display driver must save the floating-point control state, such as, rounding mode or precision, before changing the floating-point control state and must restore the floating-point control state to the previously saved setting before returning.

 

 





