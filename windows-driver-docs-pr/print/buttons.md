---
title: buttons element
description: The required buttons element specifies one or more buttons that are displayed in the event notification message box on the client computer.
keywords: ["buttons element Print Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- buttons
api_type:
- Schema
ms.date: 09/09/2022
---

# buttons element

The required **buttons** element specifies one or more buttons that are displayed in the event notification message box on the client computer.

The **buttons** element is defined in the *asyncui* namespace at this URI:

```xml
https://schemas.microsoft.com/2003/print/asyncui/v1/request
```

This resource may not be available in some languages and countries.

## Usage

```xml
<buttons>
  child elements
</buttons>
```

## Attributes

There are no attributes.

## Child elements

| Element | Description |
|--|--|
| [**button**](button.md) | A required element that specifies the characteristics of a button in a message box that is displayed on the client computer. |

## Parent elements

| Element | Description |
|--|--|
| [**messageBoxUI**](messageboxui.md) | An optional element that is used to display a message box on the client computer. |

## Remarks

See [**button**](button.md) for a code example that shows how to use the **buttons** element to enclose two **button** elements that display an **OK** and a **CANCEL** button.

## See also

[button](button.md)

[messageBoxUI](messageboxui.md)
