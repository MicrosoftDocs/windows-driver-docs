---
title: title element
description: The required title element provides text that is displayed in the title of the event notification message.
keywords: ["title element Print Devices"]
ms.date: 01/31/2024
---

# title element

The required **title** element provides text that is displayed in the title of the event notification message.

The **title** element is defined in the *asyncui* namespace at this URI:

```xml
https://schemas.microsoft.com/2003/print/asyncui/v1/request
```

This resource may not be available in some languages and countries.

## Usage

```xml
<title
  stringID = "xs:string"
  resourceDll = "xs:string"/>
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **resourceDll** | xs:string | No | An optional attribute that specifies a resource DLL that contains the title text to display in the event notification message. This DLL should be a dependent file of the printer driver and must be present in the driver resource folder (for example, %SYSTEMROOT%\system32\spool\drivers\w32x86\3). |
| **stringID** | xs:string | Yes | A required attribute that specifies the text to display in the title of the event notification message. The attribute value specifies the location of the text string in the resource DLL. |

## Child elements

There are no child elements.

## Parent elements

| Element | Description |
|--|--|
| [**balloonUI**](balloonui.md) | An optional element that is used to display a message balloon on the client computer. |

## Remarks

If the attribute **resourceDll** is not specified, title text is generated from the Microsoft-supplied user interface DLL, Prnntfy.dll.

The body text loaded from the resource DLL can contain percentage (%) characters that will be replaced with text strings specified by the [**parameter**](parameter.md) child element.

## Examples

The following code example shows how to use the **title** element to indicate the string location in the resource DLL (in this example, stringID="1234") that contains the text to be used for the title.

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

[balloonUI](balloonui.md)

[parameter](parameter.md)
