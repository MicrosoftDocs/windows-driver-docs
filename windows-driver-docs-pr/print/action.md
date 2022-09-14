---
title: action element
description: The optional action element describes an action that will be completed when a user clicks a button in the balloon message.
keywords: ["action element Print Devices"]
topic_type:
- apiref
api_name:
- action
api_type:
- Schema
ms.date: 09/06/2022
---

# action element

The optional **action** element describes an action that will be completed when a user clicks a button in the balloon message.

The **action** element is defined in the *asyncui* namespace at this URI:

```xml
https://schemas.microsoft.com/2003/print/asyncui/v1/request
```

This resource may not be available in some languages and countries.

## Usage

```xml
<action
  dll = "xs:string"
  entrypoint = "xs:string">
  text
</action>
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **dll** | xs:string | Yes | A required attribute that specifies a DLL, supplied by an IHV, that contains a function to call when a user clicks a button. |
| **entrypoint** | xs:string | Yes | A required attribute that specifies the function to call in the DLL supplied by the IHV. This function should return **NULL** when called. |

## Text value

Optional string, formatted as CDATA, to be passed to the driver resource DLL.

## Child elements

There are no child elements.

## Parent elements

| Element | Description |
|--|--|
| [**balloonUI**](balloonui.md) | Provides text that is displayed in the event notification message. This text should provide the user specific details about the printer event. |

## Remarks

The **action** element is used with an interactive balloon, which is similar to a regular balloon, but it includes a button for the user to click.

## Examples

The following XML code example will run the *IHV.exe* program on the client computer.

```xml
<?xml version="1.0" ?> 
  <asyncPrintUIRequest
    xmlns="https://schemas.microsoft.com/2003/print/asyncui/v1/request">
    <v1>
      <requestOpen>
        <balloonUI iconID="1" resourceDll="IHV.dll">
          <title stringID="1234" resourceDll="IHV.dll" />
          <body stringID="100" resourceDll="IHV.dll">
            <parameter stringID="<5>" />
            <parameter stringID="1002" resourceDll="IHV.dll" />
          </body>
        </balloonUI>
      </requestOpen>
    </v1>
  </asyncPrintUIRequest>
```

The following code example shows how to use the **action** element to pass data to a resource DLL.

```xml
<?xml version="1.0" ?>
   <asyncPrintUIRequest
    xmlns="https://schemas.microsoft.com/2003/print/asyncui/v1/request">
    <v1>
      <requestOpen>
        <balloonUI iconID="1" resourceDll="IHV.dll">
          <title stringID="1234" resourceDll="IHV.dll"/>
          <body stringID="100" resourceDll="IHV.dll">
            <parameter stringID="<5>" />
            <parameter stringID="1002" resourceDll="IHV.dll" />
          </body>
          <action dll="adc.dll" entrypoint="def" >
            IHV CDATA to pass into the resource DLL
          </action>
        </balloonUI>
      </requestOpen>
    </v1>
  </asyncPrintUIRequest>
```

## See also

[**balloonUI**](balloonui.md)
