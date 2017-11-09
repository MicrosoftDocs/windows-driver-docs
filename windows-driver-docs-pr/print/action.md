---
title: action element
description: The optional action element describes an action that will be completed when a user clicks a button in the balloon message.
MS-HAID:
- 'async\_e2652093-33ee-4394-85b6-cb69abeb94da.xml'
- 'print.action'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: dae207ad-072e-4de6-b6a2-f1188ce91065
keywords: ["action element Print Devices"]
topic_type:
- apiref
api_name:
- action
api_type:
- Schema
---

# action element


The optional **action** element describes an action that will be completed when a user clicks a button in the balloon message.

The **action** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

``` syntax
<action
  dll = "xs:string"
  entrypoint = "xs:string">
  text
</action>
```

Attributes
----------

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>dll</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies a DLL, supplied by an IHV, that contains a function to call when a user clicks a button.</p></td>
</tr>
<tr class="even">
<td><p><strong>entrypoint</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies the function to call in the DLL supplied by the IHV. This function should return <strong>NULL</strong> when called.</p></td>
</tr>
</tbody>
</table>

Text value
----------

Optional string, formatted as CDATA, to be passed to the driver resource DLL.

## Child elements


There are no child elements.

## Parent elements


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>balloonUI</strong>](balloonui.md)</p></td>
<td><p></p>
<p>Provides text that is displayed in the event notification message. This text should provide the user specific details about the printer event.</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **action** element is used with an interactive balloon, which is similar to a regular balloon, but it includes a button for the user to click.

Examples
--------

The following XML code example will run the *IHV.exe* program on the client computer

```
<?xml version="1.0" ?> 
  <asyncPrintUIRequest
    xmlns="http://schemas.microsoft.com/2003/print/asyncui/v1/request">
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

```
<?xml version="1.0" ?>
   <asyncPrintUIRequest
    xmlns="http://schemas.microsoft.com/2003/print/asyncui/v1/request">
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

## <span id="see_also"></span>See also


[**balloonUI**](balloonui.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20action%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





