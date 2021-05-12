---
title: Bug Check 0x17D PDC_UNEXPECTED_REVOCATION_LIVEDUMP
description: The PDC_UNEXPECTED_REVOCATION_LIVEDUMP bug check has a value of 0x0000017D. It indicates that an activator has been revoked unexpectedly.
keywords: ["Bug Check 0x17D PDC_UNEXPECTED_REVOCATION_LIVEDUMP", "PDC_UNEXPECTED_REVOCATION_LIVEDUMP"]
ms.date: 01/04/2019
topic_type:
- apiref
api_name:
- PDC_UNEXPECTED_REVOCATION_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x17D: PDC\_UNEXPECTED\_REVOCATION\_LIVEDUMP

The PDC\_UNEXPECTED\_REVOCATION\_LIVEDUMP bug check has a value of 0x0000017D. It indicates that an activator has been revoked unexpectedly.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).



 ## PDC\_UNEXPECTED\_REVOCATION\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| The client ID of the revoked activator.|
|2| The revoked activator client. |
|3| The revoked activation instance.|
|4| pdc!_PDC_CLIENT_PROCESS_INFO |


## ## Cause

An activator has been revoked unexpectedly.

A livedump is created to provide information to investigate.

(This code can never be used for a real bugcheck.)



## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

 




