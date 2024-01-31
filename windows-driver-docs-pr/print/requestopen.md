---
title: requestOpen element
description: The requestOpen element is used to open an event notification message on the client computer.
keywords: ["requestOpen element Print Devices"]
ms.date: 01/30/2024
---

# requestOpen element

The **requestOpen** element is used to open an event notification message on the client computer.

The **requestOpen** element is defined in the *asyncui* namespace at this URI:

```xml
https://schemas.microsoft.com/2003/print/asyncui/v1/request
```

This resource may not be available in some languages and countries.

## Usage

```xml
<requestOpen>
  child elements
</requestOpen>
```

## Attributes

There are no attributes.

## Child elements

| Element | Description |
|--|--|
| [**balloonUI**](balloonui.md) | An optional element that is used to display a message balloon on the client computer. |
| [**customUI**](customui.md) | An optional element that specifies a custom user interface to be displayed on a client computer. |
| [**messageBoxUI**](messageboxui.md) | An optional element that is used to display a message box on the client computer. |

## Parent elements

| Element | Description |
|--|--|
| [**asyncPrintUIRequest**](asyncprintuirequest.md) | A required element that describes a request issued by the printer driver to create a message on a client computer. |

## Examples

The following code example opens an event notification message.

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

[asyncPrintUIRequest](asyncprintuirequest.md)

[balloonUI](balloonui.md)

[customUI](customui.md)

[messageBoxUI](messageboxui.md)

[requestClose](requestclose.md)
