---
title: customData element
description: The optional customData element specifies a custom data source for this asynchronous notification XML schema.
keywords: ["customData element Print Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- customData
api_type:
- Schema
ms.date: 06/16/2023
---

# customData element

The optional **customData** element specifies a custom data source for this asynchronous notification XML schema.

The **customData** element is defined in the *asyncui* namespace at this URI:

```xml
https://schemas.microsoft.com/2003/print/asyncui/v1/request
```

This resource may not be available in some languages and countries.

## Usage

```xml
<customData
  dll = "xs:string"
  entryPoint = "xs:string"
  bidi = "xs:string">
  child elements
</customData>
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **bidi** | xs:string | Yes | A required attribute that specifies the type of communication between the printer driver and the event notification message. If the value is **true**, communication is bidirectional, and the driver function in the resource DLL must return a string. If the value is **false**, communication is one-way, from the printer driver to the event notification message. For more information, see the following Example and Remarks sections. |
| **dll** | xs:string | Yes | A required attribute that specifies a resource DLL that contains the custom data source. This DLL should be a dependent file of the printer driver and must be present in the driver resource folder (for example, %SYSTEMROOT%\system32\spool\drivers\w32x86\3). |
| **entryPoint** | xs:string | Yes | A required attribute that specifies the data source entry point in the resource DLL. |

## Child elements

| Element | Description |
|--|--|
| **Anything** | Specifies any child element according to the custom data schema. For more information, see the following Example section. |

## Parent elements

| Element | Description |
|--|--|
| [**requestOpen**](requestopen.md) | An element that is used to open an event notification message on the client computer. |

## Remarks

The custom data that you capture must be provided as a **CDATA** type.

## Examples

The following code example shows how you can use the **customData** element to obtain your custom data.

```xml
<?xml version="1.0"?>
  <asyncPrintUIRequest xmlns="https://schemas.microsoft.com/2003/print/asyncui/v1/request"
      xmlns:myco="https://www.myprintercompany.com">
    <requestOpen>
      <customData dll="abc.dll" entrypoint="IHVFunction" bidi="true">
        <IHV:anyXMLData />
          CDATA
      </customData>
    </requestOpen>
</asyncPrintUIRequest>
```

## See also

[requestOpen](requestopen.md)
