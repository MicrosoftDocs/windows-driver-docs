---
title: Using GetOptions and SetOptions
description: Using GetOptions and SetOptions
keywords:
- GetOptions
- SetOptions
ms.date: 01/31/2023
---

# Using GetOptions and SetOptions

[!include[Print Support Apps](../includes/print-support-apps.md)]

**GetOptions** can be called to retrieve the driver's current setting for features whose keywords are listed in the buffer pointed to by the *pmszFeaturesRequested* input parameter.

For example, in a call to **GetOptions**, suppose that the *pmszFeaturesRequested* input buffer contains this string (in MULTI_SZ format):

```GPD
"PageSize\0Duplex\0Resolution\0\0"
```

After the **GetOptions** method returns, the output *pmszFeatureOptionBuf* could contain the following string (also in MULTI_SZ format):

```GPD
"PageSize\0Letter\0Duplex\0DuplexTumble\0Resolution\0300dpi\0\0"
```

This example shows that **GetOptions** retrieved the option keywords for PageSize (Letter), Duplex (DuplexTumble), and Resolution (300dpi).

**SetOptions** can be called to change the driver's current setting based on the feature/option keyword pairs in the *pmszFeatureOptionBuf* input buffer.

There are two categories of features that are supported:

[PPD Features](ppd-features.md)

[Driver Features](driver-features.md)
