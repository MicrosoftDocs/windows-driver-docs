---
title: Routines Not Used by RDBSS
description: Routines Not Used by RDBSS
ms.assetid: bf3e2936-05c9-4012-a55b-40022844f5db
keywords:
- mini-redirectors WDK , RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Routines Not Used by RDBSS


A number of routines listed in the MINIRDR\_DISPATCH structure are not called or used by RDBSS. It is unnecessary for a network mini-redirector to implement any of these routines since they will never be called. A network mini-redirector should set a **NULL** pointer for all these routines in the MINIRDR\_DISPATCH structure passed in to [**RxRegisterMinirdr**](https://msdn.microsoft.com/library/windows/hardware/ff554693) from its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine.

The following is a complete list of the routines not used by RDBSS:

-   **MRxCancel**

-   **MRxCancelCreateSrvCall**

-   **MRxClosedFcbTimeOut**

-   **MRxClosedSrvOpenTimeOut**

-   **MRxClosePrintFile**

-   **MRxEnumeratePrintQueue**

-   **MRxLowIOSubmit\[LOWIO\_OP\_CLEAROUT\]**

-   **MRxOpenPrintFile**

-   **MRxUpdateNetRootState**

-   **MRxWritePrintFile**

 

 




