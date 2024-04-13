---
title: Numeric Values
description: Numeric Values
keywords:
- GPD file entries WDK Unidrv , numeric values
- numeric values WDK GPD files
ms.date: 01/27/2023
---

# Numeric Values

[!include[Print Support Apps](../includes/print-support-apps.md)]

All numeric values that you specify as entry values or parameter values in a GPD file must be integers. Decimal points are not allowed, except within text strings.

Numeric values are assumed to be positive unless preceded by a minus sign.

Numeric values are assumed to be decimal unless preceded by 0x, in which case they are unsigned hexadecimal values.

The asterisk character (\*) can be used to indicate either an infinite value or a "don't care" value, if applicable within the context of a particular GPD file entry.
