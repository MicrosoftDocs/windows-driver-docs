---
title: Using EnumFeatures
description: Using EnumFeatures
ms.assetid: 4a87cedf-066a-445b-ad3e-71699c9d3e07
keywords:
- EnumFeatures
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using EnumFeatures





A caller can use **EnumFeatures** to retrieve a keyword list that contains currently supported driver features and all PPD features, in addition to the following, which Pscript treats as if they were features defined within PPD \*OpenUI/\*CloseUI structure keywords:

\*LeadingEdge

\*UseHWMargins

Pscript handles certain features in a special way. If more than one of \*Resolution, \*SetResolution, and \*JCLResolution keyword appear in a PPD, they are merged into one standard feature. After merging, the feature's keyword name will be "JCLResolution" if \*JCLResolution appears first; otherwise it will be "Resolution".

**Note**   Some driver features (such as %Mirroring) are always supported, while other driver features are supported only under certain conditions. For example, when spooler EMF spooling is disabled on Windows 2000 and later operating system releases, the %PageOrder feature will not be supported. These unsupported driver features will not appear in the output keyword list of **EnumFeatures**.

 

For driver features, the keyword prefix "%" is included in the output. For PPD features, the keyword prefix "\*" is not included in the output.

 

 




