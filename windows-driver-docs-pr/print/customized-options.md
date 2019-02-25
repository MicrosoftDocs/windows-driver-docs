---
title: Customized Options
description: Customized Options
ms.assetid: 8b54c59e-b469-488a-ae31-52045c00c971
keywords:
- printer options WDK Unidrv , customized
- customized printer options WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customized Options





Customized options are those that are not defined by predefined names in the GPD language. You must create unique names for these options.

Customized options can be associated with customized features. For an example of customized options associated with customized features, see [Customized Features](customized-features.md).

You can also specify customized options for some of the [standard features](standard-features.md). For example, if your printer provides a paper size that is not described by one of the standard options for the **PaperSize** feature, you can specify a customized paper size option by creating a unique name for the option.

Customized option names must be unique within a feature, but option names can be reused in different features. Also, you can use standard option names within customized features. Thus, for example, you can use the standard option names ON and OFF within several \*[Feature](feature-entry-format.md) entries for customized features.

 

 




