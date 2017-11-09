---
title: parameter element
description: The optional parameter element specifies a text string that is substituted for a percentage ( ) character in the text of an event notification message.
MS-HAID:
- 'async\_a0adc762-3c44-49c1-ac44-83c7763cc42b.xml'
- 'print.parameter'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6a43af7d-da00-4038-b1a8-a076d07c4c1a
keywords: ["parameter element Print Devices"]
topic_type:
- apiref
api_name:
- parameter
api_type:
- Schema
---

# parameter element


The optional **parameter** element specifies a text string that is substituted for a percentage (%) character in the text of an event notification message.

The **parameter** element is defined in the *asyncui* namespace at this URI: http://schemas.microsoft.com/2003/print/asyncui/v1/request. (This resource may not be available in some languages and countries.)

Usage
-----

``` syntax
<parameter
  stringID = "xs:string"
  resourceDll = "xs:string"
  type = "xs:string"/>
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
<td><p><strong>resourceDll</strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>An optional attribute that specifies a resource DLL that contains the text to display in the event notification message. This DLL should be a dependent file of the printer driver and must be present in the driver resource folder (for example, %SYSTEMROOT%\system32\spool\drivers\w32x86\3).</p></td>
</tr>
<tr class="even">
<td><p><strong>stringID</strong></p></td>
<td><p>xs:string</p></td>
<td><p>Yes</p></td>
<td><p></p>
<p>A required attribute that specifies the text to display at the location of the percentage (%) character in the text of the event notification message. The attribute value specifies the location of the text string in the resource DLL.</p></td>
</tr>
<tr class="odd">
<td><p><strong>type</strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>An optional attribute that specifies the name of the printer or document. This attribute can take one of the following values:DocumentThe name of the document being printed.PrinterNameThe name of the printer, as listed in the Printers and Faxes folder in Control Panel, for example, &quot;Fabrikam 5000 on \\printserver&quot; or &quot;Printer in upstairs bedroom.&quot;</p></td>
</tr>
</tbody>
</table>

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
<td><p>[<strong>body</strong>](body.md)</p></td>
<td><p></p>
<p>A required element that provides text that is displayed in the event notification message. This text should provide the user specific details about the printer event.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>title</strong>](title.md)</p></td>
<td><p></p>
<p>The required title element provides text that is displayed in the title of the event notification message.</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The text loaded from the resource DLL can contain percentage (%) characters that will be replaced with text strings specified by the **parameter** element.

Examples
--------

The following code example shows how the **parameter** element can be used to generate a complete event notification message.

In this example, the **stringID** values specify the following:

-   User interface string 100 in the driver resource DLL is "Printer is out of %1 ink; please open %2 and replace the ink cartridge."
-   User interface string 5 in the Microsoft-supplied user interface DLL is "yellow".
-   User interface string 1002 in the driver resource DLL is "Side Access Door B".

```
<?xml version="1.0" ?>
   <asyncPrintUIRequest
    xmlns="http://schemas.microsoft.com/2003/print/asyncui/v1/request">
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

With the preceding XML code, the following body text (stringID="100") is displayed in the event notification message: "Printer is out of yellow ink; please open Side Access Door B and replace the ink cartridge."

## <span id="see_also"></span>See also


[**body**](body.md)

[**title**](title.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20parameter%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





