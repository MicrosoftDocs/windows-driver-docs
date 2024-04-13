---
title: Using EnumFeatures
description: Using EnumFeatures
keywords:
- EnumFeatures
ms.date: 01/31/2023
---

# Using EnumFeatures

[!include[Print Support Apps](../includes/print-support-apps.md)]

A caller can use **EnumFeatures** to retrieve a keyword list that contains currently supported driver features and all PPD features, in addition to the following, which Pscript treats as if they were features defined within PPD \*OpenUI/\*CloseUI structure keywords:

\*LeadingEdge

\*UseHWMargins

Pscript handles certain features in a special way. If more than one of \*Resolution, \*SetResolution, and \*JCLResolution keyword appear in a PPD, they're merged into one standard feature. After merging, the feature's keyword name will be "JCLResolution" if \*JCLResolution appears first; otherwise it will be "Resolution".

Some driver features (such as %Mirroring) are always supported, while other driver features are supported only under certain conditions. For example, when spooler EMF spooling is disabled on Windows 2000 and later operating system releases, the %PageOrder feature won't be supported. These unsupported driver features won't appear in the output keyword list of **EnumFeatures**.

For driver features, the keyword prefix "%" is included in the output. For PPD features, the keyword prefix "\*" isn't included in the output.
