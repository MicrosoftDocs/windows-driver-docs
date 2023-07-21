---
title: messageBoxUI element
description: The optional messageBoxUI element is used to display a message box on the client computer.
keywords: ["messageBoxUI element Print Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- messageBoxUI
api_type:
- Schema
ms.date: 07/18/2023
---

# messageBoxUI element

The optional **messageBoxUI** element is used to display a message box on the client computer.

The **messageBoxUI** element is defined in the *asyncui* namespace at this URI:

```xml
https://schemas.microsoft.com/2003/print/asyncui/v1/request
```

This resource may not be available in some languages and countries.

## Usage

```xml
<messageBoxUI>
  child elements
</messageBoxUI>
```

## Attributes

There are no attributes.

## Child elements

| Element | Description |
|--|--|
| [**bitmap**](bitmap.md) | An optional element that is used to display a bitmap image to the left of the body text in a message box. |
| [**body**](body.md) | A required element that provides text that is displayed in the event notification message. This text should provide the user specific details about the printer event. |
| [**buttons**](buttons.md) | A required element that specifies one or more buttons that are displayed in the event notification message box on the client computer. |
| [**title**](title.md) | A required element that provides text that is displayed in the title of the event notification message. |

## Parent elements

| Element | Description |
|--|--|
| [**requestOpen**](requestopen.md) | An element that is used to open an event notification message on the client computer. |

## Remarks

See [**button**](button.md) for a code example that shows how to place an **OK** button and a **CANCEL** button a message box. See the **Examples** section for information about how to capture a button-click on a message box.

## Examples

The following code example shows how to notify the printer driver that the **OK** button was clicked on the message box.

```xml
<?xml version="1.0" ?> 
  <asyncPrintUIResponse xmlns="https://schemas.microsoft.com/2003/print/asyncui/v1/response">
    <v1>
      <requestClose>
        <messageBoxUI>
          <buttonID>IDOK</buttonID>
        </messageBoxUI >
      </requestClose>
    </v1>
  </asyncPrintUIResponse>
```

## See also

[bitmap](bitmap.md)

[body](body.md)

[button](button.md)

[buttons](buttons.md)

[requestOpen](requestopen.md)

[title](title.md)
