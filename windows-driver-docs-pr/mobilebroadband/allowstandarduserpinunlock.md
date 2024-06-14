---
title: AllowStandardUserPinUnlock
description: AllowStandardUserPinUnlock
ms.date: 10/13/2023
---

# AllowStandardUserPinUnlock

[!include[MBAE deprecation warning](../includes/mbae-deprecation-warning.md)]

> [!IMPORTANT]
> Starting in Windows 10, version 1507, this element has been deprecated and may not be supported in future versions of Windows.

The AllowStandardUserPinUnlock element specifies if standard users are allowed to perform PIN unlock operations.

## Usage

```syntax
<AllowStandardUserPinUnlock>
  text
</ AllowStandardUserPinUnlock >
```

## Attributes

There are no attributes.

## Text value

A Boolean value where **true** allows standard users to perform PIN unlock operations and **false** does not.

## Child elements

There are no child elements.

## Parent elements

| Element | Description |
|--|--|
| [NetworkConfiguration](networkconfiguration.md) | Specifies the purchase and Internet mobile broadband profiles to be used or whether standard user can perform PIN unlock operations. |

## XSD

``` syntax
<xs:element name="AllowStandardUserPinUnlock" type="xs:boolean" minOccurs="0" />
```

## Remarks

The AllowStandardUserPinUnlock element is optional.
