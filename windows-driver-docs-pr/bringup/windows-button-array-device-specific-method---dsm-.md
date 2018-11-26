---
title: Windows button array Device-Specific Method (_DSM)
description: To support evolution of the Windows Button user interface (UI), Windows defines a Device-Specific Method (_DSM) for the Windows button array device with the function that is described in this article.
ms.assetid: B79ED0F9-B46A-4915-8FF3-5CF3D2E0E945
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows button array Device-Specific Method (\_DSM)


To support evolution of the Windows Button user interface (UI), Windows defines a Device-Specific Method (\_DSM) for the Windows button array device with the function that is described in this article.

## Function 1: Power Button Properties


The \_DSM control method parameters for the power button properties function are as follows:

### Arguments

-   **Arg0:** UUID = dfbcf3c5-e7a5-44e6-9c1f-29c76f6e059c
-   **Arg1:** Revision ID = 0
-   **Arg2:** Function index = 1
-   **Arg3:** Empty package (not used)

### Return

An integer (DWORD) that has the following bit-field definitions:

-   Bits 31 to 33: Reserved (must be 0).
-   Bit 2: This bit should be set to 1 if the power button is configured to detect both press and release events, and to report these events to the operating system. Otherwise, this bit should be 0.
-   Bit 1: This bit should be set to 1 if power button is wired to an interrupt controller (GPIO or otherwise) that supports level-detection. Otherwise, this bit should be 0.
-   Bit 0: This bit should be set to 1 if the platform supports ACPI Power Button Override time of 10 seconds or greater. Otherwise, this bit should be 0.

**Note**  Function index 0 of every \_DSM is a query function that returns the set of supported function indexes, and is always required. For more information, see section 9.14.1, "\_DSM (Device Specific Method)", in the [ACPI 5.0 specification](https://www.uefi.org/specifications).

 

 

 




