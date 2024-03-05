---
title: Using GetFeatureAttribute
description: Using GetFeatureAttribute
keywords:
- GetFeatureAttribute
ms.date: 02/20/2024
---

# Using GetFeatureAttribute

[!include[Print Support Apps](../includes/print-support-apps.md)]

This function is supported only for PostScript Printer Driver (PPD) features. If a certain attribute isn't available, **GetFeatureAttribute** returns E_INVALIDARG.

In the following table, the *pdwDataType* parameter takes values of the [**EATTRIBUTE_DATATYPE**](/windows-hardware/drivers/ddi/printoem/ne-printoem-_eattribute_datatype) enumerated type.

| Feature attribute | Output parameters |
|--|--|
| **DisplayName** | *pdwDataType*: kADT_UNICODE<br><br>*pbData*: null-terminated Unicode string of the feature keyword name's translation string<br><br>*pcbNeeded*: byte count of the Unicode string pointed to by pbData (including the null terminator)<br><br>This feature attribute is available to any PPD feature **EnumFeatures** can return. |
| **DefaultOption** | *pdwDataType*: kADT_ASCII<br><br>*pbData*: null-terminated ASCII string of the default option keyword name<br><br>*pcbNeeded*: byte count of the ASCII string pointed to by pbData (including the null terminator).<br><br>This feature attribute is available to any PPD feature **EnumFeatures** can return. |
| **OpenUIType** | *pdwDataType*: kADT_ASCII<br><br>*pbData*: null-terminated ASCII string containing one of following types: "PickOne", "PickMany", "Boolean"<br><br>*pcbNeeded*: byte count of the ASCII string pointed to by pbData (including the null terminator).<br><br>This feature attribute is available to any PPD feature **EnumFeatures** can return. |
| **OpenGroupType** | *pdwDataType*: kADT_ASCII<br><br>*pbData*: For features defined within the PPD's "OpenGroup: InstallableOptions ... CloseGroup: InstallableOptions" pair, a null-terminated ASCII string of "InstallableOptions" is returned. For other features, an empty ASCII string (which has only the null terminator) is returned.<br><br>*pcbNeeded*: byte count of the ASCII string pointed to by pbData (including the null terminator).<br><br>This feature attribute is available to any PPD feature that **EnumFeatures** can return. |
| **OrderDependencyValue** | *pdwDataType*: kADT_LONG<br><br>*pbData*: the relative order specified by the PPD's OrderDependency or NonUIOrderDependency keyword for this feature. Notice that the first parameter of these keywords is a real number that is converted to a LONG and returned.<br><br>*pcbNeeded*: sizeof(LONG)<br><br>This attribute is available only for a PPD feature that has an OrderDependency or NonUIOrderDependency entry in the PPD, and the entry omits optionKeyword. |
| **OrderDependencySection** | *pdwDataType*: kADT_ASCII<br><br>*pbData*: null-terminated ASCII string containing one of following section names: "ExitServer", "Prolog", "DocumentSetup", "PageSetup", "JCLSetup", or "AnySetup"<br><br>*pcbNeeded*: byte count of the ASCII string pointed to by pbData (including the null terminator).<br><br>This attribute is available only for a PPD feature that has an OrderDependency or NonUIOrderDependency entry in the PPD, and the entry omits optionKeyword. |
