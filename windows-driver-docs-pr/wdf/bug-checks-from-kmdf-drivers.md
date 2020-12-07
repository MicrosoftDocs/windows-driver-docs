---
title: Bug Checks from KMDF Drivers
description: Bug Checks from KMDF Drivers
keywords:
- debugging drivers WDK KMDF , bug checks
- bug check WDK KMDF
- verifying KMDF code
- KMDF bug checks WDK
- WDF_VIOLATION
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bug Checks from KMDF Drivers


The framework checks for several types of errors from framework-based drivers. If one of these errors occurs, the framework creates a WDF\_VIOLATION bug check.

For information about the types of driver errors that the framework checks for, see [**WDF\_VIOLATION**](../debugger/bug-check-0x10d---wdf-violation.md).

Your driver can create a bug check by calling [**WdfVerifierKeBugCheck**](/windows-hardware/drivers/ddi/wdfverifier/nf-wdfverifier-wdfverifierkebugcheck).

 

