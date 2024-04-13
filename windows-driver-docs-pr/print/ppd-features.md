---
title: PPD Features
description: PPD Features
keywords:
- PPD files WDK Pscript
- non-PPD features WDK Pscript
- driver features WDK Pscript
ms.date: 01/30/2023
---

# PPD Features

[!include[Print Support Apps](../includes/print-support-apps.md)]

PPD features are defined in the PPD file within **\*OpenUI**/**\*CloseUI** structure keyword pairs, and in certain PPD keywords that are treated similarly by the Pscript driver. Although **EnumFeatures** lists the **\*LeadingEdge** and **\*UseHWMargins** keywords, they aren't defined within PPD **\*OpenUI**/**\*CloseUI** structure keyword pairs. 

The **GetOptions** and **SetOptions** methods ignore these keywords if they appear in the feature list. The PPD feature/option keywords are case sensitive.

**SetOptions** handles certain PPD features in a special way:

- If the printer's PPD file includes the **\*OutputOrder** feature keyword and **SetOptions** is called to change the option selection for this feature, then the **%PageOrder** driver feature setting will be changed to match the new output order. This is done in order to prevent the spooler from performing unnecessary page order simulation.

- If the printer's PPD file includes the **\*OutputBin** feature keyword and **SetOptions** is called to change the option selection for this feature, and the change causes the current setting of the **%PageOrder** driver feature to be the opposite of the printer's page ordering, and **%MetafileSpooling** is "False", then **%MetafileSpooling** will be reset to "True".

- When spooler EMF spooling is enabled, and **Collate** is set to "True" (this can be set either directly in the public portion of the [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) structure or by calling **SetOptions** on the PPD's **\*Collate** feature keyword), but the **Collate** feature isn't currently available, and **%MetafileSpooling** is "False", then **%MetafileSpooling** will be reset to "True". This is done when all requested settings in the **SetOptions** call are applied.

- If **Duplex** is set to simplex (this can be set either directly in the public portion of the DEVMODE structure or by calling **SetOptions** on the PPD's **\*Duplex** feature keyword), but **%PagePerSheet** is set to "Booklet", then **%PagePerSheet** will be changed to "2". This is done when all requested settings in the **SetOptions** call are applied.
