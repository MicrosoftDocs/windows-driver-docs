---
title: Responding to an OID_CO_TAPI_LINE_CAPS Query
description: Responding to an OID_CO_TAPI_LINE_CAPS Query
ms.assetid: b1ca65c6-ecce-4d2c-b7ca-03b6a334f97b
keywords:
- voice streaming WDK networking , support specification
- OID_CO_TAPI_LINE_CAPS
- ulMediaModes
- ulAddressTypes
- UlGenerateDigitModes
- UlMonitorDigitModes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Responding to an OID\_CO\_TAPI\_LINE\_CAPS Query





In response to an [OID\_CO\_TAPI\_LINE\_CAPS](https://msdn.microsoft.com/library/windows/hardware/ff569098) query, a call manager or MCM returns a CO\_TAPI\_LINE\_CAPS structure that contains a LINE\_DEV\_CAPS structure. To support voice streaming, a call manager or MCM must specify the following values in the LINE\_DEV\_CAPS structure:

-   **ulMediaModes**

    This field should contain LINEMEDIAMODE\_AUTOMATEDVOICE, which maps to TAPIMEDIAMODE\_AUDIO in TAPI 3.0.

-   **ulAddressTypes**

    This field must be filled in appropriately. For a description of valid values, see the description of **dwAddressTypes** in the Microsoft Windows SDK documentation. This field must not be zero.

-   **ulGenerateDigitModes**

    This field must be filled in with a bitwise OR of the LINEDIGITMODE\_constants that specify the digit modes that can be generated on the line. For a description of the LINEDIGITMODE\_constant, see the description of **dwGenerateDigitModes** in the Windows SDK documentation.

-   **ulMonitorDigitModes**

    This field must be filled in with a bitwise OR of the LINEDIGITMODE\_constants that specify the digit modes than can be detected on this line. For a description of the LINEDIGITMODE\_constants, see the description of **dwMonitorDigitModes** in the Windows SDK documentation.

 

 





