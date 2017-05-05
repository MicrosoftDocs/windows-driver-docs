---
title: Determining Whether a Platform is Mobile or Desktop
description: Determining Whether a Platform is Mobile or Desktop
ms.assetid: f0a553a4-a23b-45c8-abc5-b5014ba328ae
keywords:
- TMM WDK display , determining mobile or desktop
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Determining Whether a Platform is Mobile or Desktop


TMM runs only on mobile computers and is automatically disabled on desktop computers. Hardware vendors should enable and use their own proprietary methods to enter clone view on desktop computers. They should determine if a platform is mobile so that they can avoid using their proprietary methods to enter clone view on a mobile computer and instead use TMM.

Hardware vendors can use the following code to determine if a platform is mobile or desktop. The platform can then use the appropriate mechanism to enter clone view.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Determining%20Whether%20a%20Platform%20is%20Mobile%20or%20Desktop%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




