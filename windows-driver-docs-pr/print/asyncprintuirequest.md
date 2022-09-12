---
title: asyncPrintUIRequest element
description: The required asyncPrintUIRequest element describes a request issued by the printer driver to create a message on a client computer.
keywords: ["asyncPrintUIRequest element Print Devices"]
topic_type:
- apiref
api_name:
- asyncPrintUIRequest
api_type:
- Schema
ms.date: 09/06/2022
---

# asyncPrintUIRequest element

The required **asyncPrintUIRequest** element describes a request issued by the printer driver to create a message on a client computer.

The **asyncPrintUIRequest** element is defined in the *asyncui* namespace at this URI:

```xml
https://schemas.microsoft.com/2003/print/asyncui/v1/request
```

This resource may not be available in some languages and countries.

## Usage

```xml
<asyncPrintUIRequest>
  child elements
</asyncPrintUIRequest>
```

## Attributes

There are no attributes.

## Child elements

| Element | Description |
|--|--|
| [**requestClose**](requestclose.md) | An optional element that is used to close an event notification message on the client computer. |
| [**requestOpen**](requestopen.md) | An element that is used to open an event notification message on the client computer. |

## Parent elements

There are no parent elements.

## Examples

The following code example shows how to use the **asyncPrintUIRequest** element.

```xml
<?xml version="1.0" ?>
   <asyncPrintUIRequest
    xmlns="https://schemas.microsoft.com/2003/print/asyncui/v1/request">
    <v1>
      <requestOpen>
        <balloonUI iconID="1" resourceDll="IHV.dll">
          <title stringID="1234" resourceDll="IHV.dll" />
          <body stringID="100" resourceDll="IHV.dll">
            <parameter stringID="5" />
            <parameter stringID="1002" resourceDll="IHV.dll" />
          </body>
        </balloonUI>
      </requestOpen>
    </v1>
  </asyncPrintUIRequest>
```

## See also

[**requestClose**](requestclose.md)

[**requestOpen**](requestopen.md)
