---
title: Handling the E_INVALIDARG Return Value
description: Handling the E_INVALIDARG Return Value
keywords:
- user-mode display drivers WDK Windows Vista , E_INVALIDARG return value
- E_INVALIDARG return value WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the E\_INVALIDARG Return Value


Typically, a user-mode display driver cannot fail any of its functions by returning E\_INVALIDARG. However, if the user-mode display driver receives the E\_INVALIDARG return value when it calls one of the [Microsoft Direct3D runtime-supplied functions](/windows-hardware/drivers/ddi/_display/#functions) (because of a programming error in the driver or malicious code that runs in the operating system), the driver must return E\_INVALIDARG back to the Direct3D runtime after the runtime calls one of the driver's functions. Otherwise, the user-mode display driver should never return E\_INVALIDARG to the Direct3D runtime.

 

