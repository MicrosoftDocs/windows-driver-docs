---
title: Setting the Protection Level
description: Setting the Protection Level
ms.assetid: e0fecc58-59d9-470a-83e6-9b08e2f59169
keywords:
- copy protection WDK COPP , protection levels
- video copy protection WDK COPP , protection levels
- COPP WDK DirectX VA , protection levels
- protected video WDK COPP , protection levels
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Protection Level


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

The COPP command can set the protection level of a protection type on the physical connector associated with the DirectX VA COPP device. To set the protection level, the video miniport driver's [*COPPCommand*](https://msdn.microsoft.com/library/windows/hardware/ff539642) function receives a pointer to a [**DXVA\_COPPCommand**](https://msdn.microsoft.com/library/windows/hardware/ff563141) structure with the **guidCommandID** member set to the DXVA\_COPPSetProtectionLevel GUID and the **CommandData** member set to a pointer to a [**DXVA\_COPPSetProtectionLevelCmdData**](https://msdn.microsoft.com/library/windows/hardware/ff563143) structure that specifies the type of protection to set and the level at which to set the protection. If a protection level is not available for the protection type, the COPP command sets the protection level to COPP\_NoProtectionLevelAvailable (-1). The COPP command might also specify some extended information in the **ExtendedInfoChangeMask** and **ExtendedInfoData** members of DXVA\_COPPSetProtectionLevelCmdData for the video miniport driver to set for the protection type.

The following protection levels can be set for the indicated protection types:

-   For COPP\_ProtectionType\_ACP, set one of the following values from the **COPP\_ACP\_Protection\_Level** enumerated type:
    -   COPP\_ACP\_Level0 or COPP\_ACP\_LevelMin (0)
    -   COPP\_ACP\_Level1 (1)
    -   COPP\_ACP\_Level2 (2)
    -   COPP\_ACP\_Level3 or COPP\_ACP\_LevelMax (3)

<!-- -->

-   For COPP\_ProtectionType\_CGMSA, set one of the following values from the **COPP\_CGMSA\_Protection\_Level** enumerated type:
    -   COPP\_CGMSA\_Disabled or COPP\_CGMSA\_LevelMin (0)
    -   COPP\_CGMSA\_CopyFreely (1)
    -   COPP\_CGMSA\_CopyNoMore (2)
    -   COPP\_CGMSA\_CopyOneGeneration (3)
    -   COPP\_CGMSA\_CopyNever (4)
    -   COPP\_CGMSA\_RedistributionControlRequired (0x08)
    -   (COPP\_CGMSA\_RedistributionControlRequired + COPP\_CGMSA\_CopyNever) or COPP\_CGMSA\_LevelMax

<!-- -->

-   For COPP\_ProtectionType\_HDCP, set one of the following values from the **COPP\_HDCP\_Protection\_Level** enumerated type:
    -   COPP\_HDCP\_Level0 or COPP\_HDCP\_LevelMin (0)
    -   COPP\_HDCP\_Level1 or COPP\_HDCP\_LevelMax (1)

 

 





