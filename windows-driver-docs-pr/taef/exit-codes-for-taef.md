---
title: Exit Codes for TAEF
description: Exit Codes for TAEF
ms.assetid: DEA060FE-317F-47fe-8934-22F7AF879F1C
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Exit Codes for TAEF


The "Te.exe" command line executable front-end for TAEF returns non-zero exit codes if errors occur during execution. There are different ways in which 'errors' can occur and the process exit code reflects that.

The process exit code from Te.exe is a 32-bit number, and different bits within that number reflect different types of errors. The exit code is broken down as follows:

-   Bits 0-15: The "Test Result value" - this is the number of non-passing tests.
-   Bits 16-23: The "TestMode result value" - the error from the TestMode (not yet used).
-   Bits 24-30: The "Harness result value" - the error from the harness itself.

The most significant bit (bit 31, the sign bit for signed numbers) is not used to avoid signed/unsigned confusion. The process exit code is always positive. More practically stated:

-   If the exit code is less than or equal to 0xFFFF (65535), then that is the number of non-passing tests (failed, blocked, not run, or skipped) that Te.exe executed. If more that 65535 tests didn't pass, then the value is capped at 65535.
-   If the exit code is larger than 0xFFFF/65535 then something went wrong other than the test code that was being executed.

The following list shows the current "Harness Result Values" and their interpretation.

| Harness Result Value | Te.exe Exit Code       | Interpretation                                                                                            |
|----------------------|------------------------|-----------------------------------------------------------------------------------------------------------|
| 1                    | 0x01000000 (16777216)  | Help was requested ("/?" or "/!") - no tests were executed.                                               |
| 2                    | 0x02000000 (33554432)  | Wex.Logger reported an error.                                                                             |
| 3                    | 0x03000000 (50331648)  | Wex.Logger couldn't be initialized.                                                                       |
| 4                    | 0x04000000 (67108864)  | Wex.Logger generated invalid Pass/Fail counts (typically unbalanced StartGroup/Engroup calls from a test) |
| 5                    | 0x05000000 (83886080)  | Invalid command line (no valid test files were specified, "/inproc" specified with multiple Test Files).  |
| 6                    | 0x06000000 (100663296) | Some other exception occurred.                                                                            |
| 7                    | 0x07000000 (117440512) | No tests were executed.                                                                                   |
| 8                    | 0x08000000 (134217728) | TAEF session timed out.                                                                                   |
| 9                    | 0x09000000 (150994944) | Version information was requested ("/version") - no tests were executed.                                  |

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Exit%20Codes%20for%20TAEF%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




