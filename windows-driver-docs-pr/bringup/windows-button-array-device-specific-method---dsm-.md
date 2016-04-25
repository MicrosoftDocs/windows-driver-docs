---
title: Windows button array Device-Specific Method (\_DSM)
description: To support evolution of the Windows Button user interface (UI), Windows defines a Device-Specific Method (\_DSM) for the Windows button array device with the function that is described in this article.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: B79ED0F9-B46A-4915-8FF3-5CF3D2E0E945
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

**Note**  Function index 0 of every \_DSM is a query function that returns the set of supported function indexes, and is always required. For more information, see section 9.14.1, "\_DSM (Device Specific Method)", in the [ACPI 5.0 specification](http://www.acpi.info).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Windows%20button%20array%20Device-Specific%20Method%20%28_DSM%29%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




