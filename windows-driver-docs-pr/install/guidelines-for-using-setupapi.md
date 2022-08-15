---
title: Guidelines for Using SetupAPI
description: Guidelines for Using SetupAPI
keywords:
- SetupAPI functions WDK , guidelines
- device installation functions WDK SetupAPI
- general Setup functions WDK SetupAPI
ms.date: 04/20/2017
---

# Guidelines for Using SetupAPI





The following are guidelines for using the [general Setup functions](/previous-versions/ff544985(v=vs.85)) (**Setup***Xxx*) and [device installation functions](/previous-versions/ff541299(v=vs.85)) (**SetupDi***Xxx*) that are provided by SetupAPI:

-   Never assume that installation file contents are error-free, or that an installation file that you provided hasn't been maliciously modified. Therefore, always validate all information received from SetupAPI functions. Verify that strings are of valid length, that buffers are of valid size, and that index values are within a valid range.

-   When writing installation applications for installations on Microsoft Windows XP and later systems, you can call **SetupVerifyInfFile** (described in the Windows SDK documentation), which verifies that a digitally signed INF file has not been modified.

-   Always test the return value of each SetupAPI function. If the function fails, your code should call [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) to obtain an error code that identifies the failure. Returned error codes can be defined in *Winerror.h* or *Setupapi.h*. Before calling **FormatMessage** with FORMAT_MESSAGE_FROM_SYSTEM to create a text display, always use the HRESULT_FROM_SETUPAPI macro (defined in *Winerror.h*) to convert the return value to an HRESULT value. If a SetupAPI function returns successfully, your code must not call [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror). (The [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) and **FormatMessage** functions, together with system error codes, are described in the Windows SDK documentation.)

-   If a SetupAPI function returns a handle, your code must check for a return value of INVALID_HANDLE_VALUE. Such functions do not return **NULL**.

-   Be aware of the following difference between the **SetupDi***Xxx* and **Setup***Xxx* functions that allow a caller to query for the required size of a buffer:

    -   If the caller of a **SetupDi***Xxx* function makes such a query, [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) always returns ERROR_INSUFFICIENT_BUFFER.

    -   If the caller of a **Setup***Xxx* function makes such a query, [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns NO_ERROR if no buffer length was specified or ERROR_INSUFFICIENT_BUFFER if a buffer was specified that was too small.

