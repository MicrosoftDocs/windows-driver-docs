---
title: customUI element
description: The optional customUI element specifies a custom user interface to be displayed on a client computer.
keywords: ["customUI element Print Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- customUI
api_type:
- Schema
ms.date: 06/19/2023
---

# customUI element

The optional **customUI** element specifies a custom user interface to be displayed on a client computer.

The **customUI** element is defined in the *asyncui* namespace at this URI:

```xml
https://schemas.microsoft.com/2003/print/asyncui/v1/request
```

This resource may not be available in some languages and countries.

## Usage

```xml
<customUI
  dll = "xs:string"
  entrypoint = "xs:string"
  bidi = "xs:string">
  child elements
</customUI>
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **bidi** | xs:string | Yes | A required attribute that specifies the type of communication between the printer driver and the event notification message. If the value is **true**, communication is bidirectional, and the driver function in the resource DLL must return a string; see the Example section. If the value is **false**, communication is one-way, from the printer driver to the event notification message. |
| **dll** | xs:string | Yes | A required attribute that specifies a resource DLL that contains the custom user interface display function. This DLL should be a dependent file of the printer driver and must be present in the driver resource folder (for example, %SYSTEMROOT%\system32\spool\drivers\w32x86\3). |
| **entrypoint** | xs:string | Yes | A required attribute that specifies the function to call in the resource DLL. |

## Child elements

| Element | Description |
|--|--|
| **Anything** | Specifies any child element according to the custom user interface schema. See the Example section. |

## Parent elements

| Element | Description |
|--|--|
| [**requestOpen**](requestopen.md) | An element that is used to open an event notification message on the client computer. |

## Remarks

Because the **bidi** attribute is set to **true** in the following example, the **IHVFunction** entry point function in the *Abc.dll* DLL will be called. **IHVfunction** returns the **CDATA** type data.

## Examples

The following code example shows how to use the **customUI** element to call and display a custom user interface on a client computer.

```cpp
<?xml version="1.0"?>
  <asyncPrintUIRequest xmlns="https://schemas.microsoft.com/2003/print/asyncui/1.0"
      xmlns:myco="https://www.myprintercompany.com">
    <requestOpen>
      <customUI dll="abc.dll" entrypoint="IHVFunction" bidi="true">
        <IHV:anyXMLData />
          CDATA
      </customUI>
    </requestOpen>
  </asyncPrintUIRequest>
```

## See also

[**requestOpen**](requestopen.md)
