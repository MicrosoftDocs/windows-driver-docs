---
title: Code Integrity Event Log Messages
description: Code Integrity Event Log Messages
ms.assetid: 1b47e802-ed1c-4402-86f6-5ef0608b1445
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Code Integrity Event Log Messages


The following are warning events that are logged to the Code Integrity operational log:

-   Code Integrity is unable to verify the image integrity of the file &lt;*file name*&gt; because file hash could not be found on the system.

-   Code Integrity detected an unsigned driver.

    This event is related to Software Quality Monitoring (SQM).

The following are informational events that are logged to the Code Integrity verbose log:

-   Code Integrity found a set of per-page image hashes for the file &lt;*file name*&gt; in a catalog &lt;*catalog name*&gt;.

-   Code Integrity found a set of per-page image hashes for the file &lt;*file name*&gt; in the image embedded certificate.

-   Code Integrity found a file hash for the file &lt;*file name*&gt; in a catalog &lt;*catalog name*&gt;.

-   Code Integrity found a file hash for the file &lt;*file name*&gt; in the image embedded certificate.

-   Code Integrity determined an unsigned kernel module &lt;*file name*&gt; is loaded into the system. Check with the publisher to see whether a signed version of the kernel module is available.

-   Code Integrity is unable to verify the image integrity of the file &lt;*file name*&gt; because the set of per-page image hashes could not be found on the system.

-   Code Integrity is unable to verify the image integrity of the file &lt;*file name*&gt; because the set of per-page image hashes could not be found on the system. The image is allowed to load because kernel mode debugger is attached.

-   Code Integrity is unable to verify the image integrity of the file &lt;*file name*&gt; because a file hash could not be found on the system. The image is allowed to load because kernel mode debugger is attached.

-   Code Integrity was unable to load the &lt;*file name*&gt; catalog.

-   Code Integrity successfully loaded the &lt;*file name*&gt; catalog.

 

 





