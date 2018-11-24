---
title: Wrapping or Replacing Windows Vista sAPOs
description: Wrapping or Replacing Windows Vista sAPOs
ms.assetid: 6246aaab-c540-4f86-bf7a-4764cfc10e79
keywords:
- sAPO WDK
- wrapping Windows Vista sAPOs WDK
- replacing Windows Vista sAPOs WDK
- INF files WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Wrapping or Replacing Windows Vista sAPOs


When you develop your own audio driver for Windows Vista, you must decide whether to wrap the system-supplied sAPOs or develop your own sAPOs to replace the system-supplied ones.

You can do any of the following:

-   Option 1: Develop your own audio driver, but wrap the system-supplied sAPOs.

-   Option 2: Develop your own audio driver, develop one or more custom sAPOs, and delegate the missing functionality to the appropriate system-supplied sAPOs.

-   Option 3: Develop your own audio driver together with a complete set of custom sAPOs.

Be aware that if you develop your own sAPOs, your sAPOs must match the set that is provided by default with Windows Vista before you add any new ones. For the list of system-supplied sAPOs, see the [Windows Vista Default sAPOs](windows-vista-default-sapos.md) topic.

In Option 1, you develop your own audio driver but develop custom sAPOs to wrap the system-supplied sAPOs. So you must provide an INF file that installs your audio driver and calls the standard Windows Vista INF file to load the system-supplied sAPOs. After you develop your audio driver, you must perform the following steps to implement your custom sAPOs.

1.  Create custom sAPOs to [wrap the system-supplied sAPOs](wrapping-system-supplied-sapos.md).

2.  [Write an INF file](https://msdn.microsoft.com/library/windows/hardware/ff549520) to call the standard Windows Vista INF file.

Option 2 offers the most practical approach for anyone who would like to develop their own audio driver together with one or more sAPOs to replace the system-supplied ones. The following topic explains the design considerations and the steps involved in developing sAPOs for Option 2.

[Design Considerations for sAPO Development](design-considerations-for-sapo-development.md)

In Option 3, you develop your own audio driver together with a complete set of custom sAPOs to replace the system-supplied ones. In this scenario, you develop sAPOs to provide new system effects features that are not available with Windows Vista. You must provide your own custom user interface for configuring your system effects features.

After you develop your audio driver, you must perform the following steps to implement your custom sAPOs.

1.  Create custom sAPOs to [replace all the Windows Vista sAPOs](replacing-system-supplied-sapos.md).

2.  Create a separate user interface for configuring the custom sAPOs.

3.  [Create an INF file](https://msdn.microsoft.com/library/windows/hardware/ff549520) to install and register the sAPOs and the custom user interface.

 

 




