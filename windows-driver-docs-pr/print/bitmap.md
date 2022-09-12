---
title: bitmap element
description: The optional bitmap element is used to display a bitmap image to the left of the body text in a message box.
keywords: ["bitmap element Print Devices"]
topic_type:
- apiref
api_name:
- bitmap
api_type:
- Schema
ms.date: 09/09/2022
---

# bitmap element

The optional **bitmap** element is used to display a bitmap image to the left of the body text in a message box.

The **bitmap** element is defined in the *asyncui* namespace at this URI:

```xml
https://schemas.microsoft.com/2003/print/asyncui/v1/request
```

This resource may not be available in some languages and countries.

## Usage

```xml
<bitmap
  bitmapID = "xs:string"
  resourceDll = "xs:string"/>
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **bitmapID** | xs:string | Yes | A required attribute that specifies a bitmap image to display in the message box. The attribute value specifies the location of the image in the resource DLL. The bitmap image can be any size or format; the message box will resize to accommodate it. |
| **resourceDll** | xs:string | No | An optional attribute that specifies a resource DLL that contains the bitmap image to display in the message box. This DLL should be a dependent file of the printer driver and must be present in the driver resource folder (for example, %SYSTEMROOT%\system32\spool\drivers\w32x86\3). |

## Child elements

There are no child elements.

## Parent elements

| Element | Description |
|--|--|
| [**messageBoxUI**](messageboxui.md) | An optional element that is used to display a message box on the client computer. |

## Examples

The following code example shows how to use the **bitmap** element.

```xml
<?xml version="1.0" ?>
   <asyncPrintUIRequest xmlns="https://schemas.microsoft.com/2003/print/asyncui/v1/request">
    <v1>
      <requestOpen>
        <messageBoxUI>
          <title stringID="1234" resourceDll="IHV.dll" />
          <bitmap bitmapID="100" resourceDll="IHV.dll" />
          <body stringID="100" resourceDll="IHV.dll">
            <parameter stringID="5" />
            <parameter stringID="1002" resourceDll="IHV.dll" />
          </body>
        </messageBoxUI>
      </requestOpen>
    </v1>
  </asyncPrintUIRequest>
```

## See also

[**messageBoxUI**](messageboxui.md)
