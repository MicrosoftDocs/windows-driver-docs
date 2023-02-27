---
title: button element
description: The required button element specifies the characteristics of a button in a message box that is displayed on the client computer.
keywords: ["button element Print Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- button
api_type:
- Schema
ms.date: 09/09/2022
---

# button element

The required **button** element specifies the characteristics of a button in a message box that is displayed on the client computer.

The **button** element is defined in the *asyncui* namespace at this URI:

```xml
https://schemas.microsoft.com/2003/print/asyncui/v1/request
```

This resource may not be available in some languages and countries.

## Usage

```xml
<button
  stringID = "xs:string"
  resourceDll = "xs:string"
  buttonID = "xs:string"/>
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **buttonID** | xs:string | Yes | A required attribute that specifies the string that will be returned to the printer driver when the user clicks the button. This attribute can take one of the following values:<br><br>IDOK - A button with the name "OK" will be displayed in the message box. When the user clicks the button, the message box returns the string "IDOK".<br><br>IDCANCEL - A button with the name "CANCEL" will be displayed in the message box. When the user clicks the button, the message box returns the string "IDCANCEL". |
| **resourceDll** | xs:string | No | An optional attribute that specifies a resource DLL that contains the text to display on the button. This DLL should be a dependent file of the printer driver and must be present in the driver resource folder (for example, %SYSTEMROOT%\system32\spool\drivers\w32x86\3). |
| **stringID** | xs:string | Yes | A required attribute that specifies the text to display on the button. The attribute value specifies the location of the text string in the resource DLL. |

## Child elements

There are no child elements.

## Parent elements

| Element | Description |
|--|--|
| [**buttons**](buttons.md) | A required element that specifies one or more buttons that are displayed in the event notification message box on the client computer. |

## Remarks

Buttons will be displayed at the bottom of the message box.

## Examples

The following code example shows how to use the **button** element to display **OK** and **CANCEL** buttons next to each other.

```xml
<?xml version="1.0" ?>
  <asyncPrintUIRequest
    xmlns="https://schemas.microsoft.com/2003/print/asyncui/v1/request">
    <v1>
      <requestOpen>
        <messageBoxUI>
          <title stringID="1234" resourceDll="IHV.dll" />
          <body stringID="100" resourceDll="IHV.dll">
            <parameter stringID="5" />
            <parameter stringID="1002" resourceDll="IHV.dll" />
          </body>
          <buttons>
            <button stringID="1" resourceDll="IHV.dll" buttonID="IDOK"/>
            <button stringID="2" resourceDll="IHV.dll" buttonID="IDCANCEL"/>
          </buttons>
        </messageBoxUI>
      </requestOpen>
    </v1>
  </asyncPrintUIRequest>
```

## See also

[buttons](buttons.md)
