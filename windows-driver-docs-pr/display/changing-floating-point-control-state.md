---
title: Changing Floating-Point Control State
description: Changing Floating-Point Control State
ms.assetid: de1ace72-ee3c-4adc-8e40-0d687b18cc25
keywords:
- floating-point control state WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Changing Floating-Point Control State


All functions of a display miniport driver and a user-mode display driver must save the floating-point control state, such as, rounding mode or precision, before changing the floating-point control state and must restore the floating-point control state to the previously saved setting before returning.

 

 





