---
title: Determining Whether a Platform is Mobile or Desktop
description: Determining Whether a Platform is Mobile or Desktop
ms.assetid: f0a553a4-a23b-45c8-abc5-b5014ba328ae
keywords:
- TMM WDK display , determining mobile or desktop
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining Whether a Platform is Mobile or Desktop


TMM runs only on mobile computers and is automatically disabled on desktop computers. Hardware vendors should enable and use their own proprietary methods to enter clone view on desktop computers. They should determine if a platform is mobile so that they can avoid using their proprietary methods to enter clone view on a mobile computer and instead use TMM.

Hardware vendors can use the following code to determine if a platform is mobile or desktop. The platform can then use the appropriate mechanism to enter clone view.

```cpp
#include <Powrprof.h>   // For GetPwrCapabilities

    BOOL IsMobilePlatform()
    {
        BOOL fIsMobilePlatform = FALSE;

        fIsMobilePlatform = (PlatformRoleMobile == PowerDeterminePlatformRole());

        POWER_PLATFORM_ROLE iRole;

        // Check if the operating system determines 
        // that the computer is a mobile computer.
        iRole = PowerDeterminePlatformRole();

        if (PlatformRoleMobile == iRole)
        {
            fIsMobilePlatform = TRUE;
        }
        else if (PlatformRoleDesktop == iRole) 
        // Can happen when a battery is not plugged into a laptop
        {
            SYSTEM_POWER_CAPABILITIES powerCapabilities;

            if (GetPwrCapabilities(&powerCapabilities))
            {
         // Check if a battery exists, and it is not for a UPS.
         // Note that SystemBatteriesPresent is set on a laptop even if the battery is unplugged.
                fIsMobilePlatform = ((TRUE == powerCapabilities.SystemBatteriesPresent) && (FALSE == powerCapabilities.BatteriesAreShortTerm));
            }
            // GetPwrCapabilities should never fail 
            // However, if it does, leave fReturn == FALSE.
        }

        return fIsMobilePlatform;
    }
```

For information about the functions that are called in the preceding code, see the Microsoft Windows SDK documentation.

 

 





