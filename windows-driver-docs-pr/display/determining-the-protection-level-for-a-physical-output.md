---
title: Determining the Protection Level for a Physical Output
description: Determining the Protection Level for a Physical Output
ms.assetid: ea06903a-0ad5-43fd-b2d3-013584ae6f69
keywords:
- protection levels WDK display , determining for physical output
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining the Protection Level for a Physical Output


You should use the algorithms in the following sections to determine the protection level for a physical video output connector. These algorithms are represented in pseudocode.

### <span id="algorithm_for_protection_level"></span><span id="ALGORITHM_FOR_PROTECTION_LEVEL"></span>Algorithm for Protection Level

You should use the following algorithm to determine the protection level value for a physical video output connector:

1.  **For each** protection type (ACP, CGMS-A, HDCP, and DPCP) that the physical output connector supports, perform the following steps:
    1.  Set the proposed protection level to no output protection. For example, for ACP, a driver should set the protection level to DXGKMDT\_OPM\_ACP\_OFF; for CGMS-A, a driver should set the protection level to DXGKMDT\_OPM\_CGMSA\_OFF; for HDCP, a driver should set the protection level to DXGKMDT\_OPM\_HDCP\_OFF; and for DPCP, a driver should set the protection level to DXGKMDT\_OPM\_DPCP\_OFF.
    2.  **For each** protected output that is associated with the physical output connector, perform the following steps:
        1.  Retrieve the current protected output's protection level for the current protection type.
        2.  **If** the current protection type is CGMS-A, remove the DXGKMDT\_OPM\_REDISTRIBUTION\_CONTROL\_REQUIRED flag if the flag is set.
        3.  **End if**
        4.  **If** the current protected output's protection level has a higher precedence than the proposed protection level, set the proposed protection level to the current protected output's protection level.
        5.  **End if**

    3.  **End for**
    4.  Set the physical output's protection level to the proposed protection level.

2.  **End for**

### <span id="algorithm_for_redistribution_control"></span><span id="ALGORITHM_FOR_REDISTRIBUTION_CONTROL"></span>Algorithm for Redistribution Control

You should use the following algorithm to determine if a physical output connector must enable redistribution control:

1.  **For each** protected output that is associated with the physical output connector, perform the following steps:
    1.  Retrieve the information on whether the current protected output's redistribution control flag is set.
    2.  **If** the DXGKMDT\_OPM\_REDISTRIBUTION\_CONTROL\_REQUIRED flag is set, perform the following steps:
        1.  Enable redistribution control.
        2.  Stop executing the algorithm.

    3.  **End if**

2.  **End for**

 

 





